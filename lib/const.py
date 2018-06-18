NAMESPACE = "default-global-system-config"

# These are built in by default - maybe find a way to list these programmatically?
# Until then, Go to  Settings >> Config DB >> FQ Name Table and click on "job_template" to get these
JOB_TEMPLATE_NAMES = [
    "device_import_template",
    "discover_device_template",
    "generate_underlay_template",
    "image_upgrade_template"
]

# Contrail-controller server IP/hostname
SERVER = "ec2-18-237-121-198.us-west-2.compute.amazonaws.com"
URL = "http://%s:8082" % SERVER
# ANALYTICS_URL = "http://<system IP>:8081/analytics/uves"
ANALYTICS_URL = "http://%s:8081" % SERVER
ARISTA_DEVICE = "10.10.10.232"