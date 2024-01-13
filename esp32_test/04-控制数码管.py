import machine
import time

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
def show_number(number,switch):
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


def main():
  #数码管循环显示1~9
  while True:
    for i in range(0,10):
      show_number(i,True)
      time.sleep(1)
    for i in range(9,-1,-1):
      show_number(i,True)
      time.sleep(1)

if __name__ == "__main__":
  main()

