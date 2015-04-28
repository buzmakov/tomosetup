import cython
from libc.stdint cimport int64_t, long

ctypedef struct status_t:
	unsigned int MoveSts	
	unsigned int MvCmdSts	
	unsigned int PWRSts	
	unsigned int EncSts	
	unsigned int WindSts
	int CurPosition	
	int uCurPosition	
	long EncPosition	
	int CurSpeed
	int uCurSpeed	
	int Ipwr	
	int Upwr	
	int Iusb	
	int Uusb	
	int CurT	
	unsigned int Flags
	unsigned int GPIOFlags	
	unsigned int CmdBufFreeSpace	

ctypedef struct move_settings_t:
	unsigned int Speed	
	unsigned int uSpeed
	unsigned int Accel	
	unsigned int Decel
	unsigned int AntiplaySpeed
	unsigned int uAntiplaySpeed

ctypedef struct get_position_t:
		int Position
		int uPosition
		long EncPosition

cdef extern from "ximc.h":
	int64_t enumerate_devices(int probe_flags)
	int get_device_count(int device_enumeration)
	char* get_device_name(int probe_flags, int device_index)
	int free_enumerate_devices(int probe_flags)
	int get_status(int device_id, status_t* status)
	int open_device (const char* name)
	int close_device(int* device_id)
	int command_zero(int device_id)
	int get_move_settings(int device_id, move_settings_t* move_settings)
	int set_move_settings (int device_id, const move_settings_t* move_settings);
	int command_move (int device_id, int Position, int uPosition)
	int get_position (int id, get_position_t* the_get_position)

def py_enumerate_devices(probe_flags):
	return enumerate_devices(probe_flags)

def py_get_device_count(device_enumeration):
	return get_device_count(device_enumeration)

def py_get_device_name(device_enumeration, device_index):
	return get_device_name(device_enumeration, device_index)

def py_free_enumerate_devices(device_enumeration):
	return free_enumerate_devices(device_enumeration)

def py_open_device(name):
	return open_device(name)

def py_close_device(device_id):
	cdef int tmp_device_id = device_id
	return close_device(&tmp_device_id) 

def py_get_status(device_id):
	cdef status_t status
	get_status(device_id, &status)
	return status

def py_command_zero(device_id):
	return command_zero(device_id)

def py_get_move_settings(device_id):
	cdef move_settings_t move_settings
	get_move_settings(device_id, &move_settings)
	return move_settings

def py_set_move_settings(device_id, Speed, Accel):
	cdef move_settings_t move_settings
	get_move_settings(device_id, &move_settings)
	move_settings.Speed = int(Speed)
	move_settings.Accel = int(Accel)
	move_settings.Decel = int(Accel)
	set_move_settings(device_id, &move_settings)
	return move_settings


def py_command_move(int device_id, int Position, int uPosition):
	return command_move(device_id, Position, uPosition)

def py_get_position(int device_id):
	cdef get_position_t the_get_position
	get_position(device_id, &the_get_position)
	return the_get_position