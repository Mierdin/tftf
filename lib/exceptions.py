import re

class ChildrenExist(Exception):

    def __init__(self, resp):

        # teststr = "Delete when children still present: ['http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/fabric-namespace/582a7b68-c7aa-4000-b662-b482fffdface', 'http://ec2-54-213-221-42.us-west-2.compute.amazonaws.com:8082/fabric-namespace/582a7b68-c7aa-4000-b662-b482fffdb00c']"
        self.child_uuids = re.findall('fabric-namespace\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', resp.text)
        # import pdb; pdb.set_trace()
