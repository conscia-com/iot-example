# iot-example

## Dependencies

* [AWS CLI](https://aws.amazon.com/cli/)
* [Serverless](https://serverless.com/) framework

For the iot example:

* Python 3
* Ruby, iStats (`gem install istats` on Mac OS X)


## Setup AWS credentials

```
aws configure
```

Use [profiles](http://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html) if you need to support multiple accounts.


## IoT setup

[IoT Home](https://console.aws.amazon.com/iot) in the console

Make sure that the region in the upper right corner of the console says "Ireland"

1. Create a policy under the Secure section

    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "iot:Connect",
            "iot:Publish"
          ],
          "Resource": "*"
        }
      ]
    }
    
    ```

2. Create and activate a certificate under the Secure section, download files + root CA certificate
3. Attach policy to certificate from the certificate's Actions dropdown
4. Create a Thing and assign it to the certificate from the certificate's Actions dropdown

Get the endpoint hostname in the Settings section and make sure that it's enabled.


## Lambda function setup

Install the Serverless framework (might require installation of NodeJS).

Go to the services/temperatures/ folder and run "serverless deploy"

Check the [CloudFormation](console.aws.amazon.com/cloudformation) console section for progress/errors


## Fake sensor setup on Mac OS X

Install python3, ruby with [homebrew](https://brew.sh)

Install iStats with `gem install istats`

Go to the iot/ folder

Copy the downloaded certificate files to iot/

Modify the ENDPOINT and CERT_ID variables in start-test.bash

Run `start-test.bash`

Go to the [Cloudwatch](console.aws.amazon.com/cloudwatch) console section and check for metrics


## Links and tips

http://docs.aws.amazon.com/iot/latest/developerguide

Caveats around high resolution metrics: They are only available for 3 hours, detailed 
(1 min) metrics are only available for 15 days. See:

https://aws.amazon.com/blogs/aws/new-high-resolution-custom-metrics-and-alarms-for-amazon-cloudwatch/

Python IDE: https://www.jetbrains.com/pycharm/

iStats: http://chris911.github.io/iStats/


## Deploy function with Serverless

```
# serverless create --template aws-python3 --path temperatures
# serverless deploy
# serverless deploy function --function handleTemperature
```
