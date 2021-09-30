from unittest import TestCase
import requests

#声明单元测试类
class TestBank(TestCase):
    #声明单元测试的方法
    #方法名以“test_”开头
    def test_del(self):
        url = "http://localhost:5000/bank/del/20"
        method = 'DELETE'
        resp = requests.request(method, url)
        #断言，最后一个参数表示断言失败的信息
        self.assertIs(resp.status_code, 200, '请求失败')
        print(resp.text)
    def test_publish(self):
        url="http://localhost:5000/bank/publish"
        method= 'post'
        resp = requests.request(method, url)
        # 或者写成requests.post(url)
        self.assertIs(resp.status_code, 200, '请求失败')
        print(resp.headers.get('Content-Type'))