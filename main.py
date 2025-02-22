import requests
from PyQt6.QtWidgets import *


app = QApplication([])
window = QWidget()



app.setStyleSheet("""
        QWidget {
            background: linear-gradient(135deg, #282c34, #3e4451);
            color: #8be9fd;
            font-family: sans-serif;
        }
        
        QPushButton
        {
            background-color:  #3e4451;
            border-style: solid;
            font-family: sans-serif;
            padding: 10px 20px;
            font-size: 16px;
            color: #8be9fd;
            border-width: 2px ;
            border-color: #61afef;
            border-radius:5px;
            box-shadow: 0 0 10px #61afef, 0 0 20px #8be9fd;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            
        }
        
        
        QPushButton:hover 
        {
             background-color: #52596a;
             box-shadow: 0 0 15px #8be9fd, 0 0 25px #a4ffff;
    
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



def get_result():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": val1_input.text(),
        "vs_currencies": val2_input.text()
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data[val1_input.text()][val2_input.text()])

vidpovid.clicked.connect(get_result)


window.setLayout(main_line)
window.show()
app.exec()

