ruta_de_paises_y_capitales = "/home/luci/Documentos/python/logica/paises/paises+capitales.lst"
ruta_paises = "/home/luci/Documentos/python/logica/paises/paises.lst"
ruta_capitales = "/home/luci/Documentos/python/logica/paises/capitales.lst"
archivo_paises_y_capitales = open(ruta_de_paises_y_capitales,"r").readlines()
paises = open(ruta_paises,"w")
capitales = open(ruta_capitales,"w")
for separador in archivo_paises_y_capitales:
    prueba = separador.split(":")
    paises.write(prueba[0]+ "\n")
    capitales.write(prueba[1].strip() + "\n ")