from flask import Flask,session
from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

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

    # 加密字符串
    SECRET_KEY = "dIAWjw/xHnFH+MLXDshe98mbSH8QBchWS0bS36/WFpCZndzeSPdGb++3xdhPIYNJ"
    # 调整session存储位置（存储到redis）
    # session存储到那种数据库
    SESSION_TYPE = "redis"
    # 上面指明的数据库的实例对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session数据需要加密
    SESSION_USE_SIGNER = True
    #  不设置永久存储
    SESSION_PERMANENT = False
    # 默认存储有效时常
    PERMANENT_SESSION_LIFETIME = 86400*2

# 1.创建app对象
app = Flask(__name__)
# 2.注册配置信息到app对象
app.config.from_object(Config)
# 3.创建MYSQL数据库对象
db = SQLAlchemy(app)
# 创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# ５.开启csrf后端验证保护机制
#  提取cookie中的csrf_token和ajax里面的csrf_token进行比较
csrf = CSRFProtect(app)
# 6.创建session扩展类对象
Session(app)


@app.route("/")
def index():
    return "hello word"


if __name__ == '__main__':
    app.run(debug=True)