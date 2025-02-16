import requests

def get_result():
    response = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price"
    )
    data = response.json()
    print(data)

vidpovid.clicked.connect(get_result)