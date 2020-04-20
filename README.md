# Autonomous-Vehicle-Navigation
Requirements: Pycharm IDE, Python 3.8, Numpy, OpenCV, Matplotlib

Following approaches were implemented while analyzing and leveraging image and video data to help computer equipped camera in road monitoring and traffic analysis.

#Object/Obstacle Detection:
•	Calibrated Cameras and Read Images using Python.

•	Performed  Thresh-holding and Morphological image processing operations such as Erosion, dilation for feature extraction and image segmentation

•	Pixel level analysis was applied to identify certain pixel structures on sample image

•	Integrated image filtering (Smoothing and Blurring) algorithms such as Gaussian, Median and Bilateral filters to remove noise 
(unwanted pixels) from the image.

•	Adopted the use of Canny edge detection Algorithm to sketch out the contours of the road obstacles

#Obstacle Tracking:

Amalgamated aforementioned techniques to detect obstacles in video model 

•	Experimented with 2d bounding boxes for obstacle detection and localization

•	Employed the use of Haar Cascade Algorithm for tracking motion of vehicles

•	Used  these algorithmic models to enable monocular vehicle camera  to estimate distance and predict potential positions of vehicles/obstacles  in future frames

•	Used Hough Transform for road lane line detection


Road Lane Line detection on a video
![Screenshot (49)](https://user-images.githubusercontent.com/63878323/79710727-b99e4600-827a-11ea-8981-301c696fb6e6.png)
![Screenshot (57)](https://user-images.githubusercontent.com/63878323/79710743-c3c04480-827a-11ea-908f-654a0d19a098.png)

Edge Detection
![Screenshot (50)](https://user-images.githubusercontent.com/63878323/79710763-cae75280-827a-11ea-81d2-a3273dc0e18a.png)

Object Tracking
![Screenshot (58)](https://user-images.githubusercontent.com/63878323/79710786-e3f00380-827a-11ea-8d0e-a743e9e1a451.png)

Digital Image Processing
![Screenshot (55)](https://user-images.githubusercontent.com/63878323/79710798-ed796b80-827a-11ea-878c-634627c47349.png)

 Morphological Operations
![Screenshot (56)](https://user-images.githubusercontent.com/63878323/79710801-ee120200-827a-11ea-96da-880ae11dee0e.png)
