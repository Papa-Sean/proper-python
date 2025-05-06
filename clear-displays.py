from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from RPLCD.i2c import CharLCD

def clear_led_matrix():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    device.clear()

def clear_lcd():
    lcd_address = 0x27
    lcd = CharLCD(i2c_expander='PCF8574', 
                  address=lcd_address,
                  port=1,
                  cols=16, 
                  rows=2,
                  dotsize=8)
    lcd.clear()
    lcd.close()

def main():
    try:
        print("Clearing both displays...")
        clear_led_matrix()
        clear_lcd()
        print("Displays cleared.")
    except Exception as e:
        print(f"Error clearing displays: {e}")

if __name__ == "__main__":
    main()