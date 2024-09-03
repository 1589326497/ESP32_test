import cv2 as cv
import socket
import io
import numpy as np
import os
from PIL import Image


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
#s.bind(("192.168.31.230",9090))
s.bind(("192.168.43.132",9090))#WiFi热点

#cap = cv.VideoCapture(0)

flag = 1
num = 1

while True:#检测是否在开启状态
    data, IP = s.recvfrom(100000)
    bytes_stream = io.BytesIO(data)
    image = Image.open(bytes_stream)
    Vshow = np.asarray(image)
    cv.imshow("Capture_test",Vshow)#显示图像
    k = cv.waitKey(1) & 0xFF
    if k == ord('s'):
        cv.imwrite("img/"+str(num)+".jim"+".jpg",Vshow)
        print("success to save"+str(num)+".jpg")
        print("--------")
        num +=1
    elif k == ord(' '):
        break

#释放摄像头
#cap.release()
cv.destroyAllWindows()