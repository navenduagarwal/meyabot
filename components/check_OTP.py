from meya import Component


class CheckOTP(Component):

    def start(self):
        savedOTP = self.db.user.get('otp_number')
        inputOTP = self.db.flow.get('input_otp')
        # check the otp
        if savedOTP == inputOTP:
            action = "verified"
            text = "Your number has been verified"
        else:
            action = "failure"
            text = "Incorrect OTP, Please try again"
        message = self.create_message(text=text)
        return self.respond(message=message, action=action)