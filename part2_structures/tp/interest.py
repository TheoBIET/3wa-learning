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
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]

centers = [
    (0, 'PHP'), (0, 'MySQL'), (0, 'Angular'), (1, 'MySQL'), (2, 'Python'), (3, 'PHP'), (4, 'PHP'), 
    (5, 'Angular'), (6, 'Vuejs'), (7, 'Angular'), (8, 'Big data'), (9, 'PHP'), 
    (10, 'Angular'), (10, 'NoSQL'), (11, 'NoSQL'), (12, 'Angular'), (13, 'Angular'), (14, 'Angular'), 
    (15, 'Angular'), (16, 'Angular'), (17, 'PHP'), (18, 'PHP'), (19, 'PHP'), (19,'Angular'), (19, 'Python'),
    (20, 'Python'), (21, 'Python'), (22, 'Python'), (23, 'Python'), (24, 'PHP'), 
    (25, 'NoSQL'), (26, 'NoSQL'), (27, 'Big data'), (28, 'NoSQL'), (29, 'Angular'), (29, 'PHP'), (29,'Big data')
]

for user in populations:
    user['interests'] = [lang for (id, lang) in centers if id == user['id']]

lang_interests = [{
    'lang': lang,
    'users': [user["id"] for user in populations if lang in user['interests']]
} for lang in list(set([lang for (id, lang) in centers]))]