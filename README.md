# WiscAutoApp (Wisconsin Autonomous Perception Coding Challenge Application)

## Submission Specification
This is my solution to the Wisconsin Autonomous Perception Coding Challenge. I used python and the following libraries to analyze the image:
- OpenCV
- NumPy
- Matplotlib
- sklearn




Original Image            |  Example answer | Final answer
:-------------------------:| :-------------------------: | :-------------------------:
<img src = "https://github.com/WisconsinAutonomous/CodingChallenges/blob/master/perception/red.png" width = "460" height = "460">   | <img src = "https://github.com/WisconsinAutonomous/CodingChallenges/raw/master/perception/answer.png" width = "460" height = "460"> |  <img src = "https://github.com/Fooyang/WiscoAutoApp/blob/main/answer.png" width = "460" height = "460"> 


## Methodolgy

My methodology was seperated into three main steps: 

1) Find the proper HSV values to isolate the color of the cones:
    - I created 3 sliders changing the HSV values on a continually updating mask of the original image
    - By changing the values on the slider, I could find the best HSV values to mask the image and remove all other colors except the cones
    
2) Mask the image and find the top and bottom points for the two lines of cones:
    - Using the HSV values I found, I created a black and white mask of the image
    - I split the image in half to isolate each the two lines of cones
    - Processing each half of the image as an array, I found the top-most and bottom-most non-zero cell in the arrays. 
        - Black cells have a value of 0, so any non-zero cell would be a cone pixel in the black-and-white masked image
    
3) Drew a line that went through each column of cones:
    - Using the top and bottom most pixels on both sides, I found the slope of each line of cones
    - I used those slopes to calculate the continuation of each line of cones until they reached the sides of the image
    - Using the new coordinates I found, I drew lines on the original image, producing my answer.png

## Scrapped attempts

A few things I tried and ultimately decided not to use were:

1) Isolating a cone in the image and using Matplotlib to find the color distribution of the cone, in attempt to find the perfect value to threshold the original image
2) Using sklearn to create a linear regression of the cones instead of calculating the slope by hand
    - Required the use of bounding rectangles around each cone to create data points for the linear regression, and I decided it wasn't worth it in the end
