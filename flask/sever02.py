from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
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


@app.route('/bank', methods=['GET','POST'])
def bank():
    # 加载数据（mode1 交互操作）
    data  = {'title':'绑定银行卡',
             'error_message':''}
    # 渲染模板
    html = render_template('bank_edit.html',**data)
    if request.method=='GET':
        return html
    else:
        name = request.form.get('name')
        num = request.form.get('card_num')
        if all((name,num)):
            # Flask 的日志名称就是脚本自己的名字
            app.logger.info('name:%s---> num:%s' % (name, num))

            return"""
                <h1 style="color:red;">提交成功</h1>            
                <h4 id="result"></h4>
                <script>
                    let steps = 5;
                    let interval_id = 0;
                    interval_id = setInterval(()=>{
                        if(steps >=0){
                            document.getElementById('result').innerText= steps--
                        }else {
                            //取消定时器
                            clearInterval(interval_id);
                            window.open('/hi', target='_self')
                        }
                    }, 1000)
                </script>
            """
        else:
            data['error_message']='卡号和者银行不可为空'
            return render_template('bank_edit.html',**data)

app.run('localhost',
        5000,
        True)