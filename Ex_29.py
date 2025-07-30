class Labell:
    class Address:
        def __init__(self, street, city, state):
            self.street = street
            self. city = city
            self.state =  state

        def display(self):
            return f'{self.street}, {self.city} - {self.state}'

    def __init__(self):
        self.recipient = None
        self.address = None

    def with_recipient(self, name):
        self.recipient = name
        return self
    def with_address(self, street, city, state):
        self.address = self.Address(street, city, state)
        return self

    def to_generate(self):
        print(f'Recipient: {self.recipient}')
        print(f'Address: {self.address.display()}')
        return self


Labell().with_recipient("Pedro Duarte").with_address("Rua Python", "Fortaleza", "CE").to_generate()
