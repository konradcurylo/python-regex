import re
def wyszukiwacz_emaili(tekst):
    lista_emaili = re.findall('\S+@\S+\\.\S+', tekst)
    print(lista_emaili)
