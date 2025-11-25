# Datos a tener en cuenta
temperatura_local = "ingrese la temperatura del lugar (en °C)"
humedad_del_aire = "humedad del aire"
presion_admosferica = "ingrese la presion admosferica del lugar"
velocidad_del_viento = "ingrese la velocidad del viento"
tamaño_de_nubes = "grandeingrese el tamaña de las nuves enoctas (muy pequeñas, pequeñas, medianas, grandes, muy grandes)"
tipo_de_nubes_en_la_zona = "ingrese el tipo de nuves que hay (cumulonismbus, nimbostratus, altostratus, cumulus congestus, stratus, cirrocumulus)"
lluvias_recientes = "ingrese el numero de veces que a llovido en días recientes"

#Calculo de temperatura
if  temperatura_local >= 34:
    temperatura_calor = 0.4
    temperatura_nublado = 0.45
    temperatura_lluvia = 0.7
elif temperatura_local > 30:
    temperatura_lluvia = 0.7
    temperatura_calor = 0.6
    temperatura_nublado = 0.35
elif temperatura_local >= 26:
    temperatura_calor = 0.6
    temperatura_lluvia = 0.8
    temperatura_nublado = 0.25
elif temperatura_local >= 21:
    temperatura_lluvia = 0.65
    temperatura_calor = 0.7
    temperatura_nublado = 0.25
elif temperatura_local >= 16:
    temperatura_lluvia = 0.45
    temperatura_calor = 0.55
    temperatura_nublado = 0.4
elif temperatura_local >= 11:
    temperatura_lluvia = 0.25
    temperatura_calor = 0.55
    temperatura_nublado = 0.6
elif temperatura_local >= 6:
    temperatura_lluvia = 0.1
    temperatura_calor = 0.20
    temperatura_nublado = 0.65
else: 
    Temperatura_lluvia = 0.05
    temperatura_calor = 0.2
    temperatura_nublado = 0.7

#Calcula de la humedad
if humedad_del_aire > 85:
    humedad_lluvia = 0.9
    humedad_calor = 0.1
    humedad_nublado = 0.9
elif humedad_del_aire >= 70:
    humedad_lluvia = 0.7
    humedad_calor = 0.2
    humedad_nublado = 0.75
elif humedad_del_aire >= 50:
    humedad_lluvia = 0.4
    humedad_calor = 0.4
    humedad_nublado = 0.5
elif humedad_del_aire >= 30:
    humedad_lluvia = 0.1
    humedad_calor = 0.7
    humedad_nublado = 0.25
else:
    humedad_lluvia = 0.1
    humedad_calor = 0.9
    humedad_nublado = 0.05

#Calculo de la presion
if presion_admosferica > 1025:
    presion_lluvia = 0.05
    presion_calor = 0.85
    presion_nublado = 0.1
elif presion_admosferica >= 1020:
    presion_lluvia = 0.1
    presion_calor = 0.85
    presion_nublado = 0.1
elif presion_admosferica >= 1015:
    presion_lluvia = 0.2
    presion_calor = 0.55
    presion_nublado = 0.4
elif presion_admosferica >= 1010:
    presion_lluvia = 0.4
    presion_calor = 0.55
    presion_nublado = 0.4
elif presion_admosferica >= 1005:
    presion_lluvia = 0.6
    presion_calor = 0.3
    presion_nublado = 0.6
elif presion_admosferica >= 1000:
    presion_lluvia = 0.75
    presion_calor = 0.3
    presion_nublado = 0.6
else: 
    presion_lluvia = 0.95
    presion_calor = 0.1
    presion_nublado = 0.8
#Calculo de la velocidad del tiempo
if velocidad_del_viento >= 20:
    velocidad_lluvia = 0.85
    velocidad_calor = 0.5
    velocidad_nublado = 0.5
elif velocidad_del_viento >= 12:
    velocidad_lluvia = 0.7
    velocidad_calor = 0.7
    velocidad_nublado = 0.55
elif velocidad_del_viento >= 8:
    velocidad_lluvia = 0.5
    velocidad_calor = 0.55
    velocidad_nublado = 0.55
