import time
import algoritmos
import matplotlib.pyplot as plt


#Tamaños de la lista pa el examen con 10 elevado 2,3,4 y 5
tamaños = [100, 1000, 10000, 100000]

#Número de ejecuciones que usaríamos para obtener un promedio
repeticiones = 5

#Tiempo máximo que permitiríamos para una ejecución
time_out = 3

#Función que al ser llamada, ejecuta un algoritmo varias veces y calcula el tiempo promedio
#Si alguna ejecución llega a superar el limite, entonces devuelve none para evidenciar el exceso de tiempo
def medir_tiempo(funcion, A, B, repeticiones=5, limite=3):

    tiempos = []

    for _ in range(repeticiones):

        inicio = time.perf_counter()
        funcion(A, B)
        tiempo = time.perf_counter() - inicio
        if tiempo > limite:
            return None
        tiempos.append(tiempo)
    return sum(tiempos) / len(tiempos)


#Listas para almacenar los resultados
tiempos_o_n2 = []
tiempos_o_nlogn = []
tiempos_o_n = []

print(
    f"{'N':>10} | "
    f"{'O(N^2)':>13} | "
    f"{'O(N log N)':>15} | "
    f"{'O(N)':>12}")
print("-" * 60)


for N in tamaños:

    #Generación pal peor de los casos
    #Aquí a y b son completamente disjuntos
    A = list(range(N))
    B = list(range(N, 2 * N))

    #Uso de la variante A para o(n^2)

    #Nota: Genera timeout al tratar N = 100000, eso me puso el pc como turbina de avion

    tiempo_a = medir_tiempo(
        algoritmos.interseccion_anidada,
        A,
        B,
        repeticiones,
        time_out
    )

    tiempos_o_n2.append(tiempo_a)

    #Uso de la variante B para o(n log n)

    tiempo_b = medir_tiempo(
        algoritmos.interseccion_busqueda_binaria,
        A,
        B,
        repeticiones,
        time_out
    )
    tiempos_o_nlogn.append(tiempo_b)

    #Variante C para o(n)

    tiempo_c = medir_tiempo(
        algoritmos.interseccion_hash,
        A,
        B,
        repeticiones,
        time_out
    )
    tiempos_o_n.append(tiempo_c)

    #Resultados pa mostrar en el output referente a la lista de 4 elementos a evaluar según el método

    resultado_a = (
        f"{tiempo_a:13.6f}"
        if tiempo_a is not None
        else f"{'TIMEOUT':>13}")

    resultado_b = (
        f"{tiempo_b:15.6f}"
        if tiempo_b is not None
        else f"{'TIMEOUT':>15}")

    resultado_c = (
        f"{tiempo_c:12.6f}"
        if tiempo_c is not None
        else f"{'TIMEOUT':>12}")

    print(
        f"{N:10d} | "
        f"{resultado_a} | "
        f"{resultado_b} | "
        f"{resultado_c}")


#Preparación pa los datos de las gráficas
#Aquí para o(n^2) usamos solamente los tamaños que se pudieron ejecutar
datos_n2 = [
    (N, tiempo)
    for N, tiempo in zip(tamaños, tiempos_o_n2)
    if tiempo is not None]
tamaños_n2 = [dato[0] for dato in datos_n2]
tiempos_n2 = [dato[1] for dato in datos_n2]

#Graficas
fig, (g1, g2) = plt.subplots(1, 2, figsize=(14, 6))

#Graficos lineales pa mostrar por variante de tamaño para n versus tiempo
if tiempos_n2:
    g1.plot(
        tamaños_n2,
        tiempos_n2,
        "r-o",
        label="Variante A - O(N²)")

g1.plot(
    tamaños,
    tiempos_o_nlogn,
    "g-s",
    label="Variante B - O(N log N)")

g1.plot(
    tamaños,
    tiempos_o_n,
    "b-^",
    label="Variante C - O(N)")

g1.set_title("Tamaño vs Tiempo")
g1.set_xlabel("Tamaño N")
g1.set_ylabel("Tiempo (segundos)")
g1.legend()
g1.grid(True)

#Graficos logaritmicos por variante pa mostrar de tamaño pa n versus tiempo
if tiempos_n2:
    g2.loglog(
        tamaños_n2,
        tiempos_n2,
        "r-o",
        label="Variante A - O(N²)")

g2.loglog(
    tamaños,
    tiempos_o_nlogn,
    "g-s",
    label="Variante B - O(N log N)")

g2.loglog(
    tamaños,
    tiempos_o_n,
    "b-^",
    label="Variante C - O(N)")

#Titulos pa los graficos en x y, titulo principal
g2.set_title("Escala logarítmica")
g2.set_xlabel("Tamaño N")
g2.set_ylabel("Tiempo (segundos)")
g2.legend()
g2.grid(True, which="both", linestyle="--")

plt.tight_layout()
plt.show()

#Buscar N* donde se desplaza al metodo anidado con la busqueda binaria
n_estrella = None
for N, tiempo_a, tiempo_b in zip(
    tamaños,
    tiempos_o_n2,
    tiempos_o_nlogn):
    if tiempo_a is not None and tiempo_b is not None:
        if tiempo_b < tiempo_a:
            n_estrella = N
            break

if n_estrella is not None:

    print(f"N* es igual a = {n_estrella}")
    print("En este tamaño, la búsqueda binaria presento un tiempo menor que la variante anidada")
else:
    print("No se encontro un N* dentro de lo que estamos procesando")