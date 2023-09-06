'''
Proposta do problema:
Givanildo construiu um sistema para controlar a pontuação e os prêmios que ele e seus amigos conseguem nos jogos online. No entanto, ele é prevenido e sabe que seus amigos não são confiáveis, e tentarão acessar esse sistema para alterar suas próprias pontuações e prêmios. Então ele colocou uma senha de proteção. A senha é 'Giva123'. Você deve fazer um programa que fará a leitura da senha e chamará uma função para verificar se a senha está correta ou não. O sistema deve informar se a senha está correta (e o acesso está autorizado) ou se a senha está incorreta e, portanto, não será autorizado o acesso.
'''

def valida_senha(senha_inserida: str) -> bool: 
    '''
    Este programa verifica se a senha inserida pelo usuário é de acordo com a senha que está contida no sistema, 
    que no nosso caso a senha é Giva123. Portanto, caso a senha esteja correta o programa retornará True, já caso
    a senha esteja incorreta retornará False.
    Exemplos:
    >>> valida_senha('Giva123')
    True
    >>> valida_senha('giva123')
    False
    '''

    senha = 'Giva123'

    if senha_inserida == senha:
        return True
    else:
        return False


def main():
    senha = input("Digite a senha para acessar o sistema: ")
    if valida_senha(senha):
        print("Senha correta, você entrou no sistema")
    else:
        print("Senha incorreta, você não entrou no sistema")

main()
