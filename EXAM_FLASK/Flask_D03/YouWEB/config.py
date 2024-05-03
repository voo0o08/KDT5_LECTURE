import os

# 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

# 다양한 DBMS URI
DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'

DB_MYSQL_URI = 'mysql+pymysql://root:1234@localhost:3306/testdb'

## 사용할 DBMS 설정 / SQLALCHEMY_ -> 시작 변수명 고정 
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
