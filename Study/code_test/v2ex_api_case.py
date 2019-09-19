#coding: utf-8
import requests
import unittest

class V2exAPITestCase(unittest.TestCase):

    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        payload = {"name":"python"}
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Cache-Control': 'keep-alive'
        }
        r = requests.get(url, params=payload, headers=headers).json()
        self.assertEqual(r['name'], 'python')
        self.assertEqual(r['id'], 90)


if __name__ == '__main__':
    unittest.main()