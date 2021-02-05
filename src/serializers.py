from marshmallow import Schema, fields


class JobSchema(Schema):
    id = fields.Integer()
    customer = fields.Integer()
    employees = fields.String()
    date = fields.Date()
    start_time = fields.Time()
    hours_number = fields.Float()
    end_time = fields.Time()
