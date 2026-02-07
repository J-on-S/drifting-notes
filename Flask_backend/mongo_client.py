import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
password = os.environ['DB_PASS']
uri = "mongodb+srv://jonathansandjong_db_user:" + password + "@mcwics-db.i6qruhs.mongodb.net/?appName=McWiCS-DB"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

### Writing to and reading from the database !!

# Get the database named "notes"
notes_db = client['notes']
# Get the collection also named "notes"
notes = notes_db['notes']

# Find a note in the database
print(notes.find_one())

# Create a new note then save it to the database
a_new_note = {
    "message": "hi there" + str(random.randint(0, 2000)),
    "url": "https://www.google.com",
    "tags": ['easy-going']
}
notes.insert_one(a_new_note)
