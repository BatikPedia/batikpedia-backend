from api.models import FirebaseModel
from batik.models import BatikPattern
from rest_framework.exceptions import NotFound

class Scanning(FirebaseModel):
    NOT_NULL_FIELDS = ['user', 'batik']

    def __init__(self, user:str='', batik:str='', uuid=None) -> None:
        self.user = user
        self.batik = batik
        super().__init__(uuid)

    def get(self, many=False):
        data = super().get(many)

        # Serialize batik data
        if many:
            for d in data:
                batik_data = self.get_firestore_client().read(BatikPattern().get_collection_name(), uuid=d.get('batik', ''))
                d.update({'batik': {'uuid': batik_data.id, **batik_data.to_dict()}})
        else:
            batik_data = self.get_firestore_client().read(BatikPattern().get_collection_name(), uuid=data.get('batik', ''))
            data.update({'batik': {'uuid': batik_data.id, **batik_data.to_dict()}})
        return data

    def save(self):
        # Foreign key validation
        if self.batik and not self.get_firestore_client().read(BatikPattern().get_collection_name(), uuid=self.batik).exists:
            raise NotFound(f'Batik {self.batik} does not exist.')
        return super().save()
    
    def update(self):
        # Foreign key validation
        if self.batik and not self.get_firestore_client().read(BatikPattern().get_collection_name(), uuid=self.batik).exists:
            raise NotFound(f'Batik {self.batik} does not exist.')
        return super().update()