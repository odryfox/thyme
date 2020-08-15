from flask.views import MethodView


class NewsView(MethodView):
    def __init__(self, web_app):
        self.web_app = web_app

    def get(self):
        news = self.web_app.get_news_usecase.execute()
        return {'name': n.name for n in news}
