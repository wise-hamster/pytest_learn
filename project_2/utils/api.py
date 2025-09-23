from utils.http_methods import Http_methods

base_url = 'https://rahulshettyacademy.com' #domen name
key = '?key=qaclick123' #params

class GoogleMapsApi():

    """Method for create a new location"""
    @staticmethod
    def create_new_place():
        # Body for request
        json_for_create_new_place = {
        "location": {
                    "lat": -38.383494,
                    "lng": 33.427362},
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park", "shop"],
        "website": "http://google.com",
        "language": "French-IN"}
        #Method
        post_resource = '/maps/api/place/add/json'
        post_url = base_url+post_resource+key
        print(post_url)
        result_post = Http_methods.post(post_url,json_for_create_new_place)
        print(result_post.text)
        return result_post
