from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.events import bp as events_bp
    from app.routes.news import bp as news_bp
    from app.routes.faq import bp as faq_bp
    from app.routes.health import bp as health_bp
    from app.routes.ready import bp as ready_bp

    app.register_blueprint(events_bp, url_prefix="/api/events")
    app.register_blueprint(news_bp, url_prefix="/api/news")
    app.register_blueprint(faq_bp, url_prefix="/api/faq")
    app.register_blueprint(health_bp, url_prefix="/healthz")
    app.register_blueprint(ready_bp, url_prefix="/readyz")

    return app
