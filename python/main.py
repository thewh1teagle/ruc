import ctypes

lib = ctypes.CDLL('libruc.dylib')

lib.RucAdd.argtypes = [ctypes.c_int, ctypes.c_int]
lib.RucAdd.restype = ctypes.c_int

result = lib.RucAdd(10, 20)
print(result)