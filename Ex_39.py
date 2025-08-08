from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self, msg):
        print(f'{msg} Email Notification')

class SMSNotification(Notification):
    def send(self, msg):
        print(f'{msg} SMS Notification')

class PushNotification(Notification):
    def send(self, msg):
        print(f'{msg} Push Notification')

class NotificationFactory:
    @staticmethod
    def create_notification(method: str):
        if method.lower() == 'email':
            return EmailNotification()
        elif method.lower() == 'sms':
            return SMSNotification()
        elif method.lower() == 'push':
            return PushNotification()
        else:
            raise ValueError('Unsupported payment method')


l = ['email', 'SMS', 'Push']

for i in l:
    notification = NotificationFactory.create_notification(i)
    notification.send('Hello from the system!')
