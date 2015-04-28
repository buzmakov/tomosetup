import serial


def open_shutter(tty_name, rele_number):
    with serial.Serial(tty_name) as ser:
        ser.write("$KE,REL,{},1\r\n".format(rele_number))


def close_shutter(tty_name, rele_number):
    with serial.Serial(tty_name) as ser:
        ser.write("$KE,REL,{},0\r\n".format(rele_number))
