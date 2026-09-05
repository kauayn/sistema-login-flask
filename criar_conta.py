
def criar_conta(nome, idade, cpf, senha, confirmar_senha):
        if confirmar_senha != senha:
            return None, None, None
        
        return nome, cpf, senha