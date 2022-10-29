import json
import wget
from csv import DictReader
from files import JSON_RESULT_PATH


JSON_USERS_URL = 'https://raw.githubusercontent.com/konflic/examples/master/data/users.json'
CSV_BOOKS_URL = 'https://raw.githubusercontent.com/konflic/examples/master/data/books.csv'


users_with_books = []
i = 0

with open(wget.download(JSON_USERS_URL), "r") as f:
    users_list = json.loads(f.read())

num_users = len(users_list)

with open(wget.download(CSV_BOOKS_URL)) as f:
    reader = DictReader(f)
    for book in reader:
        if i < len(users_list):
            users_with_books.append(
                {'name': users_list[i]['name'], 'gender': users_list[i]['gender'], 'address': users_list[i]['address'],
                 'age': users_list[i]['age'], 'books': [{'title': book['Title'], 'author': book['Title'],
                                                         'pages': book['Pages'], 'genre': book['Genre']}]})
        else:
            users_with_books[i % num_users]['books'].append({'title': book['Title'], 'author': book['Title'],
                                                             'pages': book['Pages'], 'genre': book['Genre']})
        i += 1

with open(JSON_RESULT_PATH, "w") as f:
    s = json.dumps(users_with_books, indent=4)
    f.write(s)
