from fechas import diferencia

def fecha_promedio(fecha_1, fecha_2):
    fecha_1_str = str(fecha_1)
    fecha_2_str = str(fecha_2)

    d1 = int(fecha_1_str[:-6])
    m1 = int(fecha_1_str[-6:-4])
    a1 = int(fecha_1_str[-4:])

    d2 = int(fecha_2_str[:-6])
    m2 = int(fecha_2_str[-6:-4])
    a2 = int(fecha_2_str[-4:])

    dias_1 = d1 + (m1 - 1) * 30 + a1 * 12 * 30
    dias_2 = d2 + (m2 - 1) * 30 + a2 * 12 * 30

    promedio_dias = (dias_1 + dias_2) // 2

    a = promedio_dias // (12 * 30)
    resto = promedio_dias % (12 * 30)
    m = (resto // 30) + 1
    d = resto % 30
    if d == 0:
        d = 30
        m -= 1
        if m == 0:
            m = 12
            a -= 1

    if m < 10:
        mes_str = "0" + str(m)
    else:
        mes_str = str(m)

    return int(str(d) + mes_str + str(a))