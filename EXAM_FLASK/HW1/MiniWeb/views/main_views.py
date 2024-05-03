### => 기능 : main 범주의 url 라우팅
### => URL : /main, /main/info, /main/about, ...

from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return "Hello, pybo!"

@bp.route('/')
def index():
    return 'Pybo index'

