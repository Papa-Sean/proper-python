import subprocess
import time

def main():
    # Start both scripts in separate processes
    p1 = subprocess.Popen(["python", "display.py"])
    p2 = subprocess.Popen(["python", "text-scroll-oled.py"])
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping both processes...")
        p1.terminate()
        p2.terminate()

if __name__ == "__main__":
    main()