from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect

blue = Blueprint('userBlue',__name__)

#申请API接口
@blue.route('/find', methods=['GET'])
def find():
    return render_template("bank_user.html",request=request)

@blue.route('/add', methods=['POST'])
def add():
    return "<h3> 添加成功</h3>"

@blue.route('/login', methods=['POST'])
def login():
    if resquet.method == 'POST':
        # 读取登陆用户信息
        # 前端页面表单域：name，password
        name = request.form.get('name')
        password = request.form.get('password')
        if all((name, password)):
            message = "用户口令不能为空"
        else:
            # 将数据写入数据库
            dao = UserDao()
            # dao.save(name=name,password=password)注册的的时候使用
            user = dao.login(name, password)
            if not user:
                message = "查无 %s 此用户，输入正确的用户和口令" % name

            else:
                # 将用户信息
                session['login_user'] = user
                # 重定向到主页去
                return redirect('/index')

    return render_template('user/login.html', locals())