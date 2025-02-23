import requests
from PyQt6.QtWidgets import *


app = QApplication([])
window = QWidget()



app.setStyleSheet("""
        QWidget {
            background: linear-gradient(135deg, #282c34, #3e4451);
            color: #8be9fd;
            font-family: fantasy;
        }
        
        QPushButton
        {
            background-color:  #3e4451;
            border-style: solid;
            font-family: fantasy;
            padding: 10px 20px;
            font-size: 16px;
            color: #8be9fd;
            border-width: 2px ;
            border-color: #61afef;
            border-radius:5px;
            
            
        }
         
       QLineEdit
       {    
            background-color: #898f8f;
            border-style: outset;
            font-family: fantasy;
            padding:  20px;
            font-size: 16px;
            color: #000000;
            border-width: 2px ;
            border-color: #22e9ccf;
            border-radius:5px;
            
       }
            
       QComboBox
       {
            background-color: #898f8f;
            border-style: outset;
            font-family: fantasy;
            padding:  20px;
            font-size: 16px;
            color: #000000;
            border-width: 2px ;
            border-color: #22e9ccf;
            border-radius:5px;
            
            
       }
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



combo = QComboBox()
combo.addItem("Bitcoin")
combo.addItem("Litecoin")
combo.addItem("Namecointcoin")
combo.addItem("SwiftCoin")
combo.addItem("BlackCoin")
combo.addItem("Dash")
combo.addItem("Ethereum")
combo.addItem("SixEleven")
combo.addItem("Titcoin")
combo.addItem("Synereo AMP")
combo.addItem("Nxt")
combo.addItem("Monero")
combo.addItem("DigitalNote")
combo.addItem("Burstcoin")
combo.addItem("Ripple")



combo2 = QComboBox()
combo2.addItem("AUD")
combo2.addItem("CZK")
combo2.addItem("CNY")
combo2.addItem("INR")
combo2.addItem("JPY")
combo2.addItem("KZT")
combo2.addItem("UAH")
combo2.addItem("USD")
combo2.addItem("EUR")
combo2.addItem("PLN")
combo2.addItem("BGN")
combo2.addItem("XDR")
combo2.addItem("GBR")
combo2.addItem("GEL")
combo2.addItem("SAR")


dodatkova_line = QHBoxLayout()
dodatkova_line.addWidget(combo)
dodatkova_line.addWidget(combo2)


main_line = QVBoxLayout()
main_line.addLayout(dodatkova_line)
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
    bit = print(data[val1_input.text()][val2_input.text()])
    result_input.setText(bit*cilckist_input)

vidpovid.clicked.connect(get_result)


window.setLayout(main_line)
window.show()
app.exec()

