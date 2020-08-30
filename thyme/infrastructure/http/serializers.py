from marshmallow import Schema, fields


class NewsSchema(Schema):
    name = fields.Str()
    content = fields.Str()


news_schema = NewsSchema()
news_list_schema = NewsSchema(many=True)
