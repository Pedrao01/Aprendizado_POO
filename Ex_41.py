from abc import ABC, abstractmethod

class TextTransformStrategy(ABC):

    @abstractmethod
    def transform(self, text: str):
        pass

class UpperCaseTransform(TextTransformStrategy):
    def transform(self, text: str):
        return text.upper()

class LowerCaseTransform(TextTransformStrategy):
    def transform(self, text: str):
        return text.lower()

class TitleCaseTransform(TextTransformStrategy):
    def transform(self, text: str):
        return text.title()

class TextProcessor:
    def __init__(self, strategy: TextTransformStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TextTransformStrategy):
        self.strategy = strategy

    def process(self, text):
        return self.strategy.transform(text)


processor = TextProcessor(TitleCaseTransform())
print(processor.process('pedRO'))

processor.set_strategy(UpperCaseTransform())
print(processor.process('Hello man!'))

processor.set_strategy(LowerCaseTransform())
print(processor.process('What is happen?'))
