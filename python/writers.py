#!/usr/bin/python3
import pymongo, random, os
mongo_host=os.environ['MONGO_HOST']
mongo_port=os.environ['MONGO_PORT']
client = pymongo.MongoClient(mongo_host, int(mongo_port))
db = client.Bible
db.Books
while True:
  index = random.randint(2, 65)
  book_name = db.Books.find_one({'book_index': index})['name']
  book_writers = db.Books.find_one({'book_index': index})['writers']
  print("\n"*10)
  print(" "*20 + "Who wrote " + book_name + "?")
  input(" "*20 + 'Press enter to see the answer?\n')
  os.system('clear')
  print("\n"*10)
  writers = ''
  for writer in book_writers:
    if len(book_writers) == 1:
      writers = writer
    if len(book_writers) > 1:
      writers = writer + ', ' + writers
  if len(book_writers) > 1:
    writers = writers[:-2]
  print(" "*20 + writers + " wrote " + book_name + ".")
  print("")
  input('Ready for the next attempt?')
  os.system('clear')