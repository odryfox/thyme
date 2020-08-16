from flask import Flask

from infrastructure.http.api import NewsView


def create_flask_app(name, thyme_web_app) -> Flask:
    app = Flask(name)

    views_kwargs = {"web_app": thyme_web_app}
    add = app.add_url_rule
    add("/", view_func=NewsView.as_view("name", **views_kwargs))
    return app
