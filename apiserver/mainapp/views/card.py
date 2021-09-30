from flask import Blueprint
# 通过函数找到返回路径
from flask import url_for

blue = Blueprint('cardBlue',__name__)

@blue.route('/add/<bankName>')
def addCard(bankName):
    return """
        %s 开户成功
        <br>
        <a href="%s">返回首页</a>
    """ % (bankName,url_for('index'))

@blue.route('/select_card')
def selectBank():
    bankName= "中国工商银行"
    next_url= "/card/add/"+bankName
    # 第一种方法
    # return """
    #     选择银行成功，三秒后<a href="%s">自动跳转到开户页面
    # """% ("/card/add/"+bankName)
    # 第二种
    # next_url
    # 第三种 反向解析
    return """
        选择银行成功，三秒后<a href="%s">自动跳转到开户页面
    """% url_for('cardBlue.addCard',bankName=bankName)
