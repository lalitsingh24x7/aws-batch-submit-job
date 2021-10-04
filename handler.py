import json
import boto3
import traceback

from batch_service import AwsBatch


def hello(event, context):
    message = "ok"
    try:
        a = AwsBatch()
        a.run()
    except Exception as e:
        traceback.print_exception()
        print(str(e))
        message = str(e)
    body = {
        "message": message
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
