from flask import Blueprint, render_template, request, redirect, url_for
from .models import FoodItem, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = FoodItem.query.all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['POST'])
def add_item():
    # Logic to add new food item
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete_item(id):
    # Logic to delete food item
    return redirect(url_for('main.index'))

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    # Logic to update food item
    return redirect(url_for('main.index'))