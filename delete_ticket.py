from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

ticket_id = input("Enter ticket ID to delete: ")

try:
    result = tickets.delete_one({"_id": ObjectId(ticket_id)})

    if result.deleted_count > 0:
        print("Ticket deleted successfully!")
    else:
        print("Ticket not found.")

except Exception:
    print("Invalid ticket ID.")