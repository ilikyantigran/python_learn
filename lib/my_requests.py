import requests
from lib.logging import Logger
import allure
class MyRequests():
    @staticmethod
    def get(url: str, headers: dict = None, cookies: dict = None, data: dict = None):
        with allure.step(f"GET Request to url '{url}'"):
            return MyRequests._send(url, data, headers, cookies, "GET")
    @staticmethod
    def post(url: str, headers: dict = None, cookies: dict = None, data: dict = None):
        with allure.step(f"POST Request to url '{url}'"):
            return MyRequests._send(url, data, headers, cookies, "POST")
    @staticmethod
    def put(url: str, headers: dict = None, cookies: dict = None, data: dict = None):
        with allure.step(f"PUT Request to url '{url}'"):
            return MyRequests._send(url, data, headers, cookies, "PUT")
    @staticmethod
    def delete(url: str, headers: dict = None, cookies: dict = None, data: dict = None):
        with allure.step(f"DELETE Request to url '{url}'"):
            return MyRequests._send(url, data, headers, cookies, "DELETE")
    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str) :
        url = f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url,data,headers,cookies,method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Unexpected method {method}")

        Logger.add_response(response)

        return response
