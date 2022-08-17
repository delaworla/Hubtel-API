from typing import Dict
from black import cancel
import requests, base64
from django.conf import settings

import pprint

class Hubtel:
    def __init__(
        self,
    ):
        self.base_url = settings.HUBTEL_LIVE_URL #"https://devp-reqsendmoney-230622-api.hubtel.com/"
        self.username = settings.HUBTEL_CLIENT_ID
        self.password = settings.HUBTEL_CLIENT_SECRET
        self.merchant_id = settings.HUBTEL_CLIENT_ID
        usernamePass = f"{self.username}:{self.password}"
        auth_byte = usernamePass.encode("utf-8")
        self.basic = base64.b64encode(auth_byte).decode('utf-8')
        self.headers = {
            "Authorization": f"Basic {self.basic}",
            "Content-Type": "application/json",
        }
        self.items = []

    def receive(self, mobileNumber):
        """This enables you to send money to a mobile money wallet. You need to have money in your Hubtel Prepaid Balance
        to be able to use this functionality. You can fund your Prepaid Balance by transfering money from your Available
        Balance to your Prepaid Balance or you can fund your Prepaid Balance at any of Hubtel's partner banks"""
        base_url = self.base_url + f"request-money/{mobileNumber}"
        payload = {
        "amount": 1,
        "title": 'string',
        "description": 'string',
        "clientReference": 'string',
        "callbackUrl": 'http://example.com',
        "cancellationUrl": 'http://example.com',
        "returnUrl": 'http://example.com',
        }

        try:
            r = requests.post(base_url, headers=self.headers, json=payload)
            
            data =  r.json()
            pprint.pprint(data)
            return data
        except Exception as e:
            print(e)

    
    def send_money(self, *, mobileNumber: str, amount: int, title: str, description: str, clientReference: str, callbackUrl:str, cancellationUrl: str, returnUrl: str) -> Dict:
        base_url = self.base_url + f"send-money/{mobileNumber}"
        payload = {
            "amount": amount,
            "title": title,
            "description":description,
            "clientReference": clientReference,
            "callbackUrl": callbackUrl,
            "cancellationUrl":cancellationUrl,
            "returnUrl": returnUrl,
            }
        try: 
            r = requests.post(base_url, headers=self.headers, json=payload)
            data = r.json()
            print(data)
            return data
        except Exception as e:
            print (e)


    def verify_transaction(self, transaction_id, *args):
        base_url = f"https://hubtelappproxy.hubtel.com/api/v1/Orders/paymentStatus/{transaction_id}/BusinessSupport"
        try:
            r = requests.get(base_url,headers=self.headers )
            data = r.json()
            print(data)
            return data
        except Exception as e:
            print(e)
    

