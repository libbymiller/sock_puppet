import smile
import sad
import grin
import grimace
import question
import bit_sad
import small_neutral
import very_sad
import cross
import neutral
import tick
import speak1
import speak2

import time
from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.3)

height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff),
    (0xff, 0xff, 0xff)
]

def wait_clear(t):
  time.sleep(t)
  rgbmatrix5x5.clear()
  rgbmatrix5x5.show()

smile.smile()
wait_clear(1)
sad.sad()
wait_clear(1)
grimace.grimace()
wait_clear(1)
bit_sad.bit_sad()
wait_clear(1)
small_neutral.small_neutral()
wait_clear(1)
very_sad.very_sad()
wait_clear(1)
neutral.neutral()
wait_clear(1)
grin.grin()
wait_clear(1)
cross.cross()
wait_clear(1)
tick.tick()
wait_clear(1)
question.question()
wait_clear(1)
speak1.speak1()
wait_clear(0.1)
speak2.speak2()
wait_clear(0.1)
speak1.speak1()
wait_clear(0.1)
speak2.speak2()
wait_clear(0.1)
speak1.speak1()
wait_clear(0.1)
speak2.speak2()
wait_clear(0.1)
speak1.speak1()
wait_clear(0.1)
speak2.speak2()
wait_clear(0.1)
speak1.speak1()
wait_clear(0.1)
speak2.speak2()
wait_clear(0.1)
