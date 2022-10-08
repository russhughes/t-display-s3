"""
lines.py

    Draws lines and rectangles in random colors at random locations on the
    display.

"""
import random
import st7789s3 as st7789
import tft_config


def main():
    tft = tft_config.config(0)
    tft.fill(st7789.BLACK)

    while True:
        tft.line(
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
                )
            )

        width = random.randint(0, tft.width // 2)
        height = random.randint(0, tft.height // 2)
        col = random.randint(0, tft.width - width)
        row = random.randint(0, tft.height - height)
        tft.fill_rect(
            col,
            row,
            width,
            height,
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
            )
        )


main()
