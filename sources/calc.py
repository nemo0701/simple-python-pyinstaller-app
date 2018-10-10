import requests
'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

# If 'value' is not an integer, convert it to a float and failing that, a string.
def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

# The 'add2' function itself
def add2(arg1, arg2):
    # Convert 'arg1' and 'arg2' to their appropriate types
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)
    # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
        arg1conv = str(arg1conv)
        arg2conv = str(arg2conv)
    return arg1conv + arg2conv


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
