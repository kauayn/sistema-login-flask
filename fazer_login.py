def fazer_login(nome, cpf, senha, cpf_login, senha_login):
    if cpf == '':
        return None
    
    if cpf_login == cpf and senha_login == senha:
        return True
    else:
        return False