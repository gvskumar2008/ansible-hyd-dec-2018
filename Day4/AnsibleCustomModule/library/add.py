#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(val1,val2):
    return float(val1) + float(val2)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            firstNumber=dict(type='float', required='True' ),
            secondNumber=dict(type='float', required='True' )
        )
    )

    value1 = module.params['firstNumber']
    value2 = module.params['secondNumber']
    response = add( value1, value2 )
   
    module.exit_json ( meta=response, changed=False)

main()
