from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

count = tickets.count_documents({})

print("Total tickets:", count)

for ticket in tickets.find():
    print(ticket)