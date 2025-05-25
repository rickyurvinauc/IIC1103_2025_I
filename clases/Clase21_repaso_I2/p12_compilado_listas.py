def dias_mas_lluvia(lluvia_mes):
    cant_mayor = 0
    dia_mayor = 0
    dias = []
    for i_lluvia in range(0,len(lluvia_mes),2):
        cant_lluvia = lluvia_mes[i_lluvia+1]
        if cant_lluvia > cant_mayor:
            cant_mayor = cant_lluvia
            dia_mayor = lluvia_mes[i_lluvia]
    for i_lluvia in range(0,len(lluvia_mes),2):
        cant_lluvia = lluvia_mes[i_lluvia+1]
        if cant_lluvia == cant_mayor:
            dia_mayor = lluvia_mes[i_lluvia]
            dias.append(dia_mayor)
    return dias
