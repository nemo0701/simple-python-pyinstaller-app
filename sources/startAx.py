import requests

#All job could use this function
def getTetstBed(tag):
    print "Get testbed from CACTUS or from local"

#eache job has it's own unique testset xml files,as parameter passed to it
def genTestSetXML(testset):
    print "Generate a testset xml file for this test"
    
#each job need a UTMS ID
def genExcutionXML(testset,testbed,user,utms):
    print "Generate excution xml file"

def startAXjob(excution_xml):
    print "Post excution to ax"

def queryAXjob(excution_id):
    print "Check if AX job finished, passed, failed"
    rest_path='execution/'+excution_id
    excution_json=sendRequest(rest_path,'get').json()
    print 'Excution Status: '+ excution_json['execution']['execution_status']
    print 'Passed tests: ' + excution_json['execution']['passed']
    print 'Total tests: '+ excution_json['execution']['total']
    print 'Log URL: '+ excution_json['execution']['results_url']


def sendRequest(path,method,payload=None):
    AUTOMATOS_URL='http://automatosx.usd.lab.emc.com/am/'
    url=AUTOMATOS_URL+path
    if method=='post':
        headers = {'Content-Type': 'text/xml','Accept': 'application/json'}
        result=requests.post(url,data=payload,headers=headers)
    if method=='get':
        headers = {'Accept': 'application/json'}
        result=requests.get(url,headers=headers)
    return result

queryAXjob("execution_1539167653_873956_16312_0")
