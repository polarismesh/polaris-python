# -*- coding: utf-8 -*-

import requests


class BaseAPIClient(object):
    def __init__(self, host):
        self.api_root = f"http://{host}:8999"

    def request_api(self, api_path, api_params):
        """
        Low-level API
        :return:
        """
        url = self.api_root + api_path
        r = requests.post(url, data=api_params)
        result = r.json()
        if 'error_code' in result and result['error_code'] != 0:
            raise ValueError(result['error_msg'])
        return result


class NamingAPIMixin(object):
    def register(self, param1, param2):
        """
        High-level API
        :return:
        """
        api_path = '/register'
        return self.request_api(api_path=api_path, api_params={'param1': param1, 'param2': param2})


class PolarisAPIClient(BaseAPIClient, NamingAPIMixin):
    pass
