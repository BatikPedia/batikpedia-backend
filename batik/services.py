from batikpedia.firebase import FirestoreClient

client = FirestoreClient()

# Create your views here.
def list_all_batik():
    result = client.read('BatikPattern')
    print(result)
    pass


def get_batik_by_id(batik_id):
    result = client.read('BatikPattern', batik_id)
    print(result)
    pass
