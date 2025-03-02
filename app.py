from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, DairyProduct
from forms import ProductForm

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = DairyProduct.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = DairyProduct(
            name=form.name.data,
            category=form.category.data,
            price=form.price.data,
            quantity=form.quantity.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_product.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = DairyProduct.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.category = form.category.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('update_product.html', form=form, product=product)

@app.route('/delete/<int:id>')
def delete_product(id):
    product = DairyProduct.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'danger')
    return redirect(url_for('index'))

@app.route('/api/products', methods=['GET'])
def get_products():
    products = DairyProduct.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'quantity': product.quantity,
        'price': product.price * product.quantity
    } for product in products])

if __name__ == '__main__':
    app.run(debug=True)
