import random as rnd

# FUNCION DE B&B
def ByB(archivos, S):
    x = []  # Lista para guardar los detalles de cada archivo
    for archivo in archivos:
        # Crear una sublista con los detalles del archivo
        detalle_archivo = [archivo["p"], archivo["s"], archivo["p"] / archivo["s"]]
        x.append(detalle_archivo)  # Agregar la sublista a x

    # Imprimir la lista x en el orden correcto
    print("\nLista de detalles de archivos (Valor, Peso, Relación p/s):")
    for idx, sublista in enumerate(x):
        print(f"x{archivos[idx]['numero_archivo']} = {sublista}")

    # Imprimir la capacidad del sistema
    print(f"Capacidad del sistema (S): {S}")

    # Inicializar la lista X y la capacidad restante
    X = []
    capacidad_restante = S

    # Iterar sobre los archivos
    for idx, archivo in enumerate(archivos):
        peso = archivo["s"]
        
        if capacidad_restante >= peso:  # Puede incluir completamente
            X.append(1)
            capacidad_restante -= peso
        else:  # No puede incluir completamente
            if capacidad_restante > 0:
                y = capacidad_restante / peso  # Proporción que se puede incluir
                X.append(y)
                capacidad_restante = 0  # Se ha llenado el espacio
            else:
                X.append(0)  # No se puede incluir nada
        
        # Si se llega a un espacio restante de 0, agregar 0 para el resto
        if capacidad_restante == 0:
            X.extend([0] * (len(archivos) - len(X)))  # Completa el resto con 0
            break

    print("Resultado de inclusión (X):", X)

    # Ordenar X de acuerdo al orden original de los archivos
    casa = archivos
    X_ordenada = [0] * len(archivos)
    for idx, archivo in enumerate(archivos):
        numero_archivo = archivo["numero_archivo"]
        X_ordenada[numero_archivo - 1] = X[idx]  # Guardar en el índice correspondiente

    print("\nSubproblema 1: ")
    print("Resultado ordenado por x1, x2, x3,...xn (X):", X_ordenada)

    # Calcular f(X) para Subproblema 1
    Z = sum(archivo["p"] * X[idx] for idx, archivo in enumerate(archivos))
    print(f"f(X) = {Z}") 

    # Contador para los subproblemas
    contador = 3
    #lista para guardar las restricciones
    Y = X.copy()
    # Modificar Y para que todos sus valores sean 1
    Y = [1] * len(Y)
    posiciones = []
    resultados_subproblemas = []

    while True:
        #print("\n",X)
        #print(Y)

        # Verificar si hay valores fraccionarios en X
        fraccionarios = any(0 < valor < 1 for valor in X)

        if fraccionarios:
            # Encuentra el primer valor fraccionario y su índice
            for idx, valor in enumerate(X):
                if 0 < valor < 1:
                    fraccionario = valor

                    # Obtener el número de archivo correspondiente al índice original
                    numero_archivo = archivos[idx]["numero_archivo"]
                    print(f"Número fraccionario: {fraccionario} en x{numero_archivo}")

                    # Definir xn
                    xn = valor  # Este será el valor fraccionario encontrado
                    xn = 0  # Asignamos xn a 0

                    # Subproblemas 2 y 3
                    print(f"\nSubproblema {contador - 1}: x{numero_archivo} = 0")
                    
                    # Inicializar Y_ordenada
                    Y_ordenada = [0] * len(archivos)

                    # Ordenar Y de acuerdo al orden original de los archivos
                    for idx, i in enumerate(casa):
                        numero_archiv = i["numero_archivo"]
                        Y_ordenada[numero_archiv - 1] = Y[idx]  # Guardar en el índice correspondiente

                    #   Imprimir el resultado
                    #print("Resultado ordenado por x1, x2, x3,...xn (Y):", Y_ordenada)



                    # Encontrar todas las posiciones donde el valor sea 0
                    posiciones_ceros = [idx for idx, valor in enumerate(Y_ordenada) if valor == 0]
                    #print("Posiciones de ceros:", posiciones_ceros)
                    # Incrementar cada posición en 1 para la impresión
                    posiciones_ceros_incrementadas = [pos + 1 for pos in posiciones_ceros]
                    if 0 not in Y_ordenada:
                        resultado = [f"Subproblema {contador}: x{numero_archivo} = 1 "]
                        print(f"Subproblema {contador}: x{numero_archivo} = 1  EN ESPERA")
                    else:
                        resultado = [f"Subproblema {contador}: x{numero_archivo} = 1 y x{posiciones_ceros_incrementadas} = 0 "]
                        print(f"Subproblema {contador}: x{numero_archivo} = 1 y x{posiciones_ceros_incrementadas} = 0  EN ESPERA")

                    
                    # Agregar el resultado a la lista de resultados
                    resultados_subproblemas.append(resultado)

                    

                    if xn == 0:
                        print(f"\nSub{contador - 1} con x{numero_archivo} = 0")

                        # Inicializar la lista X y la capacidad restante para Subproblema 2
                        X_sub2 = []
                        capacidad_restante = S

                        # Iterar sobre los archivos
                        for idx, archivo in enumerate(archivos):
                            peso = archivo["s"]
                    
                            # Si encontramos el archivo con el valor fraccionario (xn), lo marcamos como 0 en X_sub2
                            if archivo["numero_archivo"] == numero_archivo or Y[idx] == 0:
                                X_sub2.append(0)  # Marcar como 0 y no incluir este 
                                Y[idx] = 0 # guardamos en lista de fuera para hacer comparacion
                                continue  # Saltar al siguiente archivo

                            if capacidad_restante >= peso:  # Puede incluir completamente
                                X_sub2.append(1)
                                capacidad_restante -= peso
                            else:  # No puede incluir completamente
                                if capacidad_restante > 0:
                                    y = capacidad_restante / peso  # Proporción que se puede incluir
                                    X_sub2.append(y)
                                    capacidad_restante = 0  # Se ha llenado el espacio
                                else:
                                    X_sub2.append(0)  # No se puede incluir nada

                        # Si se llega a un espacio restante de 0, agregar 0 para el resto
                        if capacidad_restante == 0:
                            X_sub2.extend([0] * (len(archivos) - len(X_sub2)))  # Completa el resto con 0

                        print("Resultado de inclusión (X):", X_sub2)

                        # Calcular f(X) para Subproblema 2
                        Z_sub2 = sum(archivo["p"] * X_sub2[idx] for idx, archivo in enumerate(archivos))
                        print(f"\nSubproblema {contador - 1}: ")
                        # Subproblema 2: Ordenar X_sub2 de acuerdo al orden original de los archivos
                        X_sub2_ordenada = [0] * len(archivos)
                        for idx, archivo in enumerate(archivos):
                            numero_archivo = archivo["numero_archivo"]
                            X_sub2_ordenada[numero_archivo - 1] = X_sub2[idx]  # Guardar en el índice correspondiente

                        print(f"Resultado ordenado por x1, x2, x3,...xn para Subproblema {contador - 1}:", X_sub2_ordenada)
                        print(f"f(X) = {Z_sub2}")

                        # Actualizar X con el nuevo resultado
                        X = X_sub2

                    else:
                        print("en espera")
                        print(f"\nSub{contador} con x{numero_archivo} = 1")

                    break
            contador += 2
        else:
            if contador != 3:
                mejor = Z_sub2
                #print(mejor)
                print("Mejor valor posible de momento.")

                # Imprimir todas las sublistas
                print("\nLista de resultados de subproblemas en espera:")
                for sublista in resultados_subproblemas:
                    print("F", sublista)  # Esto imprime cada sublista

                # Imprimir el último resultado acumulado
                if resultados_subproblemas:  # Verifica si la lista no está vacía
                    ultimo_resultado = resultados_subproblemas[-1]  # Obtiene el último elemento
                    print("\nÚltimo resultado acumulado:", ultimo_resultado)

                    i = 2
                    finales = []
                    finales.append(mejor)
                    nuevo_valor = 0
                    while True:
                        
                        
                        compara,lis = espera(S, ultimo_resultado, x,archivos)
                        #print("lis",lis)
                        
                
                        # Filtrar los valores fraccionarios en la lista
                        fraccionarios = [num for num in lis if num % 1 != 0]
                        # Imprimir el resultado
                        if fraccionarios and compara > mejor:
                            print("\nporque existe fraccionario y ademas",compara,">",mejor)
                            print("Hay que ramificar por: ",fraccionarios)
                            # Ejemplo de restricción que queremos añadir

                            posicion_fraccionario = None

                            # Busca la posición del primer valor fraccionario
                            for i in range(len(lis)):
                                if isinstance(lis[i], float) and not lis[i].is_integer():
                                    posicion_fraccionario = i
                                    break  # Detiene la búsqueda al encontrar el primer fraccionario

                            print("Posición del valor fraccionario:", posicion_fraccionario + 1)
                            nuevo_var = f'x{posicion_fraccionario + 1}'
                            # Primer bloque: cuando nuevo_valor es 0
                            nuevo_valor = 1  # Define el primer nuevo_valor
                            
                            # Obtener el último subproblema (como cadena)
                            ultimo_subproblema = resultados_subproblemas[-1][0]  # Accedemos al primer elemento de la lista interna
    
                            # Extraer el número del subproblema actual
                            numero_subproblema = int(ultimo_subproblema.split()[1][:-1])  # Extrae el número después de "Subproblema"
    
                            # Verificar si es una restricción x2 = 0 o x2 = 1
                            if nuevo_valor == 1:
                                # Incrementar el número del subproblema en 2
                                nuevo_numero_subproblema = numero_subproblema + 2
                                # Agregar la nueva variable en la sección de "x = 1"
                                if 'y' in ultimo_subproblema:
                                    partes = ultimo_subproblema.split(' y ')
                                    partes[0] = f'Subproblema {nuevo_numero_subproblema}: ' + partes[0].split(': ')[-1] + f', {nuevo_var} = {nuevo_valor}'
                                    nuevo_subproblema = ' y '.join(partes)
                                else:
                                    nuevo_subproblema = f'Subproblema {nuevo_numero_subproblema}: ' + ultimo_subproblema.split(': ')[-1] + f', {nuevo_var} = {nuevo_valor}'
                                nuevo_numero_subproblema = numero_subproblema - 2
                            
                            resultados_subproblemas[-1][0] = nuevo_subproblema
                            nuevo_valor = 0
                            
                            if nuevo_valor == 0:
                                # Incrementar el número del subproblema en 1
                                nuevo_numero_subproblema = numero_subproblema + 1
                                # Agregar la nueva variable en la sección de "x[...] = 0"
                                if 'x[' in ultimo_subproblema:
                                    partes = ultimo_subproblema.split('x[')
                                    partes[0] = f'Subproblema {nuevo_numero_subproblema}: ' + partes[0].split(': ')[-1]
                                    partes[1] = f'{nuevo_var[1]}, ' + partes[1]
                                    nuevo_subproblema = 'x['.join(partes)
                                else:
                                    nuevo_subproblema = f'Subproblema {nuevo_numero_subproblema}: ' + ultimo_subproblema.split(': ')[-1] + f' y x[{nuevo_var[1]}] = {nuevo_valor}'
                                nuevo_numero_subproblema = numero_subproblema + 1
                            # Reemplazar el último subproblema en la lista
                            resultados_subproblemas[-1][0] = nuevo_subproblema

                            print("\nÚltimo subproblema modificado:", resultados_subproblemas[-1][0])

                            # Imprimir la lista completa después de la modificación
                            print("\nLista completa de resultados_subproblemas:")
                            for subproblema in resultados_subproblemas:
                                print(subproblema[0])

                            #break#ESTE ES EL BREAK IMPPORTANTE
                        else:
                            finales.append(compara)
                            print("\nya que no existe fraccionario O",compara,"<",mejor)
                            print("Ir a siguiente subproblema")
                            # Imprimir el último resultado acumulado
                            if resultados_subproblemas:  # Verifica si la lista no está vacía
                                try:
                                    del resultados_subproblemas[-1]
                                   
                                    #break
                                    ultimo_resultado = resultados_subproblemas[-1]  # Obtiene el último elemento
                                    #i = i + 1
                                    print("\nÚltimo resultado acumulado:", ultimo_resultado)
                                except IndexError:
                                    print("\nNo hay mas subproblemas")
                                    print("MEJORES SOLUCIONES POSIBLES:")
                                    print(finales)
                                    break
                            
                    
                            #break#para renar por ahora
                    

                break  # Salir del bucle si no hay valores fraccionarios
            else:
                print("Mejor valor posible.")
                break  # Salir del bucle si no hay valores fraccionarios




