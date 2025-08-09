from abc import ABC, abstractmethod

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, file_name):
        pass

class ZipCompression(CompressionStrategy):
    def compress(self, file_name):
        return f'The file {file_name} was compressed to zip.'

class TarCompress(CompressionStrategy):
    def compress(self, file_name):
        return f'The file {file_name} was compessed to tar.'

class RarCompress(CompressionStrategy):
    def compress(self, file_name):
        return f'The file {file_name}, was compress to rar'

class Compressor:
    def __init__(self, file_name, to_compress: CompressionStrategy):
        self.file_name = file_name
        self.to_compress = to_compress

    def compress(self):
        return self.to_compress.compress(self.file_name)


zip = Compressor('text.zip', ZipCompression())
tar = Compressor('text.tar', TarCompress())
rar = Compressor('text.rar', RarCompress())

print(zip.compress())
print(tar.compress())
print(rar.compress())
