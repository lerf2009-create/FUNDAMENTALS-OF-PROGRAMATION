
Encabezado = {
    "Nombre_taller": "Desarrollo taller Fundamentos de programación - Taller de entrenamiento de programación y razonamiento lógico",

    "Integrantes": """
Ayda Johanna Bermudez Leon
Luis Eduardo Reyes Fernández
Katherinne Stella Castaneda Rodriguez
""",

    "Docente": "Ivan Dario Rico Arias",

    "Universidad": "Konrad Lorenz - Especialización en analítica de datos e IA",

    "Fecha": "2026-09-16"
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
print('Se definen las variables para realizar las demás pruebas del punto 3 pero se dejan comentadas para no afectar al código, ' \
'para ejecutar cada prueba se deben dejar comentadas las otras dos.')

#Prueba 1. ok
inventario_inicial = 50

movimientos = [
    ["Salida", 30],
    ["Salida", 25],
    ["Entrada", 15],
    ["Salida", 10]
]

#Prueba 2. ok
#inventario_inicial = 20

#movimientos = [
#    ["Entrada", 10],
#    ["Salida", 8],
#    ["Entrada", 0],
#    ["Salida", 5]
#]

#Prueba 3. 
#inventario_inicial = 12

#movimientos = [
#    ["Salida", 5],
#    ["Venta", 3],
#    ["Entrada", -2],
#    ["Salida", 10]
#]

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
#La limitación es que no analiza el contenido implícito en los comentarios completos ni analiza el contexto, solo define favorabilidad o desfavorabilidad según frecuencias.
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

# Creamos la lista con las ventas sugeridas en el ejercicio.
# Cada registro contiene:
# producto, categoría, unidades, precio y porcentaje de descuento.

ventas_6 = [
    ["A", "Tecnología", 8, 120000, 0],
    ["B", "Tecnología", 2, 900000, 10],
    ["A", "Tecnología", 5, 120000, 5],
    ["C", "Accesorios", 15, 40000, 0],
    ["B", "Tecnología", 1, 900000, 15],
    ["D", "Accesorios", 0, 50000, 0]
]

# Creamos contadores para controlar las ventas recibidas,
# las ventas válidas y las ventas inválidas.

ventas_recibidas = 0
ventas_validas = 0
ventas_invalidas = 0

# Creamos acumuladores para calcular los valores globales.

total_bruto = 0
total_descuento = 0
total_neto = 0
#En esta parte se dejan listas las variables que se van a usar durante el programa. Algunas sirven para contar cuántas ventas se revisan,
#cuántas son válidas y cuántas no. Otras sirven para ir sumando el valor bruto, el descuento y el ingreso neto. También se crea el diccionario 
#productos, que más adelante nos ayudará a guardar la información agrupada de cada producto.
# Creamos un diccionario vacío para consolidar la información
# de cada producto. Los productos se incorporan cuando aparecen.

productos = {}

# Recorremos cada venta de la lista.
#Después se utiliza un ciclo for para revisar una por una las ventas que están dentro de la lista. Esto permite que el programa no trabaje 
#todas las ventas al mismo tiempo, sino que analice cada registro por separado.
for venta in ventas_6:

    producto = venta[0]
    categoria = venta[1]
    unidades = venta[2]
    precio = venta[3]
    descuento = venta[4]

    ventas_recibidas = ventas_recibidas + 1

    # Una venta es inválida si las unidades son menores o iguales a cero,
    # el precio es menor o igual a cero o el descuento está fuera de 0 a 40.
    #Luego el programa revisa si la venta tiene datos correctos. Para que una venta sea válida, las unidades y el precio deben ser mayores que cero, y el descuento debe estar entre 0 y 40. Si no cumple alguna de estas condiciones, se considera inválida, se cuenta como venta inválida y no se hacen cálculos con ella.
    #De cada venta se sacan los datos necesarios: el producto, la categoría, las unidades vendidas, el precio y el descuento. Estos datos se toman de acuerdo con la posición que ocupan dentro de cada lista. También se suma uno al contador de ventas recibidas, porque cada vez que el ciclo pasa por una venta significa que esa venta ya fue revisada.

    if unidades <= 0 or precio <= 0 or descuento < 0 or descuento > 40:

        ventas_invalidas = ventas_invalidas + 1

    else:
        #Si la venta sí cumple las condiciones, se cuenta como una venta válida. En ese caso, el programa calcula primero el valor bruto 
        #multiplicando las unidades por el precio. Luego calcula cuánto vale el descuento y finalmente obtiene el valor neto, que es lo que 
        #queda después de restar el descuento.
        ventas_validas = ventas_validas + 1

        # Calculamos valor bruto, descuento y valor neto.

        bruto = unidades * precio
        valor_descuento = bruto * descuento / 100
        neto = bruto - valor_descuento

        # Acumulamos los valores globales.

        total_bruto = total_bruto + bruto
        total_descuento = total_descuento + valor_descuento
        total_neto = total_neto + neto
        #Después de calcular los valores de una venta válida, esos resultados se van sumando a los totales generales. Así el programa 
        #puede ir acumulando poco a poco el total bruto, el total descontado y el total neto de todas las ventas que sí fueron aceptadas.
        #Si el producto aparece por primera vez lo agregamos al diccionario.

        if producto not in productos:

            productos[producto] = {
                "Categoria": categoria,
                "Unidades": unidades,
                "Ingreso": neto,
                "Operaciones": 1
            }
        #Más adelante, el programa revisa si el producto de la venta ya está guardado en el diccionario. Si no está, se crea por primera vez con su categoría, sus unidades, su ingreso neto y una operación. Esto sirve para empezar a guardar la información de ese producto.
        #Si el producto ya existía en el diccionario, entonces no se vuelve a crear. En ese caso solo se actualizan sus datos, sumando las nuevas unidades, el nuevo ingreso neto y aumentando en uno la cantidad de operaciones realizadas para ese producto.
        else:

            # Si el producto ya existe acumulamos unidades,
            # ingreso neto y número de operaciones.

            productos[producto]["Unidades"] = productos[producto]["Unidades"] + unidades
            productos[producto]["Ingreso"] = productos[producto]["Ingreso"] + neto
            productos[producto]["Operaciones"] = productos[producto]["Operaciones"] + 1


# Mostramos los resultados generales.

print()
print("Ventas recibidas:", ventas_recibidas)
print("Ventas válidas:", ventas_validas)
print("Ventas inválidas:", ventas_invalidas)
print("Valor bruto:", total_bruto)
print("Descuento:", total_descuento)
print("Ingreso neto:", total_neto)

print()
print("CONSOLIDADO POR PRODUCTO")
#Cuando termina el recorrido de todas las ventas, el programa muestra un resumen general. En ese resumen aparecen las ventas recibidas, las válidas, las inválidas, el valor bruto total, el descuento total y el ingreso neto total. Esto permite ver el resultado general del proceso.
#Después se crean algunas variables adicionales para analizar los productos. Estas variables sirven para guardar cuál fue el producto con más unidades vendidas, cuál generó mayor ingreso y cuánto ingreso se acumula al sumar todos los productos del consolidado.
# Variables para determinar el producto con más unidades
# y el producto con mayor ingreso.

producto_mas_unidades = ""
mayor_unidades = 0

producto_mayor_ingreso = ""
mayor_ingreso = 0

# Acumulador para verificar el ingreso consolidado.

ingreso_consolidado = 0

# Recorremos el diccionario de productos.

for producto in productos:
    #Luego se usa otro ciclo for, pero esta vez para recorrer los productos que quedaron guardados en el diccionario. Por cada producto se 
    #toman sus unidades, su ingreso y sus operaciones, y se muestran estos datos como parte del consolidado.
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

    # Identificamos el producto con mayor número de unidades.

    if unidades > mayor_unidades:

        mayor_unidades = unidades
        producto_mas_unidades = producto

    # Identificamos el producto con mayor ingreso.

    if ingreso > mayor_ingreso:

        mayor_ingreso = ingreso
        producto_mayor_ingreso = producto
    #Mientras se revisa cada producto, el programa también compara sus unidades y su ingreso con los mayores valores encontrados hasta ese 
    #momento. Si encuentra un producto con más unidades o con mayor ingreso, actualiza la información para dejar guardado ese producto como 
    #el más destacado.
    # Calculamos la participación de cada producto
    # dentro del ingreso neto total.

    if total_neto > 0:

        participacion = ingreso * 100 / total_neto

    else:

        participacion = 0
    #También se calcula qué porcentaje representa cada producto dentro del ingreso neto total. Para eso se divide el ingreso 
    #del producto entre el total neto y se multiplica por 100. Si el total neto fuera cero, el programa deja la participación 
    #en cero para evitar un error en la división.
    print("Participación en ingreso:", participacion, "%")


print()
print("Producto con más unidades:", producto_mas_unidades)
print("Producto con mayor ingreso:", producto_mayor_ingreso)

print("Ingreso global:", total_neto)
print("Ingreso consolidado:", ingreso_consolidado)

# Verificamos que el ingreso neto consolidado por producto
# sea igual al ingreso neto global.

if total_neto == ingreso_consolidado:

    print("VERIFICACIÓN CORRECTA")

else:

    print("VERIFICACIÓN INCORRECTA")
    #Al final, el programa compara el ingreso neto total con el ingreso consolidado por producto. Esta comparación sirve para confirmar 
    #que los datos agrupados en el diccionario coinciden con los totales generales. Si los dos valores son iguales, la verificación sale 
    #correcta; si no, significa que hubo alguna diferencia en la acumulación.

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print()
print("\033[93m" + '=' * 120 + "\033[0m")
print("PROBLEMA 7 - GESTIÓN DE PEDIDOS Y NIVEL DE CUMPLIMIENTO")
print("\033[93m" + '=' * 120 + "\033[0m")

# Creamos la lista con los pedidos sugeridos.
# Cada registro contiene:
# cliente, unidades solicitadas, unidades entregadas,
# días prometidos, días reales y estado del pago.

pedidos_7 = [
    ["C1", 10, 10, 3, 3, "Pagado"],
    ["C1", 8, 6, 4, 4, "Pagado"],
    ["C2", 5, 5, 2, 4, "Pagado"],
    ["C2", 7, 0, 3, 3, "Pagado"],
    ["C3", 6, 6, 3, 2, "Rechazado"],
    ["C3", 4, 4, 2, 2, "Pendiente"]
]

# Acumuladores de unidades solicitadas y entregadas.

solicitadas_total = 0
entregadas_total = 0

# Contadores para cada categoría.

cumplidos = 0
parciales = 0
incumplidos = 0

# Acumuladores para calcular los retrasos.

dias_retraso_total = 0
pedidos_tardios = 0

# Diccionario para generar el resumen por cliente.

clientes = {}

# Lista para guardar los clientes con al menos un incumplimiento.

clientes_incumplidos = []

# Recorremos cada pedido.

for pedido in pedidos_7:

    cliente = pedido[0]
    solicitadas = pedido[1]
    entregadas = pedido[2]
    prometidos = pedido[3]
    reales = pedido[4]
    pago = pedido[5]

    # Acumulamos las unidades solicitadas y entregadas.

    solicitadas_total = solicitadas_total + solicitadas
    entregadas_total = entregadas_total + entregadas

    # Calculamos el porcentaje entregado.
    # La validación evita una división entre cero.

    if solicitadas > 0:

        porcentaje_entregado = entregadas * 100 / solicitadas

    else:

        porcentaje_entregado = 0

    # Primero se determina si el pedido es Incumplido.
    # Es incumplido cuando no se entregan unidades,
    # el pago es Rechazado o se entregan más unidades
    # de las solicitadas.

    if entregadas == 0 or pago == "Rechazado" or entregadas > solicitadas:

        categoria = "Incumplido"
        incumplidos = incumplidos + 1

        # Guardamos una sola vez al cliente que tenga incumplimientos.

        if cliente not in clientes_incumplidos:

            clientes_incumplidos.append(cliente)

    # Si no fue incumplido, se considera Cumplido
    # cuando se entrega el 100 %, dentro del plazo
    # y el pago se encuentra Pagado.

    elif entregadas == solicitadas and reales <= prometidos and pago == "Pagado":

        categoria = "Cumplido"
        cumplidos = cumplidos + 1

    # Los demás pedidos procesables se clasifican
    # como Cumplimiento parcial.

    else:

        categoria = "Cumplimiento parcial"
        parciales = parciales + 1

    # Calculamos el retraso cuando los días reales
    # son superiores a los prometidos.

    if reales > prometidos:

        retraso = reales - prometidos
        pedidos_tardios = pedidos_tardios + 1
        dias_retraso_total = dias_retraso_total + retraso

    else:

        retraso = 0

    # Mostramos el resultado individual del pedido.

    print()
    print("Cliente:", cliente)
    print("Porcentaje entregado:", porcentaje_entregado, "%")
    print("Categoría:", categoria)
    print("Días de retraso:", retraso)

    # Si el cliente aparece por primera vez,
    # creamos su registro dentro del diccionario.

    if cliente not in clientes:

        clientes[cliente] = {
            "Pedidos": 1,
            "Cumplidos": 0,
            "Parciales": 0,
            "Incumplidos": 0
        }

    else:

        clientes[cliente]["Pedidos"] = clientes[cliente]["Pedidos"] + 1

    # Actualizamos la categoría del pedido
    # dentro del resumen del cliente.

    if categoria == "Cumplido":

        clientes[cliente]["Cumplidos"] = clientes[cliente]["Cumplidos"] + 1

    elif categoria == "Cumplimiento parcial":

        clientes[cliente]["Parciales"] = clientes[cliente]["Parciales"] + 1

    else:

        clientes[cliente]["Incumplidos"] = clientes[cliente]["Incumplidos"] + 1


# Mostramos los indicadores generales.

print()
print("Pedidos totales:", len(pedidos_7))
print("Cumplidos:", cumplidos)
print("Parciales:", parciales)
print("Incumplidos:", incumplidos)

print("Unidades solicitadas:", solicitadas_total)
print("Unidades entregadas:", entregadas_total)

# Decisión de diseño:
# El porcentaje global de cumplimiento se calcula dividiendo
# las unidades entregadas entre las unidades solicitadas.

if solicitadas_total > 0:

    porcentaje_global = entregadas_total * 100 / solicitadas_total

else:

    porcentaje_global = 0

print("Porcentaje global de cumplimiento:", porcentaje_global, "%")

# El promedio de retraso considera únicamente
# los pedidos que presentaron retraso.

if pedidos_tardios > 0:

    promedio_retraso = dias_retraso_total / pedidos_tardios

else:

    promedio_retraso = 0

print("Promedio de días de retraso:", promedio_retraso)
print("Clientes con incumplimientos:", clientes_incumplidos)

# Mostramos el resumen por cliente.

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


# Función para asignar el puntaje correspondiente
# al porcentaje de entregas a tiempo.
# Recibe: porcentaje de puntualidad del proveedor.
# Devuelve: 30, 20, 10 o 0 puntos.
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


# Función para asignar el puntaje correspondiente
# al porcentaje de pedidos completos.
# Recibe: porcentaje de pedidos completos.
# Devuelve: 30, 20, 10 o 0 puntos.

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


# Función para evaluar el porcentaje de productos rechazados.
# Recibe: porcentaje de productos rechazados.
# Devuelve: 30, 20, 10 o 0 puntos.

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


# Función para asignar puntos según la cantidad de incidentes.
# Recibe: número de incidentes del proveedor.
# Devuelve: 10, 5 o 0 puntos.

def puntos_incidentes(incidentes):

    if incidentes == 0:

        puntos = 10

    elif incidentes == 1:

        puntos = 5

    else:

        puntos = 0

    return puntos


# Función para calcular el puntaje total.
# Recibe: los cuatro puntajes obtenidos en los criterios.
# Devuelve: la suma de los cuatro puntajes.

def calcular_puntaje_total(p1, p2, p3, p4):

    puntaje_total = p1 + p2 + p3 + p4

    return puntaje_total


# Función para determinar la categoría final del proveedor.
# Recibe: puntaje total, meses de antigüedad,
# porcentaje de rechazo y cantidad de incidentes.
# Devuelve: Estratégico, Confiable,
# En observación o Crítico.

def clasificar_proveedor(puntaje, meses, rechazo, incidentes):

    # Primero obtenemos la categoría general de acuerdo con el puntaje.

    if puntaje >= 90:

        categoria = "Estratégico"

    elif puntaje >= 75:

        categoria = "Confiable"

    elif puntaje >= 60:

        categoria = "En observación"

    else:

        categoria = "Crítico"

    # Luego aplicamos las restricciones obligatorias.
    # Un proveedor con menos de 6 meses no puede quedar Estratégico.

    if meses < 6 and categoria == "Estratégico":

        categoria = "Confiable"

    # Un porcentaje de rechazos superior al 8 %
    # obliga a clasificar al proveedor como Crítico.

    if rechazo > 8:

        categoria = "Crítico"

    # Con 3 o más incidentes el proveedor no puede quedar
    # por encima de En observación.
    # Si ya era Crítico, se mantiene como Crítico.

    if incidentes >= 3:

        if categoria == "Estratégico" or categoria == "Confiable":

            categoria = "En observación"

    return categoria


proveedores = [
    ["P1", 95, 98, 1, 0, 30],
    ["P2", 94.9, 90, 2, 1, 18],
    ["P3", 85, 89.9, 4, 0, 12],
    ["P4", 98, 99, 0.5, 0, 4],
    ["P5", 96, 99, 9, 0, 36],
    ["P6", 96, 99, 1, 3, 36]
]

# Contadores por categoría.

#Se crean los contadores para realizar la acumulación de los resultados solicitados:
conteo_estrategico = 0
conteo_confiable = 0
conteo_observacion = 0
conteo_critico = 0

# Acumuladores utilizados para calcular
# máximo, mínimo, promedio y porcentajes.

total_puntajes = 0
mayor_puntaje = 0
menor_puntaje = 100

cantidad_proveedores = 0

# Recorremos cada proveedor para calcular los cuatro puntajes,
# obtener el puntaje total y determinar su categoría.

#Se invoca la función for para crear temporalmente las variables por cada índice 
for proveedor in proveedores:

    nombre = proveedor[0]
    puntualidad = proveedor[1]
    completo = proveedor[2]
    rechazo = proveedor[3]
    incidentes = proveedor[4]
    meses = proveedor[5]

    # Invocamos las funciones de cada criterio.

    p1 = puntos_puntualidad(puntualidad)
    p2 = puntos_completos(completo)
    p3 = puntos_rechazos(rechazo)
    p4 = puntos_incidentes(incidentes)

    # Calculamos el puntaje total mediante una función.

    puntaje = calcular_puntaje_total(p1, p2, p3, p4)

    # Determinamos la categoría final mediante una función.

    categoria = clasificar_proveedor(
        puntaje,
        meses,
        rechazo,
        incidentes
    )

    # Acumulamos puntajes y cantidad de proveedores.

    total_puntajes = total_puntajes + puntaje
    cantidad_proveedores = cantidad_proveedores + 1

    # Identificamos puntaje máximo y mínimo.

    if puntaje > mayor_puntaje:

        mayor_puntaje = puntaje

    if puntaje < menor_puntaje:

        menor_puntaje = puntaje

    # Contamos proveedores por categoría.

    if categoria == "Estratégico":

        conteo_estrategico = conteo_estrategico + 1

    elif categoria == "Confiable":

        conteo_confiable = conteo_confiable + 1

    elif categoria == "En observación":

        conteo_observacion = conteo_observacion + 1

    else:

        conteo_critico = conteo_critico + 1

    # Mostramos el resultado individual de cada proveedor.

    print()
    print("Proveedor:", nombre)
    print("Puntualidad:", p1)
    print("Completos:", p2)
    print("Rechazos:", p3)
    print("Incidentes:", p4)
    print("Puntaje total:", puntaje)
    print("Categoría:", categoria)


# Calculamos promedio y porcentaje de proveedores
# clasificados como Crítico o En observación.

if cantidad_proveedores > 0:

    promedio_puntaje = total_puntajes / cantidad_proveedores

    porcentaje_critico_observacion = (
        (conteo_critico + conteo_observacion)
        * 100
        / cantidad_proveedores
    )

else:

    promedio_puntaje = 0
    porcentaje_critico_observacion = 0


# Mostramos los resultados generales.

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
print("PROBLEMA 9 - SISTEMA INTEGRADO DE ANÁLISIS DE OPERACIONES")
print("\033[93m" + '=' * 120 + "\033[0m")

# Creamos la lista con las operaciones sugeridas.
# Cada registro contiene:
# código, cliente, producto, unidades, precio,
# descuento, estado, días reales y días prometidos.

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


# Función para validar si una operación puede procesarse.
# Recibe: unidades, precio, descuento, estado y días prometidos.
# Devuelve: True si el registro es válido
# o False si incumple alguna regla.

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


# Función para calcular los valores comerciales.
# Recibe: unidades, precio y porcentaje de descuento.
# Devuelve: valor bruto, descuento y valor neto.

def calcular_valores(unidades, precio, descuento):

    bruto = unidades * precio

    valor_descuento = bruto * descuento / 100

    neto = bruto - valor_descuento

    return bruto, valor_descuento, neto


# Contadores generales.

recibidos = 0
validos = 0
invalidos = 0

# Contadores por estado.

entregados = 0
pendientes = 0
cancelados = 0

# Acumuladores de valores.

bruto_global = 0
descuento_global = 0
ingreso_efectivo = 0

# Acumulador de unidades efectivamente entregadas.

unidades_entregadas = 0

# Diccionarios para consolidar información
# por producto y por cliente.

productos_9 = {}
clientes_9 = {}

# Variables para identificar productos y clientes destacados.

producto_mas_solicitado = ""
mayor_unidades = 0

producto_mayor_ingreso = ""
mayor_ingreso_producto = 0

cliente_mayor_ingreso = ""
mayor_ingreso_cliente = 0

# Lista para guardar clientes con cancelaciones.

clientes_cancelaciones = []

# Indicadores de puntualidad.

entregas_puntuales = 0
pedidos_tardios = 0
dias_retraso_total = 0


# Recorremos todas las operaciones.

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

    # Validamos cada operación mediante la función.

    valido = validar_operacion(
        unidades,
        precio,
        descuento,
        estado,
        prometidos
    )

    # Si la operación es inválida
    # solamente aumentamos el contador correspondiente.

    if valido == False:

        invalidos = invalidos + 1

        print()
        print("Registro inválido:", codigo)

    else:

        validos = validos + 1

        # Calculamos los valores comerciales
        # de cada registro válido.

        bruto, valor_descuento, neto = calcular_valores(
            unidades,
            precio,
            descuento
        )

        # El valor bruto y los descuentos consideran
        # todos los pedidos válidos.

        bruto_global = bruto_global + bruto
        descuento_global = descuento_global + valor_descuento

        # Clasificamos cada pedido según su estado.

        if estado == "Entregado":

            entregados = entregados + 1

            # El ingreso efectivo y las unidades entregadas
            # solamente consideran los pedidos Entregado.

            ingreso_efectivo = ingreso_efectivo + neto
            unidades_entregadas = unidades_entregadas + unidades

        elif estado == "Pendiente":

            pendientes = pendientes + 1

        else:

            cancelados = cancelados + 1

            # Guardamos una sola vez cada cliente
            # que tenga pedidos cancelados.

            if cliente not in clientes_cancelaciones:

                clientes_cancelaciones.append(cliente)


        # Consolidamos la información por producto.

        if producto not in productos_9:

            productos_9[producto] = {
                "Unidades": unidades,
                "Ingreso": 0
            }

        else:

            productos_9[producto]["Unidades"] = (
                productos_9[producto]["Unidades"] + unidades
            )

        # El ingreso por producto solamente considera
        # los pedidos Entregado.

        if estado == "Entregado":

            productos_9[producto]["Ingreso"] = (
                productos_9[producto]["Ingreso"] + neto
            )


        # Consolidamos la información por cliente.

        if cliente not in clientes_9:

            clientes_9[cliente] = {
                "Ingreso": 0,
                "Pedidos": 1
            }

        else:

            clientes_9[cliente]["Pedidos"] = (
                clientes_9[cliente]["Pedidos"] + 1
            )

        # El ingreso por cliente solamente considera
        # los pedidos Entregado.

        if estado == "Entregado":

            clientes_9[cliente]["Ingreso"] = (
                clientes_9[cliente]["Ingreso"] + neto
            )


        # Analizamos la puntualidad únicamente
        # en los pedidos Entregado.

        if estado == "Entregado":

            if reales <= prometidos:

                entregas_puntuales = entregas_puntuales + 1

                print(codigo, "entrega puntual")

            else:

                retraso = reales - prometidos

                pedidos_tardios = pedidos_tardios + 1
                dias_retraso_total = dias_retraso_total + retraso

                print(
                    codigo,
                    "entrega tardía:",
                    retraso,
                    "días"
                )


# ANÁLISIS POR PRODUCTO

print()
print("ANÁLISIS POR PRODUCTO")

ingreso_productos = 0

# Recorremos el consolidado por producto.

for producto in productos_9:

    unidades = productos_9[producto]["Unidades"]
    ingreso = productos_9[producto]["Ingreso"]

    print()
    print("Producto:", producto)
    print("Unidades solicitadas:", unidades)
    print("Ingreso efectivo:", ingreso)

    ingreso_productos = ingreso_productos + ingreso

    # Identificamos el producto más solicitado.

    if unidades > mayor_unidades:

        mayor_unidades = unidades
        producto_mas_solicitado = producto

    # Identificamos el producto con mayor ingreso.

    if ingreso > mayor_ingreso_producto:

        mayor_ingreso_producto = ingreso
        producto_mayor_ingreso = producto


# ANÁLISIS POR CLIENTE

print()
print("ANÁLISIS POR CLIENTE")

ingreso_clientes = 0

# Recorremos el consolidado por cliente.

for cliente in clientes_9:

    ingreso = clientes_9[cliente]["Ingreso"]
    pedidos = clientes_9[cliente]["Pedidos"]

    print()
    print("Cliente:", cliente)
    print("Pedidos:", pedidos)
    print("Ingreso:", ingreso)

    ingreso_clientes = ingreso_clientes + ingreso

    # Identificamos el cliente con mayor ingreso efectivo.

    if ingreso > mayor_ingreso_cliente:

        mayor_ingreso_cliente = ingreso
        cliente_mayor_ingreso = cliente


#---------------------------------------------------------------------------------------------------------------------
# RESULTADOS FINALES - PROBLEMA 9
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

# Calculamos el promedio de días de retraso
# solamente entre las entregas tardías.

if pedidos_tardios > 0:

    promedio_retraso = dias_retraso_total / pedidos_tardios

else:

    promedio_retraso = 0

print("Entregas puntuales:", entregas_puntuales)
print("Pedidos tardíos:", pedidos_tardios)
print("Promedio días de retraso:", promedio_retraso)


# VERIFICACIONES

print()
print("VERIFICACIONES")

# Verificación 1:
# válidos + inválidos debe ser igual a recibidos.

if validos + invalidos == recibidos:

    print("1. Válidos + inválidos = recibidos: CORRECTO")

else:

    print("1. Válidos + inválidos = recibidos: INCORRECTO")


# Verificación 2:
# Entregado + Pendiente + Cancelado
# debe ser igual al número de registros válidos.

if entregados + pendientes + cancelados == validos:

    print("2. Estados = válidos: CORRECTO")

else:

    print("2. Estados = válidos: INCORRECTO")


# Verificación 3:
# ingreso por productos, ingreso por clientes
# e ingreso efectivo global deben coincidir.

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
