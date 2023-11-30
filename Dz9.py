class CurrencyConverter:

   def __init__(self):

       self.rates = {}

   def get_rates(self):

       response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

       data = response.json()

       for item in data:

           self.rates[item['cc']] = item['rate']

   def convert(self, amount, from_currency, to_currency):

       if from_currency != "USD":

           amount = amount / self.rates[from_currency]

       amount = round(amount * self.rates[to_currency], 2)

       return amount