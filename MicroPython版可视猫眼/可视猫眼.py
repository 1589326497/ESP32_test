from machine import Pin,SPI
import st7789py as st7789
import camera,time,image


spi = SPI(2, baudrate=20000000, polarity=1, sck=Pin(12), mosi=Pin(13))
tft = st7789.ST7789(spi, 320,240, reset=Pin(15, Pin.OUT), dc=Pin(14, Pin.OUT),backlight=Pin(2,Pin.OUT))
tft.rotation(3)
tft.fill(st7789.BLUE)
tft.inversion_mode(0)
tft._set_color_mode(st7789.COLOR_MODE_16BIT)

camera.init(0,format=0)
camera.mirror(0)
face_cascade = image.HaarCascade("frontalface", stages=25)


while True:
    ea=camera.capture()
    byte_arr = ea.to_bytes()
    tft.blit_buffer(byte_arr, 0, 0, 320, 240)
    
