# ejercicio 1

# notas
datos = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0, 6.5, 4.3, 5.7, 3.2,
6.1, 4.6]

# grados celcius
grados_C = [0, 15, 25, 30, 100]

# ciudades
ciudades = [
{"ciudad": "Santiago", "temperaturas": [30.2, 28.5, 25.1, 18.3, 12.7, 9.5, 8.8, 10.1, 14.6, 19.3, 24.8, 28.9]},
{"ciudad": "Valparaíso", "temperaturas": [22.1, 21.8, 20.5, 17.2, 14.3, 12.1, 11.5, 12.0, 13.8, 16.5, 19.2, 21.0]},
{"ciudad": "Concepción", "temperaturas": [20.5, 19.8, 17.2, 13.5, 10.8, 8.5, 7.9, 9.2, 11.5, 14.8, 17.5, 19.8]},
{"ciudad": "Temuco", "temperaturas": [22.3, 21.5, 18.0, 13.2, 9.5, 7.0, 6.5, 8.0, 10.5, 14.0, 17.8, 20.5]},
{"ciudad": "Punta Arenas", "temperaturas": [14.2, 13.5, 11.0, 7.5, 4.2, 2.0, 1.5, 3.0, 6.5, 9.8, 12.0, 13.8]},
]


def calcular_suma(datos):
    total = 0
    for numeros in datos:
        total += numeros
    return total

def calcular_larg(datos):
    return len(datos)

def calcular_prom(datos):
    largo = calcular_larg(datos)
    if largo == 0:
        return 0
    return calcular_suma(datos) / largo

def calcular_min(datos):
    if not datos:
        return None
    minimo = datos[0]
    for numeros in datos:
        if numeros < minimo:
            minimo = numeros
    return minimo

def calcular_max(datos):
    if not datos:
        return None
    maximo = datos[0]
    for numeros in datos:
        if numeros > maximo:
            maximo = numeros
    return maximo

def dubble_sort(datos, descendentes=False):
    arr = list(datos)
    n = calcular_larg(arr)
    for i in range(n):
        for j in range(0, n - i- 1):
            if descendentes:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def calcular_mediana(datos):
    arr = dubble_sort(datos)
    n = calcular_larg(arr)
    if n == 0:
        return 0
    mitad = n // 2
    if n % 2 == 0:
        return (arr[mitad -1] + arr[mitad]) / 2
    else:
        return arr[mitad]
    
def calcular_desv_estandar(datos):
    n = calcular_larg(datos)
    if n == 0:
        return 0
    promedios = calcular_prom(datos)
    sum_cuadrados = 0
    for x in datos:
        sum_cuadrados += (x - promedios) ** 2
    return (sum_cuadrados / n) ** 0.5

def C_A_F(grados_C):
    return[(c * 9/5) + 32 for c in grados_C]

def reportes_de_ciudades(ciudades):
    print("Reportes de Ciudades")
    for ciudad_dict in ciudades:
        nombre = ciudad_dict["ciudad"]
        temps = ciudad_dict["temperatura"]
        prom = calcular_prom(temps)
        minimo = calcular_min(temps)
        maximo = calcular_max(temps)
        print(f"Ciudad: {nombre} | Promedio: {prom: .2f}°C | Min: {minimo}°C | Max: {maximo}°C")

