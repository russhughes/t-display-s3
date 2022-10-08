"""
scroll.py

    Smoothly scrolls all font characters up the screen on the display.

"""
import utime
import random
import st7789s3 as st7789
import tft_config

# choose a font

# import vga1_8x8 as font
# import vga2_8x8 as font
# import vga1_8x16 as font
# import vga2_8x16 as font
# import vga1_16x16 as font
# import vga1_bold_16x16 as font
# import vga2_16x16 as font
import vga2_bold_16x16 as font


def main():
    tft = tft_config.config(0)
    last_line = tft.height - font.HEIGHT
    tfa = tft_config.TFA
    tfb = tft_config.BFA
    tft.vscrdef(tfa, 320, tfb)

    tft.fill(st7789.BLUE)
    scroll = 0
    character = 0
    while True:
        tft.fill_rect(0, scroll, tft.width, 1, st7789.BLUE)

        if scroll % font.HEIGHT == 0:
            tft.text(
                font,
                '\\x{:02x}= {:s} '.format(character, chr(character)),
                0,
                (scroll + last_line) % tft.height,
                st7789.WHITE,
                st7789.BLUE)

            character = character + 1 if character < 256 else 0

        tft.vscsad(scroll + tfa)
        scroll += 1

        if scroll == tft.height:
            scroll = 0

        utime.sleep(0.01)


main()
