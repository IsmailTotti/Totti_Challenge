import json




def hello(event, context):
    with open('index.html', 'r') as file:
        body = file.read()
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': body,
    }

