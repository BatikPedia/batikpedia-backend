'''
# Custom Base Model for Batikpedia
Override NOT_NULL_FIELDS and add model attributes as public attributes.

Example:
```
# The following snippet defines a model that has name and age as its attributes
# Attribute "name" is required so we put it in NOT_NULL_FIELDS.
NOT_NULL_FIELDS = ['name']

... __init__(self, name:str="", age:int=0, ...):
    self.name = name
    self.age = age
```

#### DO NOT EDIT!
Call our abang-abangan if you have any issue, thanks!
'''
from datetime import datetime
from batikpedia.firebase import FirestoreClient
from rest_framework.exceptions import ValidationError, NotFound

class FirebaseModel:
    NOT_NULL_FIELDS: list

    def __init__(self, document=None, uuid=None) -> None:
        self.__collection = self.__class__.__name__
        self.__created_at = datetime.now().isoformat()
        self.__updated_at = self.__created_at
        self.__fsclient = FirestoreClient()
        self.__uuid = uuid or ''
    
    def get_firestore_client(self):
        return self.__fsclient
    
    def get_collection_name(self):
        return self.__collection
    
    def __update_updated_at(self):
        self.__updated_at = datetime.now().isoformat()
    
    def __exists(self):
        if not self.__fsclient.read(collection=self.__collection, uuid=self.__uuid).exists:
            raise NotFound(f'Document {self.__uuid} does not exist.')

    def get(self, many=False):
        data = {}
        if many:
            docs = self.__fsclient.read(self.__collection)
            data = [{'uuid': doc.id, **doc.to_dict()} for doc in docs]
        else:
            doc = self.__fsclient.read(self.__collection, uuid=self.__uuid)
            if doc.exists: data = {'uuid': doc.id, **doc.to_dict()}
            else: raise NotFound(f'Document {self.__uuid} does not exists.')
        return data

    def save(self):
        data = {k: v for k, v in self.__dict__.items() if k in self.NOT_NULL_FIELDS}
        for key, value in data.items():
            if not value: raise ValidationError(f'Field {key} should not be null.')
        data.update({'created_at': self.__created_at, 'updated_at': self.__updated_at})
        self.__fsclient.create(collection=self.__collection, data=data)
        return data
    
    def update(self):
        self.__exists()
        self.__update_updated_at
        data = {k: v for k, v in self.__dict__.items() if '__' not in k and v}
        data.update({'updated_at': self.__updated_at})
        self.__fsclient.update(collection=self.__collection, uuid=self.__uuid, data=data)
        return data
    
    def delete(self):
        self.__exists()
        self.__fsclient.delete(collection=self.__collection, uuid=self.__uuid)
        return