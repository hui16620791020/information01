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



class DevelopmentConfig(Config):
    """开发阶段项目配置类"""
    # 开启debug模式
    DEBUG = True


class ProductionConfig(Config):
    """生产阶段项目配置类"""
    # 开启debug模式
    DEBUG = False
    # 修改数据库配置链接对象
    # 数据库链接配置
    # SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@阿里云ip地址:3306/information01"


#  暴露一个接口给外部调用
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}