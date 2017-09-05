# -*- coding: utf-8 -*-
import requests
from meya import Component

def getPolicy(number, auth_key):
    url = "https://smartvision.cybernaptics.mu/api/insurancepolicy/custom-search/"
    key = auth_key
    auth = 'Token {}'.format(key)
    querystring = {"insuredMobileNumber": number}
    headers = {
        'authorization': auth,
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    policyNumber = ''
    if response.status_code == 200:
        policies = response.json()
        policyNumber = 'Found following policies: '
        if policies:
            if len(policies) > 1:
                for policy in policies:
                    policyNumber += policy['number'] + ';'
            else:
                policyNumber += policies[0]['number']
        else:
            policyNumber = 'No Policy found'
    else:
        policyNumber = 'Network Issue, try again later'
    return (policyNumber)


class FindPolicy(Component):

    def start(self):
        API_KEY = 'ce2a5af503091c63028a329fd7a2b8f1a5c8d632'
        number = self.db.user.get('mobile_number')
        text = getPolicy(number,API_KEY)
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")