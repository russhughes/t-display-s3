"""
fonts.py

    Pages through all characters of four fonts on the display.

"""
import utime
import st7789s3 as st7789
import tft_config

# Choose fonts

# import vga1_8x8 as font
import vga2_8x8 as font1
# import vga1_8x16 as font
import vga2_8x16 as font2
# import vga1_16x16 as font
# import vga1_bold_16x16 as font
# import vga2_16x16 as font
import vga2_bold_16x16 as font3
# import vga1_16x32 as font
# import vga1_bold_16x32 as font
# import vga2_16x32 as font
import vga2_bold_16x32 as font4


def main():
    tft = tft_config.config(0)
    tft.vscrdef(tft_config.TFA, 320, tft_config.BFA)

    while True:
        for font in (font1, font2, font3, font4):
            tft.fill(st7789.BLUE)
            line = 0
            col = 0

            for char in range(font.FIRST, font.LAST):
                tft.text(font, chr(char), col, line, st7789.WHITE, st7789.BLUE)
                col += font.WIDTH
                if col > tft.width - font.WIDTH:
                    col = 0
                    line += font.HEIGHT

                    if line > tft.height-font.HEIGHT:
                        utime.sleep(3)
                        tft.fill(st7789.BLUE)
                        line = 0
                        col = 0

            utime.sleep(3)


main()
