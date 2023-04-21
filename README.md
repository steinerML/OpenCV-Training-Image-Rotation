# OpenCV Image Rotation
Image rotation using OpenCV.
## Contents :
I have used the following functions/methods:

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.VideoCapture | Creates a video capture object, which would help stream or display the video.|
|cv2.VideoWriter  | Saves the output video to a directory.                                       |
|     cv2.imshow()|  Displays image.                                                             |
|    cv2.waitKey()|  Wait for key.                                                               |
|     get()       |  Retrieves video metadata                                                    |



## Test Image used: 
I have used image-15.png that can be found in the repository.

![Source Image Sequence](image-15.png)
![Source Image Sequence](rotated_image.jpg)
## Summary:

```python
#Slicing to crop the image
cropped_image = img[80:280, 150:330]

```
