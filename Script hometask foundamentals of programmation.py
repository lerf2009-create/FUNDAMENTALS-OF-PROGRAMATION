Encabezado ={ 
    "Nombre_taller" : "Desarrollo taller Fundamentos de programación - Taller de entrenamiento de programación y razonamiento lógico",
    "Integrantes" : """
                    """

    """
    Ayda Johanna Bermudez Leon 
    Luis Eduardo Reyes Fernández
    Katherinne Stella Castaneda Rodriguez""",
    "Docente" : "Ivan Dario Rico Arias",
    "Universidad": "Konrad Lorenz - Especialización en analítica de datos e IA",
    "Fecha" : "2024-09-16",
    }

print("\033[93m" + '=' * 120 + "\033[0m")
print("\033[1m" + Encabezado["Nombre_taller"] + "\033[0m")  
print()
print("\033[1m" + "Integrantes:", Encabezado["Integrantes"] + "\033[0m") 
print()
print("\033[1m" + "Docente:", Encabezado["Docente"] + "\033[0m")
print()
print("\033[1m" + "Universidad", Encabezado["Universidad"]+ "\033[0m")
print()
print("\033[1m" + "Fecha:", Encabezado["Fecha"]+ "\033[0m")
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 1 - EVALUACIÓN DE PEDIDOS PARA DESPACHO")
print("\033[93m" + '=' * 120 + "\033[0m")
print()

#Creamos diccionario con los datos de cada cliente utilizando listas')
#Recibe: Todos los datos de la tabla de pedidos.
#Devuelve: Un diccionario de listas y "alimenta" todos los calculos de las funciones posteriores.

pedidos_1 = {
    "Clientes": [
        "Laura",
        "Carlos",
        "Distribuciones ABC",
        "Andrea",
        "Comercial XYZ"
    ],

    "Tipo": [
        "Regular",
        "Preferencial",
        "Corporativo",
        "Regular",
        "Regular"
    ],

    "Valor": [
        1500000,
        1800000,
        6000000,
        900000,
        3500000
    ],

    "Inventario": [
        50,
        30,
        100,
        8,
        15
    ],

    "Unidades": [
        10,
        12,
        25,
        12,
        20
    ],

    "Mora": [
        0,
        15,
        0,
        0,
        45
    ]
}

#Utilizamos la función for para recorrer todos los valores del diccionario creando un recorrido por cada indice de cada lista dentro del conjunto' \
#y creamos las variables cliente hasta mora para que for recorra los 5 índices.
#Se crean las variables de la tabla del ejercicio con base en el diccionario "pedidos_1", invocamos el elemento de la lista según su índice.
#los if agregan elementos a la lista causas si la condicion se cumple y en el caso de que la mora esté entre 1 y 30 días revisa el tipo de cliente y el valor.
#si len causas es mayor a 0 entonces devuelve los datos del cliente con valores en 0 exceptuando las unidades que siguen siendo las mismas y el valor del pedido.

for i in range(5):

    cliente = pedidos_1["Clientes"][i]
    tipo = pedidos_1["Tipo"][i]
    valor = pedidos_1["Valor"][i]
    inventario = pedidos_1["Inventario"][i]
    unidades = pedidos_1["Unidades"][i]
    mora = pedidos_1["Mora"][i]

    causas = []

    if unidades > inventario:
        causas.append("Inventario insuficiente")

    if mora > 30:
        causas.append("Más de 30 días de mora")

    if mora >= 1 and mora <= 30:

        if tipo != "Preferencial" and tipo != "Corporativo":
            causas.append("Cliente no autorizado por mora")

        if valor > 2000000:
            causas.append("Pedido superior a $2.000.000 con mora")

    if len(causas) > 0:

        estado = "RECHAZADO"
        descuento = 0
        valor_descuento = 0
        valor_despues_descuento = valor
        envio = 0
        valor_final = 0
        inventario_restante = inventario

#si nada de lo anterior se cumple entonces el pedido es aprobado y al ser aprobado se revisa que tipo de cliente 
# es para asignar el % de descuento.
#se crean las variables valor de descuento y valor despues de descuento y dependiendo del valor después del 
# descuento se asigna valor 0 al envio o de lo contrario 35000.
    else:

        estado = "APROBADO"

        if tipo == "Regular":
            descuento = 0
        elif tipo == "Preferencial":
            descuento = 5
        else:
            descuento = 8

        valor_descuento = valor * descuento / 100
        valor_despues_descuento = valor - valor_descuento

        if valor_despues_descuento >= 5000000:
            envio = 0
        else:
            envio = 35000

        valor_final = valor_despues_descuento + envio
        inventario_restante = inventario - unidades

#Finalmente se imprimen los nombres de cada variable y sus datos contenidos tantas veces como la función for recorre cada 
#índice de cada lista.
    print ()
    print("Cliente:", cliente)
    print("Estado:", estado)

    if estado == "RECHAZADO":
        print("Causas:", causas)

    print("Descuento:", descuento, "%")
    print("Valor después del descuento:", valor_despues_descuento)
    print("Envío:", envio)
    print("Valor final:", valor_final)
    print("Inventario restante:", inventario_restante)
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 2 - RIESGO OPERATIVO")
print("\033[93m" + '=' * 120 + "\033[0m")

