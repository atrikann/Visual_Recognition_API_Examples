#!/bin/bash

. ./envvars


curl -X POST -F "right_positive_examples=@trump.zip"  -F "negative_examples=@hillary.zip" -F "name=parties" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=${api_key}&version=2016-05-20"
