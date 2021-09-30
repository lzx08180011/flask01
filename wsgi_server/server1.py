from wsgiref.simple_server import make_server
import os

def app(env, make_response):
    #处理核心业务函数
    """
    请求路径：PATH_INFO  以斜杠开头
    请求方法：REQUEST_METHOD
    请求查询参数：QUERY_STRING
    客户端地址：REMOTE_ADDR 
    上传数据类型：CONTENT_TYPE
    客户端代理（浏览器）：HTTP_USER_AGENT
    """
    # for k, v in env.items():
    #     print(k, ':' ,v)
    # 生成响应头
    path = env.get('PATH_INFO') #获取资源路径
    headers = [] #响应头  根据响应的数据不同 头对应也不同
    body = [] #响应数据

    static_dir = 'Html'
    if path == '/favicon.ico':
        res_path = os.path.join(static_dir, 'images/2.jpg')
        # 图片资源
        headers.append(('Content-Type','image/*'))
    elif path == '/':
        # 网页资源
        res_path = os.path.join(static_dir, 'test04.html')
        headers.append(('Content-Type', 'text/html;charset=utf-8'))
    else:
        #其他资源 css/js/图片/mp4/mp3
        res_path = os.path.join(static_dir, path[1:])
        if res_path.endswith('.html'):
            headers.append(('Content-Type', 'text/html;charset=utf-8'))
        elif any((res_path.endswith('.png'),
                  res_path.endswith('.jpg'),
                  res_path.endswith('.gif'))):
            headers.append(('Content-Type','image/*'))
        else:
            headers.append(('Content-Type', 'text/*;charset=utf-8'))
    #Content-Type 响应头
    # make_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    # return ['<h3>Hi, WSGI</h3>'.encode('utf-8')]   #响应数据
    #判断数据资源是否存在
    status_code = 200
    if not os.path.exists(res_path):
        status_code = 404
        body.append('<h4 style="color:red">请求数据不存在：404</h4>'.encode('utf-8'))
    else:
        with open(res_path, 'rb') as f:
            body.append(f.read())
    make_response('%s OK' %status_code, headers)
    return body
#生成WEB进程
host = '0.0.0.0'
port = 8000
httpd = make_server(host,port,app)
print('running http://%s:%s' % (host, port))
#启动服务
httpd.serve_forever()

