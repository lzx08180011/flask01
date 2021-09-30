from mainapp import app
from flask_script import Manager
from mainapp.views import bank
from mainapp.views import user
from mainapp.views import card
from flask_cors import CORS
from flask import url_for
from flask import render_template
@app.route('/')
def index():
    return """
        <ul>
            <li><a href="%s">银行卡开户</li>
            <li><a href="%s">银行管理</li>
            <li><a href="%s">用户管理</li>
        </ul>
    """% (url_for('cardBlue.addCard',bankName="中国工商银行"),
          url_for('bankBlue.edit',bank_id=1),
          url_for('userBlue.find')
          )

if __name__ == '__main__':

    #使接口通用
    CORS().init_app(app)

    #将蓝图对象导入flask服务里面
    app.register_blueprint(bank.blue, url_prefix='/bank')
    app.register_blueprint(card.blue, url_prefix='/card')
    # 前缀 url_prefix
    app.register_blueprint(user.blue, url_prefix='/user')
    manager = Manager(app)




    manager.run()
