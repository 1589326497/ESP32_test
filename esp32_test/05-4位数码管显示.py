import machine
import time

led1=machine.Pin(5,machine.Pin.OUT,value=1)
led2=machine.Pin(18,machine.Pin.OUT,value=1)
led3=machine.Pin(19,machine.Pin.OUT,value=1)
led4=machine.Pin(21,machine.Pin.OUT,value=1)



a = machine.Pin(13, machine.Pin.OUT)
b = machine.Pin(12, machine.Pin.OUT)
c = machine.Pin(14, machine.Pin.OUT)
d = machine.Pin(27, machine.Pin.OUT)
e = machine.Pin(26, machine.Pin.OUT)
f = machine.Pin(25, machine.Pin.OUT)
g = machine.Pin(33, machine.Pin.OUT)
dot = machine.Pin(32, machine.Pin.OUT)
#将对应的引脚对象存放到链表中
number_led = [a, b, c, d, e, f, g]
led_list=[led1,led2,led3,led4]

number_dict = {
    0: "1111110",
    1: "0110000",
    2: "1101101",
    3: "1111001",
    4: "0110011",
    5: "1011011",
    6: "1011111",
    7: "1110000",
    8: "1111111",
    9: "1111011",
    "open": "1111111",
    "close": "0000000"
}
#数码管显示函数 number为数字 switch为小数点
def show_number(number,switch=False):
  if number_dict.get(number): #判断number是否为字典中的key
    i=0
    for num in number_dict.get(number):   #取出value 遍历字符串
        if num=='1':
          number_led[i].value(1)
        else:
          number_led[i].value(0)
        i+=1
  if switch:
    dot.value(1)
  else:
    dot.value(0)


#数码管4位显示函数 number为数字 switch为小数点
def show_4_number(number,switch=False):
  if 0<= number<=9999: #判断number是否为字典中的key
    i=0
    for num in "%04d" % number:
        for led in led_list:    #位选全部清空
            led.value(1)
        show_number(int(num))   #显示对应位的数
        led_list[i].value(0)    #选位 先显示对应位的数在选位 要不然会短暂的显示上一个数
        i+=1
        time.sleep_ms(10)   #延迟10ms




def main():
    while True:
        show_4_number(6754)
  

if __name__ == "__main__":
  main()


