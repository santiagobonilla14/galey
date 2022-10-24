import functools
from flask import(Blueprint, render_template, request, flash, redirect, url_for,session,g)
from app.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('control', __name__, url_prefix="/")

@bp.route ('/', methods=['GET'])
def index():
    return render_template('galeria/index.html')

@bp.route ('/login', methods=['GET'])
def login():
    return render_template('galeria/login.html')