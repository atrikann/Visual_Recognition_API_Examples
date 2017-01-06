#!/bin/bash

. ./envvars

# only needs the apikey

echo "The api_key is $api_key"
echo "If there are any classifiers libraries that you have created earlier, then you should see them below."
echo " If there are NOT - then create them first using the custom_classifiers in this repo"

curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=${api_key}&version=2016-05-20"

echo ""
echo ""
echo ""
echo "If this fails create a new account on IBM Bluemix, create a service on Visual Recognition, and get the correct API KEY."
echo "Later create some classifiers, and run this command again"

# A sample API Key would look like ..
#
#{
#  "url": "https://gateway-a.watsonplatform.net/visual-recognition/api",
#
#  "note": "It may take up to 5 minutes for this key to become active",
#  "api_key": "03884318f81782ff1a98cd1de04f29322c7dfc8b"
#}
