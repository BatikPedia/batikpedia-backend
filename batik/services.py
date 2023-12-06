from batikpedia.firebase import FirestoreClient

client = FirestoreClient()

BATIK_PATTERN_COLLECTION_NAME = 'BatikPattern'

def __batik_doc_to_batik_obj(document) :
    batik_obj = {
        "id" : document.id,
        "name" : document.to_dict()["name"],
        "province" : document.to_dict()["province"],
        "history" : document.to_dict()["history"],
        "references" : document.to_dict()["references"],
    }
    return batik_obj


# Create your views here.
def list_all_batik():
    from_fs = client.read(BATIK_PATTERN_COLLECTION_NAME)
    result = []
    for document in from_fs:
        result.append(__batik_doc_to_batik_obj(document))
    return result


def get_batik_by_id(batik_id):
    result = client.read(BATIK_PATTERN_COLLECTION_NAME, batik_id)
    try:
        return __batik_doc_to_batik_obj(result)
    except TypeError:
        return None
