def esta_patron(circuito, patron):
    circuito.extend(circuito)
    circuit_s = ''.join(circuito)
    if patron in circuit_s:
        return True
    return False