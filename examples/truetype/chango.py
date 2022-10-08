"""
chango.py

    Test for font2bitmap converter for the driver.
    See the font2bitmap program in the utils directory.
"""
import gc
import st7789s3 as st7789
import tft_config

import chango_16 as font_16
import chango_32 as font_32
import chango_64 as font_64

gc.collect()


def main():
    # enable display and clear screen
    tft = tft_config.config(1)
    tft.fill(st7789.BLACK)

    row = 0
    tft.write(font_16, "abcdefghijklmnopqrst", 0, row, st7789.RED)
    row += font_16.HEIGHT

    tft.write(font_32, "abcdefghij", 0, row, st7789.GREEN)
    row += font_32.HEIGHT

    tft.write(font_64, "abcd", 0, row, st7789.BLUE)
    row += font_64.HEIGHT


main()
