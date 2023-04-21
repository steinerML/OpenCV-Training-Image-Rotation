import cv2

#We read the image
image = cv2.imread('image-15.png')

#We get the dimensions of the image with the shape() function through a tuple!
height, width = image.shape[:2]
print("Width:", width ,"Height:",height)

#We calculate the center of the image that will allow us to set a reference point (0,0)
center = (width/2,height/2)

# By using getRotationMatrix2D() we get the rotation matrix :)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
 
#We rotate the image using cv2.warpAffine
#We could have used the borderMode or borderValue if we wished.
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

#print images
cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)

# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)

# save the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)

cv2.waitKey(0)