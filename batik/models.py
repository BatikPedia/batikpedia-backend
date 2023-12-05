from api.models import FirebaseModel

class BatikPattern(FirebaseModel):
    NOT_NULL_FIELDS = ['name', 'history', 'province', 'references']

    def __init__(self, name:str='', history:str='', province:str='', references:list=[], document=None, uuid=None) -> None:
        self.name = name
        self.history = history
        self.province = province
        self.references = references
        super().__init__(document, uuid)