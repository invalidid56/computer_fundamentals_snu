# mandrill.py
# 2022-14673 강준서
# Image Processing With the Python Pillow Library

from PIL import Image
import pprint

img_origin = Image.open('mandrill.png')
pxl_o = img_origin.load()
img_steg = Image.open('mandrill_stegano.png')
pxl_s = img_steg.load()

width, height = img_origin.size

temp = []
temp_r = []
temp_b = []
for h in range(0, height, 16):
    for w in range(0, width, 16):
        if w >= 48 and h >= 448:
            r, g, b = pxl_s[w, h]
            # lsb = bin(r)[-1]
            temp_r.append(bin(r)[-1])
            temp.append(g)
            temp_b.append(b)

print(temp)
# length = 16; spl = [int('0b'+''.join(temp[i:i+length]), 2) for i in range(0, len(temp), length)]
length = 16; spl = [temp[i:i+length] for i in range(0, len(temp), length)]
spl = sum(spl, [])
spl = ''.join([chr(s) for s in spl])
print(spl)

length = 16; spl = [temp_b[i:i+length] for i in range(0, len(temp), length)]
spl = sum(spl, [])
spl = ''.join([chr(s) for s in spl])
print(spl)

length = 16; spl = [temp_r[i:i+length] for i in range(0, len(temp), length)]
spl = sum(spl, [])
spl = ''.join([chr(int(s, 2)) for s in spl])
print(spl)

temp = []
for h in range(height):
    for w in range(width):
        if w and h:
            r, g, b = pxl_s[w, h]
            lsb = bin(r)[-1]
            temp.append(lsb)

temp_ = []

for h in range(height):
    for w in range(width):
        if w and h:
            r, g, b = pxl_o[w, h]
            lsb = bin(r)[-1]
            temp_.append(lsb)

temp___ = []
for t, tt in zip(temp, temp_):
    if t != tt:
        temp___.append(t)

length = 16; spl = [temp___[i:i+length] for i in range(0, len(temp___), length)]
print(spl)

