#!/usr/bin/env python3
import time
import psutil
import socket
import re
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

def get_system_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    temps = psutil.sensors_temperatures()
    temp = "N/A"
    for key in temps:
        if temps[key]:
            temp = temps[key][0].current
            break
    return cpu, ram, disk, temp

def get_network_stats():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "No Connection"

    net_io = psutil.net_io_counters()
    upload = (net_io.bytes_sent / 1024)
    download = (net_io.bytes_recv / 1024)
    return ip, upload, download

def format_stats():
    cpu, ram, disk, temp = get_system_stats()
    ip, upload, download = get_network_stats()

    # One long string for horizontal scroll
    stats = f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | Disk: {disk:.1f}% | Temp: {temp}C | IP: {ip} | Up: {upload:.1f}KB/s | Down: {download:.1f}KB/s"
    return re.sub(" +", " ", stats)  # Collapse extra spaces

def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
    serial,
    cascaded=4,  # 4 x 8 = 32 columns
    block_orientation=-90,  # Modules mounted horizontally
    rotate=0,
    blocks_arranged_in_reverse_order=False
)
    device.contrast(0x80)

    while True:
        message = format_stats()
        show_message(
            device,
            message,
            fill="white",
            font=proportional(CP437_FONT),
            scroll_delay=0.1  # Adjust for speed
        )
        time.sleep(1)

if __name__ == "__main__":
    main()