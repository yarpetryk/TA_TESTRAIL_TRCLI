from faker import Faker


class GenerateUserData:
    """ Fake providers are here: https://faker.readthedocs.io/en/master/providers.html
    """
    fake = Faker()

    def first_name(self):
        first_name = self.fake.first_name()
        return first_name

    def last_name(self):
        last_name = self.fake.last_name()
        return last_name

    def password(self):
        password = self.fake.password()
        return password

    def address(self):
        address = self.fake.address()
        return address

    def email(self):
        email = self.fake.free_email()
        return email

    def mobile_phone_number(self):
        mobile_phone_number = self.fake.random_int(min=100000000, max=999999999)
        return '+380' + str(mobile_phone_number)

    def company(self):
        company = self.fake.company()
        return company

    def notification_message(self):
        text = self.fake.text().split('.')[0]
        return text
