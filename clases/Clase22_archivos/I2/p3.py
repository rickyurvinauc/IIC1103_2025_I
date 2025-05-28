def mismo_circuito(cir1, cir2):
    cir2.extend(cir2)
    cir1_s = ''.join(cir1)
    cir2_s = ''.join(cir2)
    if cir1_s in cir2_s:
        return True
    return False