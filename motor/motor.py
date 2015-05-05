from ximc_wrapper import py_enumerate_devices, py_get_device_count, py_get_device_name, py_open_device
from ximc_wrapper import py_get_status, py_close_device, py_free_enumerate_devices, py_command_zero
from ximc_wrapper import py_get_move_settings, py_set_move_settings, py_command_move, py_get_position
from pprint import pprint
import time


class Motor(object):

    """docstring for Motor"""

    def __init__(self, name):
        super(Motor, self).__init__()
        self.name = name
        self.device_id = py_open_device(self.name)

    def get_status(self):
        """
        Description of status structure:
        unsigned int MoveSts;  Flags of move state
        unsigned int MvCmdSts; Move command state
        unsigned int PWRSts;   Flags of power state of stepper motor
        unsigned int EncSts;   Encoder state
        unsigned int WindSts;  Winding state
        int CurPosition;       Current position
        int uCurPosition;      Step motor shaft position in 1/256 microsteps
        long_t EncPosition;    Current encoder position
        int CurSpeed;          Motor shaft speed
        int uCurSpeed;         Part of motor shaft speed in 1/256 microsteps. Used only with stepper motor
        int Ipwr;              Engine current
        int Upwr;              Power supply voltage
        int Iusb;              USB current consumption
        int Uusb;              USB voltage
        int CurT;              Temperature in tenths of degrees C
        unsigned int Flags;    Status flags
        unsigned int GPIOFlags; GPIOStatus flags
        unsigned int CmdBufFreeSpace;   This field shows the amount of free cells buffer synchronization chain
        """
        # TODO: add more status fields

        status = py_get_status(self.device_id)
        return {'speed': status['CurSpeed'],
                'possition': status['CurPosition']}

    def set_speed_acceleration(self, speed, accel):
        py_set_move_settings(self.device_id, speed, accel)

    def get_speed_acceleration(self):
        move_settings = py_get_move_settings(self.device_id)
        return {'speed': move_settings['Speed'],
                'acceleration': move_settings['Accel']}

    def get_position(self):
        position = py_get_position(self.device_id)
        return position['Position']

    def move_to_position(self, position):
        py_command_move(self.device_id, position, 0)

        # waiting until motor rotated
        while self.get_status()['speed'] != 0 or self.get_position() != position:
            # print 'Current angle: {}'.format(self.get_position())
            time.sleep(0.1)

    def set_position_to_zero(self):
        py_command_zero(self.device_id)


class MotorsPool(object):

    """docstring for MotorsPool"""

    def __init__(self):
        super(MotorsPool, self).__init__()
        self.motors = []
        self.enumerate_motors()

    def enumerate_motors(self):
        dev_enum = py_enumerate_devices(0)
        self.devices_count = py_get_device_count(dev_enum)

        if self.devices_count == 0:
            print 'No devices found'
            return

        for i in range(self.devices_count):
            device_name = py_get_device_name(dev_enum, i)
            motor = Motor(device_name)
            self.motors.append(motor)
