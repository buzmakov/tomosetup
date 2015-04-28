from ximc_wrapper import py_enumerate_devices, py_get_device_count, py_get_device_name, py_open_device
from ximc_wrapper import py_get_status, py_close_device, py_free_enumerate_devices, py_command_zero
from ximc_wrapper import py_get_move_settings, py_set_move_settings, py_command_move, py_get_position

from pprint import pprint
import time


def main():
    dev_enum = py_enumerate_devices(0)
    devices_count = py_get_device_count(dev_enum)

    if devices_count == 0:
        print 'No devices found'
        return

    for i in range(devices_count):

        device_name = py_get_device_name(dev_enum, i)
        print 'Device name: {}'.format(device_name)

        device_id = py_open_device(device_name)
        py_command_zero(device_id)

        status = py_get_status(device_id)
        print 'Current status:'
        pprint(status)
        print

        move_settings = py_get_move_settings(device_id)
        print 'Current move settings:'
        pprint(move_settings)
        print

        move_settings = py_set_move_settings(device_id, 1000, 1000)

        print 'Modified move settings:'
        pprint(move_settings)
        print

        position = py_get_position(device_id)
        print 'Current position:'
        pprint(position)
        print

        position = 1000
        py_command_move(device_id, position, 0)

        # waiting until motor rotated

        status = py_get_status(device_id)
        while status['MoveSts'] != 0 or status['CurPosition'] != position:
            print 'Current angle: {}'.format(status['CurPosition'])
            time.sleep(0.1)
            status = py_get_status(device_id)

        print    
        position = py_get_position(device_id)
        print 'Current position:'
        pprint(position)
        print

        py_close_device(device_id)

    py_free_enumerate_devices(dev_enum)

    device_id = py_open_device
if __name__ == "__main__":
    main()
