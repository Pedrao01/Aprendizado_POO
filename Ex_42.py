from abc import ABC, abstractmethod
from dataclasses import dataclass

class Observer(ABC):
     @abstractmethod
     def update(self, news):
         pass

class NewsAgency:
    def __init__(self):
        self.observers = []
        self.news = None

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.news)

    def set_news(self, news):
        print(f'News posted: {news}')
        self.news = news
        self.notify()


@dataclass(slots=True)
class Subscriber(Observer):
    name: str

    def update(self, news):
        print(f'{self.name} received the news: {news}')


news_agency = NewsAgency()
subscriber1 = Subscriber('Pedro')
subscriber2 = Subscriber('Andrey')

news_agency.attach(subscriber1)
news_agency.attach(subscriber2)

news_agency.set_news('War against China!')
