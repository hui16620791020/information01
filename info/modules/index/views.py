from . import index_bp
from flask import session,current_app
# from info import redis_store,models

# 2.使用蓝图对象
# 127.0.0.1:5000/index/
@index_bp.route("/")
def index():


    # redis_store.set("name", "laowang")
    current_app.logger.debug("记录日志")
    # 没有调整之前：　数据存在flask后端服务器　　只是讲session_id使用cookie传给客户端
    session["name"] = "James"
    return "hello word"
