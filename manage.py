from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis

# 创建项目配置类
class Config(object):
    """项目配置类"""

    # 开启debug模式
    DEBUG = True

    # mysql数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information01"
    #  不跟踪数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

# 1.创建app对象
app = Flask(__name__)
# 2.注册配置信息到app对象
app.config.from_object(Config)
# 3.创建MYSQL数据库对象
db = SQLAlchemy(app)
# 创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route("/")
def index():
    return "hello word"


if __name__ == '__main__':
    app.run(debug=True)