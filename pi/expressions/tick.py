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


def tick():
  r, g, b = colours[1]

#  rgbmatrix5x5.set_pixel(1, 4, r, g, b)
#  rgbmatrix5x5.set_pixel(0, 3, r, g, b)
#  rgbmatrix5x5.set_pixel(1, 2, r, g, b)
#  rgbmatrix5x5.set_pixel(2, 1, r, g, b)
#  rgbmatrix5x5.set_pixel(3, 0, r, g, b)

  rgbmatrix5x5.set_pixel(3, 0, r, g, b)
  rgbmatrix5x5.set_pixel(4, 1, r, g, b)
  rgbmatrix5x5.set_pixel(3, 2, r, g, b)
  rgbmatrix5x5.set_pixel(2, 3, r, g, b)
  rgbmatrix5x5.set_pixel(1, 4, r, g, b)


  rgbmatrix5x5.show()

#  time.sleep(0.5)
#  rgbmatrix5x5.clear()
#  rgbmatrix5x5.show()
