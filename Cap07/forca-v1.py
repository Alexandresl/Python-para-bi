import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # no Windows
    if name == 'nt':
        _ = system('cls')
    # no Mac ou Linux
    else:
        _ = system('clear')

