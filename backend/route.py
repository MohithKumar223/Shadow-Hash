from flask import Blueprint, jsonify
from data import customers
from utils import calculate_health

routes = Blueprint("routes", __name__)

@routes.route("/customers")
def get_customers():
    result = []
    for c in customers:
        temp = c.copy()
        temp["health"] = calculate_health(c)
        result.append(temp)
    return jsonify(result)