from flask import Blueprint, jsonify

bp = Blueprint("news", __name__)

@bp.route("", methods=["GET"])
def get_news():
    return jsonify({
        "items": []
    })
