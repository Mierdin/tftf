import requests

from lib.tag import get_mgmt_tag
from lib.const import JOB_TEMPLATE_NAMES, ARISTA_DEVICE
from lib.exceptions import ChildrenExist
from lib.getuuid import get_uuid
from lib.jobs import execute_job, get_job
from lib.fabric import create_fabric, delete_fabric, get_fabric
from lib.fabricnamespace import create_fabric_namespace, delete_fabric_namespace, get_fabric_namespace

from netmiko import ConnectHandler
import napalm

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler


def main():

    jobs = {}

    for t in JOB_TEMPLATE_NAMES:
        jobs[t] = get_uuid(t, "job_template")

    discover_uuid = get_uuid("discover_device_template", "job_template")

    mgmt_tag = get_mgmt_tag()

    fabric = get_fabric("foobar_fabric")
    if fabric:
        print("Deleting fabric %s" % fabric['uuid'])
        try:
            delete_fabric(fabric['uuid'])
        except ChildrenExist as ce:
            for fns_uuid in ce.child_uuids:
                print("Error - children exist. Need to delete them.")
                print("Deleting child fabric namespace %s" % fns_uuid)
                delete_fabric_namespace(fns_uuid)

            print("Finally deleting fabric %s" % fabric['uuid'])
            delete_fabric(fabric['uuid'])

    foobar_fabric = create_fabric("foobar_fabric")
    print("Created fabric %s" % foobar_fabric['uuid'])

    fns = create_fabric_namespace("foobar_fns", foobar_fabric['fq_name'], "%s/32" % ARISTA_DEVICE, mgmt_tag)
    print("Created fabric namespace %s" % fns['uuid'])

    device_list = [ARISTA_DEVICE]
    job_uuid = execute_job(discover_uuid, foobar_fabric['uuid'], device_list)
    print("Executed job %s" % job_uuid)

    fabric = get_fabric("foobar_fabric")
    print(fabric)

    # Wait for ansible playbook to finish since we don't know how to poll the jobs API yet
    import pdb; pdb.set_trace()

    fabric = get_fabric("foobar_fabric")
    prouters = fabric['physical_router_refs']
    print(prouters)

if __name__ == "__main__":
    main()
