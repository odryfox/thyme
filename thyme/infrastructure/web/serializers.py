from domain.constants import TaskStatusEnum
from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    status = fields.Str(validate=validate.OneOf([status.value for status in TaskStatusEnum]))
    date_start = fields.Date()
    time_start = fields.Time()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
