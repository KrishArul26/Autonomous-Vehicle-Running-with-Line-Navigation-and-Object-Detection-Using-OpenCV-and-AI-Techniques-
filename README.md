<h2 align="center"> Live-streaming-Autonomous-Vehicle-running-With-line-detection-using-OpenCV</h2>

<h3 align="left">Introduction
  
<h4 align="left">Mobility on a wide scale is moving towards complete automation. Though the technology for automating the vehicles already exists, these technologies must be optimised to fit the current environment.  This project would be a scaled-down model of the Autonomous Car and focus on the live streaming lane detection using OpenCV.</h4>
  
  
 <p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/128623886-e2144326-a462-47c9-aac2-612a97886c73.jpg">
</p> 
  
  
<h3 align="left"> Project Limitations
  
<h4 align="left"> * Three wheels were used instead of four wheels. To build a three-wheel Car, three-wheeled was to have a mounting where the third wheel could be assembled. This mount is designed based on the space available on the model car. To provide the steering, a servo motor must be fitted so that the mounting used for the steering wheel could be extended for mounting the servo motor.</h4>
  
 <p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/128624299-5317b1e7-3a50-4782-b7a8-712d9fddc145.gif">
</p> 

<h4 align="left"> * camera mounting is required to place the camera in an optimal height to get the future images which would be adjacent to the vehicle.</h4>
 
<h3 align="left"> Camera Holder</h4>
  
 <p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128624444-04313456-55c2-49fe-a04c-a23d535d910e.png">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128624392-3fa6aaec-ce00-4208-9fb8-587b618c407a.jpg">
</p> 
  
<h3 align="center"> Lane Detection</h3> 
  
<h4 align="left"> This project involves locating Blue lane lines in an image using Python and OpenCV.</h4>
 
<h3 align="left"> HSV Space</h3>
 
<p style= 'text-align: justify;'> The HSV colour space is often used in computer vision tasks because it has better performance than the RGB colour under different lighting conditions. So, firstly, the blue colour area is isolated from the original image to locate the path. RGB image, different levels of the blue tape may be lit with different light, resulting in them appearing as darker blue or light blue. However, in HSV colour space, the Hue component will render the entire blue tape as one colour regardless of its shading. To do this, with the help of the OpenCV's function is converted to the HSV space.</p>
  
<h3 align="center"> Finding HSV value</h3>   
<p align="left">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128625968-96b267d8-38cc-4193-832c-0e95342c5051.png">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/128626171-8621e60e-99e0-424c-b372-6db2f0d36873.png">
  
</p> 

  
<h3 align="left"> Mask Image</h3>
 
<p style= 'text-align: justify;'> After converting the image to HSV space, the area of the path is extracted from the blueish colours of the image. By defining the upper level and the lower-level blue values of the paths the separation is done from the HSV space image.</p>
  
  
<p align="left">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626252-98b0a5c1-5af1-465a-ae96-591cdbd2d52b.png">  
</p> 

<h3 align="left">Canny - Edge Detection</h3>
 
<p style= 'text-align: justify;'> The goal of edge detection is to identify the lane boundaries and areas within the image.Canny edge detection function is applied to get the edges or boundaries in the mask image. </p>
  
<p align="left">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626310-51c07ccb-5130-45ac-a55a-54e724c97f82.png">  
</p> 

<h3 align="left">Region of Interest</h3>
 
<p style= 'text-align: justify;'> The features of the image which contained the path are chosen. Based on the dimension matrix of the Canny image the masked image is created by replacing the values with zeros. Further, the half-height of the Canny image features is extracted by defining a polygon from the Car's edge. The original image is plotted using Matplotlib to find the coordinates for the Region of interest. By assigning the polygon on the mask image with the intensity of 255, the Region of interest is turned white. Further, a bitwise and operation is applied on the canny image and the mask image to get the final Region of interest (masked image).</p>
  
<p align="left">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626380-9dfdb503-11eb-41f3-9f8d-5b58b476538c.png">  
</p>   
 

