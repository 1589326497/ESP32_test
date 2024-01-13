#让esp32链接wifi，让其拥有ip地址
#创建UDP socket
#接收UDB数据
#根据接收到的数据控制亮灭
import network
import time
import socket
import machine
def do_connect():
    #链接wifi网络
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('HUAWEI-NZX_2.4G', '987654321')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
def start_udp():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("0.0.0.0", 7788))	#"0.0.0.0"接受所有的ip
    return udp_socket

def main():
    #连接wifi
    do_connect()
    #创建udp对象
    udp_socket=start_udp()
    #创建GPIO对象
    pin2=machine.Pin(2,machine.Pin.OUT)
    #接收udp数据
    while True:
        recv_data,sender_info=udp_socket.recvfrom(1024)
        print("{}发送的数据：{}".format(sender_info,recv_data))
        recv_data_str=recv_data.decode("utf-8")	#解码
        print("解码后的数据：{}".format(recv_data_str))
        #根据解码后的udp数据控制led
        if recv_data_str =='on':
            pin2.value(1) 
        elif recv_data_str=='off':
            pin2.value(0) 
    
    
    

if __name__ == "__main__":
    main()

