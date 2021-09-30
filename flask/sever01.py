from flask import Flask

app = Flask(__name__)  #__name__ 可以是任意的小写字母。表示Flask的应用对象名称

#  声明web服务的请求资源（指定资源访问路由）
# RESTful 设计风格中关于资源的动作 GET(获取) POST(更新) PUT DELLE(删除) PATCH(批量更新)
@app.route('/hi', methods=['GET','POST'])#装饰器
def hi():
    #request是请求对象（HTTPrequest）包含路径 方法 请求头 上传表单数据
    # name = request.args.get('username')
    # password = request.args.get('password')
    from flask import request
    # 获取平台参数
    #限制移动设备 可以设置参数
    platform = request.args.get('platform', 'pc')

    if platform.lower() != 'android':
        return """
            <h2> 目前只支持Android设备 </h2>
        """

    if request.method =='GET':
    #返回生成的HTML网页内容
        return """
        <h1>用户登录界面</h1>
        <form action="/hi" method="post">
            <input name="name" placeholder="用户名"><br>
            <input name="pwd" placeholder="口令"><br>
            <button>提交</button>
        </form> 
        """
    else:
        #获取表单参数
        name = request.form.get('name')
        pwd = request.form.get('pwd')

        if all((
            name == 'lzx',
            pwd == '123'
        )):
            return """
                <h2 style="color:bule;">登录成功<h2>
            """
        else:
            return """
                <h2 style="color:red;">登录失败, <a href="/hi">重试</a></h2>
            """

app.run(host = "localhost", port = 5000)