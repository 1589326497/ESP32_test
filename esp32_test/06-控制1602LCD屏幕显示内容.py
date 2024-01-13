import time
from machine import SoftI2C, Pin
from esp32_i2c_1602lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27 #I1602C 地址为 0x27
#创建软I2C对象
i2c = SoftI2C(sda=Pin(15),scl=Pin(2),freq=100000)
#创建LCD1602对象
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def main():
    i=0
    while True:
        lcd.clear()
        lcd.putstr("time {}\n".format(i))
        lcd.putstr("hello world")
        time.sleep(1)
        i+=1

if __name__ =="__main__":
    main()


# SDA GPIO15
# SCL GPIO2
# Vcc 5V （3V显示不清楚）
# GND GND