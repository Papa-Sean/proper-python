from RPLCD.i2c import CharLCD
import time
import textwrap

# Update this address based on your I2C device
lcd_address = 0x27

# Initialize the LCD (adjust parameters for your LCD size if needed)
lcd = CharLCD(i2c_expander='PCF8574', 
              address=lcd_address,
              port=1,
              cols=16, 
              rows=2,
              dotsize=8)

def chunk_message(large_message, width=16, rows=2):
    wrapped = textwrap.wrap(large_message, width)
    chunks = []
    for i in range(0, len(wrapped), rows):
        lines = wrapped[i:i+rows]
        for idx, line in enumerate(lines):
            lines[idx] = line.ljust(width)
        chunks.append("".join(lines).strip())
    return chunks

# Example long text
long_text = "Look up ^       Good boy...     " * 5
messages = chunk_message(long_text)

def type_message(message, typing_delay=0.1):
    lcd.clear()
    row, col = 0, 0
    for char in message:
        if col >= 16:
            row = 1
            col = 0
            lcd.cursor_pos = (row, col)
        lcd.write_string(char)
        col += 1
        time.sleep(typing_delay)

def run_animation_loop():
    while True:
        for message in messages:
            type_message(message)
            time.sleep(5)
            lcd.clear()

if __name__ == "__main__":
    try:
        print("Starting LCD typing animation. Press CTRL+C to stop.")
        run_animation_loop()
    except KeyboardInterrupt:
        print("Animation stopped by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        lcd.clear()
        lcd.close()