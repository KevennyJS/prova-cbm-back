from schemas.perfil import Perfil
from datetime import datetime


class PerfilValidacao():
    def __init__(self, perfil: Perfil):
        self.perfil = perfil

    def validar_campos(self):
        print(self.perfil)
        error_message = ""
        if self.perfil.cpf is None:
            error_message = "Insira um CPF para o perfil"
        elif self.perfil.nome is None:
            error_message = "Insira um nome para o perfil"
        elif self.perfil.data_nascimento is None:
            error_message = "Insira uma data de nascimento para o perfil"
        elif self.perfil.email is None:
            error_message = "Insira um email para o perfil"
        elif self.perfil.telefone is None:
            error_message = "Insira um telefone para o perfil"
        elif self.perfil.tipos_sanguineo_id is None:
            error_message = "Insira um tipo sanguíneo para o perfil"
        elif self.perfil.signo_id is None:
            error_message = "Insira um signo para o perfil"
        return error_message

    def validar_cpf(self):
        self.perfil.cpf = self.perfil.cpf.replace(".", "").replace("-", "")
        tamanho_cpf = len(self.perfil.cpf)

        if tamanho_cpf != 11:
            return False

        elif self.perfil.cpf == self.perfil.cpf[::-1]:
            return False

        elif tamanho_cpf == 11:
            for i in range(9, 11):
                soma_digitos = sum((self.perfil.cpf[num] * ((i + 1) - num) for num in range(0, i)))
                digit = ((soma_digitos * 10) % 11) % 10
                if digit != self.perfil.cpf[i]:
                    return False
            return True

    def validar_idade(self):
        data_atual = datetime.now()
        data_nascimento = self.perfil.data_nascimento
        idade = data_atual.year - data_nascimento.year
        if idade < 18:
            return False
        else:
            return True

    def validar_email(self):
        if "@" in self.perfil.email:
            return True
        else:
            return False

    def validar_telefone(self):
        self.perfil.telefone = self.perfil.telefone.replace("(", "").replace(")", "").replace("-", "")
        if len(self.perfil.telefone) < 11:
            return False
        else:
            return True

    def validar_perfil(self):
        error_message = ""
        if self.validar_campos() != "":
            error_message = self.validar_campos()
        elif self.validar_cpf() is False:
            error_message = "Insira um CPF válido"
        elif self.validar_idade() is False:
            error_message = "O perfil deve ter mais de 18 anos"
        elif self.validar_email() is False:
            error_message = "Insira um email válido"
        elif self.validar_telefone() is False:
            error_message = "Insira um telefone válido"
        return error_message
