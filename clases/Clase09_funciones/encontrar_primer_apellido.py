# Contar cuantas veces aparece el primer apellido de la lista

lista_estudiantes = [
    "ABEL BAEZ EMILIA MAGDALENA",
    "ACUÑA PIZARRO DANIEL JOSÉ ALEJANDRO",
    "ALDUNCE ARAVENA EILEEN PAZ",
    "ALLENDES ROJAS LUCAS BENJAMÍN",
    "ÁLVAREZ REYES MACARENA",
    "ANTIVIL OBERG JUAN ANDRÉS",
    "ARAYA PETIT AGUSTÍN FRANCISCO",
    "ARAYA ROJAS CARLA MARISOL",
    "AROS POLANCO KATTY AYLEEN",
    "ASCENCIO PÉREZ SEBASTIAN GABRIEL",
    "ASTUDILLO VELÁSQUEZ MAGDALENA ISABEL",
    "BARRIENTOS CRISPIERI ROCÍO DANIELA",
    "BASUALTO CARRANCA CRESCENTE ENRIQUE",
    "BENAVENTE RUIZ AGUSTINA MARÍA ISABEL",
    "BERTERO CABELLO CRISTINA GORETY",
    "BERTERO CABELLO GIULIANA ANTONIA",
    "BRAVO SILVA AGUSTÍN PATRICIO DE JESÚS",
    "BRITO MICER ROMIUSKA NICOL",
    "BUSTAMANTE ESPÍNDOLA KASSIDY ANTONIA",
    "BUZETA SOZA MATÍAS IGNACIO",
    "CAMPAÑA SILVA IGNACIO",
    "CAMPUSANO SOTO ALEJANDRO GUILLERMO",
    "CARREÑO HOFFMANN DIEGO IGNACIO",
    "CASANEGRA DE ANDRACA SOFÍA",
    "CASTRO MORENO SEBASTIAN ALEJANDRO",
    "CEPEDA LINZMAYER JOAQUIN",
    "CHAPARRO DIAZ DANIELA ANGELICA MARIA",
    "CONNELLY DUPRE NICOLAS",
    "CRUZ BEZANILLA JUAN JOSÉ",
    "CRUZAT RAMÍREZ MARTÍN ANDRÉS",
    "DE GIORGIS SANGUINETI CARLOS FEDERICO",
    "DELPIANO DEL CAMPO EMA",
    "DÍAZ DEL RÍO SANTIAGO",
    "DROGUETT GONZÁLEZ LUIS IGNACIO",
    "DUCCI ALDUNATE MARTÍN",
    "DURÁN VALDEBENITO CAROLINA ANTONIA",
    "EDWARDS CONSIGLIERE DIEGO JOSÉ",
    "ERRÁZURIZ MORENO MARÍA",
    "FELLAY MARÍN MARIA CAROLINA",
    "FLORES EDWARDS JULIETA ANTONIA",
    "FURNIEL CONTARDO FRANCO BORIS",
    "GALDAMES ORTIZ FRANCISCO IGNACIO",
    "GARCÍA-HUIDOBRO MONTERO PEDRO ENRIQUE",
    "GIL URIARTE JUAN CARLOS",
    "GOEHLER PEÑALOZA MATÍAS ANDRÉS",
    "GOLDENBERG CELUME JOSÉ TOMÁS",
    "GÓMEZ ALVEAL ANTONIA VALENTINA",
    "GOMILA PAULSEN MARIANA BELÉN",
    "GONZÁLEZ ATABALES ISIDORA PAZ",
    "GONZÁLEZ SOBARZO YANNAINA ESPERANZA",
    "GRASS BRIONES MATEO",
    "GRAZIOLI HARTWIG PEDRO MASSIMO",
    "GREZ RUIZ-TAGLE JUAN DIEGO",
    "HERNÁNDEZ SEGURA BENJAMÍN IGNACIO",
    "HERRERA TORO LUCAS",
    "HONORATO ROJAS LEÓN JOSÉ",
    "HURTADO EYZAGUIRRE JORGE",
    "JEREZ GARCÍA CATALINA ELENA",
    "KAMKE MARDONES SANTIAGO ROBERTO",
    "KEVRIC LÓPEZ BRUNO MAXIMILIANO",
    "KOSTIN RADNIC MATEO DOMINGO",
    "LOARTE LARA JAVIERA ARACELY",
    "LÓPEZ DÍAZ PAULO TOMÁS",
    "LUTJENS OLIVA PEDRO",
    "MAC-KAY AGUILERA TRINIDAD FLORENCIA",
    "MAGNASCO MONTALVA LAURA",
    "MANRÍQUEZ ARAYA CATALINA MARÍA",
    "MANSILLA BECERRA MATÍAS IGNACIO",
    "MANZUR PICHARA VALENTINA NAYAT",
    "MARAMBIO MIRANDA ELIEL IGNACIO",
    "MARTÍNEZ ROJAS BENJAMÍN ANTONIO",
    "MERINO REYES FRANCO ANDRÉS",
    "MIRANDA MARTINEZ ANDREA MELANIE",
    "MIRANDA OÑATE LUIS MIGUEL",
    "MONTTI ALVEAR CONSTANZA CAMILLA",
    "MOYANO VALAREZO ANDREA GIANELLA",
    "NÚÑEZ MUÑOZ ANGEL JESÚS",
    "ORTIZ BERRÍOS MARTÍN ALEJANDRO",
    "ORTIZ ROJAS IGNACIO ALBERTO",
    "OSSES MENDOZA VICTORIA ALEJANDRA",
    "PEREIRA URREA ANAIS ANTONIA",
    "POUR KHATIBI TORRES KEYVAN DANIEL",
    "PROPHETE SARA ISABELLE",
    "REYES BAEZA MIGUEL IGNACIO",
    "RIFFO SILVA DIEGO IGNACIO",
    "RODRÍGUEZ ECHEVERRÍA RICARDO ANDRÉS",
    "RODRÍGUEZ HARASIC DIEGO EMILIO",
    "RODRÍGUEZ RAMÍREZ DIEGO ANDRE",
    "ROJAS ALBORNOZ MIGUEL ANTONIO",
    "ROJAS DOMÍNGUEZ ALONSO TOMÁS",
    "ROJAS PRADO VICENTE ALBERTO",
    "SAAVEDRA CANALES JOSUÉ ZACARIAS",
    "SABUGAL BRESCIANI SOFÍA MARÍA",
    "SAGREDO ORTIZ MATEO ALFREDO",
    "SALINAS HERNÁNDEZ CATALINA VANESSA",
    "SHEA MONGE NICOLÁS JOSÉ",
    "SILVA PASTOR JOSÉ MANUEL",
    "SOFFIA CANALES BERNARDITA",
    "SOLER HARDY PEDRO",
    "SOMAVIA ESTEVEZ AMELIA LUNA",
    "SOTO LEAL JOSEFINA ISIDORA",
    "SOTO SAFFIE CRISTOBAL IGNACIO",
    "SOTO VENT AMALIA JAVIERA",
    "STUVEN OROZCO LAURA HELENA",
    "SUTIL SILVA LAURA",
    "TORREBLANCA JARA ALEX",
    "UBEDA ESPARZA ALTUÉ",
    "VALDÉS LARRAÍN PEDRO",
    "VEGA YUNES JORGE ALBERTO",
    "VENEGAS MERINO AYLIN CATALINA",
    "VERGARA MESA EMILIANO",
    "VON TEUBER LIRA AUGUSTO MAURICIO",
    "ZENG ZIHUI",
    "ZHANG LI KEVIN CAAPOU JACK",
    "ZÚÑIGA GALLARDO SEBASTIÁN ANDRÉS"
]

