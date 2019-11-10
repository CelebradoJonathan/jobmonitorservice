from flask import request, json, Response, Blueprint, g

from ..models.JobModel import JobModel, JobSchema
from ..models.JobIdModel import JobIdModel, JobIdSchema

# from ..shared.Authentication import Auth

jobid_api = Blueprint('jobid', __name__)

jobid_schema = JobIdSchema()


@jobid_api.route('/', methods=['POST'])
def create():
    """
    Create Job Function
    """

    req_data = request.get_json()
    data = jobid_schema.load(req_data)
    jobid = JobIdModel(data)
    jobid.save()
    jobid_message = jobid_schema.dump(jobid)

    return custom_response(jobid_message, 201)


def custom_response(res, status_code):
    """
    Custom Response Function
    """

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


@jobid_api.route('/<int:id>', methods=['GET'])
def get_a_job(id):
    """
    Get a single jobid
    """

    jobid = JobIdModel.get_one_jobid(id)
    print(jobid)
    if not jobid:
        return custom_response({'error': 'jobId not found'}, 404)

    jobid_message = jobid_schema.dump(jobid)
    return custom_response(jobid_message, 200)
#
#
# @jobid_api.route('/<int:job_id>', methods=['DELETE'])
# def delete():
#     """
#   Delete a user
#   """
#
#     job = JobModel.get_one_job(g.job.get('id'))
#
#     job.delete()
#
#     return custom_response({'message': 'deleted'}, 204)



