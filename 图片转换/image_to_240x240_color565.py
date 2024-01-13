import struct
import numpy as np
from PIL import Image  # PIL就是pillow库
#将图片转化为二进制

def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3


def main():
    for i in range(0,13):
        img = Image.open("gif/gif1-{}.jpg".format(i))
        print(img.format, img.size, img.mode)
        img_data = np.array(img)  # 240行240列有3个 240x240x3

        with open("text_img{}.dat".format(i), "wb") as f:
            for line in img_data:
                for dot in line:
                    f.write(struct.pack("H", color565(*dot))[::-1])


if __name__ == '__main__':
    main()
