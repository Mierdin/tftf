import requests

from lib.getuuid import get_uuid
from lib.const import NAMESPACE, URL

def create_fabric_namespace(fns_name, parentfabric_fq_name, v4prefix, mgmt_tag):

    

    # This is how objects are assigned parents - through the FQ name
    fns_fq_name = parentfabric_fq_name + [fns_name]

    data_dict = {
        "fabric-namespace": {  # http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/documentation/contrail_openapi.html#fabricnamespacecreate
            "fq_name": fns_fq_name,
            "parent_type": "fabric",
            "fabric_namespace_type": "IPV4-CIDR",
            "fabric_namespace_value": {
                "ipv4_cidr": {
                    "subnet": [{
                        "ip_prefix": v4prefix[:v4prefix.index("/")],
                        "ip_prefix_len": v4prefix[v4prefix.index("/")+1:]
                    }]
                }
            },
            "tag_refs": [mgmt_tag]
        }
    }
    resp  = requests.post('%s/fabric-namespaces' % URL, json=data_dict)
    # import pdb; pdb.set_trace()
    return resp.json()["fabric-namespace"]

def get_fabric_namespace(fns_name):
    
    try:
        fns_uuid = get_uuid(fns_name, "fabric-namespace")
    except ValueError:
        return None

    resp = requests.get('%s/fabric/%s' % (URL, fns_uuid))
    if resp.status_code != 200:
            return None
    else:
        return resp.json()["fabric-namespace"]

def delete_fabric_namespace(fns_uuid):
    resp = requests.delete('%s/fabric-namespace/%s' % (URL, fns_uuid))
    if resp.status_code != 200:
        # import pdb; pdb.set_trace()
        raise Exception("FNS delete failed.")
