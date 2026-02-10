from flask import Blueprint, jsonify

bp = Blueprint("events", __name__)

@bp.route("", methods=["GET"])
def get_events():
    return jsonify({
        "items": []
    })
