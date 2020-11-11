import time

from rgbmatrix5x5 import RGBMatrix5x5


rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.3)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff)
]


def cross():

  r, g, b = colours[0]

  rgbmatrix5x5.set_pixel(0, 0, r, g, b)
  rgbmatrix5x5.set_pixel(1, 1, r, g, b)
  rgbmatrix5x5.set_pixel(2, 2, r, g, b)
  rgbmatrix5x5.set_pixel(3, 3, r, g, b)
  rgbmatrix5x5.set_pixel(4, 4, r, g, b)
  rgbmatrix5x5.set_pixel(1, 3, r, g, b)
  rgbmatrix5x5.set_pixel(0, 4, r, g, b)
  rgbmatrix5x5.set_pixel(3, 1, r, g, b)
  rgbmatrix5x5.set_pixel(4, 0, r, g, b)

  rgbmatrix5x5.show()

#  time.sleep(1)
#  rgbmatrix5x5.clear()
  return