def espera(S, ultimo_subproblema, x, archivos):
    # Mostrar información inicial
    print("\n\nCapacidad del sistema (S):", S)
    print("\nÚltimo subproblema:", ultimo_subproblema)



    # Inicializar la lista 'guarda' con valor por defecto 2
    guarda = [2] * len(archivos)

    # Procesar el contenido de ultimo_subproblema para extraer los valores correctos
    for elemento in ultimo_subproblema:
        if 'x' in elemento:
            partes = elemento.split(': ')[-1]  # Ignorar el prefijo 'Subproblema X:'
            sub_elementos = partes.split(' y ')
            
            for sub in sub_elementos:
                if '=' in sub:
                    var, valor = sub.split('=')
                    valor = int(valor.strip())
                    
                    if 'x' in var and '[' not in var:
                        index = int(var.strip()[1:]) - 1  # Extrae el índice y ajusta a base 0
                        guarda[index] = valor

                    elif 'x[' in var and ']' in var:
                        indices_str = var.replace('x[', '').replace(']', '')
                        indices = [int(i.strip()) - 1 for i in indices_str.split(',')]
                        for idx in indices:
                            guarda[idx] = valor

    print("Lista 'guarda':", guarda)

    print("\nLista de detalles de archivos (Valor, Peso, Relación p/s):")
    for idx, sublista in enumerate(x):
        print(f"x{archivos[idx]['numero_archivo']} = {sublista}")

    
    # Inicializar la lista X y la capacidad restante
    X = [0] * len(archivos)
    capacidad_restante = S

    # Paso 1: Procesar los archivos prioritarios en 'guarda' con valor 1
    for idx, prioridad in enumerate(guarda):
        if prioridad == 1:
            # Buscar el archivo con el número de archivo correspondiente
            archivo = next((a for a in archivos if a["numero_archivo"] == idx + 1), None)
            if archivo:
                peso = archivo["s"]
            #archivo = archivos[idx]
            #peso = archivo["s"]
            if capacidad_restante > 0:
                if capacidad_restante >= peso:
                    X[idx] = 1
                    #print(capacidad_restante)
                    #print(peso)
                    capacidad_restante = capacidad_restante - peso
                    #print(capacidad_restante)
                else:
                    X[idx] = capacidad_restante / peso
                    capacidad_restante = 0
                    X = [0 if valor > 1 else valor for valor in X]
                    break
            

    
    # Paso 2: Procesar los archivos en 'guarda' con valor mayor a 1
    for idx, prioridad in enumerate(guarda):
        if prioridad > 1:
           X[idx] = 2  # Asigna 2 en X para prioridades mayores a 1
    
    


    # Paso 3: Procesar el resto de archivos en orden descendente de la relación p/s
    for archivo in archivos:
        idx = archivo["numero_archivo"] - 1
        if X[idx] < 2:  # Saltar los archivos ya procesados en el paso anterior
            continue
        
        peso = archivo["s"]
        if capacidad_restante > 0:
            if capacidad_restante >= peso:  # Puede incluir completamente
                X[idx] = 1
                capacidad_restante -= peso
            else:  # No puede incluir completamente
                X[idx] = capacidad_restante / peso
                capacidad_restante = 0
                X = [0 if valor > 1 else valor for valor in X]
                break

    

    # Calcular f(X) para el subproblema actual
    Z = sum(archivo["p"] * X[archivo["numero_archivo"] - 1] for archivo in archivos)
    #print("Resultado de inclusión (X): ",X)

    # Extraer el número del subproblema del primer valor de ultimo_subproblema
    subproblema_num = int(ultimo_subproblema[0].split()[1].rstrip(':'))  # Elimina los ':' al final

    print(f"\nSubproblema {subproblema_num}: ")
    # Ordenar X de acuerdo al orden original de los archivos
    X_ordenada = [0] * len(archivos)
    for idx, archivo in enumerate(archivos):
        numero_archivo = archivo["numero_archivo"]
        X_ordenada[numero_archivo - 1] = X[idx]  # Guardar en el índice correspondiente

    print(f"Resultado ordenado por x1, x2, x3,...xn para Subproblema {subproblema_num}:", X)
    print(f"f(X) = {Z}")

    #AHORA importante para la logica
    return Z,X


