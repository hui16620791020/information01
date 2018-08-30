from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict
from flask import Flask

# 外界使用　　　create_app("development")-->  开发模式的app
#            create_app("production")-->  生产模式的app
def create_app(config_name):
    # """生产app的工长方法"""
    # 1.创建app对象
    app = Flask(__name__)
    # 2.注册配置信息到app对象
    # config_dict["development"]: DevelopmentConfig.开发阶段配置
    configClass = config_dict[config_name]
    app.config.from_object(configClass)
    # 3.创建MYSQL数据库对象
    db = SQLAlchemy(app)
    # 创建redis数据库对象
    redis_store = StrictRedis(host=configClass.REDIS_HOST, port=configClass.REDIS_PORT)
    # ５.开启csrf后端验证保护机制
    #  提取cookie中的csrf_token和ajax里面的csrf_token进行比较
    csrf = CSRFProtect(app)
    # 6.创建session扩展类对象
    Session(app)
    return app
