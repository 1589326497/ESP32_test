import time
import network
import machine
import socket


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('dongfeiqiu', 'wangmingdong1225')
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())


# 0. 链接wifi
do_connect()

# 1. 创建TCP套接字
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息
server_s.bind(("", 8080))

# 3. 设置为被动的
server_s.listen(128)

print("等待对方链接...")

# 4. 等待客户端链接
new_s, client_info = server_s.accept()

print("等待对方发送图片数据...")

# 3. 创建文件，接收数据
with open("text_img.dat", "wb") as f:
    for i in range(240):
        # 3.1 接收数据
        data = new_s.recv(480)  # 240*2=480 一行有240个点，每个点有2个字节
        # 3.2 写到文件
        f.write(data)
        print("接收第%d行" % (i+1))

print("接收完毕")

# 7. 关闭套接字
new_s.close()
server_s.close()

