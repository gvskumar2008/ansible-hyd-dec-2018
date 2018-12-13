#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def createNginxConfFile( serverCount, startingIPAddress ):
    file = open ( "nginx.conf", "w" )

    ipTokens = startingIPAddress.split(".") 	

    firstOctet  = ipTokens[0]
    secondOctet = ipTokens[1]
    thirdOctet  = ipTokens[2]
    fourthOctet = ipTokens[3] 		

    file.write ( "events {\n\tworker_connections 1024;\n}\n" )

    file.write ( "http {\n" )

    file.write ( "\tupstream servers {\n" )
    
    for count in range(int(fourthOctet), int(fourthOctet)+serverCount ):
	server = "\t\t" + "server " + firstOctet + "." + secondOctet + "." +  thirdOctet + "." + str( count ) + ";\n"
	file.write ( server )

    file.write ( "\t}\n" )

    file.write ( "\tserver {\n" )
    file.write ( "\t\tlisten 80;" )
    file.write ( "\n" )
    file.write ( "\t\tlocation / {\n" )
    file.write ( "\t\t\tproxy_pass  http://servers;\n" )
    file.write ( "\t\t}\n")
    file.write ( "\t}\n}" )

    file.close()

def main():
    module = AnsibleModule(
	argument_spec=dict(
		serverCount=dict(type='int', required='yes'),
		startingIPAddress=dict(type='str', required='yes')
	)
    )	

    totalServers = module.params['serverCount']
    ipAddress    = module.params['startingIPAddress']

    createNginxConfFile ( totalServers, ipAddress ) 

    module.exit_json ( msg="Nginx Loadbalancing configured!", changed='True' )

main()

