import requests

from lib.getuuid import get_uuid
from lib.const import NAMESPACE, URL, ANALYTICS_URL

def execute_job(job_template_id, fabric_uuid, device_list):

    # Specific to discover device schema for now: https://github.com/Juniper/contrail-controller/blob/R5.0/src/config/fabric-ansible/ansible-playbooks/schema/discover_device_schema.json#L23:13
    # data_dict = 

    data_dict = {
        "job_template_id": job_template_id,
        "device_list": device_list,
        "device_id": "la dee da",
        "input": {
            "fabric_uuid": fabric_uuid
            # "fabric_fq_name": [
            #         NAMESPACE,
            #         "foobar_fabric"
            # ]
        }
    }

    resp  = requests.post('%s/execute-job' % URL, json=data_dict)
    return resp.json()["job_execution_id"]

def get_job(job_execution_id):
    
    resp  = requests.get('%s/analytics/uves/job-executions' % ANALYTICS_URL)

    # data_dict = {
    #     # "sort": 1,
    #     "start_time": 1525983392000,
    #     # "sort_fields": ["MessageTS"],
    #     # "filter": [
    #     #     {"name": "Type", "value": "1", "op": 1}
    #     # ],
    #     "end_time": 1526069795000,
    #     "select_fields": [
    #         "MessageTS"
    #     ],
    #     "table": "ObjectJobExecutionTable"
    #     # "where": [[{"name": "ModuleId", "value": "ControlNode", "op": 1}, {"name": "Messagetype", "value": "BgpPeerMessageLog", "op": 1}]]
    # }

    # resp  = requests.post('%s/analytics/query' % ANALYTICS_URL, json=data_dict)

    # import pdb; pdb.set_trace()

    