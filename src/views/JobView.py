from flask import request, json, Response, Blueprint, g

from ..models.JobModel import JobModel, JobSchema
from ..models.JobIdModel import JobIdModel, JobIdSchema

# from ..shared.Authentication import Auth

job_api = Blueprint('jobs', __name__)

job_schema = JobSchema()


@job_api.route('/', methods=['POST'])
def create():
    """
    Create Job Function
    """

    req_data = request.get_json()
    data = job_schema.load(req_data)
    job = JobModel(data)
    job.save()
    job_message = job_schema.dump(job)

    return custom_response(job_message, 201)


def custom_response(res, status_code):
    """
    Custom Response Function
    """

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


@job_api.route('/<int:job_id>', methods=['GET'])
def get_a_job(job_id):
    """
    Get a single user
    """

    job = JobModel.get_one_user(job_id)

    if not job:
        return custom_response({'error': 'job not found'}, 404)

    job_message = job_schema.dump(job).data
    return custom_response(job_message, 200)


@job_api.route('/<int:job_id>', methods=['DELETE'])
def delete():
    """
  Delete a user
  """

    job = JobModel.get_one_job(g.job.get('id'))

    job.delete()

    return custom_response({'message': 'deleted'}, 204)



