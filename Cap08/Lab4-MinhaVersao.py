# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
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

# Board (tabuleiro)
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


# Classe
class Hangman:

	# Método Construtor
    def __init__(self):
        
        self.palavras = ["cachorro", "gato", "livro", "computador", "mesa", "cadeira", "telefone", "caneta", 
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
        
        self.palavra = random.choice(self.palavras)

        self.letras_descobertas = ['_' for letra in self.palavra]

        self.chances = 6

        self.letras_erradas = []
        
        self.game_status = 'on'
        

	# Método para adivinhar a letra
    def adivinhar_letra(self):
        
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in self.palavra:
            index = 0
            for letra in self.palavra:
                if tentativa == letra:
                    self.letras_descobertas[index] = letra
                index += 1
        else:
            self.chances -= 1
            self.letras_erradas.append(tentativa)
          
	
	# Método para verificar se o jogo terminou
    def jogo_nao_terminou(self):
        if self.chances == 0 or "_" not in self.letras_descobertas:
            self.game_status = "fim"
            self.status_jogo()
            return False
        return True

    def jogador_perdeu(self):
        print(stages[self.chances])
        print("\nVocê perdeu, a palavra era:", self.palavra)

	# Método para verificar se o jogador venceu
    def jogador_venceu(self):
        print("\nVocê venceu, a palavra era:", self.palavra)


	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela
    def status_jogo(self):
            
        if self.game_status == "on":
            limpa_tela()
            print("\nBem-vindo(a) ao jogo da forca!")
            print("\nAdivinhe a palavra abaixo:\n")
            print(stages[self.chances])
            print(" ".join(self.letras_descobertas))
            print("\nChances restantes:", self.chances)
            print("Letras erradas:", " ".join(self.letras_erradas))
            self.adivinhar_letra()
            
        if self.game_status == "fim":
            if "_" not in self.letras_descobertas:
                self.jogador_venceu()
            else:
                self.jogador_perdeu()
                
    def game(self):
        while self.jogo_nao_terminou():
            self.status_jogo()

if __name__ == "__main__":
    hangman = Hangman()
    hangman.game()