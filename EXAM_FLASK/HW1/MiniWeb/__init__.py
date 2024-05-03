### 모듈 로딩 
from flask import Flask, render_template, Blueprint

### 어플리케이션 팩토리 
def create_app():
    app=Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('iframe.html')
    
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app
