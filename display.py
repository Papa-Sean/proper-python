#!/usr/bin/env python3
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    device.contrast(0x80)

    message = (
        "Welcome Uncle Mike and Aunt Trish! "
        "New WiFi password: "
        "trump2028"
        "... Don't laugh, this is going to save our lives!"
    )

    while True:
        show_message(
            device, 
            message, 
            fill="white", 
            font=proportional(CP437_FONT), 
            scroll_delay=0.1
        )
        time.sleep(1)

if __name__ == "__main__":
    main()