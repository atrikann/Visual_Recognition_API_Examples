import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from pprint import pprint

# Picked from https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/?python#create_a_classifier

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2ad1de1d6651cba0046f8b4d7056d6d9ae61f53e')

#now classify  or identify 
with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
    classifier_ids=['CarsvsTrucks_1542682384', 'default']), indent=2))


#print(json.dumps(visual_recognition.list_classifiers(), indent=2))


