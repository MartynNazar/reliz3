from PyQt5.QtWidgets import *
import requests

app = QApplication([])
window = QWidget()



val1_input = QLineEdit()
val1_input.setPlaceholderText("Валюта з якої перевести")

val2_input = QLineEdit()
val2_input.setPlaceholderText("Валюта в яку перевести")

cilckist_input = QLineEdit()
cilckist_input.setPlaceholderText("Введіть кількість")

result_input = QLineEdit()
result_input.setPlaceholderText("Результат")

vidpovid = QPushButton("Конвертація")




main_line = QVBoxLayout()
main_line.addWidget(val1_input)
main_line.addWidget(val2_input)
main_line.addWidget(cilckist_input)
main_line.addWidget(result_input)
main_line.addWidget(vidpovid)


def get_result():
    response = requests.get()
    data = response.json()
    print(data)
    print(data[0]["rate"])


vidpovid.clicked.connect(get_result)


window.setLayout(main_line)
window.show()
app.exec()

