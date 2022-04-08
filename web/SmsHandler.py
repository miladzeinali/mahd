import requests
import json

from .HelperDate import HelperDate
# from web.models.models import UserProfile


class SmsHandler:

    def __init__(self):
        self.secret_key = '###abbas%^987'
        self.api_key = '91ac6e7a6a16964dfe9f8cbd'
        self.line_number = '30004747472909'


    def get_token(self):
        body = {
            'SecretKey': self.secret_key,
            'UserApiKey': self.api_key,
        }
        header = {
            'Content-Type': 'application/json'
        }
        r = requests.post('https://RestfulSms.com/api/Token', data=json.dumps(body), headers=header)

        token = r.json().get('TokenKey')
        return token

    def send(self, text, mobile, token):
        body = {
            "Messages": [text],
            "MobileNumbers":[mobile],
            "LineNumber": self.line_number,
            "SendDateTime": "",
            "CanContinueInCaseOfError": "false"
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }

        r = requests.post("https://RestfulSms.com/api/MessageSend", data=json.dumps(body), headers=header).json()

        return r

    def send_register_report(self, name, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "name","ParameterValue": name + ""}],
            "Mobile":mobile,
            "TemplateId": "49448",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }

        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()

        return r