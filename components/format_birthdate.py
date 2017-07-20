from meya import Component
import arrow

class FormatBirthDate(Component):
    """format datetime"""
    
    def start(self):
        birthdate= arrow.get(self.db.user.get("birth_date"))
        text = "Saving birth date as {}".format(birthdate.format('DD-MMM-YYYY'))
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")