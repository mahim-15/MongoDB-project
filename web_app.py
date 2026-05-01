from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["ticket_management"]
tickets = db["tickets"]


@app.route("/")
def index():
    all_tickets = list(tickets.find().sort("created_at", -1))

    total_tickets = tickets.count_documents({})
    open_tickets = tickets.count_documents({"status": "open"})
    progress_tickets = tickets.count_documents({"status": "in_progress"})
    resolved_tickets = tickets.count_documents({"status": "resolved"})
    closed_tickets = tickets.count_documents({"status": "closed"})

    return render_template(
        "index.html",
        tickets=all_tickets,
        total_tickets=total_tickets,
        open_tickets=open_tickets,
        progress_tickets=progress_tickets,
        resolved_tickets=resolved_tickets,
        closed_tickets=closed_tickets
    )


@app.route("/add", methods=["POST"])
def add_ticket():
    title = request.form.get("title")
    description = request.form.get("description")
    created_by = request.form.get("created_by")
    assigned_to = request.form.get("assigned_to")
    priority = request.form.get("priority")

    if priority not in ["low", "medium", "high"]:
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

    tickets.insert_one(ticket)
    return redirect(url_for("index"))


@app.route("/update_status/<ticket_id>", methods=["POST"])
def update_status(ticket_id):
    new_status = request.form.get("status")

    if new_status in ["open", "in_progress", "resolved", "closed"]:
        tickets.update_one(
            {"_id": ObjectId(ticket_id)},
            {
                "$set": {
                    "status": new_status,
                    "updated_at": datetime.now()
                }
            }
        )

    return redirect(url_for("index"))


@app.route("/delete/<ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):
    tickets.delete_one({"_id": ObjectId(ticket_id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)