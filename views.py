import pandas as pd
from flask import Blueprint, render_template
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


views_bp = Blueprint('views_bp', __name__)

@views_bp.route('/')
def home():
    return render_template('home.html', title='Home')

@views_bp.route('/data')
def data():
    return render_template('data.html', title='Data')

@views_bp.route('/stats')
def stats():
    return render_template('stats.html', title='Stats')

@views_bp.route('/update')
def update():
    return render_template('update.html', title='Update')
