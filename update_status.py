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
new_status = input("New status (open/in_progress/resolved/closed): ").lower()

if new_status not in ["open", "in_progress", "resolved", "closed"]:
    print("Invalid status.")
    exit()

try:
    result = tickets.update_one(
        {"_id": ObjectId(ticket_id)},
        {
            "$set": {
                "status": new_status,
                "updated_at": datetime.now()
            }
        }
    )

    if result.modified_count > 0:
        print("Ticket status updated successfully!")
    else:
        print("Ticket not found or status already same.")

except Exception:
    print("Invalid ticket ID.")