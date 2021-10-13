phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."

def phr_stats(phr):
    words = phr.replace(r'[^\w\s]i', ' ').split(' ')
    return {
        'letter_avg': round(sum(len(word) for word in words) / len(words), 2),
        'most_common_word': max(words, key=words.count)
    }

res = phr_stats(phrase)

print('Average word size :', res['letter_avg'])
print('Most used word :', res['most_common_word'])