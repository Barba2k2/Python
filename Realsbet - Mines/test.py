import random


class BoardGame:
    def __init__(self, width, height, num_bombs):
        self.width = width
        self.height = height
        self.num_bombs = num_bombs
        self.board = self.generate_board()

    def generate_board(self):
        # Criar um tabuleiro com "width" colunas e "height" linhas
        # com "num_bombs" bombas aleatoriamente distribuídas
        board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        bomb_count = 0
        while bomb_count < self.num_bombs:
            row = random.randint(0, self.height-1)
            col = random.randint(0, self.width-1)
            if board[row][col] != -1:
                board[row][col] = -1
                bomb_count += 1
        return board

    def print_board(self):
        # Imprimir o tabuleiro
        for row in self.board:
            print(row)


# Loop principal
while True:
    # Pedir ao usuário para inserir o número de bombas
    # e criar um novo objeto BoardGame
    num_bombs = int(input("Insira o número de bombas: "))
    game = BoardGame(5, 5, num_bombs)

    # Imprimir o tabuleiro com as bombas marcadas como "-1"
    print("Posições das bombas:")
    for i in range(game.height):
        for j in range(game.width):
            if game.board[i][j] == -1:
                print(f"({i}, {j})")
    print()
    game.print_board()

    # Pedir ao usuário se ele deseja fazer uma nova jogada ou sair
    choice = input("Deseja fazer uma nova jogada? (s/n): ")
    if choice.lower() == 'n':
        break
