from shutter import Shutter

from time import sleep
if __name__ == "__main__":
    shutter = Shutter('COM4', 4)
    print shutter.is_open()
    shutter.open()
    print shutter.is_open()
    sleep(0.5)
    shutter.close()
    print shutter.is_open()