
ingreso_mensual = 81000
gasto_mensual = 90000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print ('estás en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print ('vas bien, te alcanza para otros gastos')
    elif ingreso_mensual - gasto_mensual > 50000:
        print('eres todo un ahorrador')
    else:
        print('estas gastando por demas, no sabemos si te alcanza')