#Creamos lista con diccionarios con los datos de la tabla del ejercicio 2. 
ordenes_2 = [
    {
        "Valor": 4000000,
        "Tipo": "Frecuente",
        "Antiguedad": 18,
        "Modificaciones": 0,
        "Retraso": 0,
        "Documentacion": True
    },

    {
        "Valor": 6000000,
        "Tipo": "Nuevo",
        "Antiguedad": 2,
        "Modificaciones": 0,
        "Retraso": 0,
        "Documentacion": True
    },

    {
        "Valor": 9000000,
        "Tipo": "Frecuente",
        "Antiguedad": 12,
        "Modificaciones": 3,
        "Retraso": 25,
        "Documentacion": True
    },

    {
        "Valor": 10000000,
        "Tipo": "Corporativo",
        "Antiguedad": 36,
        "Modificaciones": 0,
        "Retraso": 3,
        "Documentacion": True
    },

    {
        "Valor": 16000000,
        "Tipo": "Corporativo",
        "Antiguedad": 40,
        "Modificaciones": 0,
        "Retraso": 0,
        "Documentacion": True
    }
]


#creamos n for que recorra cada diccionario en la lista.

for orden in ordenes_2:

    valor = orden["Valor"]
    tipo = orden["Tipo"]
    antiguedad = orden["Antiguedad"]
    modificaciones = orden["Modificaciones"]
    retraso = orden["Retraso"]
    documentacion = orden["Documentacion"]

#Creamos las condiciones a revisar y creamos las variables riesgo y riesgo inicial dependiendo de los montos.
    if valor <= 8000000:
        riesgo = 1
        riesgo_inicial = "Bajo"

    elif valor <= 15000000:
        riesgo = 2
        riesgo_inicial = "Medio"

    else:
        riesgo = 3
        riesgo_inicial = "Alto"
#creamos una lista vacía en donde se almacenarán índices definidos por la validación de tipo de cliente,
#número de modificaciones, días de retraso y finalmente si es corporatico con documentación al día y retraso menor
#a 5 días.
    reglas = []

    if tipo == "Nuevo" and antiguedad < 3:
        riesgo = riesgo + 1
        reglas.append("Cliente nuevo con menos de 3 meses")

    if modificaciones >= 3:
        riesgo = riesgo + 1
        reglas.append("Tres o más modificaciones")

    if retraso > 20:
        riesgo = riesgo + 1
        reglas.append("Retraso superior a 20 días")

    if tipo == "Corporativo":

        if antiguedad >= 24 and documentacion == True and retraso <= 5:
            riesgo = riesgo - 1
            reglas.append("Reducción por cliente corporativo")
#si la documentación no está al día y si el monto es mayor a 15' se aplica riesgo 3
    if documentacion == False:
        riesgo = 3
        reglas.append("Documentación incompleta")

    if valor > 15000000:
        riesgo = 3
        reglas.append("Valor superior a $15.000.000")

    if riesgo < 1:
        riesgo = 1

    if riesgo > 3:
        riesgo = 3
#se definen las variables  y se asigna variable riesgo final y acción deacuerdo a dicha suma. 
    if riesgo == 1:
        riesgo_final = "Bajo"
        accion = "Procesar"

    elif riesgo == 2:
        riesgo_final = "Medio"
        accion = "Revisar"

    else:
        riesgo_final = "Alto"
        accion = "Retener"

    print()
    print("Valor:", valor)
    print("Riesgo inicial:", riesgo_inicial)
    print("Reglas activadas:", reglas)
    print("Riesgo final:", riesgo_final)
    print("Acción:", accion)
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 3 - CONTROL DE INVENTARIO")
print("\033[93m" + '=' * 120 + "\033[0m")

#Creamos las variables y listas de datos necesarias:

inventario_inicial = 50

movimientos = [
    ["Salida", 30],
    ["Salida", 25],
    ["Entrada", 15],
    ["Salida", 10]
]

inventario = inventario_inicial
#Definimos los contadores:
recibidos = 0
invalidos = 0
entradas_aceptadas = 0
salidas_aceptadas = 0
salidas_rechazadas = 0
unidades_ingresadas = 0
unidades_salidas = 0

#Definimos variable critico y primer momento crítico

critico = False
primer_momento_critico = 0

#Invocamos la función for para que en los ídices 0 sean reconocidos como el tipo de movimiento y el índice 1 como 
# las unidades de dichos movimientos.

