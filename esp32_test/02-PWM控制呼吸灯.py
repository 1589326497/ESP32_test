from machine import Pin,PWM
import time
"""
 需求:从不亮慢慢到亮  
"""

#在Pin2生成输出PWM脉冲
pwm2=PWM(Pin(2))
#设置频率
pwm2.freq(1000)

while True:
    #设置占空比 0~1023/1023
    for i in range(0,1024):
        pwm2.duty(i)
        time.sleep_ms(3)
    for i in range(1023,-1,-1):
        pwm2.duty(i)
        time.sleep_ms(3)