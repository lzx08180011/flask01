from dao import BaseDao
import hashlib

class UserDao(BaseDao):
    def login(self,name,password):
        pwd = hashlib.md5(password.encode('utf-8')).hexdigest()
        pes = super().find_all('bank',' where name=%s and password=%s',name,pwd)
        if pes:
            return pes[0]



if __name__ == '__main__':
    dao = UserDao()
    result= dao.login('辣子','888888')
    print(result)