for movimiento in movimientos:

    tipo = movimiento[0]
    unidades = movimiento[1]

    recibidos = recibidos + 1 #Definimos que los pedidos recibidos serán iguala  la suma de los recibids iniciales 
                              #(0) más los que se reciban, en total 4.

    if unidades <= 0 or (tipo != "Entrada" and tipo != "Salida"): #busca los tipos de movimiento y verifica si las 
                                                                  #unidades son menores a 0, si las unidades son 
                                                                  #menores a 0 o hay algún otro tipo de movimiento 
                                                                  #entonces lo registra como inválido.

        invalidos = invalidos + 1
        print("Movimiento inválido:", movimiento)

    else:                                                         #Si no es iválido entonces es válido y valida si es 
                                                                  #una entrada o una salida y dependiendo de eso suma o 
                                                                  #resta unidades al inventario y actualiza las unidades 
                                                                  #aceptadas y las unidades salidas.

        if tipo == "Entrada":

            inventario = inventario + unidades
            entradas_aceptadas = entradas_aceptadas + 1
            unidades_ingresadas = unidades_ingresadas + unidades #Se utiliza acumulador para registrar todas las unidades entradas.

        else:

            if unidades <= inventario:

                inventario = inventario - unidades
                salidas_aceptadas = salidas_aceptadas + 1
                unidades_salidas = unidades_salidas + unidades #Se utiliza acumulador para registrar todas las unidades salidas.

            else:

                salidas_rechazadas = salidas_rechazadas + 1
                print("Salida rechazada por inventario insuficiente") #si no es una entrada y tampoco es menor al 
                                                                      #inventario entonces es rechazada por superar el inventario disponible.

        if inventario < 10 and critico == False: #se define una bandera de alerta para el momento crítico de inventario <10
                                                 #si se cumple con el inventario < a 10 y crítico es false entonces crítico
                                                 #pasa a ser True y el primer momento "Inventario".
            critico = True
            primer_momento_critico = inventario

print()
print("Movimientos recibidos:", recibidos)
print("Movimientos inválidos:", invalidos)
print("Entradas aceptadas:", entradas_aceptadas)
print("Salidas aceptadas:", salidas_aceptadas)
print("Salidas rechazadas:", salidas_rechazadas)
print("Unidades ingresadas:", unidades_ingresadas)
print("Unidades salidas:", unidades_salidas)
print("Inventario final:", inventario)

if critico == True:
    print("Primer momento crítico:", primer_momento_critico)
else:
    print("No hubo inventario crítico")

inventario_verificado = inventario_inicial + unidades_ingresadas - unidades_salidas

print("Inventario final:", inventario) #Imprime el inventario acumulado sumando y restando movimientos desde el inventario inicial.
print("Inventario verificado:", inventario_verificado) #Se realiza la verificación del inventario inicial mas ingresos y menos salidas.

if inventario == inventario_verificado: #Si coinciden ambas cantidades es correcto el calculo de la acumulación entre entredas y salidas vs el paso a paso del script.
    print("VERIFICACIÓN CORRECTA")
else:
    print("VERIFICACIÓN INCORRECTA")
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 4 - AUDITORÍA DE TRANSACCIONES")
print("\033[93m" + '=' * 120 + "\033[0m")
#Creamos la base de datos con una lista con listas.
transacciones_4 = [
    ["T01", 800000, "Compra", 14, True],
    ["T02", 6200000, "Compra", 2, True],
    ["T03", 2500000, "Devolucion", 11, False],
    ["T04", 700000, "Ajuste", 4, True],
    ["T05", -100000, "Compra", 10, True],
    ["T06", 900000, "Compra", 25, True]
]
#Acumuladores de jornada de transacciones
recibidas = 0
validas = 0
invalidas = 0
valor_total_valido = 0
transacciones_alertadas = 0
alertas_totales = 0

#Acumuladores de alertas por transacción.
alerta_valor = 0
alerta_hora = 0
alerta_devolucion = 0
alerta_no_autorizada = 0
alerta_ajuste = 0

codigos_revision = [] #lista para acumular transacciones a revisar

mayor_transaccion = 0 #acumulador de la mayor transacción, se revisará el valor de cada transacción de la base hasta dar con la más alta.
codigo_mayor = "" #contendrá el código de la transacción con el valor más alto calculados en las lineas 501 a 504.

#Invocamos un for para asignar una variable a cada dato de la lista que alimenta al programa y poder repetir la busqueda de condiciones en cada variable.
for transaccion in transacciones_4:

    codigo = transaccion[0]
    valor = transaccion[1]
    tipo = transaccion[2]
    hora = transaccion[3]
    autorizada = transaccion[4]

    recibidas = recibidas + 1 #suma las veces que la función for procesa un registro para tomar cada registro como transacciones recibidas.

    #En este punto se definen las funciones condicionales para validar cada transacción y cada condición se revisa en cada transacción o registro debido a que se encuentra dentro del jor en la identación jerárquica.
    #Es decir se definen las líneas de código para validar primero si hay transacciones inválidas y reportarlas:
    if valor <= 0 or (tipo != "Compra" and tipo != "Devolucion" and tipo != "Ajuste") or hora < 0 or hora > 23:

        invalidas = invalidas + 1
        print("Transacción inválida:", codigo)
    #Posterior a la validación de trx inválidas se procede a procesar las validas:
    else:

        validas = validas + 1 #Acumula cada transacción válida en el acumulador de trx validas de la línea 430.
        valor_total_valido = valor_total_valido + valor #define la variable como el siguiente valor que recorre y suma el posterior.

        alertas = 0 #Acumulador de alertas en las validaciones de las filas 475-480-485-490-495
        #en los siguientes 5 if se validan las condiciones que generan alerta por monto, hora, tipo y monto, estado de autorización
        if valor > 5000000:

            alertas = alertas + 1
            alerta_valor = alerta_valor + 1

        if hora >= 0 and hora <= 5 and valor > 1000000:

            alertas = alertas + 1
            alerta_hora = alerta_hora + 1

        if tipo == "Devolucion" and valor > 2000000:

            alertas = alertas + 1
            alerta_devolucion = alerta_devolucion + 1

        if autorizada == False:

            alertas = alertas + 1
            alerta_no_autorizada = alerta_no_autorizada + 1

        if tipo == "Ajuste" and valor > 500000:

            alertas = alertas + 1
            alerta_ajuste = alerta_ajuste + 1
        #Se valida cantidad de alertas para arrojar el total de alertas encontradas en los recorridos del for en cada registro.
        #arroja el total del acumulador alertas_totales más las alertas generadas en el recorrido del for.
        #posteriormente se agregan los códigos de las transacciones que generaron alerta  a la lista códigos_revisión.
        if alertas > 0:

            transacciones_alertadas = transacciones_alertadas + 1
            alertas_totales = alertas_totales + alertas
            codigos_revision.append(codigo)

        if valor > mayor_transaccion:

            mayor_transaccion = valor
            codigo_mayor = codigo

