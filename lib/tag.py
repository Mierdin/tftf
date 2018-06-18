import requests

from lib.exceptions import ChildrenExist
from lib.getuuid import get_uuid
from lib.const import NAMESPACE, URL

def create_tag(tag_name, parent_fq_name):

    # This is how objects are assigned parents - through the FQ name
    tag_fq_name = parent_fq_name + [tag_name]

    data_dict = {
        "tag": {
            "fq_name": tag_fq_name,
            "parent_type": "fabric_namespace",
            "tag_type_name": "label",   # 0fedd836-01b7-45a7-b253-8ba4ba473c66
            "tag_value": "fabric-management_ip"
        }
    }
    resp  = requests.post('%s/tags' % URL, json=data_dict)
    import pdb; pdb.set_trace()
    return resp.json()["tag"]

def get_mgmt_tag():
    resp  = requests.get('%s/tags' % URL)
    for tag in resp.json()['tags']:
        if 'label=fabric-management_ip' in tag['fq_name']:
            return {  # to comply with resourcereference
                "href": tag["href"],
                "uuid": tag["uuid"],
                "to": tag["fq_name"]
            }

    # {"tags": [
        
    #     {
    #             "href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/808b7e0f-5f79-42be-a03e-7a278d12acee",
    #             "fq_name": ["k8s-svc=kube-dns"],
    #             "uuid": "808b7e0f-5f79-42be-a03e-7a278d12acee"
    #     },
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/a8631d86-2f93-4851-af20-2ae4bbc887af",
    #             "fq_name": ["namespace=kube-public"], "uuid": "a8631d86-2f93-4851-af20-2ae4bbc887af"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/abf535c4-fb07-4920-9f28-8cf73c0b2485",
    #             "fq_name": ["namespace=kube-system"], "uuid": "abf535c4-fb07-4920-9f28-8cf73c0b2485"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/f227ca79-d7fa-4248-9e00-6554242cdaf2",
    #             "fq_name": ["label=fabric-as_number"], "uuid": "f227ca79-d7fa-4248-9e00-6554242cdaf2"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/a9755843-8306-4bfd-9baf-d8eaa3051f9b",
    #             "fq_name": ["k8s-svc=kubernetes-dashboard"], "uuid": "a9755843-8306-4bfd-9baf-d8eaa3051f9b"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/c309579c-6be2-4730-adf7-e919f6b63d2f",
    #             "fq_name": ["namespace=default"], "uuid": "c309579c-6be2-4730-adf7-e919f6b63d2f"},

    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/642f4c0e-3bae-478e-a5ee-cc83d51f8ee9",
    #             "fq_name": ["label=fabric-management_ip"], "uuid": "642f4c0e-3bae-478e-a5ee-cc83d51f8ee9"},

    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/dbb292e5-77d9-4321-a63b-9e2abd29abc7",
    #             "fq_name": ["k8s-app=kube-dns"], "uuid": "dbb292e5-77d9-4321-a63b-9e2abd29abc7"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/a3032266-f78a-42ee-9a67-26c5b4d6b4f8",
    #             "fq_name": ["pod-template-hash=290980689"], "uuid": "a3032266-f78a-42ee-9a67-26c5b4d6b4f8"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/4622527a-01eb-4a4d-b785-04240daac3a9",
    #             "fq_name": ["k8s-svc=kubernetes"], "uuid": "4622527a-01eb-4a4d-b785-04240daac3a9"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/a3bbb474-1a5f-4fc3-a6c1-cb1bbf90f87d",
    #             "fq_name": ["application=k8s"], "uuid": "a3bbb474-1a5f-4fc3-a6c1-cb1bbf90f87d"},
    #             {"href": "http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/tag/89941f1e-56ba-4f1b-8990-cffefd918d62",
    #             "fq_name": ["namespace=contrail"], "uuid": "89941f1e-56ba-4f1b-8990-cffefd918d62"}]}


# def get_fabric(fabric_name):
    
#     try:
#         fabric_uuid = get_uuid(fabric_name, "fabric")
#     except ValueError:
#         return None

#     resp = requests.get('%s/fabric/%s' % (URL, fabric_uuid))
#     if resp.status_code != 200:
#             return None
#     else:
#         return resp.json()["fabric"]

# def delete_fabric(fabric_uuid):
#     resp = requests.delete('%s/fabric/%s' % (URL, fabric_uuid))
#     if resp.status_code == 409:
#         raise ChildrenExist(resp)
