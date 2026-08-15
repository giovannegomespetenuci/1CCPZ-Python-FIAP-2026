t = 'a', 'b', 'c'
print(t)

#t[0] = '1' - esse código dá erro, pois uma tupla não pode ser alterada além da sua criação

t1 = 'A',
print(t1)

t2 = t1 + t[1:] # as tuplas foram somadas para criar uma terceira tupla
print(t2)

# atribuição de tuplas
a = 5
b = 10
a, b = b, a
print(a, b)

email = "fulano@gmail.com"
username, dominio = email.split("@")
print(username)
print(dominio)