from PyQt6.QtWidgets import *


app = QApplication([])
window = QWidget()



app.setStyleSheet("""
        QWidget {
            background: #76e0ab;
        }
        
        QPushButton
        {
            background-color: #d27edd;
            border-style: dashed double none;
            font-family: cursive;
            padding: 7px;
            font-size: 25px;
            color: black;
            border-width: 7px;
            border-color: green;
            border-radius:30px;
            
            
    
""")




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





vidpovid.clicked.connect(get_result)


window.setLayout(main_line)
window.show()
app.exec()

