import boto3
import datetime

client = boto3.client('cloudwatch')

def temperature(event, context):

    message = event

    print(context)

    sensorid = str(message['sensorid'])
    temperature = float(message['temperature'])

    response = client.put_metric_data(
        Namespace='Temperatures',
        MetricData=[
            {
                'MetricName': 'Temperature',
                'Dimensions': [
                    {
                        'Name': 'Sensor',
                        'Value': sensorid
                    }
                ],
                'Timestamp': datetime.datetime.utcnow(),
                'Value': float(temperature),
                'Unit': 'None',
                'StorageResolution': 1
            },
        ]
    )


    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event,
        "response": response
    }
