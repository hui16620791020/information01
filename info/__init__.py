from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict
from flask import Flask
import logging

def create_log(config_name):
    """"记录日志的函数"""
    # 设置日志的记录等级
    logging.basicConfig(level=config_dict[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

# 外界使用　　　create_app("development")-->  开发模式的app
#            create_app("production")-->  生产模式的app
def create_app(config_name):
    # """生产app的工长方法"""
    # 记录日志
    create_log(config_name)
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