elif velocidad_del_viento >= 4:
    velocidad_lluvia = 0.35
    velocidad_calor = 0.55
    velocidad_nublado = 0.55
elif velocidad_del_viento >= 1:
    velocidad_lluvia = 0.2
    velocidad_calor = 0.3
    velocidad_nublado = 0.7
else:
    velocidad_lluvia = 0.12
    velocidad_calor = 0.3
    velocidad_nublado = 0.7

#Calculo del tamaño de la nuve
if tamaño_de_nubes == "muy pequeño":
    tamaño_lluvia = 0.05
    tamaño_calor = 0.95
    tamaño_nublado = 0.05
elif tamaño_de_nubes == "pequeño":
    tamaño_lluvia = 0.15
    tamaño_calor = 0.8
    tamaño_nublado = 0.2
elif tamaño_de_nubes == "mediano":
    tamaño_lluvia = 0.35
    tamaño_calor = 0.5
    tamaño_nublado = 0.5
elif tamaño_de_nubes == "grande":
    tamaño_lluvia = 0.65 
    tamaño_calor = 0.2
    tamaño_nublado = 0.8
elif tamaño_de_nubes == "muy grande":
    tamaño_lluvia = 0.9
    tamaño_calor = 0.05
    tamaño_nublado = 0.95
else:  
    tamaño_lluvia = 0.3
    tamaño_calor = 0.3
    tamaño_nublado = 0.3

#Calculo del tipo de nube
if tipo_de_nubes_en_la_zona == "cumulonimbus":
    tipo_lluvia = 0.95
    tipo_calor = 0
    tipo_nublado = 0.7
elif tipo_de_nubes_en_la_zona == "nimbostratus":
    tipo_lluvia = 0.85
    tipo_calor = 0.05
    tipo_nublado = 0.9
elif tipo_de_nubes_en_la_zona == "altostratus":
    tipo_lluvia = 0.4
    tipo_calor = 0.25
    tipo_nublado = 0.8
elif tipo_de_nubes_en_la_zona == "cumulus congestus":
    tipo_lluvia = 0.6
    tipo_calor = 0.2
    tipo_nublado = 0.65
elif tipo_de_nubes_en_la_zona == "stratus":
    tipo_lluvia = 0.2
    tipo_calor = 0.1
    tipo_nublado = 0.95
elif tipo_de_nubes_en_la_zona == "cirrocumulus":
    tipo_lluvia = 0
    tipo_calor = 0.9
    tipo_nublado = 0.2

#Calculo de la cantidad de nubes
if lluvias_recientes >= 8:
    cantidad_lluvia = 0.85
    cantidad_calor = 0.05
    cantidad_nublado = 0.95
elif lluvias_recientes >= 6:
    cantidad_lluvia = 0.4
    cantidad_calor = 0.15
    cantidad_nublado = 0.8
elif lluvias_recientes >= 4:
    cantidad_lluvia = 0.2
    cantidad_calor = 0.4
    cantidad_nublado = 0.5
elif lluvias_recientes >= 2:
    cantidad_lluvia = 0.05
    cantidad_calor = 0.7
    cantidad_nublado = 0.15
else: 
    cantidad_lluvia = 0
    cantidad_calor = 0.95
    cantidad_nublado = 0.05

#probabilidades del clima
lluvia = (temperatura_lluvia+humedad_lluvia+presion_lluvia+velocidad_lluvia+tamaño_lluvia+tipo_lluvia+cantidad_lluvia)*100/7
sol = (temperatura_calor+humedad_calor+presion_calor+velocidad_calor+tamaño_calor+tipo_calor+cantidad_calor)*100/7
nublisca =(temperatura_nublado+humedad_nublado+presion_nublado+velocidad_nublado+tamaño_nublado+tipo_nublado+cantidad_nublado)*100/7

print("la probabilidad de que llueva es de", round(lluvia),"%")
print("La probabilidad de que haga un sol es de", round(sol),"%")
print("La probabilidad de que este nublado es de", round(nublisca),"%")

if lluvia > sol and lluvia > nublisca:
    clima = "Lluvioso"
elif sol > lluvia and sol > nublisca:
    clima = "Soleado"
else:
    clima = "Nublado"
    
print("Lo mas probable es que hoy sea un dia", clima)