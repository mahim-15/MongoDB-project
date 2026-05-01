from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["ticket_management"]
tickets = db["tickets"]

title = input("Ticket title: ")
description = input("Description: ")
created_by = input("Created by: ")
assigned_to = input("Assigned to: ")
priority = input("Priority (low/medium/high/urgent): ").lower()

if priority not in ["low", "medium", "high", "urgent"]:
    print("Invalid priority. Default set to medium.")
    priority = "medium"

ticket = {
    "title": title,
    "description": description,
    "status": "open",
    "priority": priority,
    "created_by": created_by,
    "assigned_to": assigned_to,
    "created_at": datetime.now(),
    "updated_at": datetime.now()
}

result = tickets.insert_one(ticket)

print("Ticket created successfully!")
print("Ticket ID:", result.inserted_id)