from pyaspeller import YandexSpeller


spellatore = YandexSpeller()

sistemato =spellatore.spelled('Ciao sano luca e o diec ann')

print(sistemato)