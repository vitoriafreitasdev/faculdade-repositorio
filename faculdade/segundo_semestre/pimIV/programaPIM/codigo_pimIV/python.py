
# arquivo python
import ctypes
import os
from ctypes import c_float, c_int, c_ulong, c_char, POINTER, Structure

# Caminho absoluto da DLL (garante que o Python a encontre)
os.chdir(os.path.dirname(__file__))
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "bib.dll"))
lib = ctypes.CDLL(dll_path)

#  Mapeando as structs do C 
class Imagens(Structure):
    _fields_ = [
        ("imagem_nome", c_char * 50),
        ("imagem_formato", c_char * 10),
        ("tamanho", c_ulong),
        ("imagem_dados", POINTER(ctypes.c_ubyte))
    ]

class Coeficientes(Structure):
    _fields_ = [
        ("b0", c_float),
        ("b1", c_float),
        ("b2", c_float),
        ("a1", c_float),
        ("a2", c_float),
    ]

# Configurando os protótipos das funções 

lib.sinais_normalizados.argtypes = (POINTER(c_int), c_int, c_int, POINTER(c_float))
lib.sinais_normalizados.restype = None

lib.filtroIIR.argtypes = (POINTER(c_float), POINTER(c_float), c_int, Coeficientes)
lib.filtroIIR.restype = None

lib.ler_imagem_binaria.argtypes = (ctypes.c_char_p,)
lib.ler_imagem_binaria.restype = ctypes.POINTER(Imagens)

#  Chamando uma função da DLL 

entrada = (c_int * 7)(-32700, -15000, -8000, 0, 12000, 25000, 31000)
saida = (c_float * 7)()

lib.sinais_normalizados(entrada, 7, 32767, saida)
print("==================================")
print("Resultado da normalização:")
for x in saida:
    print(round(x, 3))
print("=================================")
#  Chamando filtro IIR 
coef = Coeficientes(0.2929, 0.5858, 0.2929, -0.0000, 0.1716)

entrada_iir = (c_float * 8)(0.0, 0.5, 0.8, 0.3, -0.2, -0.5, -0.3, 0.1)
saida_iir = (c_float * 8)()

lib.filtroIIR(entrada_iir, saida_iir, 8, coef)

print("Resultado do filtro IIR:")
for x in saida_iir:
    print(round(x, 3))
print("==================================")

#  Ler a imagem salva 
img_ptr = lib.ler_imagem_binaria(b"amostra_clinica.bin")

if img_ptr:
    img = img_ptr.contents
    print("\nImagem lida:")
    print("Nome:", img.imagem_nome.decode())
    print("Formato:", img.imagem_formato.decode())
    print("Tamanho:", img.tamanho)

#############################################################

from ctypes import *

# --- Tipos auxiliares ---
c_float_p = POINTER(c_float)
c_int_p = POINTER(c_int)


# MAPEAMENTO DAS FUNÇÕES DA DLL

# downsample
lib.downsample.argtypes = [c_float_p, c_int, c_int, c_float_p]
lib.downsample.restype = None

# denoising
lib.denoising.argtypes = [c_float_p, c_int, c_int, c_float_p]
lib.denoising.restype = None

# codificação delta
lib.codificacao_delta.argtypes = [c_float_p, c_int, c_float_p]
lib.codificacao_delta.restype = None

# decodificação delta
lib.decodificacao_delta.argtypes = [c_float_p, c_int, c_float_p]
lib.decodificacao_delta.restype = None

# RLE adaptativo
lib.RLEAdaptativo.argtypes = [c_float_p, c_int, c_float, c_float_p, c_int_p, POINTER(c_int)]
lib.RLEAdaptativo.restype = None

# entropia janela
lib.entropia_janela.argtypes = [c_float_p, c_int, c_int, c_float_p]
lib.entropia_janela.restype = None

# checksum
lib.integridade_checksum.argtypes = [c_float_p, c_int]
lib.integridade_checksum.restype = c_float


#chamar essas funções no Python
entrada = (c_float * 4)(1.3, 2.0, 4.3, 3.1)
saida = (c_float * 2)()

lib.downsample(entrada, 4, 2, saida)

print("==================================")
print("Downsample:", list(saida))

entrada = (c_float * 4)(4.3, 5.0, 4.6, 4.8)
cod = (c_float * 4)()
decod = (c_float * 4)()
janela_entropia = 2
entropia = (c_float * (4 - janela_entropia + 1))()
denoising = (c_float * 4)()

lib.codificacao_delta(entrada, 4, cod)
lib.decodificacao_delta(cod, 4, decod)

lib.entropia_janela(entrada, 4, janela_entropia, entropia)
lib.denoising(entrada, 4, 2, denoising)
print("==================================")
print("Delta encoder: ", list(cod))
print("==================================")
print("Delta decoded: ", list(decod))
print("==================================")
print("Entropia: ", list(entropia))
print("==================================")
print("Denoising: ", list(denoising))
print("==================================")


entrada = (c_float * 4)(2.3, 4.0, 3.1, 7.8)
valores = (c_float * 4)()
contagens = (c_int * 4)()
tam_saida = c_int()

lib.RLEAdaptativo(entrada, 4, 2.0, valores, contagens, byref(tam_saida))

print("RLE:")
for i in range(tam_saida.value):
    print(f"Valor: {valores[i]}  | Contagem: {contagens[i]}")
print("==================================")


entrada = (c_float * 4)(1.2, 3.0, 4.5, 2.3)

checksum = lib.integridade_checksum(entrada, 4)

print("Checksum:", checksum)
print("==================================")

# Gravar imagem: 
lib.gravar_imagem.argtypes = (POINTER(Imagens), ctypes.c_char_p)
lib.gravar_imagem.restype = None

# criar objeto de imagem
img = Imagens()
img.imagem_nome = b"amostra_clinica"
img.imagem_formato = b"jpg"
img.tamanho = 6

# exemplo de bytes da imagem
dados = (ctypes.c_ubyte * img.tamanho)(10, 20, 30, 40, 50, 60)
img.imagem_dados = dados

# salvar usando a DLL
lib.gravar_imagem(ctypes.byref(img), b"amostra_clinica.bin")

print("Imagem salva com sucesso!")
