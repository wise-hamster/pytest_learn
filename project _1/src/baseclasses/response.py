from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages
from pydantic import field_validator, model_validator


class Response:

    def __init__(self,response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None

    def validate (self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.model_validate(item)
                self.parsed_object = parsed_object
        else:
            schema.pars_obj(self.response_json)
                
        validate(self.response_json, schema)
        return self
    
    def validate_pydantic(self, schema):
        try:
            schema.model_validate(self.response_json)
        except ValueError as e:
            raise AssertionError(f'Pydantic validation errror: {e}') from e
        return self

    def assert_status_code(self,status_code):
        if isinstance(status_code,list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
    
    def assert_len_response(self,len_response):
        assert len(self.response_json) == len_response, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self
    
    def assert_ceo (self,ceo_name):
        assert self.response_json.get('ceo') == ceo_name,GlobalErrorMessages.WRONG_SEO.value
        return self
    def get_parsed_object (self):
        return self.parsed_object

    def __str__(self):
        return f'Status code: {self.response_status}'
        
         
