from importation import session
from create_table import Book, Rating, User


def affichage_par_titre(critere):
    books = session.query(Book).filter_by(title=critere).all()
    if books :
        for book in books :
            # print(f"{book.title} [{book.author}] ({book.year})")
            print(book) # après avoir redéfini méthode de classe __repr__ pour l'affichage correct du livre
    else :
        print("Book not found")

# affichage_par_titre("The Hobbit")
# Rating.stat_notes(session)

users = session.query(User).all()
for user in users:
    user.affiche_stat(session, 8)



































# users = session.query(User).all()
# for user in users:
#     rating_count = user.nb_rating_by_user(session)
#     avg_by_user = user.avg_rating_by_user(session)
#     ecart_t = user.ecart_type(session)
# #     if rating_count != 0 :
# #         print(f"User: {user.UserId}, Number of Ratings: {rating_count}, average : {round(avg_by_user, 2)}")

#     if user.UserId == 8 :
#         print(f"User: {user.UserId}, Number of Ratings: {rating_count}, , ecart type : {round(ecart_t, 2)}")



# books = session.query(Book).all()
# for book in books:
#     rating_count = book.nb_rating_by_book(session)
#     avg_by_book = book.avg_rating_by_book(session)
#     ecart_t = book.ecart_type(session)
#     # if avg_by_book != 0 :
#     #     print(f"User: {book.ISBN}, Number of Ratings: {rating_count}, average : {round(avg_by_book, 2)}")

#     if book.ISBN == "553263226" :
#         print(f"Book: {book.ISBN}, title : {book.title}, Number of Ratings: {rating_count}, , ecart type : {round(ecart_t, 2)}")