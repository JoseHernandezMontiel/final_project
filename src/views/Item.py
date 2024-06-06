from flask import Blueprint, redirect, render_template, request, url_for

from models.Item import Item
from services.ItemService import Service

item_views_blueprint = Blueprint('item_views_blueprint', __name__)

service = Service()



# CREATE

@item_views_blueprint.route('/add', methods=['POST'])
def add():

   item = Item(
      sku=request.form['sku'],
      name=request.form['name'],
      description=request.form['description'],
      price=request.form['price'],
      quantity=request.form['quantity'],
      expiration_date=request.form['expiration_date']
   )

   if service.store(item) is False:
      return render_template('add.html', error="Item sku already exists", data=item)

   return redirect(url_for('item_views_blueprint.index'))


@item_views_blueprint.route('/add')
def add_view():
   return render_template('add.html')



# READ

@item_views_blueprint.route('/')
def index():
   items = service.index()
   
   data = [
      {
         "id": item.id,
         "sku": item.sku,
         "name": item.name,
         "description": item.description,
         "price": item.price,
         "quantity": item.quantity,
         "expiration_date": item.expiration_date
      } for item in items
   ]

   return render_template('index.html', data=data)



# UPDATE

@item_views_blueprint.route('/edit/<id>', methods=['POST'])
def edit(id):
   for key in ['sku', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.form:
         return redirect(url_for('item_views_blueprint.index'))

   if service.show(id) is False:
      return redirect(url_for('item_views_blueprint.index'))

   item = Item(
      id=id,
      sku=request.form['sku'],
      name=request.form['name'],
      description=request.form['description'],
      price=request.form['price'],
      quantity=request.form['quantity'],
      expiration_date=request.form['expiration_date']
   )

   if service.update(item) is False:
      return render_template('edit.html', error="Item sku already exists", data=item)

   return redirect(url_for('item_views_blueprint.index'))



@item_views_blueprint.route('/edit/<id>')
def edit_view(id):

   item = service.show(id)

   if item is False:
      return redirect(url_for('item_views_blueprint.index'))

   return render_template('edit.html', data=item)



# DELETE

@item_views_blueprint.route('/delete/<id>')
def destroy(id):
   service.destroy(id)
   
   return redirect(url_for('item_views_blueprint.index'))