def loto():
    import random
    lista_brojeva = []

    for x in range(6):
        slucajni_broj = random.randint(1, 46)
    
        while slucajni_broj in lista_brojeva:
            random.randint(1, 46)
        else: 
            lista_brojeva.append(slucajni_broj)

    return lista_brojeva.sort()
