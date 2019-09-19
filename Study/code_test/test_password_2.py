#coding:utf-8
import unittest
import json

class PasswordWithJsonTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data_file_path = './user_data.json'
        print('before all test methods')
        with open(data_file_path) as f:
            cls.test_data = json.loads(f.read())

    def test_weak_password(self):
        for data in self.test_data:
            passwd = data['password']

            self.assertTrue(len(passwd) >= 6)

            msg = "user %s has a weak password" %(data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'password123', msg)

    def test_dummy(self):
        pass

if __name__ == '__main__':
    unittest.main()

