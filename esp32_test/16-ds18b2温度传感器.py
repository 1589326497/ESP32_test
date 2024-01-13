from machine import Pin
import onewire, ds18x20
import time


GP_ds = Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(GP_ds))


def read_ds_sensor():
    roms = ds_sensor.scan()
    print('发现设备: ', roms)   #打印18B20传感器地址
    ds_sensor.convert_temp()    #转换当前温度
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        if isinstance(temp, float):
            temp = round(temp, 2)
            return temp
    
def main():
    while True:
        print(read_ds_sensor())
        time.sleep(1)

if __name__ == "__main__":
    main()



