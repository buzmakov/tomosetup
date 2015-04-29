import serial


def open_shutter(tty_name, rele_number):
    with serial.Serial(tty_name) as serial_port:
        serial_port.write("$KE,REL,{},1\r\n".format(rele_number))


def close_shutter(tty_name, rele_number):
    with serial.Serial(tty_name) as serial_port:
        serial_port.write("$KE,REL,{},0\r\n".format(rele_number))


class Shutter(object):

    """Shutter for x-ray source """

    def __init__(self, tty_name):
        """
        Init shutter object

        :param tty_name: COM port name to connect
        """
        super(Shutter, self).__init__()
        self.tty_name = tty_name
        self.check_module()

    def check_module(self):
        """
        Is controller alive?
        """
        with serial.Serial(self.tty_name) as serial_port:
            if serial_port.readline() != '#OK\r\n':
                raise RuntimeError("XRayShutter_ConnectionFailed")

    def open_shutter(self, rele_number):
        """
        Open rele

        :param rele_number: number of rele 1-4

        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE,REL,{},1\r\n".format(rele_number))

    def close_shutter(self, rele_number):
        """
        Close rele

        :param rele_number: number of rele 1-4

        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE,REL,{},1\r\n".format(rele_number))
