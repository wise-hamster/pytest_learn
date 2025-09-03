from enums.user_enums import Statuses
from .player_local import PlayerLocal

from src.generators.player_local import PlayerLocal
from src.baseclasses.builder import BuilderBaseClase

player = {
    "account_status": 'ACTIVE',
    "balance": 10,
    "localize":{
        "en": {"nickname":"Kwerk"},
        "ru": {"nickname":'Кверк'}
    },
    "avatar": "https://www.google.com"
}

class Player(BuilderBaseClase):
    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com"):
        self.result["avatar"] = avatar
        return self
    
    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result['localize'] = {
                "en": PlayerLocal('en_US').build(),
                "ru": PlayerLocal('ru_RU').build()}
        return self
    


