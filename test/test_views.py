import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        test_data = {"imie": "Sylwia", "msg": "Hello World!"}
        js = json.loads(rv.data)
        self.assertEqual(test_data['imie'],js['imie'])
        self.assertEqual(test_data['msg'], js['msg'])
        self.assertEqual(len(test_data), len(js))


    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Sylwia</name><msg>Hello World!</msg></greetings>', rv.data)
