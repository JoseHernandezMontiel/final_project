from flask import Blueprint, jsonify, request

from models.Item import Item
from services.ItemService import Service

item_controller_blueprint = Blueprint('item_controller_blueprint', __name__)

service = Service()


# CREATE

@item_controller_blueprint.route('/items', methods=['POST'])
def store():
    
   for key in ['sku', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.json:
         return {"error": f"Missing field: {key}"}, 400

   item = Item(
      sku=request.json['sku'], 
      name=request.json['name'], 
      description=request.json['description'], 
      price=request.json['price'], 
      quantity=request.json['quantity'], 
      expiration_date=request.json['expiration_date']
   )

   serviceResponse = service.store(item)

   if serviceResponse is False:
      return {"error": "Item sku already exists"}, 400

   return {
      "id": serviceResponse.id,
      "sku": serviceResponse.sku,
      "name": serviceResponse.name,
      "description": serviceResponse.description,
      "price": serviceResponse.price,
      "quantity": serviceResponse.quantity,
      "expiration_date": serviceResponse.expiration_date
   }, 201



# READ

@item_controller_blueprint.route('/items/<id>')
def show(id):
   
   item = service.show(id)

   if item is False:
      return {"error": "Item not found"}, 404

   return {
      "id": item.id,
      "sku": item.sku,
      "name": item.name,
      "description": item.description,
      "price": item.price,
      "quantity": item.quantity,
      "expiration_date": item.expiration_date
   }

@item_controller_blueprint.route('/items/<id>/convert', methods=['GET'])
def convert(id):
   item = service.show(id)

   if item is False:
      return {"error": "Item not found"}, 404

   if 'currency' in request.args:
      currency = request.args['currency']

      if currency not in [
         'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 
         'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 
         'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 
         'CLF', 'CLP', 'CNY', 'CNH', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK',
         'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 
         'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 
         'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 
         'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 
         'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL',
         'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 
         'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 
         'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 
         'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 
         'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL',
         'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 
         'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 
         'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW',
         'ZWL'
      ]:
         return {"error": "Invalid currency"}, 400

      item.price = service.convert(item.price, currency)

   return {
      "id": item.id,
      "sku": item.sku,
      "name": item.name,
      "description": item.description,
      "price": item.price,
      "quantity": item.quantity,
      "expiration_date": item.expiration_date
   }

@item_controller_blueprint.route('/items')
def index():
   items = service.index()
   
   return jsonify([
      {
         "id": item.id,
         "sku": item.sku,
         "name": item.name,
         "description": item.description,
         "price": item.price,
         "quantity": item.quantity,
         "expiration_date": item.expiration_date
      } for item in items
   ])



# UPDATE

@item_controller_blueprint.route('/items/<id>', methods=['PUT'])
def update(id):
   for key in ['sku', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.json:
         return {"error": f"Missing field: {key}"}, 400

   if service.show(id) is False:
      return {"error": "Item not found"}, 404

   item = Item(
      id=id,
      sku=request.json['sku'], 
      name=request.json['name'], 
      description=request.json['description'], 
      price=request.json['price'], 
      quantity=request.json['quantity'], 
      expiration_date=request.json['expiration_date']
   )

   serviceResponse = service.update(item)

   if serviceResponse is False:
      return {"error": "Item sku already exists"}, 400

   return {
      "id": serviceResponse.id,
      "sku": serviceResponse.sku,
      "name": serviceResponse.name,
      "description": serviceResponse.description,
      "price": serviceResponse.price,
      "quantity": serviceResponse.quantity,
      "expiration_date": serviceResponse.expiration_date
   }



# DELETE

@item_controller_blueprint.route('/items/<id>', methods=['DELETE'])
def destroy(id):
   serviceResponse = service.destroy(id)

   if "error" in serviceResponse:
      return serviceResponse, 400

   return serviceResponse