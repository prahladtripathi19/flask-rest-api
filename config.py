import os
#SQLALCHEMY_DATABASE_URI = ' = 'mysql://root:password@localhost/workindia'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/workindia??charset=utf8mb4'
SECRET_KEY = os.getenv('SECRET_KEY', 'workindia')