def artista_favorito(lista):
    artistas = []
    for item in lista:
        artistas.append(item[1])
    cant_max = 0
    artistita_max = ""
    for artista in artistas:
        cant = artistas.count(artista)
        if cant > cant_max:
            cant_max = cant
            artistita_max = artista
    return artistita_max