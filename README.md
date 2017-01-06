# Visual_Recognition_API_Examples

Most of my learning is from the Watson Developer Cloud portal 

https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/#introduction


The first thing is to train the Watson library with the images, to be used for reference later.
The library is a zip file that you create, having images of the object/person/location  in different angles/shots.

This is called creating a classifier. 
Once this is done - then check if the training is done by issuing a REST call and validating if Watson has completed its processing.

Later, feed in the reference image and let the Watson Visual Recognition Engine check if the image exists in the library and return a score. Higher the score -higher the likeliness that this will match the one in the library.

Look at readme file in this repo - for the starter scripts.

