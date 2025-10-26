import ctypes
import os

# Caminho absoluto da DLL (garante que o Python a encontre)
os.chdir(os.path.dirname(__file__))
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "biblioteca.dll"))
lib = ctypes.CDLL(dll_path)


# Define os tipos de argumentos e retorno das funções
#Argumentos da gravarPessoa
lib.gravarPessoa.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char, ctypes.c_float]
#Retorno da gravarPessoa
lib.gravarPessoa.restype = None

#lerPessoa argumentos
lib.lerPessoa.argtypes = []
#lerPessoa retorno
lib.lerPessoa.restype = None

# === Teste ===
# Cria dados e grava no arquivo
nome = b"Kal"  # precisa ser bytes!
idade = 22
sexo = b'M'     # também bytes
pressao = ctypes.c_float(129.0)

lib.gravarPessoa(nome, idade, sexo, pressao)

lib.lerPessoa()



#gcc -shared -o biblioteca.dll -fPIC biblioteca.c