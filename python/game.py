#!/usr/bin/python3
import pymongo, random, os
client = pymongo.MongoClient("mongo", 27017)
db = client.Bible
db.Books
while True:
    index = random.randint(2, 65)
    index_previous = index - 1
    index_next = index + 1
    book_name = db.Books.find_one({'book_index': index})['name']
    book_name_previous = db.Books.find_one({'book_index': index_previous})['name']
    book_name_next = db.Books.find_one({'book_index': index_next})['name']
    print("\n"*20)
    print("*"*len(book_name_previous) + " --- " + book_name + " --- " + "*"*len(book_name_next))
    print("")
    input('Press enter to see the answer?\n')
    os.system('clear')
    print("\n"*20)
    print(book_name_previous + " --- " + book_name + " --- " + book_name_next)
    print("")
    input('Ready for the next attempt?')
    os.system('clear')