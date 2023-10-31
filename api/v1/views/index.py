#!/usr/bin/python3
"""Create a status route"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import PLace
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status"""

    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """
    Retrives the number of each objects by type
    """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "review", "state", "user"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
