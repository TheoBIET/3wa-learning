import re

phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."

class HasCap:
    def __init__(self, t):
        self._t = self.santize(t)

    def santize(self, t):
        return re.sub(r"[^\w\s]", "", t)

    def parse(self):
        return { word: self._t.count(word) for word in self._t.split() if word[0].isupper() }


phr = HasCap(phrase)
print(phr.parse())