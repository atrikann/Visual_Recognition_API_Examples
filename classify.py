import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from pprint import pprint

test_url = 'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2ad1de1d6651cba0046f8b4d7056d6d9ae61f53e')

#image of a car.
# works
#with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
#    print(json.dumps(visual_recognition.classify(images_file=image_file), indent=2))

#image of prez works
#print(json.dumps(visual_recognition.classify(images_url='https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'), indent=2))

#with open(join(dirname(__file__), 'car.jpg'), 'rb') as image_file:
#    print(json.dumps(visual_recognition.classify(images_file=image_file),indent=2))

with open(join(dirname(__file__), 'indianprez.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file),indent=2))

#with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
#    print(json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))
#with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
#    data = json.dumps(visual_recognition.classify(images_file=image_file))
#    with open('data.txt', 'w') as outfile:
#        print ( json.dump(data, outfile))
##    with open('data.txt') as data_file:
#        data = json.load(data_file)
#        print data['images']
##
#{
#  "images": [
#    {
#      "image": "photo.jpg", 
#      "classifiers": [
#        {
#          "classes": [
#            {
#              "score": 0.964429, 
#              "class": "car", 
#              "type_hierarchy": "/vehicles/car"
#            }, 
#            {
#              "score": 0.549834, 
#              "class": "auto"
#            }
#          ], 
#          "classifier_id": "default", 
#          "name": "default"
#        }
#      ]
#    }
#  ], 
#  "custom_classes": 0, 
#  "images_processed": 1
#}
#	print data['images'][0]['faces'][0]['face_location']
#	print "print face_location width"
#	print data['images'][0]['faces'][0]['face_location']['width']
