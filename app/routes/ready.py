from flask import Blueprint, jsonify

bp = Blueprint("ready", __name__)

@bp.route("", methods=["GET"])
def ready():
    return jsonify({
        "status": "ready"
    })
