from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox

def uncor():
    mass = QMessageBox()
    mass setText("Відповідь не правильна")
    mass.exec_()
app = QApplication([])
window = QWidget()


window.resize(500,300)
window.setWindowTitle("Конкурс")


question = QLabel("У якому році канал отримав золоту кнопку на YouTube")
rbtn_1 = QRadioButton("2005")
rbtn_2 = QRadioButton("2010")
rbtn_3 = QRadioButton("2015")
rbtn_4 = QRadioButton("2020")

v_line = QVBoxLayout()
h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()

h_line_1.addWidget(question, alligament=Qt AlignCenter)
h_line_2.addWidget(rbtn_1, alligament=Qt AlignCenter)
h_line_2.addWidget(rbtn_2, alligament=Qt AlignCenter)
h_line_3.addWidget(rbtn_3, alligament=Qt AlignCenter)
h_line_3.addWidget(rbtn_4, alligament=Qt AlignCenter)

v_line.addLayout(h_line_1)
v_line.addLayout(h_line_2)
v_line.addLayout(h_line_3)
window.setLayout(v_line)

rbtn_1.clicked.connect(uncor)
rbtn_1.clicked.connect(uncor)
rbtn_1.clicked.connect(uncor)
rbtn_1.clicked.connect(uncor)



window.show()
app.exec_()