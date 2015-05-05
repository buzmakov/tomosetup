import serial

#TODO: check errors

# def open_shutter(tty_name, rele_number):
#     with serial.Serial(tty_name) as serial_port:
#         serial_port.write("$KE,REL,{},1\r\n".format(rele_number))


# def close_shutter(tty_name, rele_number):
#     with serial.Serial(tty_name) as serial_port:
#         serial_port.write("$KE,REL,{},0\r\n".format(rele_number))


class Shutter(object):

    """Shutter for x-ray source """

    def __init__(self, tty_name, rele_number):
        """
        Init shutter object

        :param tty_name: COM port name to connect
        :param rele_number: number of rele 1-4
        """
        super(Shutter, self).__init__()
        
        #TODO: check input parameters

        self.tty_name = tty_name
        self.rele_number = rele_number
        self.check_module()

    def check_module(self):
        """
        Is controller alive?
        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE\r\n")
            if not '#OK' in serial_port.readline(): 
                raise RuntimeError('Shutter not operated')
        
    def open(self):
        """
        Open shutter
        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE,REL,{},1\r\n".format(self.rele_number))
            if not '#REL,OK' in serial_port.readline(): 
                raise RuntimeError('Shutter not opened')

    def close(self):
        """
        Close shutter      

        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE,REL,{},0\r\n".format(self.rele_number))
            if not '#REL,OK' in serial_port.readline(): 
                raise RuntimeError('Shutter not closed')


    def is_open(self):
        """
        Check is shutter in open state
        """
        with serial.Serial(self.tty_name) as serial_port:
            serial_port.write("$KE,RDR,{}\r\n".format(self.rele_number))
            response = serial_port.readline()
            if "#RDR,{},".format(self.rele_number) in response:
                state = int(response.split(',')[-1])
            else:
                raise ValueError('Bad response')

            if state == 1:
                return True
            elif state == 0:
                return False
            else:
                raise ValueError('Bad response')
            # if not '#REL,OK' in serial_port.readline(): 
            #     raise RuntimeError('Shutter not closed')
