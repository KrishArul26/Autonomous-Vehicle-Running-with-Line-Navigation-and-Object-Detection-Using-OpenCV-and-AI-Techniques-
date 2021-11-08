<h2 align="center"> Live-streaming-Autonomous-Vehicle-running-With-line-detection-using-OpenCV</h2>

 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/128628482-a327be8f-5cdb-41ce-9af2-a93bc327814c.gif">
</p> 

<h4 align="center"> <span style="color:green">Line detection/OpenCV/ SSD_mobilenet, Keras/TensorFlow/ Deep Learning and Computer Vision </span></h4>

<h3 align="left">Introduction</h3>
 
<p style= 'text-align: justify;'> Mobility on a wide scale is moving towards complete automation. Though the technology for automating the vehicles already exists, these technologies must be optimised to fit the current environment.  This project would be a scaled-down model of the Autonomous Car and focus on the live streaming lane detection using OpenCV.</p>

  
 <p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/128623886-e2144326-a462-47c9-aac2-612a97886c73.jpg">
</p> 
 
  
<h3 align="left"> Project Limitations
 
 <p style= 'text-align: justify;'> T* Three wheels were used instead of four wheels. To build a three-wheel Car, three-wheeled was to have a mounting where the third wheel could be assembled. This mount is designed based on the space available on the model car. To provide the steering, a servo motor must be fitted so that the mounting used for the steering wheel could be extended for mounting the servo motor.</p>
  
  
 <p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/128624299-5317b1e7-3a50-4782-b7a8-712d9fddc145.gif">
</p> 

<h4 align="left"> * camera mounting is required to place the camera in an optimal height to get the future images which would be adjacent to the vehicle.</h4>
 
<h3 align="left"> Camera Holder</h4>
  
 <p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128624444-04313456-55c2-49fe-a04c-a23d535d910e.png">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128624392-3fa6aaec-ce00-4208-9fb8-587b618c407a.jpg">
</p> 
  
 ### 🔑 Prerequisites
 