# Separo el problema en tareas pequeñas.
# Primera tarea que identifico es obtener el primer apellido de la lista

# accedo al primer elemento de la lista
primer_nombre = lista_estudiantes[0]  # accedo al primero item de la lista

primer_apellido = ""  # variable en donde voy a formar el apellido
contador_apellidos = 0  # contador de cuantas veces se repite el apellido
for caracter in primer_nombre:  # recorrdo caracter por caracter del primer nombre
    if caracter == " ":
        break  # si encuentro el primer espacio significo que se termino el primer apellido
    primer_apellido += caracter  # formo el apellido, es decir voy sumando los caracteres al primer apellido

print("primer apellido formado a partir del nombre:", primer_apellido)

# Ahora que forme el primer apellido, necesito saber cuantas veces se repite en la lista, para eso necesito recorrer la lista
for nombre in lista_estudiantes:  # aqui estoy recorriendo los nombres
    # por cada nombre necesito recorrer los caracteres del nombre
    apellido_nombre = ""  # cada vez que estoy recorriendo cada nombre, reinicio la variable apellido nombre para que sea un string vacio
    for caracter in nombre:
        if caracter == " ":  # una vez que encuentro el espacio en blanco se que he recorrido el primer apellido
            if apellido_nombre == primer_apellido:  # comparo el apellido formado con el primer apellido de la lista
                contador_apellidos += 1
            break
        apellido_nombre += caracter  # voy formando los apellidos de los nombres

print("El apellido:", primer_apellido, "se repite:", contador_apellidos, "veces")