print()
print("Recibidas:", recibidas)
print("Válidas:", validas)
print("Inválidas:", invalidas)
print("Valor total válido:", valor_total_valido)
print("Transacciones alertadas:", transacciones_alertadas)
print("Alertas totales:", alertas_totales)

print()
print("Alertas por regla:")
print("Valor superior a $5.000.000:", alerta_valor)
print("Horario 0-5:", alerta_hora)
print("Devolución superior a $2.000.000:", alerta_devolucion)
print("No autorizada:", alerta_no_autorizada)
print("Ajuste superior a $500.000:", alerta_ajuste)

print()
print("Códigos a revisar:", codigos_revision)
print("Mayor transacción válida:", codigo_mayor, mayor_transaccion)

if validas > 0:
    porcentaje_alerta = transacciones_alertadas * 100 / validas
else:
    porcentaje_alerta = 0

print("Porcentaje de válidas con alerta:", porcentaje_alerta, "%")

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 5 - ANÁLISIS DE COMENTARIOS")
print("\033[93m" + '=' * 120 + "\033[0m")
#Creamos las listas con las palabras clasificadas en registros de palabras favorables y desfavorables, así mismo la lista de comentarios.
favorables = [
    "excelente",
    "rápido",
    "bueno",
    "amable",
    "claro",
    "recomendado"
]

desfavorables = [
    "malo",
    "lento",
    "demora",
    "problema",
    "deficiente",
    "incompleto"
]

comentarios = [
    "El servicio fue excelente y el asesor amable",
    "El servicio fue lento y hubo demora",
    "El producto fue bueno pero hubo problema",
    "Excelente excelente servicio recomendado",
    "La atención terminó a tiempo",
    "El servicio fue malo deficiente e incompleto"
]
#creamos contador de frecuencias en diccionario para contar las veces que aparece cada palabra de las listas Favorables y desfaborables.
frecuencia = {}
#Creamos contadores de total por tipo de comentario
total_favorables = 0
total_desfavorables = 0
#Recorremos cada comentario definiendo que la variable palabras va a ser definida como el comentario en minúscula y separado por espacio.
for comentario in comentarios:

    palabras = comentario.lower().split()
#se crean los contadores según tipo de comentario antes de hacer el recorrido por cada palabra de cada comentario ya separado por espacios en cada lista.
    favorables_comentario = 0
    desfavorables_comentario = 0
#recorremos cada palabra de cada comentario.
    for palabra in palabras:
#si encuentra palabras en la lista de palabras favorables lo que procede es que suma el número inicial de favorables_comentario más esa palabra favorable consecutivamente.
        if palabra in favorables:

            favorables_comentario = favorables_comentario + 1
            total_favorables = total_favorables + 1 #acumula 1 a la variable total favorables.

            if palabra in frecuencia: #si cada palabra que se recorra y se identifique como favorable está en el diccionario de frecuencia se suma 1 a la palabra, si no está entonces se crea la palabra dentro del diccionario como una ueva llave y se suma 1.
                frecuencia[palabra] = frecuencia[palabra] + 1
            else:
                frecuencia[palabra] = 1

        elif palabra in desfavorables: #este elif funciona como un "y si" las palabras se encuentran el la lista de desfavorables entonces realiza la acumulación en desfavorables_comentario y en el total de desfavorables.

            desfavorables_comentario = desfavorables_comentario + 1
            total_desfavorables = total_desfavorables + 1

            if palabra in frecuencia: #en este punto nuevamente revisa si la palabra está en el diccionario de frecuencia y si aparece ñe suma uno y si no crea la nueva llave e inicia a acumular.
                frecuencia[palabra] = frecuencia[palabra] + 1
            else:
                frecuencia[palabra] = 1
    #se compara la cantidad de palabras favorables vs las desfavorables y viceversa en cada comentario. si ninguna es mayor que la otra entonces 
    #se busca si hay almenos una palabra favorable entonces se clasifica como mixto.
    if favorables_comentario > desfavorables_comentario:

        clasificacion = "Favorable"

    elif desfavorables_comentario > favorables_comentario:

        clasificacion = "Desfavorable"

    elif favorables_comentario > 0: #una vez se validan las dos condiciones anteriores se valida que por lo menos haya 1 favorable para claseificarlo como mixto.

        clasificacion = "Mixto"

    else:

        clasificacion = "Sin clasificación" # si no encuentra palabras dentro de las listas favorables o desfavorables entonces se registra como sin clasificación.

    print()
    print("Comentario:", comentario)
    print("Favorables:", favorables_comentario)
    print("Desfavorables:", desfavorables_comentario)
    print("Clasificación:", clasificacion)

