# 01 QCM Python

## Question 1

Quels sont les objets fondamentaux de la librairie Numpy ?

Répondez en choisissant une seule et bonne réponse ci-dessous.

_Réponses_ :

- [ ] Ndarray.
- [x] Ndarray, indexation avancée, vectorisation et le broadcasting.
- [ ] indexation avancée, vectorisation et le broadcasting.
- [ ] Ndarray et le broadcasting

## Question 2

Est-ce le script suivant est valide ? 

```python
import numpy as np

a = np.empty(10, dtype=np.dtype('f8'))
a[10] = 1.
```

Répondez en choisissant une seule et bonne réponse ci-dessous.

_Réponses_ :

- [ ] Oui l'assignation de la valeur 1. se fait à l'indice 10.
- [ ] Non l'assignation ne se fait pas à l'indice 10, car 1. n'a pas le bon type.
- [x] Non l'assignation ne se fait pas à l'indice 10, car le tableau n'a pas d'indice 10.
- [ ] Non l'assignation ne se fait pas à l'indice 10, car les valeurs d'empty sont des valeurs constantes.

## Question 3

Combien de dimension à le tableau m suivant.

Répondez en choisissant une seule et bonne réponse ci-dessous.

```python
import numpy as np

m = np.array( [ [[1,2,3]], [[4,5,6]] , [[7,8,9]]])
```

_Réponses_ :

- [ ] (1, 1, 3)
- [ ] (3, 3, 3)
- [x] (3, 1, 3)
- [ ] (3, 1, 1)

## Question 4

Comment faire la somme des multiples de 11 de la matrice m ?

Répondez en choisissant une seule et bonne réponse ci-dessous.

```python
import numpy as np

m = np.array([
       [[10, 11, 12], [13, 14, 15], [16, 17, 18]], # matrix 0
       [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
       [[30, 31, 32], [33, 34, 35], [36, 37, 38]]
])
```

_Réponses_ :

- [ ] . (a % 11 ).sum()
- [ ] . (a % 11 == 0).sum()
- [x] . a[(a % 11 == 0)].sum()
- [ ] . (a  // 11 == 0 ).sum()

## Question 5

Comment compter le nombre de valeur(s) paire(s) par colonne de la matrice m suivante ?

Répondez en choisissant une seule et bonne réponse ci-dessous.

```python
import numpy as np

m = np.random.randint(1, 20, (10,10))
```

_Réponses_ :

- [ ] (m % 2 == 1).sum(0)
- [ ] (m.T % 2 == 1).sum(0)
- [x] (m % 2 == 0).sum(0)
- [ ] (m % 2 == 1).T.sum(0)

## Question 6

On aimerait maintenant faire la somme des valeurs paires de chacune des colonnes de la matrice m suivante.

Répondez en choisissant une seule et bonne réponse ci-dessous.

```python
import numpy as np

m = np.random.randint(1, 20, (10,10))
```

_Réponses_ :

- [ ] m[(m % 2) == 0].sum()
- [x] m.T[(m.T % 2) == 0].sum()
- [ ] np.where( m % 2 == 0, m , 0 ).sum(0)

## Question 7

On aimerait calculer la distance des points de la matrice A par rapport aux points X.

Répondez en choisissant une seule et bonne réponse ci-dessous.

```python
A = np.array([[1,2,8], [7,4,2], [9,1,7], [0,1,5], [6,4,3]])
X = np.array([1,2,3])
```

_Réponses_ :

- [x] d = np.sqrt( ((a - x)**2).sum(1) )
- [ ] d = np.sqrt( ((a - x)**2).sum(0) )
- [ ] d = np.sqrt( ((a - x)**2).sum() )

## Question 8

Quel est à votre avis la méthode la plus rapide, si elle existe, pour calculer le polynôme X**2 + 2X + 1 ?

```python
import numpy as np

a = np.arange(100)

# Methode 1
[x**2 + 2*x + 1 for x in a ]

# Méthode 2
a**2 + 2*a + 1
```

Répondez en choisissant une seule et bonne réponse ci-dessous.

_Réponses_ :

- [ ] La méthode 1, car les compréhensions de liste sont trés optimisées en Python.
- [x] La méthode 2, car la vectorisation en Numpy est plus rapide.
- [ ] Il n'y a aucune différence entre ces deux approches, en terme de rapidité d'exécution.

## Question 9

Comment définissez-vous une variable qualitative ? 

Répondez en choisissant une seule et bonne réponse ci-dessous.

_Réponses_ :

- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des quantités discrètes. 
- [x] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des noms. 
- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des valeurs 0 ou 1. 
- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des quantités continues. 

## Question 10

Comment définissez-vous une variable quantitative ? 

Répondez en choisissant une seule et bonne réponse ci-dessous.

_Réponses_ :

- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des quantités discrètes. 
- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des noms. 
- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des valeurs 0 ou 1. 
- [ ] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des quantités continues.
- [x] Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des nombres, discrète si elle ne peut être que 0,1,2,3,4,5..., continue s'il elle peut prendre tous les nombres dans un intervalle. (Je l'ai rajouté, car je ne trouvais pas les propositions du dessus assez précises quant à la question).
