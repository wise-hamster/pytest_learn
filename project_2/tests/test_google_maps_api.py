from utils.api import GoogleMapsApi
from requests import Response

'''Create, modification and delete new location'''
class Test_create_place():

    def test_create_new_place(self):
        
        print('Method POST')
        result_post: Response = GoogleMapsApi.create_new_place()
