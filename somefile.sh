. ./envvars

curl -X POST -F "images_file=@leftimage_sample.png" -F "parameters=@myparams.json" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=${api_key}&version=2016-05-20"
