import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from pprint import pprint

# Picked from https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/?python#create_a_classifier

#TRAIN is also - Create Classifiers

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2ad1de1d6651cba0046f8b4d7056d6d9ae61f53e')

# Create first
with open(join(dirname(__file__), 'trucks.zip'), 'rb') as trucks, \
      open(join(dirname(__file__), 'cars.zip'), 'rb') as cars:
   print(json.dumps(visual_recognition.create_classifier('CarsvsTrucks', trucks_positive_examples=trucks, negative_examples=cars), indent=2))

# a New Classifier gets created each time. e.g: CarsvsTrucks_76292,  CarsvsTrucks_68229
# How do I pass that the classify () API below,  

#now classify  or identify 
#with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
#    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
#    classifier_ids=['CarsvsTrucks_2080211793', 'default']), indent=2))


print(json.dumps(visual_recognition.list_classifiers(), indent=2))


