import requests

from lib.const import NAMESPACE, URL

def get_uuid(name, obj_type):

    data_dict = {
        "fq_name": [
            NAMESPACE,
            name
        ],
        "type": obj_type
    }
    resp  = requests.post('%s/fqname-to-id' % URL, json=data_dict)
    # import pdb; pdb.set_trace()
    return resp.json()["uuid"]
