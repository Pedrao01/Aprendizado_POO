class GameSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.volume = kwargs.get('volume', 50)
            cls._instance.difficulty = kwargs.get('difficulty', 'Normal')
            cls._instance.full_screen = kwargs.get('full_screen', False)
        return cls._instance


# --- TESTE ---
# Modifique e acesse as configurações
config1 = GameSettings(volume=80)
config2 = GameSettings(volume=10)

print(config1 is config2)  # Deve imprimir True (mesma instância)

# Verifique se config2 reflete as alterações
print(config1.volume)  # Deve imprimir 80
print(config2.volume)  # Deve imprimir 80, também
