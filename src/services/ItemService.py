import requests
from models.Item import Item, SqlAlchemyRepository

class Service:
   def __init__(self):
      self.repository = SqlAlchemyRepository()


   def store(self, item: Item):
      item = self.repository.create(item)
            
      return item
   

   def show(self, id):
      item = self.repository.find(id)
      
      if item is None:
         return False
      
      return item


   def index(self):
      return self.repository.all()
   

   def update(self, item: Item):      
      return self.repository.update(item)


   def destroy(self, id):
      if self.repository.find(id) is None:
         return {"error": "Item not found"}
      
      self.repository.delete(id)
      
      return {"message": "Item deleted"}
   
   def convert(self, price, currency):
      access_key = 'cc9ced7d7834ea301647a894ed33de65'

      url = f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}"
      
      response = requests.get(url).json()

      usd_price_to_eur = price / response['rates']['USD']

      return usd_price_to_eur * response['rates'][currency]