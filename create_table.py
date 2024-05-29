from sqlalchemy import Column, Integer, String, func, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import numpy as np


Base = declarative_base() # classe de base à partir de laquelle toutes les classes ORM vont hériter

class Book(Base): # représente une table dans la base de données
                  # définir des colonnes qui correspondent aux attributs de chaque livre
                  # chaque colonne est définie avec un type et des contraintes ex : Integer / nullable=False pour indiquer que la colonne ne peut pas être vide
    __tablename__ = "books"
    ISBN = Column(String, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)
    image_url_s = Column(String, nullable=False)
    image_url_m = Column(String, nullable=False)
    image_url_l = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.title} [{self.author}] ({self.year})"
    

    def nb_rating_by_book(self, session):
        return session.query(func.count(Rating.id)).filter(Rating.ref == self.ISBN).scalar()

    def avg_rating_by_book(self, session):
        return session.query(func.avg(Rating.rating)).filter(Rating.ref == self.ISBN).scalar()
    
    def ecart_type(self, session):
        return np.std(session.query((Rating.rating)).filter(Rating.ref == self.ISBN).all())

class User(Base): 

    __tablename__ = "users"
    UserId = Column(Integer, primary_key=True, unique=True, nullable=False)
    location = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    ratings = relationship('Rating', back_populates='user')


    def nb_rating_by_user(self, session):
        return session.query(func.count(Rating.id)).filter(Rating.UserId == self.UserId).scalar()

    def avg_rating_by_user(self, session):
        return session.query(func.avg(Rating.rating)).filter(Rating.UserId == self.UserId).scalar()
    
    def ecart_type(self, session):
        return np.std(session.query((Rating.rating)).filter(Rating.UserId == self.UserId).all())
    
    def affiche_stat(self, session, UserId):
        rating_count = self.nb_rating_by_user(session)
        avg_by_user = self.avg_rating_by_user(session)
        ecart_t = self.ecart_type(session)
        if rating_count != 0 and UserId == self.UserId:
            print(f"User: {self.UserId}, Number of Ratings: {rating_count}, average : {round(avg_by_user, 2)}, écart type : {round(ecart_t, 2)}")

class Rating(Base): 
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("users.UserId"))
    ref = Column(String, ForeignKey("books.ISBN"))
    rating = Column(Integer)

    user = relationship('User', back_populates='ratings')

    def __repr__(self):
        return f"{self.rating}"

    @classmethod
    def stat_notes(cls, session):
        somme = session.query(func.sum(cls.rating)).scalar()
        nb = session.query(func.count(cls.rating)).scalar()
        ecart_type = np.std(session.query(cls.rating).all())
        print(f"la moyenne des notes est : {round(somme/nb, 2)} \nl'écart type est : {round(ecart_type, 2)}")
    

##############################################################################################################

# Configuration de la base de données
engine = create_engine('sqlite:///books.db')  # crée un moteur de base de connées SQLite nommé books.db

if __name__ == "__main__" :
    Base.metadata.create_all(engine)              # crée toutes les tables définies par les classes ORM dans la bdd
