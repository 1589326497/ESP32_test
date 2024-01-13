import random
from machine import Pin, SPI
import st7789_itprojects as st7789
import st7789py
from romfonts import vga2_bold_16x32 as font
import time


# 解决第1次启动时，不亮的问题
st7789.ST7789(SPI(2, 60000000), dc=Pin(2), cs=Pin(5), rst=Pin(15))

# 创建显示屏对象
tft = st7789py.ST7789(SPI(2, 60000000), 240, 240, reset=Pin(15), dc=Pin(2), cs=Pin(5), rotation=0)

# 屏幕背景显示
#tft.fill(st7789py.color565(0,0,255))

# 某个点
#tft.pixel(100,100,st7789.color565(255, 0, 0))
# 显示Hello
# tft.text(font, "Hello world", 0, 0, st7789py.color565(255, 0, 0), st7789py.color565(0, 0, 255))

text=['Hello.',"tell you.","I like you!."]

def show_text():
    i=0
    for rotation in range(4):
        tft.rotation(rotation)
        tft.fill(0)
        col_max = tft.width - font.WIDTH*len(text[0])
        row_max = tft.height - font.HEIGHT

        if i<3:
                for _ in range(100):
                    tft.text(
                        font,
                        text[i],
                        random.randint(0, col_max),
                        random.randint(0, row_max),
                        st7789py.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)),
                        st7789py.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
                    )
                tft.fill(st7789py.color565(0,0,255))
                tft.rotation(0)
                tft.text(font,text[i],30,80,st7789py.color565(255, 0, 0),st7789py.color565(0, 0, 255))
                i+=1
                time.sleep(3)

def main():  
    # 随机显示
    while True:
       show_text()

if __name__=="__main__":
    main()


