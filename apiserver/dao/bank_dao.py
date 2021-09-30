from dao import BaseDao

class BackDao(BaseDao):
    def find_all(self):
        return super().find_all('bank')


if __name__ == '__main__':
    dao = BackDao()
    print(dao.find_all())