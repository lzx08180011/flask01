from flask import Blueprint
from flask import request
from flask import jsonify
from dao import bank_dao
from flask import make_response
from flask import Response
from flask import render_template
from flask import redirect
from flask import abort
from datetime import datetime
from flask import url_for
blue = Blueprint('bankBlue', __name__)

@blue.route('/login')
def login():
    response = make_response('进入登陆界面')

    # 添加Cookie
    # datetime.strptime(date_string,format) format查表
    # response.delete_cookie('username',domain='127.0.0.0.1')
    response.set_cookie('username','disen',expires=datetime.strptime('2021-04-10 17:23:00','%Y-%m-%d %H:%M:%S'))
    return response
@blue.route('/delCookie/<cookie_name>')
def del_cookie(cookie_name):
    resp = make_response("删除cookie")
    resp.delete_cookie(cookie_name)
    return  resp

@blue.route('/publish', methods=['POST'])
def publish_bank():
    data = '{"id": 101, "data": 20}'
    code = 200
    Response()
    # 将数据和响应状态码封装到response对象中
    response = make_response(data,code)
    # 根据数据的类型，设置响应头
    response.headers['Content-Type']='application/json;charset=utf-8'
    return response

@blue.route('/bank', methods=['GET','POST'])

def bank():
    dao = bank_dao.BackDao()
    data = dao.find_all()
    return jsonify({
        'status':20,
        'message':'find_all ok',
        'data':data
    })

@blue.route('/delbank', methods=['GET'])
def del_bank():
    bank_id = request.args.get('id')

    return "<h3>正在删除银行: %s</h3>" % bank_id

@blue.route('/edit/<int:bank_id>',methods=['GET','POST'])
def edit(bank_id):
    return "正在编辑：银行编号 %s" %bank_id

@blue.route('/find/<keyword>/',methods=['GET','POST'])
def find(keyword):
    return "返回的是 %s" %keyword

@blue.route('/forward/<path:url>',methods=['GET'])
def forward(url):
    return """
        <div id="result"></div>
        <script>
            let steps = 5;
            let id = setInterval(()=>{
                if (steps >1){
                    document.getElementById("result").innerText="剩余"+ (--steps) +"秒";
                }else{
                    open("%s", target="_self")
                    let steps= 0;
                }
            },1000);
        </script>   
    """ % url

@blue.route('/del/<int:ban_id>',methods=['DELETE'])
def delete4id(ban_id):
    return "删除成功！！！！"

@blue.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        # 接受开户信息
        bankID = request.form.get('bank')
        username = request.form.get('username')
        phone = request.form.get('phone')
        if phone =='15529060464':
            # 可以中断请求页面
            abort(403)

    #     验证数据是否为空
    #     假如操作成功
    #     进入列表
        return redirect(url_for('bankBlue.listCard'))
    # GET请求。响应是开户页面
    return render_template('card/add.html')
@blue.route('/list',methods=['GET','POST'])
def listCard():
    # raise Exception('抛出我们自己的异常')
    return render_template('card/list.html')