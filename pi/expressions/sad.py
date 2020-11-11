import time

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.3)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff),
    (0xff, 0xff, 0xff)
]


def sad():
  r, g, b = colours[3]

  rgbmatrix5x5.set_pixel(2, 0, r, g, b)

  rgbmatrix5x5.set_pixel(1, 1, r, g, b)
  rgbmatrix5x5.set_pixel(1, 2, r, g, b)
  rgbmatrix5x5.set_pixel(1, 3, r, g, b)

  rgbmatrix5x5.set_pixel(2, 4, r, g, b)

  rgbmatrix5x5.show()

#sad()
#time.sleep(3)
