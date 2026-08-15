eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)
print(eng2sp['two'])

print('two' in eng2sp) # checa se 'two' é uma CHAVE em eng2sp, retorna True se for e False se não for
print('dos' in eng2sp) # nesse caso não é chave, então retorna False

def conta_letras(s):
    d = dict()
    for letra in s:
        if letra not in d:
            d[letra] = 1
        else:
            d[letra] += 1
    return d

print(conta_letras("giovanne"))