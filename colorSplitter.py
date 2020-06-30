import cv2

img = cv2.imread("BGR_Original.jpeg") # Source image
print(img.shape)

# BGR - Blue Green Red - 0 1 2
# I defined all color channels a seperate variable
blue_channle = img[:,:,0]
green_channle = img[:,:,1]
red_channle = img[:,:,2]

print("# > Color Extraction Started!")

while True:

    cv2.imwrite("BlueShow.jpeg", blue_channle) # I merged Blue channels and made it a unique grayscale image
    cv2.imwrite("GreenShow.jpeg", green_channle) # I merged Green channels and made it a unique grayscale image
    cv2.imwrite("RedShow.jpeg", red_channle) # I merged Red channels and made it a unique grayscale image


    if cv2.waitKey(2000): # Breaks the while loop after 2 second its complated (Its cooler this way xd)
        break

print("! > Color Extraction Ended Shutting Down...")
