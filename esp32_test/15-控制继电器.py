from machine import Pin


p13 = Pin(13, Pin.OUT)
p13.value(1)  # 吸合
# p13.value(0)  # 断开
