from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'
    WRONG_SEO = 'Name Seo is Elon Mask. Error in test'
    WRONG_EMAIL_NO_VALID = 'Email is not valid'