from flask import Flask,session,current_app
from info import create_app
from flask_script import Manager
import logging

app = create_app("development")
# 7.创建manager管理类
manager = Manager(app)


@app.route("/")
def index():
    # 没有调整之前：　数据存在flask后端服务器　　只是讲session_id使用cookie传给客户端
    session["name"] = "James"
    return "hello word"


if __name__ == '__main__':
    # logging.debug("debug的日志信息")
    # logging.info("info的日志信息")
    # logging.warning("warning的日志信息")
    # logging.error("error的日志信息")
    # logging.critical("critical的日志信息")
    # current_app.logger.debug("使用flask里面封装的方法，记录debug日志")
    manager.run()