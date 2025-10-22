import ctypes
import os

dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "library.dll"))
lib = ctypes.CDLL(dll_path)

# Define o tipo dos argumentos e o tipo de retorno de cada função
lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int

lib.sub.argtypes = (ctypes.c_int, ctypes.c_int)
lib.sub.restype = ctypes.c_int

# Chama as funções C
print("4 + 5 =", lib.add(4, 5))
print("10 - 7 =", lib.sub(10, 7))