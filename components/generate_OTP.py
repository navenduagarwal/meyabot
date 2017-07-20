import requests
from random import randint
from meya import Component

API_URL = (
    "http://api.onehop.co/v1/sms/send/?mobile_number={phone}"
    "&sms_text={message}&label={label}&sender_id=TESTIN&apiKey={api_key}&encoding=plaintext"
)
API_KEY = 'sm03205f8bbb634adba11be82f16b4ffa0'


def generate_otp(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


class SendOtp(Component):
    def start(self):
        otp_number = generate_otp(6)
        self.db.user.set('otp_number', otp_number)
        mobile_number = self.db.user.get('mobile_number')
        otp_message = 'To verify your mobile number with SBI General Chatbot you will need a One Time Password(OTP). The OTP is ' \
                      + str(otp_number)
        otp_label = 'transaction'
        url = API_URL.format(phone=mobile_number, message=otp_message, label=otp_label, api_key=API_KEY)
        data = requests.get(url)
        if data.status_code == 200:
            action = "success"
        else:
            action = "failure"
        return self.respond(message=None, action=action)
