class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f'User {self.username} logged in with email {self.email}')

    def access_dashboard(self):
        print('accessing user dashboard')

class Admin(User):
    def __init__(self, username, email, level):
        super().__init__(username, email)
        self.level = level.lower()

    def access_dashboard(self):
        if self.level  == 'super':
            print('Accessing admin control panel.')
        elif self.level == 'moderator':
            print('Access moderator tools.')
        else:
            print('invalid level.')

class Guest(User):
    def access_dashboard(self):
        print('Guest cannot access the dashboard')


admin = Admin('admin01', 'admin@example.com', 'super')
guest = Guest('visitor01', 'guest@example.com')

admin.login()
admin.access_dashboard()

guest.login()
guest.access_dashboard()