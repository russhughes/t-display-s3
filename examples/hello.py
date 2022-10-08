"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.

"""
import random
import st7789s3 as st7789
import tft_config

# Choose a font

# import vga1_8x8 as font
# import vga2_8x8 as font
# import vga1_8x16 as font
# import vga2_8x16 as font
# import vga1_16x16 as font
# import vga1_bold_16x16 as font
# import vga2_16x16 as font
# import vga2_bold_16x16 as font
# import vga1_16x32 as font
# import vga1_bold_16x32 as font
# import vga2_16x32 as font
import vga2_bold_16x32 as font


def main():
    tft = tft_config.config(0)

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width - font.WIDTH*6
            row_max = tft.height - font.HEIGHT

            for _ in range(100):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                )


main()
