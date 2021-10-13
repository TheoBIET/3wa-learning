populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

# 0 - Ajoute une clé "relations" à chaque élément de populations qui est une liste vide
for user in populations:
    user["relationships"] = [oid for (uid, oid) in relationships if uid == user["id"]]
    user["relationships"] = [uid for (uid, oid) in relationships if oid == user["id"]]

# 1 - Calculer la moyenne des relations
total_relations = round(len(relationships) * 2 / len(populations), 2)
print("La moyenne des relations est de:", total_relations)

# 2 - Liste des utilisateurs avec leurs id et leur nombre de relations
user_rel_list = [(user["id"], len(user["relationships"])) for user in populations]
print("Liste des utilisateurs avec leurs id et leur nombre de relations:", user_rel_list)

# 3 - Le premier utilisateur qui correspond au max
# user_with_most_relations = max(user_rel_list, key=lambda x: x[1])
# La liste de tous les utilisateurs correpondant au max
users_with_most_relations = [(user["id"], len(user["relationships"])) for user in populations if len(user["relationships"]) == max(user_rel_list, key=lambda x: x[1])[1]]

print("L'utilisateur avec le plus de relations est:", users_with_most_relations)

# 4 - Amis des amis
def get_friends_of_friends(user):
    return [friend for other_user in populations for friend in other_user["relationships"] if other_user["id"] in user["relationships"]]

get_friends_of_friends(populations[0])