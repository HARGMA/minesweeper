import sys
import numpy as np
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

# Create a 5x5 Minesweeper grid
m = np.full((5, 5), "0", dtype="U1")  # Hidden mines grid
m1 = np.full((5, 5), "_", dtype="U1")  # Player's revealed grid
bombs = 0

# Place 5 bombs randomly
while bombs < 5:
    i, j = randint(0, 4), randint(0, 4)
    if m[i, j] == "0":
        m[i, j] = "💣"
        bombs += 1

# Function to calculate adjacent bomb count
def calcul(m, i, j):
    if m[i, j] == "💣":
        return "💣"
    
    count = sum(m[x, y] == "💣" for x in range(max(0, i - 1), min(5, i + 2))
                               for y in range(max(0, j - 1), min(5, j + 2)))
    return str(count)

# Initialize the board with bomb counts
for i in range(5):
    for j in range(5):
        m[i, j] = calcul(m, i, j)

# GUI Application
class Minesweeper(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.buttons = {}

        # Create buttons dynamically
        for i in range(5):
            for j in range(5):
                btn = QPushButton("_")
                btn.setFixedSize(50, 50)
                btn.clicked.connect(lambda _, x=i, y=j: self.reveal(x, y))
                self.grid.addWidget(btn, i, j)
                self.buttons[(i, j)] = btn

        self.setLayout(self.grid)
        self.setWindowTitle("Minesweeper")
        self.show()

    def reveal(self, x, y):
        """Reveals the selected button."""
        if m[x, y] == "💣":
            self.buttons[(x, y)].setText("💣")
            self.gameOver()
        else:
            self.buttons[(x, y)].setText(m[x, y])

    def gameOver(self):
        """Displays all mines when game is lost."""
        for (i, j), btn in self.buttons.items():
            if m[i, j] == "💣":
                btn.setText("💣")

# Run the Application
app = QApplication(sys.argv)
window = Minesweeper()
sys.exit(app.exec())
