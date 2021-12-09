import cv2
import numpy as np

def display_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

sun_image = cv2.imread("images/sun_image_3.jpg")
cv2.imshow("Original Image", sun_image)
cv2.waitKey(0)
grayscale_sun = cv2.cvtColor(sun_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale sun image", grayscale_sun)
cv2.waitKey(0)

(min_intensity, max_intensity, min_loc, max_loc) = cv2.minMaxLoc(grayscale_sun)
print(f"Max intensity: {max_intensity} & Min intensity: {min_intensity}")
print(f"Max intensity Location: {max_loc} & Min intensity Location: {min_loc}")
sun_image[min_loc[1], min_loc[0]] = (0, 0, 0)
sun_image = cv2.circle(sun_image, max_loc, 20, (0, 0, 0), 5)
display_image("Max Intensity", sun_image)

width = sun_image.shape[1]
height = sun_image.shape[0]

for row in range(height-1):
    for col in range(width-1):
        if (grayscale_sun[row, col] <= max_intensity - 10):
            grayscale_sun[row, col] = 0
        else:
            grayscale_sun[row, col] = 255

binary_sun = grayscale_sun
display_image("Binary Image", binary_sun)

for row in range(height-1):
    for col in range(width-1):
        if (binary_sun[row, col] == 255):
            break
    if (binary_sun[row, col] == 255):
            print(row)
            print(col)
            break

cv2.destroyAllWindows()

