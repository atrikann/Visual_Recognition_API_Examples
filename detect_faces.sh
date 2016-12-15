#!/bin/bash
. ./envvars
echo ${api_key}

curl -X POST -F "images_file=@oldprez.png" -F "parameters=@myparams.json" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/detect_faces?api_key=${api_key}&version=2016-05-20"

