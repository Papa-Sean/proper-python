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
        "Your website lives here! Pretty neat, eh?"
    )

    while True:
        show_message(
            device, 
            message, 
            fill="white", 
            font=proportional(CP437_FONT), 
            scroll_delay=0.06
        )
        time.sleep(1)

if __name__ == "__main__":
    main()