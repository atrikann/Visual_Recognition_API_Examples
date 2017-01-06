# Visual_Recognition_API_Examples

Most of my learning is from the Watson Developer Cloud portal 

https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/#introduction


The first thing is to train the Watson library with the images, to be used for reference later.
The library is a zip file that you create, having images of the object/person/location  in different angles/shots.

This is called creating a classifier. 
Once this is done - then check if the training is done by issuing a REST call and validating if Watson has completed its processing.

Later, feed in the reference image and let the Watson Visual Recognition Engine check if the image exists in the library and return a score. Higher the score -higher the likeliness that this will match the one in the library.

Look at readme file in this repo - for the starter scripts.


Some snapshot when I was experimenting with the tools.

<img width="839" alt="screen shot 2017-01-06 at 11 48 06 am" src="https://cloud.githubusercontent.com/assets/14288989/21709454/1a6c0650-d407-11e6-9a77-aeb03ce32696.png">

Create the library ( classifier) by stating zip files, as Positive and negative images.

The word(s) "positive images", and "negative images" are keywords !! - this indicates to the VR engine how to score when the reference image is given.



<img width="1104" alt="screen shot 2017-01-06 at 11 59 39 am" src="https://cloud.githubusercontent.com/assets/14288989/21709530/a7201f46-d407-11e6-8b79-c7d2c587d7d5.png">

Listing classifiers. Since I have already created the library you will see the road_signs_159xxx  listed.


<img width="839" alt="screen shot 2017-01-06 at 12 00 24 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709548/bdba9efc-d407-11e6-86bb-2591214e976c.png">

This error is when you already have a classifier ( library ) created and try to create it again.

<img width="1080" alt="screen shot 2017-01-06 at 12 01 06 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709559/d8360942-d407-11e6-9e59-9056637e7ea1.png">

Snapshot - after we have created the classifier ( library ) - The engine takes time to digest the data.

Run the REST API to check if the VR Engine is ready to start referencing ( or interpret ) the image we are about to feed.

The status should say "ready", before we can start experimenting with our images. ( should take 2-3 minutes )


<img width="881" alt="screen shot 2017-01-06 at 12 02 30 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709581/0bbb3fc6-d408-11e6-9dd6-90775aadfd30.png">



Feed in a Right direction image and check that the VR engine can detect it and give me a positive score.

A score of higher value indicates that the new image I just passed is likeliness of the images in the positive zip files.

Likewise a lower score indicates that the image is not resembling any images in the positive images zip file.

This is not about the exact match - but likeliness of the image being matched in the library ( zip ) file.

The myparams.json - can have another classifier called "default" - i.e the VR Engine's default library, 


<img width="1099" alt="screen shot 2017-01-06 at 12 10 36 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709705/2c51358c-d409-11e6-9773-50d096b5dfd9.png">


Example of a lower score - this happened because I tried to feed in a left side image and tried to validate with the VR engine's library that I have already configured.



<img width="1099" alt="screen shot 2017-01-06 at 12 24 19 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709948/33382d2c-d40b-11e6-9f27-93d26166922e.png">


This is the right image that I used to check if it resembled any images in the right_images.zip library.


<img width="248" alt="screen shot 2017-01-06 at 12 27 27 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709986/95d48840-d40b-11e6-8e4e-3c287dd8d5c7.png">


Left image that I used to check that if it matched any image in the positive ( or right images ) zip file.


<img width="248" alt="screen shot 2017-01-06 at 12 27 08 pm" src="https://cloud.githubusercontent.com/assets/14288989/21709987/95d7ec6a-d40b-11e6-819b-5ac2bde7c7fe.png">
