from flask import Blueprint, jsonify

bp = Blueprint("faq", __name__)

@bp.route("", methods=["GET"])
def get_faq():
    return jsonify({
        "items": []
    })
