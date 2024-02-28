import cv2


""" 
// Resim Okuma
"""
# img = cv2.imread("Necati.jpg")
# print(img)


# if img is None:
#     print("Görüntü Yüklenemedi. Dosya yolunu kontrol et.")
# else:
#     cv2.namedWindow("Necati", cv2.WINDOW_NORMAL)
#     cv2.imshow("Necati",img)
#     cv2.imwrite("../Images/animal.jpg", img)
#     cv2.waitKey(0)
#     # cv2.destroyAllWindow()


""" 
// Video Okuma
"""
#Kameradan
movie = cv2.VideoCapture(0)

while True:
    state, frame = movie.read()
    frame = cv2.flip(frame, 1) # Aynalama yapar. 1 yerine 0 değeri de verilebilir. 0 X eksenine göre aynalar. 1 Y eksenine göre aynalar.
    cv2.imshow("Live Cam" ,frame)
    cv2.waitKey(25)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

movie.release()
# cv2.destroyAllWindow()
