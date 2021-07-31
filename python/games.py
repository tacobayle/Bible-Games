#!/usr/bin/python3
import pymongo, random, os
mongo_host=os.environ['MONGO_HOST']
mongo_port=os.environ['MONGO_PORT']
client = pymongo.MongoClient(mongo_host, int(mongo_port))
db = client.Bible
db.Books
while True:
    index = random.randint(2, 65)
    index_previous = index - 1
    index_next = index + 1
    book_name = db.Books.find_one({'book_index': index})['name']
    book_name_previous = db.Books.find_one({'book_index': index_previous})['name']
    book_name_next = db.Books.find_one({'book_index': index_next})['name']
    print("\n"*10)
    print(" "*20 + "*"*len(book_name_previous) + " --- " + book_name + " --- " + "*"*len(book_name_next))
    print("")
    input(" "*20 + 'Press enter to see the answer?\n')
    os.system('clear')
    print("\n"*10)
    print(" "*20 + book_name_previous + " --- " + book_name + " --- " + book_name_next)
    print("")
    input('Ready for the next attempt?')
    os.system('clear')