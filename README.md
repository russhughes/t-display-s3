Python T-Display-S3 ST7789 driver for MicroPython
=================================================

This driver is a quick hack to get the ST7789 display working on the T-Display-S3 board.
It is based on devbis' st7789py_mpy module from https://github.com/devbis/st7789py_mpy.

This driver adds support for:

- 320x240, 170x320, 240x240 and 135x240 pixel displays
- Display rotation
- Hardware based scrolling
- Drawing text using 8 and 16 bit wide bitmap fonts with heights that are
  multiples of 8.  Included are 12 bitmap fonts derived from classic pc
  BIOS text mode fonts.
- Drawing text using converted TrueType fonts.
- Drawing converted bitmaps
- Parallel interface.


This is a work in progress. Documentation can be found in the docs directory
and at https://penfold.owt.com/st7789s3.


Examples
--------

See the examples directory for example programs that run on the LILYGO® TTGO T-Display-S3.
The example programs require the tft_config.py module to be present.

Fonts
-----

See the subdirectories in the fonts directory for the converted font modules
used in the examples. These modules can be compiled using the mpy-cross
compiler before uploading to save memory.
