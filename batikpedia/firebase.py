import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from dotenv import dotenv_values
import json
import os

# Write some neccessary constants here
SERVICE_ACCOUNT_KEY = 'service_account_key'

# env = dotenv_values('.env')
env = os.environ
print("os.environ:")
print(env)

firebase, data = {
    SERVICE_ACCOUNT_KEY: {k: v for k, v in env.items() if k.startswith('FIREBASE.SERVICE_ACCOUNT_KEY')}
}, {}

for key in firebase.keys():
    payload = ''
    for k, v in firebase[key].items():
        k = k.lower()
        payload += f'  "{k[k.index(key) + len(key) + 1:]}": "{v}",\n'
    payload = '{\n' + payload[:-2] + '\n}'
    data.update({key: json.loads(payload)})

print("Loaded variables:")
print(data.get(SERVICE_ACCOUNT_KEY))

# Certificate definition
cred = credentials.Certificate(data.get(SERVICE_ACCOUNT_KEY, None))

firebase_admin.initialize_app(cred)

class FirestoreClient():
    ''' Commonly used to perform CRUD or things in Firestore. '''

    def __init__(self):
        self.__fs = firestore
        self.__db = self.__fs.client()

    def create(self, collection: str, data: dict, sub: dict=None):
        '''
        Create (POST) new instance into collection.
        If sub is provided, it will be used as a subcollection: { uuid, collection }
        '''
        if not sub:
            self.__db.collection(collection).add(data)
            return
        if 'uuid' not in sub.keys() or 'collection' not in sub.keys():
            print('"uuid" and "collection" should be found as keys.')
            return
        self.__db.collection(collection).document(sub['uuid']).collection(sub['collection']).add(data)
        return

    def read(self, collection: str, uuid: str = None, where: list=None):
        '''
        Read (GET) instance(s) from a collection.
        If uuid is provided, it will return a single instance.
        If where is provided, it will be used as a WHERE query: [ key, operator, value ]
        '''
        if not uuid:
            if not where:
                return self.__db.collection(collection).get()
            return self.__db.collection(collection).where(where[0], where[1], where[2]).get()
        return self.__db.collection(collection).document(uuid).get()

    def update(self, collection: str, uuid: str, data: dict, sub: dict=None):
        '''
        Update (PUT) an instance from a collection.
        If sub is provided, it will be used as a subcollection: { collection }
        '''
        if not sub:
            self.__db.collection(collection).document(uuid).update(data)
            return
        if 'collection' not in sub.keys():
            print('"collection" not found in sub keys.')
            return
        self.__db.collection(collection).document(uuid).collection(sub['collection']).update(data)
        return

    def delete(self, collection: str, uuid: str, field: str=None):
        '''
        Delete (DELETE) an instance from a collection.
        If field is provided, it will be used to delete a field from an instance.
        '''
        if not field:
            return self.__db.collection(collection).document(uuid).delete()
        return self.__db.collection(collection).document(uuid).update({f'{field}': self.__fs.DELETE_FIELD})