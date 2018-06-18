import requests

from lib.exceptions import ChildrenExist
from lib.getuuid import get_uuid
from lib.const import NAMESPACE, URL

def create_fabric(fabric_name):
    data_dict = {
        "fabric": {                     # http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/documentation/contrail_openapi.html#fabriccreate
            "fq_name": [
                NAMESPACE,
                fabric_name
            ],
            "fabric_credentials": {     # http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/documentation/contrail_openapi.html#devicecredentiallist
                "device_credential": [  # TODO(mierdin): I believe the docs need to be updated to be more clear this should be a list.
                    {

                        # Can this be named differently so we can have different credentials?
                        "credential": {     # http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/documentation/contrail_openapi.html#usercredentials
                            "username": "admin",
                            "password": "arista"
                        },
                        "vendor": "arista"
                        # "device_family": ""
                    }
                ]
            }  
            # "physical_router_refs": [   # http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/documentation/contrail_openapi.html#resourcereference
            #     {
            #         "href": "",
            #         "uuid": "",
            #         "to": ""
            #     }
            # ]
        }
    }
    resp  = requests.post('%s/fabrics' % URL, json=data_dict)
    return resp.json()["fabric"]

def get_fabric(fabric_name):
    
    try:
        fabric_uuid = get_uuid(fabric_name, "fabric")
    except ValueError:
        return None

    resp = requests.get('%s/fabric/%s' % (URL, fabric_uuid))
    if resp.status_code != 200:
            return None
    else:
        return resp.json()["fabric"]

def delete_fabric(fabric_uuid):
    resp = requests.delete('%s/fabric/%s' % (URL, fabric_uuid))
    if resp.status_code == 409:
        raise ChildrenExist(resp)
