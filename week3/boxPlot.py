import cv2
import numpy as np

minVal = 10
masxVal = 70
q1 = 25
q3 = 45
medianVal = 30

oH = 50
oV = 400
c = 5

screen = np.zeros((500, 500, 3), dtype=np.uint8) + 255

# Sayı doğrusu çizgisi
cv2.line(screen,(oH, oV), (450, oV), (0, 0, 0), 2)
# Min-Q1 arası
cv2.line(screen, (oH + minVal*c, oV-50), (oH + q1*c, oV-50), (0, 0, 0), 2)
# Box
cv2.rectangle(screen, (oH + c*q1, oV-75), (oH + q3*c, oV-25), (0,0,0),2)
# Median
cv2.line(screen, (oH+c*medianVal, oV-75), (oH+c*medianVal, oV-25), (0, 0, 255), 2)
# Q3-Max
cv2.line(screen, (oH+c*q3, oV-50),(oH+c*masxVal, oV-50), (0,0,0), 2)

cv2.imshow("Screen", screen)
cv2.waitKey(0)
cv2.destroyAllWindows()