# Función para ordenar archivos por su relación prioridad/tamaño
def ordenar_archivos_por_relacion(archivos):
    archivos.sort(key=lambda archivo: archivo["p"] / archivo["s"], reverse=True)

# Función que selecciona el primer archivo no revisado
def seleccionar_archivo(archivos):
    i = 0
    while i < len(archivos):
        if not archivos[i]["r"]:  # Busca el siguiente archivo no revisado
            return i
        i += 1
    return -1  # Retorna -1 si ya no hay más archivos por revisar

def sistema_de_almacenamiento():
    S = rnd.randint(50, 100)  # Capacidad aleatoria del sistema
    print(f"Capacidad del sistema: {S}")
    cantidad_archivos = rnd.randint(5, 10)  # Cantidad aleatoria de archivos
    print(f"Cantidad de archivos: {cantidad_archivos}")
    
    archivos = []
    
    # Generar los archivos aleatoriamente con tamaño y prioridad
    for i in range(cantidad_archivos):
        s = rnd.randint(20, 30)  # Tamaño del archivo
        p = rnd.randint(15, 25)  # Prioridad del archivo
        print(f"Archivo {i + 1} - Tamaño: {s}, Prioridad: {p}")
        archivos.append({"p": p, "s": s, "i": False, "r": False, "numero_archivo": i + 1})  # Añadir los archivos a la lista

    # Ordenar los archivos por relación prioridad/tamaño
    ordenar_archivos_por_relacion(archivos)
    
    # Imprimir los archivos ordenados
    print("\nArchivos ordenados por relación prioridad/tamaño:")
    for idx, archivo in enumerate(archivos):
        relacion = archivo["p"] / archivo["s"]
        # Mostrar el índice del archivo y sus detalles
        print(f"{idx + 1}-Archivo {archivo['numero_archivo']} - Prioridad: {archivo['p']}, Tamaño: {archivo['s']}, Relación p/s: {relacion:.2f} -->x{archivo['numero_archivo']}")

    tamano_total = 0
    i = 0
    
    # Seleccionar archivos con el algoritmo greedy
    while i >= 0 and tamano_total < S:
        i = seleccionar_archivo(archivos)  # Selecciona el archivo con mejor relación
        
        if i == -1:  # Si ya no hay archivos disponibles, termina
            break
        
        if tamano_total + archivos[i]["s"] <= S:  # Si cabe el archivo en el sistema
            archivos[i]["i"] = True  # Marca el archivo como seleccionado
            tamano_total += archivos[i]["s"]  # Actualiza el tamaño acumulado
        archivos[i]["r"] = True  # Marca el archivo como revisado
    
    return archivos, S  # Devuelve los archivos y la capacidad S

def main():
    resultado, S = sistema_de_almacenamiento()  # Llama a la función del sistema de almacenamiento
    print("\nArchivos seleccionados:")
    print("{prioridad,tamaño,si está dentro de la mochila,si se revisó por greedy}")  # Encabezado
    for archivo in resultado:
        # Imprime cada archivo en el formato requerido
        print(archivo)

    # VAMOS AL B&B
    ByB(resultado, S)  # Pasa los archivos y la capacidad a la función ByB

if __name__ == "__main__":
    main()
