from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
import random


app = QApplication([])

main_window = QWidget()
main_window.setGeometry(100,100,200,200)

button = QPushButton("натисни")
ladel = QLabel("хомяк")
ladel.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout = QVBoxLayout()
layout.addWidget(ladel)
layout.addWidget(button)
main_window.setLayout(layout)
main_window.show()

def click_button():
    n = random.randint(1000,1488)
    ladel.setText(str(n))

button.clicked.connect(click_button)
app.exec()