import csv

from models.Item import Item, SqlAlchemyRepository

def read_csv_to_dict(filename):
   with open(filename, 'r') as f:
      reader = csv.DictReader(f)
      return list(reader)
  
def seed_database_from_csv(filename):
   items = read_csv_to_dict(filename)

   repository = SqlAlchemyRepository()

   for item in items:
      item = Item(
         sku=item['SKU'],
         name=item['Name'],
         description=item['Description'],
         price=item['Price'],
         quantity=item['Quantity'],
         expiration_date=item['Expiration Date']
      )
      repository.create(item)
