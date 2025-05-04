
def dcc_banco(saldo, transacciones):

    lista_transacciones_fallidas = []
    print("Saldo inicial", saldo)

    while True:
        for transaccion in transacciones:
            if transaccion < 0:
                if saldo+transaccion < 0:
                    print(f"Retiro fallido {transaccion*-1} - Saldo {saldo}")
                    lista_transacciones_fallidas.append(transaccion)
                else:
                    saldo += transaccion
                    print(f"Retiro {transaccion*-1} - Saldo {saldo}")
            else:
                saldo += transaccion
                print(f"Deposito {transaccion} - Saldo {saldo}")
        
        if len(lista_transacciones_fallidas) == 0:
            break
        
        transacciones = lista_transacciones_fallidas
        lista_transacciones_fallidas = []