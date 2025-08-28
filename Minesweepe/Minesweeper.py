import random

class Minesweeper:
    def __init__(self, size=5, mines=5):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.visible = [[False for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self._place_mines()

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mine_positions.add((x, y))

    def _count_adjacent_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if (nx, ny) in self.mine_positions and 0 <= nx < self.size and 0 <= ny < self.size:
                    count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mine_positions:
            return False
        self.visible[x][y] = True
        self.board[x][y] = str(self._count_adjacent_mines(x, y))
        if self.board[x][y] == '0':  # auto reveal neighbors
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < self.size and 0 <= ny < self.size and not self.visible[nx][ny]:
                        self.reveal(nx, ny)
        return True

    def display(self):
        print("\n   " + " ".join([str(i) for i in range(self.size)]))
        print("   " + "--" * self.size)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.visible[i][j]:
                    row.append(self.board[i][j])
                else:
                    row.append("?")
            print(f"{i} | " + " ".join(row))
        print()

    def check_win(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in self.mine_positions and not self.visible[i][j]:
                    return False
        return True


def play():
    size = 5
    mines = 5
    game = Minesweeper(size, mines)
    print("\n=== Minesweeper ===")
    print("Reveal safe spots. Avoid the mines!")
    print("Input format: row col (e.g., 1 2)")
    
    while True:
        game.display()
        move = input("Enter coordinates (or 'q' to quit): ").strip().lower()
        if move == 'q':
            print("Game exited.")
            break
        try:
            x, y = map(int, move.split())
            if not (0 <= x < size and 0 <= y < size):
                print("Invalid coordinates. Try again.")
                continue
        except:
            print("Invalid input. Use row col format.")
            continue

        if not game.reveal(x, y):
            print("\nBoom! You hit a mine. Game Over!")
            print("Mines were at:", game.mine_positions)
            break
        if game.check_win():
            game.display()
            print("Congratulations! You cleared the board!")
            break

if __name__ == "__main__":
    play()
