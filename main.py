from PyQt5.QtWidgets import *
import requests

app = QApplication([])
window = QWidget()



val1 = QLineEdit("Валюта з якої перевести")
val2 = QLineEdit("Валюта в яку перевести")
kilkist = QLineEdit("Кількість")
result = QLineEdit("Результат")
vidpovid = QPushButton("Конвертація")




main_line = QVBoxLayout()
main_line.addWidget(val1)
main_line.addWidget(val2)
main_line.addWidget(kilkist)
main_line.addWidget(result)
main_line.addWidget(vidpovid)





window.setLayout(main_line)
window.show()
app.exec()

