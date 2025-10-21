import ctypes
import os

dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "library.dll"))
lib = ctypes.CDLL(dll_path)

lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int

print(lib.add(3, 4))
