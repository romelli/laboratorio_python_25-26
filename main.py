def is_pari(n):
    '''controllo se il numero è pari'''

    if n%2 == 0:
        return True
    else:
        return False

def is_pari_flex(n):

    return n%2 == 0

res = is_pari_flex(4)
print(res)
res = is_pari_flex(5)
print(res)