import cv2


""" 
// Resim Okuma
"""
img = cv2.imread("Necati.jpg")
print(img)


if img is None:
    print("Görüntü Yüklenemedi. Dosya yolunu kontrol et.")
else:
    cv2.namedWindow("Necati", cv2.WINDOW_NORMAL)
    cv2.imshow("Necati",img)
    cv2.imwrite("../Images/animal.jpg", img)
    cv2.waitKey(0)
    # cv2.destroyAllWindow()