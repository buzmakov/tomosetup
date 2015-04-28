from shutter import open_shutter, close_shutter

from time import sleep
if __name__ == "__main__":
    open_shutter('COM4', 4)
    sleep(0.5)
    close_shutter('COM4',4)
