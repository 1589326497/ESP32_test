import cv2
import socket
import io
import numpy as np
import os
from PIL import Image
# coding=utf-8
import urllib
import urllib.request
import hashlib

aa = 0

#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')
names=[]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
#s.bind(("192.168.31.230",9090)) #办公室局域网
s.bind(("192.168.43.132",9090))#WiFi热点

#准备识别的图片
def face_detect_demo(img):
    global aa
    #print("aa=",aa)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
    #face_detector=cv2.CascadeClassifier('C:/Users/cktn/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face_detector = cv2.CascadeClassifier('C:/Users/cktn/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    #face=face_detector.detectMultiScale(gray)
    if len(face) == 0:
        # s.sendto(b'4', ("192.168.31.137", 9090))#办公室局域网
        s.sendto(b'4', ("192.168.43.228", 9090))
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        if confidence > 85:
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            #s.sendto(b'4', ("192.168.31.137", 9090))
            print("4444444444")
            s.sendto(b'4', ("192.168.43.228", 9090))
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            #s.sendto(b'3', ("192.168.31.137", 9090))
            s.sendto(b'3', ("192.168.43.228", 9090))
            print("3333333333")
    cv2.imshow('result',img)

    #print('bug:',ids)
    aa += 1

def name():
    path = './img/'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


#cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture('1.mp4')
name()
while True:
    data, IP = s.recvfrom(100000)
    bytes_stream = io.BytesIO(data)
    image = Image.open(bytes_stream)
    img = np.asarray(image)
    face_detect_demo(img)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
#cap.release()
#print(names)