print()
print("Total favorables:", total_favorables)
print("Total desfavorables:", total_desfavorables)
print("Frecuencia de palabras:", frecuencia)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 6 - CONSOLIDACIÓN DE VENTAS")
print("\033[93m" + '=' * 120 + "\033[0m")

ventas_6 = [
    ["A", "Tecnología", 8, 120000, 0],
    ["B", "Tecnología", 2, 900000, 10],
    ["A", "Tecnología", 5, 120000, 5],
    ["C", "Accesorios", 15, 40000, 0],
    ["B", "Tecnología", 1, 900000, 15],
    ["D", "Accesorios", 0, 50000, 0]
]

ventas_recibidas = 0
ventas_validas = 0
ventas_invalidas = 0

total_bruto = 0
total_descuento = 0
total_neto = 0

productos = {}

for venta in ventas_6:

    producto = venta[0]
    categoria = venta[1]
    unidades = venta[2]
    precio = venta[3]
    descuento = venta[4]

    ventas_recibidas = ventas_recibidas + 1

    if unidades <= 0 or precio <= 0 or descuento < 0 or descuento > 40:

        ventas_invalidas = ventas_invalidas + 1

    else:

        ventas_validas = ventas_validas + 1

        bruto = unidades * precio
        valor_descuento = bruto * descuento / 100
        neto = bruto - valor_descuento

        total_bruto = total_bruto + bruto
        total_descuento = total_descuento + valor_descuento
        total_neto = total_neto + neto

        if producto not in productos:

            productos[producto] = {
                "Categoria": categoria,
                "Unidades": unidades,
                "Ingreso": neto,
                "Operaciones": 1
            }

        else:

            productos[producto]["Unidades"] = productos[producto]["Unidades"] + unidades
            productos[producto]["Ingreso"] = productos[producto]["Ingreso"] + neto
            productos[producto]["Operaciones"] = productos[producto]["Operaciones"] + 1

print()
print("Ventas recibidas:", ventas_recibidas)
print("Ventas válidas:", ventas_validas)
print("Ventas inválidas:", ventas_invalidas)
print("Valor bruto:", total_bruto)
print("Descuento:", total_descuento)
print("Ingreso neto:", total_neto)

print()
print("CONSOLIDADO POR PRODUCTO")

producto_mas_unidades = ""
mayor_unidades = 0

producto_mayor_ingreso = ""
mayor_ingreso = 0

ingreso_consolidado = 0

for producto in productos:

    unidades = productos[producto]["Unidades"]
    ingreso = productos[producto]["Ingreso"]
    operaciones = productos[producto]["Operaciones"]

    ingreso_consolidado = ingreso_consolidado + ingreso

    print()
    print("Producto:", producto)
    print("Categoría:", productos[producto]["Categoria"])
    print("Unidades:", unidades)
    print("Ingreso neto:", ingreso)
    print("Operaciones:", operaciones)

    if unidades > mayor_unidades:

        mayor_unidades = unidades
        producto_mas_unidades = producto

    if ingreso > mayor_ingreso:

        mayor_ingreso = ingreso
        producto_mayor_ingreso = producto

    if total_neto > 0:

        participacion = ingreso * 100 / total_neto

    else:

        participacion = 0

    print("Participación en ingreso:", participacion, "%")

print()
print("Producto con más unidades:", producto_mas_unidades)
print("Producto con mayor ingreso:", producto_mayor_ingreso)

print("Ingreso global:", total_neto)
print("Ingreso consolidado:", ingreso_consolidado)

if total_neto == ingreso_consolidado:
    print("VERIFICACIÓN CORRECTA")
else:
    print("VERIFICACIÓN INCORRECTA")

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 7 - GESTIÓN DE PEDIDOS")
print("\033[93m" + '=' * 120 + "\033[0m")

pedidos_7 = [
    ["C1", 10, 10, 3, 3, "Pagado"],
    ["C1", 8, 6, 4, 4, "Pagado"],
    ["C2", 5, 5, 2, 4, "Pagado"],
    ["C2", 7, 0, 3, 3, "Pagado"],
    ["C3", 6, 6, 3, 2, "Rechazado"],
    ["C3", 4, 4, 2, 2, "Pendiente"]
]

solicitadas_total = 0
entregadas_total = 0

cumplidos = 0
parciales = 0
incumplidos = 0

