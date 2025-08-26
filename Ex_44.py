from abc import ABC, abstractmethod
from dataclasses import dataclass

class Observer(ABC):
    @abstractmethod
    def update(self, news: str):
        pass

class NoticiaPublisher:
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
        print(f'New posted: {news}')
        self.news = news
        self.notify()


class SportSubscriber(Observer):
    def update(self, news: str):
        if 'esporte' in news.lower():
            print(f'Sport News: {news}')

class PoliticalSubscriber(Observer):
    def update(self, news: str):
        if 'politica' in news.lower():
            print(f'Political News: {news}')

class GeralSubscriber(Observer):
    def update(self, news: str):
        print(f'Geral News: {news}')


news_agenci = NoticiaPublisher()

sport = SportSubscriber()
polical = PoliticalSubscriber()
geral = GeralSubscriber()

news_agenci.attach(sport)
news_agenci.attach(polical)
news_agenci.attach(geral)

news_agenci.set_news('Noticias de esporte! Novo jogador do vasco anunciado!')
news_agenci.set_news('Noticia de politica! Governo Lula tem uma alta reprovação no governo.')
news_agenci.set_news('Noticia de tecnologia! Anunciação das maravilhas de um computador quantico.')
