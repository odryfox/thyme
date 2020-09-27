from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    status = fields.Str()
    date_start = fields.Date()
    time_start = fields.Time()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
