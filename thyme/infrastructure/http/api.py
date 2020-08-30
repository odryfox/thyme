from flask_restful import Resource
from infrastructure.http.serializers import news_list_schema


class ApiNewsResource(Resource):
    def __init__(self, web_app):
        self.web_app = web_app

    def get(self):
        news = self.web_app.get_news_usecase.execute()
        return news_list_schema.dump(news)