dias_retraso_total = 0
pedidos_tardios = 0

clientes = {}

for pedido in pedidos_7:

    cliente = pedido[0]
    solicitadas = pedido[1]
    entregadas = pedido[2]
    prometidos = pedido[3]
    reales = pedido[4]
    pago = pedido[5]

    solicitadas_total = solicitadas_total + solicitadas
    entregadas_total = entregadas_total + entregadas

    porcentaje_entregado = entregadas * 100 / solicitadas

    if entregadas == 0 or pago == "Rechazado" or entregadas > solicitadas:

        categoria = "Incumplido"
        incumplidos = incumplidos + 1

    elif entregadas == solicitadas and reales <= prometidos and pago == "Pagado":

        categoria = "Cumplido"
        cumplidos = cumplidos + 1

    else:

        categoria = "Cumplimiento parcial"
        parciales = parciales + 1

    if reales > prometidos:

        retraso = reales - prometidos
        pedidos_tardios = pedidos_tardios + 1
        dias_retraso_total = dias_retraso_total + retraso

    else:

        retraso = 0

    print()
    print("Cliente:", cliente)
    print("Porcentaje entregado:", porcentaje_entregado, "%")
    print("Categoría:", categoria)
    print("Días de retraso:", retraso)

    if cliente not in clientes:

        clientes[cliente] = {
            "Pedidos": 1,
            "Cumplidos": 0,
            "Parciales": 0,
            "Incumplidos": 0
        }

    else:

        clientes[cliente]["Pedidos"] = clientes[cliente]["Pedidos"] + 1

    if categoria == "Cumplido":

        clientes[cliente]["Cumplidos"] = clientes[cliente]["Cumplidos"] + 1

    elif categoria == "Cumplimiento parcial":

        clientes[cliente]["Parciales"] = clientes[cliente]["Parciales"] + 1

    else:

        clientes[cliente]["Incumplidos"] = clientes[cliente]["Incumplidos"] + 1

print()
print("Pedidos totales:", len(pedidos_7))
print("Cumplidos:", cumplidos)
print("Parciales:", parciales)
print("Incumplidos:", incumplidos)

print("Unidades solicitadas:", solicitadas_total)
print("Unidades entregadas:", entregadas_total)

porcentaje_global = entregadas_total * 100 / solicitadas_total

print("Porcentaje global de cumplimiento:", porcentaje_global, "%")

if pedidos_tardios > 0:

    promedio_retraso = dias_retraso_total / pedidos_tardios

else:

    promedio_retraso = 0

print("Promedio de días de retraso:", promedio_retraso)

print()
print("RESUMEN POR CLIENTE")

for cliente in clientes:

    print()
    print("Cliente:", cliente)
    print("Pedidos:", clientes[cliente]["Pedidos"])
    print("Cumplidos:", clientes[cliente]["Cumplidos"])
    print("Parciales:", clientes[cliente]["Parciales"])
    print("Incumplidos:", clientes[cliente]["Incumplidos"])

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 8 - EVALUACIÓN DE PROVEEDORES")
print("\033[93m" + '=' * 120 + "\033[0m")

#Para el punto 8 se consultaron otras fuentes para poder obtener orientación de su solución y se utilizó "def" para poder llevar 
#a cabo el ejercicio aunque no se ha visto dicho concepto en las sesiones presenciales.
#Se crean las funciones necesarias para crear las clasificaciones de clientes, la escala de puntos, clasificación de proveedor.
def puntos_puntualidad(porcentaje):

    if porcentaje >= 95:
        puntos = 30

    elif porcentaje >= 85:
        puntos = 20

    elif porcentaje >= 70:
        puntos = 10

    else:
        puntos = 0

    return puntos


def puntos_completos(porcentaje):

    if porcentaje >= 98:
        puntos = 30

    elif porcentaje >= 90:
        puntos = 20

    elif porcentaje >= 80:
        puntos = 10

    else:
        puntos = 0

    return puntos


def puntos_rechazos(porcentaje):

    if porcentaje <= 1:
        puntos = 30

    elif porcentaje <= 3:
        puntos = 20

    elif porcentaje <= 5:
        puntos = 10

    else:
        puntos = 0

    return puntos


def puntos_incidentes(incidentes):

    if incidentes == 0:
        puntos = 10

    elif incidentes == 1:
        puntos = 5

    else:
        puntos = 0

    return puntos


def clasificar_proveedor(puntaje, meses, rechazo, incidentes):

    if rechazo > 8:

        categoria = "Crítico"

    elif incidentes >= 3:

        categoria = "En observación"

    elif meses < 6 and puntaje >= 90:

        categoria = "Confiable"

    elif puntaje >= 90:

        categoria = "Estratégico"

    elif puntaje >= 75:

        categoria = "Confiable"

    elif puntaje >= 60:

        categoria = "En observación"

    else:

        categoria = "Crítico"

    return categoria

#Se crean las listas de proveedores con cada índice
proveedores = [
    ["P1", 95, 98, 1, 0, 30],
    ["P2", 94.9, 90, 2, 1, 18],
    ["P3", 85, 89.9, 4, 0, 12],
    ["P4", 98, 99, 0.5, 0, 4],
    ["P5", 96, 99, 9, 0, 36],
    ["P6", 96, 99, 1, 3, 36]
]

