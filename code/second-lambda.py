import json


def main(event, context):
    print('Second Lambda')
    return {
        "statusCode": 200,
        "body": json.dumps('Cheers from second lambda')
    }
