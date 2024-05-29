from create_table import Book, User, Rating, engine
from sqlalchemy.orm import sessionmaker
import csv

Session = sessionmaker(bind=engine)  # configure une classe de session liées à notre moteur de bdd
session = Session()                  # crée une instance de session pour interagir avec la base de données


def import_books_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        #csvreader = csv.DictReader(csvfile) # to Update???  
        csvreader = csv.DictReader(csvfile, quotechar='"') # pour lire le fichier CSV et traiter chaque ligne comme un dictionnaire, où les clés sont les noms de colonnes
        for row in csvreader:
            book = Book(
                ISBN=row["ISBN"],
                title=row["Book-Title"],
                author=row["Book-Author"],
                year=row["Year-Of-Publication"],
                publisher=row["Publisher"],
                image_url_s=row["Image-URL-S"],
                image_url_m=row["Image-URL-M"],
                image_url_l=row["Image-URL-L"]
            )
            session.add(book)  # mise en tampon
        session.commit()       # écriture dans la bdd


def import_users_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, quotechar='"') # pour lire le fichier CSV et traiter chaque ligne comme un dictionnaire, où les clés sont les noms de colonnes
        for row in csvreader: #User-ID,Location,Age
            user = User(
                UserId=row["User-ID"],
                location=row["Location"],
                age=row["Age"]
            )
            session.add(user)  # mise en tampon
        session.commit()       # écriture dans la bdd

def import_ratings_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, quotechar='"') # pour lire le fichier CSV et traiter chaque ligne comme un dictionnaire, où les clés sont les noms de colonnes
        for row in csvreader: # User-ID,ISBN,Book-Rating
            rating = Rating(
                UserId=row["User-ID"],
                ref=row["ISBN"],
                rating=row["Book-Rating"]
            )
            session.add(rating)  # mise en tampon
        session.commit()       # écriture dans la bdd

if __name__ == "__main__" :
    # Importation des fichiers csv
    csv_file_path_1 = 'data/books_reduce.csv'
    import_books_from_csv(csv_file_path_1)

    csv_file_path_2 = 'data/users_reduce.csv'
    import_users_from_csv(csv_file_path_2)

    csv_file_path_3 = 'data/ratings_reduce.csv'
    import_ratings_from_csv(csv_file_path_3)

