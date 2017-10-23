import boto3
import datetime

client = boto3.client('cloudwatch')

def temperature(event, context):

    message = event

#   ts = datetime.datetime.strptime(str(message['Timestamp']), '%Y-%m-%dT%H:%M:%S')
    ts = datetime.datetime.utcnow()

    sensorid = str(message['Device ID'])
    temperature = float(message['Temperatur'])
    co2sensor = float(message['Co2Sensor'])

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
                'Timestamp': ts,
                'Value': float(temperature),
                'Unit': 'None',
                'StorageResolution': 1
            },
            {
                'MetricName': 'Co2',
                'Dimensions': [
                    {
                        'Name': 'Sensor',
                        'Value': sensorid
                    }
                ],
                'Timestamp': ts,
                'Value': float(co2sensor),
                'Unit': 'None',
                'StorageResolution': 1
            },
        ]
    )


    return {
        "message": "Executed successfully!",
        "event": event,
        "response": response
    }
