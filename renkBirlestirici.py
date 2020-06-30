import cv2

bgr = cv2.imread("BlueShow.jpeg") # I forgot the Blue one with 3 channle so I use my stupidity to my advantage and used it to reconstruct the 3 channle image :)

# Reading grayscale images
blue = cv2.imread("BlueShow.jpeg", cv2.COLOR_BGR2GRAY)
green = cv2.imread("GreenShow.jpeg", cv2.COLOR_BGR2GRAY)
red = cv2.imread("RedShow.jpeg", cv2.COLOR_BGR2GRAY)

# In this part I just insert every single grayscale image into the 3 channle image and from 3 grayscale image I generated a 1 BGR image
bgr[:,:,0] = blue
bgr[:,:,1] = green
bgr[:,:,2] = red

print("# > Image Reconstruction Started...")

while True:
    cv2.imwrite("BGRShow.jpeg", bgr)  # Just saving my masterpiece from ram to hdd

    if cv2.waitKey(2000): # Breaks the while loop after 2 seconds its complated (again its cooler this way xd)
        break

print("! > Image Successfully Reconstructed!")
