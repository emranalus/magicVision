import cv2

img = cv2.imread("bgrMerch.jpeg") # kaynak resmim
print(img.shape)

# BGR - Blue Green Red - 0 1 2
# Renk kanallarını tanımladım
blue_channle = img[:,:,0]
green_channle = img[:,:,1]
red_channle = img[:,:,2]

print("# > Color Extraction Started!")

while True:

    cv2.imwrite("BlueShow.jpeg", blue_channle) # Mavi kanalı ayırıp resim haline getirdim
    cv2.imwrite("GreenShow.jpeg", green_channle) # Yeşil kanalı ayırıp resim haline getirdim
    cv2.imwrite("RedShow.jpeg", red_channle) # Kırmızı kanalı ayırıp resim haline getirdim


    if cv2.waitKey(2000): # 2s sonra döngüyü durduyor(daha havalı oluyor xd)
        break

print("! > Color Extraction Ended Shutting Down...")
