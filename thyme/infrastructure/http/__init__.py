from flask import Flask

from infrastructure.http.api import ApiNewsView
from infrastructure.http.views import NewsView


def create_flask_app(name, thyme_web_app) -> Flask:
    app = Flask(name, template_folder="infrastructure/http/templates")

    views_kwargs = {"web_app": thyme_web_app}
    add = app.add_url_rule
    add("/", view_func=NewsView.as_view("news", **views_kwargs))
    add("/api/", view_func=ApiNewsView.as_view("news api", **views_kwargs))
    return app
