# COSC 2306 - Data Programming 
## Programming Assignment - 1 ##

### Due Date: February. 17, 11:59 PM ###

#### The goal of this assignment is to become familiar with manipulating arrays.  You will write a class to read, write, and manipulate images.  ####

PBM, PGM, and PPM files are all image file formats that hold data corresponding to pixels of an image. Compared to formats like PNG, JPG, etc, these formats are very simplistic, offering no compression. These are simple formats that store the colors of pixels as bytes which can be read into your program.

There are 3 types for a reason:

PBM (Portable BitMap) - 2 colours only. Black and White (0-1)
PGM (Portable GrayMap) - 255 colours only. Black-Gray-White (0-255)
PPM (Portable PixMap) - 16,777,216 colors. Colored RGB (0-255, 0-255, 0-255)

Each of these files also contain a magic number that tells if the information is stored as text or as bytes. We will primarily work with files that store pixel values as text.

We will only consider PPM and PGM files for this assignment. The format of the PPM file may look like the following:

P3<br>
3 2<br>
255<br>
255   0   0     0 255   0     0   0 255<br>
255 255   0   255 255 255     0   0   0<br>

The first 3 lines provide the attributes of the image.<br>
P3 - Magic Number (Tells the program this is a PPM file)<br>
3 - Width<br>
2 - Height<br>
255 – Value indicating the maximum bit range to represent intensity value (255 – 8-bit, 65536 – 16-bit). In representing intensity value, 0 = Black, This Number = White)

Everything beyond these numbers is pixel information about the image. The intensity value at each pixel is given by a tri-color representation – RGB.  The first value is the intensity to represent the amount of RED, the second the amount of GREEN, and the third the amount of BLUE.  Hence, the values 255 0 0 would represent the highest intensity for RED and no presence of GREEN and BLUE.

PGM files are similar to PPM files and differ only in the use of P2 as the magic number and in the fact that only one value is needed to represent each pixel's intensity considering that PGM files represent gray scale images.  Hence, the format of an example PGM file may look like the following:

P2<br>
3 2<br>
255<br>
255 128 0<br>
0 128 255<br>

The first 3 lines provide the attributes of the image.<br>
P2 - Magic Number (Tells the program this is a PGM file)<br>
3 - Width<br>
2 - Height<br>
255 – Value indicating the maximum bit range to represent intensity value (255 – 8-bit, 65536 – 16-bit). In representing intensity value, 0 = Black, This Number = White)

Everything beyond these numbers is pixel information about the image. The intensity value at each pixel is indicated by an integer in the range of 0 to the highest value possible based on the bit representation.

In this Assignment, you are given an implementation of the base class named MyImage to work with PPM and PGM images.  We will restrict ourselves to manage 8-bit representations such that the highest intensity possible for PGM images would be 255 and for PPM images would be 255 255 255.
All code is to be implemented in the files **COSC2306/MyImage.py**.  You are already given several methods within the base class to be able to read and write images.  Additional methods for manipulating image data are needed.  Methods that are already implemented include:

1. Load image from a file. <br>

2. Save image to a file. <br>

3. Create a new image.<br>

4. Get width and height of the image. <br>

5. Get value of a pixel in the image. <br>

6. Set value of a pixel in the image. <br>

7. Get sub-image values as specified by a bounding box, where the bounding box is given by starting x, y index and the width and height of the bounding box.<br>

8. Set sub-image values as specified by a bounding box, where the bounding box is given by starting x, y index and the width and height of the bounding box.<br>

You are required to write additional methods for the following:

[20 pts] 1. Convert image to a gray level image and return the new gray level image.<br>
Use the following as the formula to calculate the gray level value for each pixel having an RGB value. Please note that all pixel values should always be integers.<br>
gray_value = (R + G + B)/3<br>
Please note that all gray level values are to be integers.<br>
If the image is originally a gray level image, a new gray level image should be returned.<br>
Note that new image is to be a PGM image.<br>

[20 pts] 2. Threshold image assuming a bimodal distribution of image intensities. <br>
A threshold operation converts a gray level image into an image that has only two intensity values, 0 and 255.  
Each pixel value is either changed to 0 or 255 by comparing against the threshold value.
To threshold a gray level image, the operation to be performed is:<br>
threshold_image_pixel_value = 0; if gray_value <= N<br>
threshold_image_pixel_value = 255; if gray_value > N<br>
While a thresholded image will have only two resulting intensity values, 0 and 255, we will treat these images
as gray level images and hence would be treated as PGM images with magic number 'P2'.<br>
The threshold value `N` is to be estimated as the mean of the means, where the two means represent the average
of all intensities that are less than `N` and average of intensities greater than `N`. <br>
You will write an algorithm to iteratively estimate the value of `N` and define a stopping criterion.<br>
The method should return both the estimated threshold value and the thresholded image as a tuple. <br>

[30 pts] 3. Image rotation given an angle of rotation in degrees around the image center. <br>
You are to write a method to perform image rotation.  In general, a point (x,y) in the image is rotated 
to a new points (x', y') defined by the rotation matrix 

```math
\left(\begin{array}{cc}
cos\theta & -sin\theta\\
sin\theta & cos\theta
\end{array}\right)
```

This allows for each pixel value at position (x, y) to be mapped to the new position (x', y') in the rotated image.
Theta is the angle in radians and defines a clockwise rotation.  The image rotation method should perform an anti-clockwise
rotation and return the rotated image.<br>

[30 pts] 4. Image rotation using inverse given an angle of rotation in degrees around the image center. <br>
While performing image rotations, often times the size of the rotated image is larger than the original image
and hence results in aliasing artifacts.  To address such artifacts, image rotation can be performed by
ensuring that every grid position in the rotated image is mapped to the pixel value in the
original image.  This method should perform the image rotation using inverse mapping where every new position (x', y') is
inverse mapped to the position (x, y) in the original image to find the pixel intensity that should be assigned to 
position (x', y').  The method should return the rotated image.<br>

**Note:**

Do not use any in-built functions or external modules/libraries for image operations (E.g: np.mean, PIL). In general, you can use function from math library. <br/>
**Only Functions allowed** for this part are: np.array(), np.matrix(), np.zeros(), np.ones(), np.reshape().
   
  - Please do not change the code structure.
  - Usage:
   
        - python ca_01.py -i <image-name> -d 0
        - Example: python ca_01.py -i Images/cells-1.ppm -d 0
  - Please make sure the code runs when you run the above command from prompt/terminal
  - All the output images and files are saved to "output/" folder
  - You can set the value of -d to 1 if you would like to display images so you can verify them
  - In this case, the example usage would be:
  
        - Example: python ca_01.py -i Images/cells-1.ppm -d 1

Two images are provided for testing: Images\cells-1.ppm, Images\cells-2.ppm and Images\cells-3.ppm.<br>

**PS. Please do not change: ca_01.py, requirements.txt, and Jenkinsfile.**

-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the Data Programming course offered at University of Houston. The contents are not to be reproduced and shared with anyone with out the permission of the author. The contents are not to be posted on any online public hosting websites without the permission of the author. The software is cloned and is available to the students for the duration of the course. At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>
