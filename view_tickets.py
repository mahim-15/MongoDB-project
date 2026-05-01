from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

all_tickets = tickets.find().sort("created_at", -1)

print("\n===== All Tickets =====")

found = False

for ticket in all_tickets:
    found = True
    print("-" * 50)
    print("ID:", ticket["_id"])
    print("Title:", ticket["title"])
    print("Description:", ticket["description"])
    print("Status:", ticket["status"])
    print("Priority:", ticket["priority"])
    print("Created By:", ticket["created_by"])
    print("Assigned To:", ticket["assigned_to"])
    print("Created At:", ticket["created_at"])

if not found:
    print("No tickets found.")