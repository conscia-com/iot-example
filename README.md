# iot-example

### Dependencies

* Python 3
* Serverless

### Deploy and run function

```
serverless create --template aws-python3 --path temperatures
serverless deploy
serverless deploy function --function handleTemperature
serverless invoke -f temperature -l
```

### Links and tips

http://docs.aws.amazon.com/iot/latest/developerguide

Caveats around high resolution metrics: They are only available for 3 hours, detailed 
(1 min) metrics are only available for 15 days. See:

https://aws.amazon.com/blogs/aws/new-high-resolution-custom-metrics-and-alarms-for-amazon-cloudwatch/

https://www.jetbrains.com/pycharm/

### IoT policy

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": [
        "arn:aws:iot:eu-west-1:579970091892:topic/temperatureMetric",
        "arn:aws:iot:eu-west-1:579970091892:topic/temperatureMetric/*"
      ]
    }
  ]
}

```