* [Freenove 4WD Smart Car Kit](https://www.amazon.de/-/en/Freenove-Raspberry-Avoidance-Colourful-Ultrasonic/dp/B07YD2LT9D/ref=sr_1_5?crid=3VP3TDHEI052K&dchild=1&keywords=pi%20car%20kit&qid=1628421094&sprefix=pi%20car,aps,194&sr=8-5)

 ### 🚀 Initialization For Running the car Autonomously
 
 1. Clone the repo with local computer

```
git clone https://github.com/KrishArul26/Live--streaming-Autonomous-Vehicle-running-With-line-detection-using-OpenCV.git

```
 2. Connect the raspberry Module with local computer via Power shell(with wireless network)

```
ssh pi@car_name
``` 
 3.Navigate the Raspberry Module code directory 

```
cd ...
```  
```
cd share/Code
```  
4. For running the car: Run the main.py

```
sudo python main.py
```  
4. For visualization on the browser to see line detection: Run the app.py
 
```
sudo python app.py
``` 
 
<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128630468-f4e658c5-f878-4ae9-af5a-9fe3c541ddb8.jpg">
</p>
<h2 align="center"> Results</h2> 
    
<h4 align="left"> This project involves locating Blue lane lines in an image using Python and OpenCV.</h4>
 
<h3 align="left"> HSV Space</h3>
 
<p style= 'text-align: justify;'> The HSV colour space is often used in computer vision tasks because it has better performance than the RGB colour under different lighting conditions. So, firstly, the blue colour area is isolated from the original image to locate the path. RGB image, different levels of the blue tape may be lit with different light, resulting in them appearing as darker blue or light blue. However, in HSV colour space, the Hue component will render the entire blue tape as one colour regardless of 
its shading. To do this, with the help of the OpenCV's function is converted to the HSV space.</p>
  
<h3 align="center"> Finding HSV value</h3>   
<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128625968-96b267d8-38cc-4193-832c-0e95342c5051.png">
 
</p> 

  
<h3 align="left"> Mask Image</h3>
 
<p style= 'text-align: justify;'> After converting the image to HSV space, the area of the path is extracted from the blueish colours of the image. By defining the upper level and the lower-level blue values of the paths the separation is done from the HSV space image.</p>
  
  
<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626252-98b0a5c1-5af1-465a-ae96-591cdbd2d52b.png">  
</p> 

<h3 align="left">Canny - Edge Detection</h3>
 
<p style= 'text-align: justify;'> The goal of edge detection is to identify the lane boundaries and areas within the image.Canny edge detection function is applied to get the edges or boundaries in the mask image. </p>
  
<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626310-51c07ccb-5130-45ac-a55a-54e724c97f82.png">  
</p> 

<h3 align="left">Region of Interest</h3>
 
<p style= 'text-align: justify;'> The features of the image which contained the path are chosen. Based on the dimension matrix of the Canny image the masked image is created by replacing the values with zeros. Further, the half-height of the Canny image features is extracted by defining a polygon from the Car's edge. The original image is plotted using Matplotlib to find the coordinates for the Region of interest. By assigning the polygon on the mask image with the intensity of 255, the Region of interest is turned white. Further, a bitwise and operation is applied on the canny image and the mask image to get the final Region of interest (masked image).</p>
  
<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/74568334/128626380-9dfdb503-11eb-41f3-9f8d-5b58b476538c.png">  
</p>   
 
<h3 align="left">Hough Transform</h3>
 
<p style= 'text-align: justify;'> In the Hough Space, a point is plotted if the y-intercept and the slopes are known. With changing m(Slope) and b(Intercept) values, there is 
 a possibility to plot different lines. To identify the lines, firstly, the Hough space is split into a grid. Each bin inside the grid corresponding to the slope and y-intercept value of the line. For every point of intersection in a Hough Space bin, a vote is to be cast inside of the bin to which it belongs. The bin with the maximum number of votes will be the resulting line. OpenCV contains Hough Transform, which performs this process. The function HoughLinesP essentially tries to fit many lines through all the white pixels and return the most likely set of lines, subject to certain minimum threshold constraints.</p>

 <h3 align="left">Average Slope-Intercept</h3>
 
<p style= 'text-align: justify;'> Subsequently, the left lane line and right lane line (according to the Car) consists of multiple discontinuous lines. Therefore, the average slope and intercept are calculated to combine these lines into one left lane line and the right lane line.</p>
  
<p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128626480-60770c20-250b-41a1-9b46-62cf9f57b421.png">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128626478-e44c5334-32b7-4105-bf3f-bea5ab96c918.png"
</p>   
  
<h3 align="left">Steering Angles</h3>
 
<p style= 'text-align: justify;'> The steering angle is calculated based on three different scenarios; these are: 
"both lines detection condition", "only the left line detection condition" and "only right line detection condition”.</p>
 
 <h3 align="left">both lines detection condition</h3>
 
<p style= 'text-align: justify;'>If both lines are detected by the program, firstly the X-coordinate of the left line and right line are separated from their corresponding lines and X offset is calculated using the equation “((left_x2+right_x2)-width)/(height)”. Trigonometry is used to find the angle is from the vertical axis.</p> 
  
<p align="center">
  <img width="550" src="https://user-images.githubusercontent.com/74568334/128626623-ea98c431-638d-4c39-9813-189b1cae83b2.png">
</p>    
  
<h3 align="left">one line detection condition</h3>
 
<p style= 'text-align: justify;'>If one line is detected by the program,firstly the X-coordinate of the left line or right line are separated from their corresponding lines and X offset is calculated using the equation"(left_x2-left_x1)/(height/2)" or "(right_x2-right_x1)/(height/2)".Trigonometry is used to find the angle is from the vertical axis.</p> 
  
<p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128626939-6808d58a-640b-4038-a156-5a49cb447f15.png">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/128626940-29c7ed9f-b32a-4c0b-a191-8212d8736e30.png">
</p>    
  
<h3 align="center">Clockwise Testing Results</h3>  
  
 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/128627857-77f03478-be80-4788-8ad7-122eee4f20dd.gif">
</p>  
  
 <h3 align="center">Anti Clockwise Testing Result</h3>  
  
 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/128627942-48f66816-8631-46f1-958b-925a182839b4.gif">
</p>  
  
  
