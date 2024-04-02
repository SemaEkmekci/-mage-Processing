import cv2
"""
### Resim Okuma ###
img = cv2.imread("kertenkele.jpg")
img2 = cv2.imread("../Images/tom.jpg", cv2.IMREAD_GRAYSCALE)
#print(img)

cv2.namedWindow("Animal", cv2.WINDOW_NORMAL)
cv2.imshow("Animal", img)
# cv2.imwrite("../Images/animal.jpg", img)

cv2.imshow("Tom", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


### Video Okuma ###
# Kameradan
movie = cv2.VideoCapture(0)

while True:
    state, frame = movie.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Live Cam", frame)
    cv2.waitKey(25)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindows()
"""

# Kayıtlı vide okuma
movie = cv2.VideoCapture("../Movies/kopek.mp4")
while True:
    state, frame = movie.read()
    if state == 0:
        break
    frame = cv2.resize(frame, (480, 480))
    cv2.imshow("Animal", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindows()
