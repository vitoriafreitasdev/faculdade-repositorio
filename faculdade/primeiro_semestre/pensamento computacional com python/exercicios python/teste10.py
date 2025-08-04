import unittest
import re

class Validacoes:
    def validar_senha(self, senha):
        senha_num = re.search(r'\d', senha)
        senha_letraMaius = re.search(r'[A-Z]', senha)
        senha_letraMinus = re.search(r'[a-z]', senha)

        if senha_num and senha_letraMaius and senha_letraMinus:
            return True
        else:
            return False

    def validar_idade(self, idade):
        
        if idade >= 18:
            return True
        else:
            return False
    
class Teste_de_unidade(unittest.TestCase):
    def setUp(self):
        self.teste = Validacoes()
    def teste_senha(self):
        self.assertTrue(self.teste.validar_senha("abc12DE"))
        self.assertFalse(self.teste.validar_senha("abc"))
        self.assertFalse(self.teste.validar_senha("abc12"))
    def teste_idade(self):
        self.assertFalse(self.teste.validar_idade(17))
        self.assertTrue(self.teste.validar_idade(18))
        self.assertTrue(self.teste.validar_idade(19))

#para chamar no terminal e fazer a verificação python -m unittest teste10.py -v