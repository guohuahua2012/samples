#coding:utf-8
import unittest
import json

class WeakPasswordTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data_file_path = './user_data.json'
        print('before all test methods')
        with open(data_file_path) as f:
            cls.test_data = json.loads(f.read())

    def test_weak_password(self):
        res = True
        msg = []
        for data in self.test_data:
            passwd = data['password']
            tmp_res = True

            tmp_res = tmp_res and (len(passwd) >= 6)
            tmp_res = tmp_res and (passwd != 'password')
            tmp_res = tmp_res and (passwd != 'password123')
            if not tmp_res:
                msg.append("user %s has a weak password %s" %(data['name'], data['password']))
            res = res and tmp_res

        self.assertTrue(res, "\n".join(msg))
    def test_dummy(self):
        pass

if __name__ == '__main__':
    unittest.main()