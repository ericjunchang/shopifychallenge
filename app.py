import os

# from cs50 import SQL
import sqlite3
from inventory_manager import InventoryManager
con = sqlite3.connect('inventory.db', check_same_thread=False)
con.isolation_level = None
db = con.cursor()

from flask import Flask, flash, jsonify, redirect, render_template, request, session


inv_manager = InventoryManager(db)
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///inventory.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        item = request.form.get("item")
        ref = request.form.get("ref")
        quantity = request.form.get("quantity")
        if not item or not ref or not quantity:
            inventory = inv_manager.get_unarchived_inventory()
            return render_template("index.html", inventory=inventory)
        inv_manager.create_item(item, ref, quantity)
        
        return redirect("/")

    else:
        inventory = inv_manager.get_unarchived_inventory()
        return render_template("index.html", inventory=inventory)

@app.route("/archive", methods=["POST"])
def archive():
    id = request.form.get("id")
    comment = request.form.get("comment")
    if id:
        db.execute("UPDATE inventory SET archive = ?, comment = ? WHERE id = ?", (0, comment, id))
    return redirect("/")

@app.route("/edit", methods=["POST"])
def edit():
    id = request.form.get("id")
    item = request.form.get("item")
    ref = request.form.get("ref")
    quantity = request.form.get("quantity")

    current_item = inv_manager.get_item_by_id(id)

    if id and (item or ref or quantity):
        db.execute(
            "UPDATE inventory SET item = ?, ref = ?, quantity = ? WHERE id = ?",
            (item or current_item['item'], ref or current_item['ref'], quantity or current_item['quantity'], id)
        )
    return redirect("/")

@app.route("/unarchive", methods=["GET", "POST"])
def unarchive():
    if request.method == "POST":

        id = request.form.get("id")
        quantity = request.form.get("quantity")
        if not id or not quantity:
            inventory = inv_manager.get_archived_inventory()
            return render_template("archive.html", inventory=inventory)

        db.execute("UPDATE inventory SET archive = ?, quantity = ? WHERE id = ?", (1, quantity, id))
        return redirect("/unarchive")

    else:

        inventory = inv_manager.get_archived_inventory()
        return render_template("archive.html", inventory=inventory)

@app.route("/archivelist", methods=["GET"])
def archivelist():
        inventory = inv_manager.get_archived_inventory()
        return render_template("archive.html", inventory=inventory)

@app.route("/permadelete", methods=["POST"])
def permadelete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM inventory WHERE id = ?", id)
    return redirect("/unarchive")