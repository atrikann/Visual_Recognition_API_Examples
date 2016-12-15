#!/bin/bash

echo $1

. ./envvars

if [ ! -z "$1" ]
then

    echo "deleting this classifier $1"
    curl -X DELETE "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/$1?api_key=${api_key}&version=2016-05-20"
    exit

fi
echo ${api_key}

list=("CarsvsTrucks_907069919" "CarsvsTrucks_1416907346" "CarsvsTrucks_434648442" "CarsvsTrucks_1787725993" "CarsvsTrucks_1844068283" "CarsvsTrucks_807937695" "CarsvsTrucks_545673675" "CarsvsTrucks_726425911" "CarsvsTrucks_502925986" "CarsvsTrucks_1565132879" "CarsvsTrucks_55782086" "CarsvsTrucks_1542682384" "CarsvsTrucks_2080211793" "CarsvsTrucks_925742542" "CarsvsTrucks_262467076" "CarsvsTrucks_355736796" "CarsvsTrucks_1185063319")


for ix in ${!list[*]}
do
    printf "   %s\n" "${list[$ix]}"
curl -X DELETE "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/${list[$ix]}?api_key=${api_key}&version=2016-05-20"
done

