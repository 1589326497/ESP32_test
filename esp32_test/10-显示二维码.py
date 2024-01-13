from uQR import QRCode
from machine import Pin, SPI
import st7789_itprojects


tft = st7789_itprojects.ST7889_Image(SPI(2, 60000000), dc=Pin(2), cs=Pin(5), rst=Pin(15))
tft.fill(st7789_itprojects.color565(255, 255, 255))  # 背景设置为白色


qr = QRCode(border=2)
qr.add_data('宁子希')  # 这里是要生成的二维码，被扫码之后的得到的内容
matrix = qr.get_matrix()

row_len = len(matrix)
col_len = len(matrix[0])

# 放大倍数
# 默认情况下输出的二维码太小，可以按照你实际屏幕的大小进行缩放，当前我的240x240屏幕缩放8倍正合适
scale_rate = 10

for row in range(row_len * scale_rate):	#25x10
    for col in range(col_len * scale_rate):
        if matrix[row//scale_rate][col//scale_rate]:
            tft.pixel(row, col, st7789_itprojects.color565(0, 0, 0))
        else:
            tft.pixel(row, col, st7789_itprojects.color565(255, 255, 255))
        col += 1
    row += 1
