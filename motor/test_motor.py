from pprint import pprint
from motor import MotorsPool


def obj_main():
    motors_pool = MotorsPool()
    for motor in motors_pool.motors:
        print motor.name, motor.device_id
        pprint(motor.get_status())
        pprint(motor.get_speed_acceleration())
        motor.set_speed_acceleration(500, 500)
        pprint(motor.get_speed_acceleration())
        motor.set_position_to_zero()
        pprint(motor.get_position())
        motor.move_to_position(1000)
        pprint(motor.get_position())
        motor.move_to_position(-1000)
        pprint(motor.get_position())

if __name__ == "__main__":
    obj_main()
