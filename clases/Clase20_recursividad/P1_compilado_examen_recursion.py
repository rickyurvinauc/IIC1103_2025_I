# letras = ['r', 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's']
# instrucciones = ['ignorar', 1, 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2]

def descifrar_rec(letras, instrucciones):
    if len(instrucciones) == 2:
        accion = instrucciones[0]
        cantidad = instrucciones[1]
        if accion == "agregar":
            return letras[:cantidad]
        else:
            return []
    accion = instrucciones[0]
    cantidad = instrucciones[1]
    if accion == "agregar":
        return letras[:cantidad] + descifrar_rec(letras[cantidad:], instrucciones[2:])
    else:
        return descifrar_rec(letras[cantidad:], instrucciones[2:])

# 1. descifrar_rec(['r', 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], ['ignorar', 1, 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 2. descifrar_rec([ 'g', 'a', 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], [ 'agregar', 2, 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 3. [ 'g', 'a'] + descifrar_rec([ 'p', 't', 'b', 'b', 'a', 't', 'o', 's'], [ 'ignorar', 1, 'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 4.  descifrar_rec([ 't', 'b', 'b', 'a', 't', 'o', 's'], [  'agregar', 1, 'ignorar', 4, 'agregar', 2])
# 5.  [ 't'] + descifrar_rec([ 'b', 'b', 'a', 't', 'o', 's'], [ 'ignorar', 4, 'agregar', 2])
# 6.  descifrar_rec([ 'o', 's'], [ 'ignorar', 4, 'agregar', 2])
# 6.  [ 'o', 's']

# Resultado ->[ 'g', 'a']+ [ 't'] + [ 'o', 's']