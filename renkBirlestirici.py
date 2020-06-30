import cv2

bgr = cv2.imread("BlueShow.jpeg") # Resimleri ayırdıktan sonra 3 kanal olarak bırakmışım bütün her pixel aynı değerden 3 tanesine sahipti bende bu unutkanlığımı avantajıma kullandım ve 3 bgr değişkenini 3 kanallı olarak tanımladım

# 3 kanallı resimleri tek kanallı hale çevirdim
blue = cv2.imread("BlueShow.jpeg", cv2.COLOR_BGR2GRAY)
green = cv2.imread("GreenShow.jpeg", cv2.COLOR_BGR2GRAY)
red = cv2.imread("RedShow.jpeg", cv2.COLOR_BGR2GRAY)

# 3 kanallı bgr'ın her kanalına doğru grayscale resimleri bastım ve 3 grayscale görüntüden renkli bir görüntü elde ettim
bgr[:,:,0] = blue
bgr[:,:,1] = green
bgr[:,:,2] = red

print("# > Image Reconstruction Started...")

while True:
    cv2.imwrite("BGRShow.jpeg", bgr)  # elde ettiğim görüntüyü yazdırdım

    if cv2.waitKey(2000): # 2 saniye sonra döngüyü bitirdim(daha havalı çünkü xd)
        break

print("! > Image Successfully Reconstructed!")
