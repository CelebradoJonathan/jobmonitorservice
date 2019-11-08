from marshmallow import fields, Schema
from sqlalchemy.dialects.postgresql import UUID
import datetime
import enum
from . import db


# class PossibleStates(enum.Enum):
#     started = "STARTED"
#     finished = "FINISHED"
#     error = "ERROR"


class JobModel(db.Model):
    """
    Job Model
    """
    # table name
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(UUID(as_uuid=True), db.ForeignKey('jobid.job_id'), nullable=False)
    app_name = db.Column(db.String(128), nullable=False)
    # state = db.Column(db.Enum(PossibleStates))
    state = db.Column(db.String(10))
    created_at = db.Column(db.Integer())

    # class constructor

    def __init__(self, data):
        """
        Class constructor
        """

        self.job_id = data.get('job_id')
        self.app_name = data.get('app_name')
        self.state = data.get('state')
        self.created_at = data.get('created_at')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_jobs():
        return JobModel.query.all()

    @staticmethod
    def get_one_job(id):
        return JobModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class JobSchema(Schema):
    """
  User Schema
  """

    id = fields.Int(dump_only=True)
    job_id = fields.UUID(required=True)
    app_name = fields.Str(required=True)
    state = fields.Str(required=True)
    created_at = fields.Int(required=True)
