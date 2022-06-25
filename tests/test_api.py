import unittest


from polaris_python.api import PolarisAPIClient


class MyTestCase(unittest.TestCase):
    def test_request_api(self):
        client = PolarisAPIClient()
        result = client.request_api()

    def test_register(self):
        client = PolarisAPIClient()
        result = client.register('1', '2')


if __name__ == '__main__':
    unittest.main()
