import json
import os
import boto3
import traceback
from datetime import datetime


class AwsBatch:
    def __init__(self):
        self.client = boto3.client("batch", region_name='us-east-1')

    def run(self, job_name="Test", job_queue='python-demo', job_definition='python-demo-3'):
        response = self.client.submit_job(
            jobName=f'{job_name}-1',
            jobQueue=job_queue,
            jobDefinition=job_definition,
            containerOverrides={
                "command": ["python3", "main.py"],
                'environment': [
                    {
                        'name': 'TEST_ENV',
                        'value': os.getenv('TEST_ENV')
                    },
                ]
            },
            timeout={
                'attemptDurationSeconds': 300
            }
        )
