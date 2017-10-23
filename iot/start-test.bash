#!/bin/bash
set -e 
ENDPOINT=a2zgbqm9dcuutb.iot.eu-west-1.amazonaws.com
CERT_ID=6cd520f6b5

if [ ! -d python3env ]; then
  python3 -m venv python3env
fi
. python3env/bin/activate

# install AWS Device SDK for Python if not already installed
if [ ! -d ./aws-iot-device-sdk-python ]; then
  printf "\nInstalling AWS SDK...\n"
  git clone https://github.com/aws/aws-iot-device-sdk-python.git
  pushd aws-iot-device-sdk-python
  python3 setup.py install
  popd
fi


# Check to see if root CA file exists, download if not
if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from Symantec...\n"
  curl -s https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem >root-CA.crt
fi

# run sample app
python3 basicMetric.py -e $ENDPOINT -r root-CA.crt -c $CERT_ID-certificate.pem.crt -k $CERT_ID-private.pem.key -t temperatureMetric

exit 0
