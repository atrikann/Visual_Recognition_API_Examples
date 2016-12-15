#!/bin/bash

. ./envvars

# only needs the apikey

curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=${api_key}&version=2016-05-20"

echo ""