#Se crean los contadores para realizar la acumulación de los resultados solicitados:
conteo_estrategico = 0
conteo_confiable = 0
conteo_observacion = 0
conteo_critico = 0

total_puntajes = 0
mayor_puntaje = 0
menor_puntaje = 100

cantidad_proveedores = 0

#Se invoca la función for para crear temporalmente las variables por cada índice 
for proveedor in proveedores:

    nombre = proveedor[0]
    puntualidad = proveedor[1]
    completo = proveedor[2]
    rechazo = proveedor[3]
    incidentes = proveedor[4]
    meses = proveedor[5]

    p1 = puntos_puntualidad(puntualidad)
    p2 = puntos_completos(completo)
    p3 = puntos_rechazos(rechazo)
    p4 = puntos_incidentes(incidentes)

    puntaje = p1 + p2 + p3 + p4

    categoria = clasificar_proveedor(
        puntaje,
        meses,
        rechazo,
        incidentes
    )

    total_puntajes = total_puntajes + puntaje
    cantidad_proveedores = cantidad_proveedores + 1

    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje

    if puntaje < menor_puntaje:
        menor_puntaje = puntaje

    if categoria == "Estratégico":
        conteo_estrategico = conteo_estrategico + 1

    elif categoria == "Confiable":
        conteo_confiable = conteo_confiable + 1

    elif categoria == "En observación":
        conteo_observacion = conteo_observacion + 1

    else:
        conteo_critico = conteo_critico + 1

    print()
    print("Proveedor:", nombre)
    print("Puntualidad:", p1)
    print("Completos:", p2)
    print("Rechazos:", p3)
    print("Incidentes:", p4)
    print("Puntaje total:", puntaje)
    print("Categoría:", categoria)

promedio_puntaje = total_puntajes / cantidad_proveedores

porcentaje_critico_observacion = (
    (conteo_critico + conteo_observacion)
    * 100
    / cantidad_proveedores
)

print()
print("Máximo:", mayor_puntaje)
print("Mínimo:", menor_puntaje)
print("Promedio:", promedio_puntaje)

print("Estratégicos:", conteo_estrategico)
print("Confiables:", conteo_confiable)
print("En observación:", conteo_observacion)
print("Críticos:", conteo_critico)

print(
    "Porcentaje Crítico/En observación:",
    porcentaje_critico_observacion,
    "%"
)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 9 - SISTEMA INTEGRADO")
print("\033[93m" + '=' * 120 + "\033[0m")

operaciones = [
    ["P01", "C1", "A", 5, 100000, 0, "Entregado", 2, 3],
    ["P02", "C1", "B", 2, 800000, 10, "Pendiente", 0, 4],
    ["P03", "C2", "A", 8, 100000, 5, "Entregado", 5, 3],
    ["P04", "C2", "C", 4, 300000, 0, "Cancelado", 0, 2],
    ["P05", "C3", "B", 3, 800000, 10, "Entregado", 4, 4],
    ["P06", "C3", "C", 6, 300000, 20, "Entregado", 5, 3],
    ["P07", "C1", "A", 0, 100000, 0, "Entregado", 2, 3],
    ["P08", "C4", "D", 2, 1500000, 45, "Pendiente", 0, 5],
    ["P09", "C4", "D", 2, 1500000, 15, "Entregado", 4, 5],
    ["P10", "C2", "B", 1, 800000, 0, "Pendiente", 0, 3]
]


def validar_operacion(unidades, precio, descuento, estado, prometidos):

    valido = True

    if unidades <= 0:
        valido = False

    if precio <= 0:
        valido = False

    if descuento < 0 or descuento > 40:
        valido = False

    if estado != "Entregado" and estado != "Pendiente" and estado != "Cancelado":
        valido = False

    if prometidos <= 0:
        valido = False

    return valido


def calcular_valores(unidades, precio, descuento):

    bruto = unidades * precio

    valor_descuento = bruto * descuento / 100

    neto = bruto - valor_descuento

    return bruto, valor_descuento, neto


recibidos = 0
validos = 0
invalidos = 0

entregados = 0
pendientes = 0
cancelados = 0

bruto_global = 0
descuento_global = 0
ingreso_efectivo = 0

unidades_entregadas = 0

productos_9 = {}
clientes_9 = {}

producto_mas_solicitado = ""
mayor_unidades = 0

producto_mayor_ingreso = ""
mayor_ingreso_producto = 0

cliente_mayor_ingreso = ""
mayor_ingreso_cliente = 0

clientes_cancelaciones = []

pedidos_tardios = 0
dias_retraso_total = 0


