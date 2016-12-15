#!/bin/bash

if [ -z "$1" ]
then
    echo "Please enter the classifier id"
    exit
fi 
. ./envvars
classifier_id=$1
echo ${api_key}

echo "classifier id ${classifier_id}"

curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/${classifier_id}?api_key=${api_key}&version=2016-05-20"
