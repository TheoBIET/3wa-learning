import re
phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."

def clean_phr_to_list(phr):
    return re.sub(r"[^\w\s]", "", phr).split()

def letter_avg(phr):
    words = clean_phr_to_list(phr)
    return round(sum(len(word) for word in words) / len(words), 2)

def most_user_word(phr): 
    words = clean_phr_to_list(phr)
    return max(words, key=words.count)

res = letter_avg(phrase)
res2 = most_user_word(phrase)

print('Average word size :', res)
print('Most used word :', res2)