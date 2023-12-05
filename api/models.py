''' Custom base model for Batikpedia. '''
from datetime import datetime
from batikpedia.firebase import FirestoreClient
from rest_framework.exceptions import ValidationError, NotFound

# Create your models here.
class BaseModel:
    COLLECTION_NAME: str
    NOT_NULL_FIELDS: list

    def __init__(self, document=None, uuid=None) -> None:
        self.__created_at = datetime.now().isoformat()
        self.__updated_at = self.created_at
        self.__fsclient = FirestoreClient()
        self.__uuid = uuid or ''
    
    def __update_updated_at(self): self.__updated_at = datetime.now().isoformat()
    def __exists(self): return self.__fsclient.read(collection=self.COLLECTION_NAME, uuid=self.__uuid).exists

    def get(self, many=False):
        data = {}
        if many:
            docs = self.__fsclient.read(self.COLLECTION_NAME)
            data = [{'uuid': doc.id, **doc.to_dict()} for doc in docs]
        else:
            doc = self.__fsclient.read(self.COLLECTION_NAME, uuid=self.__uuid)
            if doc.exists: data = {'uuid': doc.id, **doc.to_dict()}
        return data

    def save(self):
        data = {k: v for k, v in self.__dict__.items() if k in self.NOT_NULL_FIELDS}
        for key, value in data.items():
            if not value: raise ValidationError(f'Field {key} should not be null.')
        data.update({'created_at': self.__created_at, 'updated_at': self.__updated_at})
        self.__fsclient.create(collection=self.COLLECTION_NAME, data=data)
        return data
    
    def update(self):
        self.__exists()
        self.__update_updated_at()
        data = {k: v for k, v in self.__dict__.items() if '__' not in k and v}
        data.update({'created_at': self.__created_at, 'updated_at': self.__updated_at})
        return data