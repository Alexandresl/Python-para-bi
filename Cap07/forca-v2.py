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

def display_hangman(chances):
    stages = [
        # Estágio 6
        """
            =======
            |     |
            |     0
            |    \\|/
            |     |
            |    / \\
          ====  
        """,
        # Estágio 5
        """
            =======
            |     |
            |     0
            |    \\|/
            |     |
            |    /
          ====
        """,
        # Estágio 4
        """
            =======
            |     |
            |     0
            |    \\|/
            |     |
            |
          ====
        """,
        # Estágio 3
        """
            =======
            |     |
            |     0
            |    \\|
            |     |
            |
          ====   
        """,
        # Estágio 2
        """
            =======
            |     |
            |     0
            |     |
            |     |
            |
          ====  
        """,
        # Estágio 1
        """
            =======
            |     |
            |     0
            |   
            |     
            |    
        """,
        # Estágio 0
        """
            =======
            |     |
            |     
            |   
            |     
            |
          ==== 
        """,
    ]
    return stages[chances]

def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("\nAdivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ["cachorro", "gato", "livro", "computador", "mesa", "cadeira", "telefone", "caneta", 
                "futebol", "escola", "amor", "felicidade", "tristeza", "brinquedo", "frio", "calor", 
                "chuva", "sol", "lua", "estrela", "carro", "bicicleta", "avião", "ônibus", "trem", 
                "barco", "navio", "sorriso", "risada", "lágrima", "amizade", "família", "amor", 
                "ódio", "verão", "inverno", "primavera", "outono", "praia", "montanha", "cidade", 
                "campo", "floresta", "deserto", "rio", "lago", "mar", "oceano", "vermelho", "azul",
                "verde", "amarelo", "branco", "preto", "rosa", "roxo", "laranja", "cinza", "marrom", 
                "dente", "cabelo", "olho", "nariz", "boca", "orelha", "braço", "perna", "mão", "pé", 
                "dedo", "cabeça", "coração", "peito", "costa", "barriga", "joelho", "cotovelo", 
                "ombro", "pescoço", "rosto", "café", "chá", "suco", "refrigerante", "água", "leite", 
                "cerveja", "vinho", "chocolate", "doce", "bolo", "pão", "queijo", "fruta", "vegetal", 
                "carne", "peixe", "arroz", "feijão", "macarrão"]
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    # List Comprehension
    letras_descobertas = ['_' for letra in palavra]
    # Número de chances
    chances = 6
    # Lista de letras erradas
    letras_erradas = []

    while chances > 0:

        # Print
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))



        # captura a primeira letra
        tentativa = input("\nDigite uma letrar: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

        limpa_tela()
        print("\nBem-vindo(a) ao jogo da forca!")
        print("\nAdivinhe a palavra abaixo:\n")

    # condicional
    if "_" in letras_descobertas:
        print(display_hangman(chances))
        print("\nVocê perdeu, a palavra era:", palavra)

if __name__ == "__main__":
    game()
    print("\nParabéns. Você está programando em Python!")