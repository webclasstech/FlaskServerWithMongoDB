from bson import ObjectId

def serialize_objectid(document):
    if isinstance(document, dict):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
            elif isinstance(value, dict):
                document[key] = serialize_objectid(value)
            elif isinstance(value, list):
                document[key] = [serialize_objectid(item) \
                                     if isinstance(item, dict) \
                                     else item for item in value]
    return document