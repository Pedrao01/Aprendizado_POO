class DatabaseConnection:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'status'):
            self.status = 'Desconnected'

    def connect(self):
        if self.status == 'desconnected':
            print('Connected to database')
            self.status = 'Connected'


db1 = DatabaseConnection()
db2 = DatabaseConnection()

db1.connect()
db2.connect()

print(db1 is db2)  # True (mesma instância)
print(db1.status)  # connected
print(db2.status)  # connected
