def soma(x,y):
    return x + y

print(soma(3,5))

print(soma(1,5))
print(soma(15,6))
print(soma(20,7))

def simples(cor):
    if cor == 'azul':
        return 'escolheu certo'
    
    def medio(cor):
        if cor =='rosa':
            return 'escolheu certo'
        else:
            return 'tente outra cor'
    
    
def completo(cor):
    if cor == 'azul':
        return 'escolheu certo'
    elif cor == 'marrom':
        return 'nao tem salvação'
    else:
        return 'tente outra cor'