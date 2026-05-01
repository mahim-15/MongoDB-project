from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from datetime import datetime
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

ticket_id = input("Enter ticket ID: ")
assigned_to = input("Assign to: ")

try:
    result = tickets.update_one(
        {"_id": ObjectId(ticket_id)},
        {
            "$set": {
                "assigned_to": assigned_to,
                "updated_at": datetime.now()
            }
        }
    )

    if result.modified_count > 0:
        print("Ticket assigned successfully!")
    else:
        print("Ticket not found or assignee already same.")

except Exception:
    print("Invalid ticket ID.")