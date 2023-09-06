'''
Projete três funções: uma delas deve receber como entrada o RA, o nome e o curso de um aluno. Essas informações serão passadas para uma segunda função que deve atribuir essas informações a uma estrutura de dados. Depois de retornar a estrutura cadastrada, chame a terceira função para imprimir os dados da estrutura que foram cadastrados.
'''

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    curso: str
    ra: str

def atribuir_dado_composto(nome: str, curso: str, ra: str):
    '''
    Recebe nome,curso e ra como parametros e retorna um dado composto Aluno
    Exemplos:
    >>> atribuir_dado_composto("Victor", "Computacao", "133070")
    Aluno(nome="Victor", curso="Computacao", ra="133070") 
    '''
    aluno = Aluno(nome,curso,ra)
    
    return aluno

def show_dados(aluno: Aluno):
    print(f"Aluno: {aluno.nome}\nCurso: {aluno.curso}\nRA: {aluno.ra}")

def entrada():
    print("Insira o seu nome, curso e RA abaixo:")
    nome: str = str(input("Nome: "))
    curso: str = str(input("Curso: "))
    ra: str = str(input("RA: "))
    
    show_dados(atribuir_dado_composto(nome,curso,ra))

entrada()
