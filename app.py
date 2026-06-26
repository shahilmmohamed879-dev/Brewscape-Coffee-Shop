from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB Compass
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["Brewscap"]

# Collection
orders = db["orders"]


@app.route("/place-order", methods=["POST"])
def place_order():

    data = request.json

    orders.insert_one(data)

    return jsonify({
        "success": True,
        "message": "Order Stored Successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)