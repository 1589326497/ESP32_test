import socket
import network
import camera
import time
import machine
 
#连接wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    #wlan.connect('CKTN', '18900744765')
    wlan.connect('xiao', '12345678')
    
    while not wlan.isconnected():
        pass
print('网络配置:', wlan.ifconfig())

 
#摄像头初始化
try:
    camera.init(0, format=camera.JPEG)
except Exception as e:
    camera.deinit()
    camera.init(0, format=camera.JPEG)
 
 
#图像设置----------------------------  
  
## Other settings:
# flip up side down
camera.flip(0)
# left / right
camera.mirror(1)
 
# framesize
camera.framesize(camera.FRAME_VGA)
# The options are the following:
# FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
# FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
# FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA FRAME_FHD
# FRAME_P_HD FRAME_P_3MP FRAME_QXGA FRAME_QHD FRAME_WQXGA
# FRAME_P_FHD FRAME_QSXGA
# Check this link for more information: https://bit.ly/2YOzizz
 
# special effects
camera.speffect(camera.EFFECT_NONE)
# The options are the following:
# EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO
 
# white balance
camera.whitebalance(camera.WB_NONE)
# The options are the following:
# WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME
 
# saturation
camera.saturation(0)
# -2,2 (default 0). -2 grayscale 
 
# brightness
camera.brightness(0)
# -2,2 (default 0). 2 brightness
 
# contrast
camera.contrast(0)
#-2,2 (default 0). 2 highcontrast
 
# quality
camera.quality(10)
# 10-63 lower number means higher quality
 
#图像设置----------------------------   
 
 
#socket UDP 的创建
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)


while True:
    buf = camera.capture() # 获取图像数据
    #s.sendto(buf,("192.168.31.230",9090)) # 向服务器发送图像数据
    s.sendto(buf,("192.168.43.132",9090)) # 手机热点
    time.sleep(0.1)
 
 
 
 
 
