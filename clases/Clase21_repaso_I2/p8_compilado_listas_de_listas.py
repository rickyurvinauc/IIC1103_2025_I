def faltas_eticas(t):
    faltas = []
    for est in t:
        if 1.1 in est[1] or 1.1 in est[2] or 1.1 == est[3]:
            faltas.append(est[0])
    return faltas