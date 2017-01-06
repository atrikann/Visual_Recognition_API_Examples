#!/bin/bash

. ./envvars

#curl -X POST -F "beagle_positive_examples=@beagle.zip" -F "husky_positive_examples=@husky.zip"  -F "negative_examples=@cats.zip" -F "name=dogs" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=${api_key}&version=2016-05-20"

curl -X POST -F "right_positive_examples=@rightimages.zip"  -F "negative_examples=@leftimages.zip" -F "name=roadsigns" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=${api_key}&version=2016-05-20"

echo "" 
