from datetime import datetime, timedelta
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
    
db = client["Drifting_Notes"]
notes = db["notes"]

def insert_note(text: str, sender_anon_id: str):
    result = notes.insert_one({
        "text": text,
        "createdAt": datetime.utcnow(),
        "senderAnonId": sender_anon_id
    })
    return result.inserted_id

def get_random_note(exclude_anon_id: str):
    cutoff = datetime.utcnow() - timedelta(days=1)

    pipeline = [
        {"$match": {
            "senderAnonId": {"$ne": exclude_anon_id},
            "createdAt": {"$gte": cutoff}
        }},
        {"$sample": {"size": 1}}
    ]

    docs = list(notes.aggregate(pipeline))
    return docs[0] if docs else None

