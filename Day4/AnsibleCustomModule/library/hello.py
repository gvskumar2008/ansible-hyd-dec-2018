#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return msg

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str', required='True' )
        )
    )

    msg = module.params['message']
    response = sayHello( msg )
   
    module.exit_json ( meta=response, changed=True)

main()
