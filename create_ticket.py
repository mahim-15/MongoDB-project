from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

ticket = {
    "title": "Login problem",
    "description": "User correct password diyeo login korte partese na",
    "status": "open",
    "priority": "high",
    "created_by": "Client A",
    "assigned_to": "Mahim",
    "created_at": datetime.now(),
    "updated_at": datetime.now()
}

result = tickets.insert_one(ticket)

print("Ticket created successfully!")
print("Ticket ID:", result.inserted_id)