for operacion in operaciones:

    codigo = operacion[0]
    cliente = operacion[1]
    producto = operacion[2]
    unidades = operacion[3]
    precio = operacion[4]
    descuento = operacion[5]
    estado = operacion[6]
    reales = operacion[7]
    prometidos = operacion[8]

    recibidos = recibidos + 1

    valido = validar_operacion(
        unidades,
        precio,
        descuento,
        estado,
        prometidos
    )

    if valido == False:

        invalidos = invalidos + 1

        print()
        print("Registro inválido:", codigo)

    else:

        validos = validos + 1

        bruto, valor_descuento, neto = calcular_valores(
            unidades,
            precio,
            descuento
        )

        bruto_global = bruto_global + bruto
        descuento_global = descuento_global + valor_descuento

        if estado == "Entregado":

            entregados = entregados + 1

            ingreso_efectivo = ingreso_efectivo + neto
            unidades_entregadas = unidades_entregadas + unidades

        elif estado == "Pendiente":

            pendientes = pendientes + 1

        else:

            cancelados = cancelados + 1

            if cliente not in clientes_cancelaciones:
                clientes_cancelaciones.append(cliente)

        if producto not in productos_9:

            productos_9[producto] = {
                "Unidades": unidades,
                "Ingreso": 0
            }

        else:

            productos_9[producto]["Unidades"] = (
                productos_9[producto]["Unidades"] + unidades
            )

        if estado == "Entregado":

            productos_9[producto]["Ingreso"] = (
                productos_9[producto]["Ingreso"] + neto
            )

        if cliente not in clientes_9:

            clientes_9[cliente] = {
                "Ingreso": 0,
                "Pedidos": 1
            }

        else:

            clientes_9[cliente]["Pedidos"] = (
                clientes_9[cliente]["Pedidos"] + 1
            )

        if estado == "Entregado":

            clientes_9[cliente]["Ingreso"] = (
                clientes_9[cliente]["Ingreso"] + neto
            )

        if estado == "Entregado":

            if reales <= prometidos:

                print(codigo, "entrega puntual")

            else:

                retraso = reales - prometidos

                pedidos_tardios = pedidos_tardios + 1
                dias_retraso_total = dias_retraso_total + retraso

                print(codigo, "entrega tardía:", retraso, "días")


print()
print("ANÁLISIS POR PRODUCTO")

ingreso_productos = 0

for producto in productos_9:

    unidades = productos_9[producto]["Unidades"]
    ingreso = productos_9[producto]["Ingreso"]

    print()
    print("Producto:", producto)
    print("Unidades solicitadas:", unidades)
    print("Ingreso efectivo:", ingreso)

    ingreso_productos = ingreso_productos + ingreso

    if unidades > mayor_unidades:

        mayor_unidades = unidades
        producto_mas_solicitado = producto

    if ingreso > mayor_ingreso_producto:

        mayor_ingreso_producto = ingreso
        producto_mayor_ingreso = producto


print()
print("ANÁLISIS POR CLIENTE")

ingreso_clientes = 0

for cliente in clientes_9:

    ingreso = clientes_9[cliente]["Ingreso"]
    pedidos = clientes_9[cliente]["Pedidos"]

    print()
    print("Cliente:", cliente)
    print("Pedidos:", pedidos)
    print("Ingreso:", ingreso)

    ingreso_clientes = ingreso_clientes + ingreso

    if ingreso > mayor_ingreso_cliente:

        mayor_ingreso_cliente = ingreso
        cliente_mayor_ingreso = cliente

        
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("RESULTADOS FINALES - PROBLEMA 9")
print("\033[93m" + '=' * 120 + "\033[0m")

print("Registros recibidos:", recibidos)
print("Registros válidos:", validos)
print("Registros inválidos:", invalidos)

print()
print("Estados:")
print("Entregados:", entregados)
print("Pendientes:", pendientes)
print("Cancelados:", cancelados)

print()
print("Valor bruto global:", bruto_global)
print("Descuentos globales:", descuento_global)
print("Ingreso efectivo:", ingreso_efectivo)

print()
print("Unidades entregadas:", unidades_entregadas)

print()
print("Producto más solicitado:", producto_mas_solicitado)
print("Producto de mayor ingreso:", producto_mayor_ingreso)

print()
print("Cliente de mayor ingreso:", cliente_mayor_ingreso)

print()
print("Clientes con cancelaciones:", clientes_cancelaciones)

if pedidos_tardios > 0:

    promedio_retraso = dias_retraso_total / pedidos_tardios

else:

    promedio_retraso = 0

print("Pedidos tardíos:", pedidos_tardios)
print("Promedio días de retraso:", promedio_retraso)

print()
print("VERIFICACIONES")

if validos + invalidos == recibidos:

    print("1. Válidos + inválidos = recibidos: CORRECTO")

else:

    print("1. Válidos + inválidos = recibidos: INCORRECTO")


if entregados + pendientes + cancelados == validos:

    print("2. Estados = válidos: CORRECTO")

else:

    print("2. Estados = válidos: INCORRECTO")


print("Ingreso por productos:", ingreso_productos)
print("Ingreso por clientes:", ingreso_clientes)
print("Ingreso efectivo global:", ingreso_efectivo)

if ingreso_productos == ingreso_clientes and ingreso_clientes == ingreso_efectivo:

    print("3. Ingresos coinciden: CORRECTO")

else:

    print("3. Ingresos coinciden: INCORRECTO")

print('*' * 120)

print("Fin, gracias.")

print('*' * 120)
   