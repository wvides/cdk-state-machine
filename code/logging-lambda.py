import json


def main(event, context):
    print('Hello')
    return {
        "statusCode": 200,
        "body": json.dumps('Cheers from AWS Lambda!!')
    }
