import tasas

def realizar_conversion(monto, moneda_origen, moneda_destino):
    """
    Convierte un monto de una moneda a otra moneda usando el diccionario de tasas.
    Fómula: (monto / tasas origen) * tasa destino
    """

    #Verificar que exista la moneda
    if moneda_origen not in tasas.TASAS or moneda_destino not in tasas.TASAS:
        return None

    valor_en_usd = monto / tasas.TASAS[moneda_origen]
    valor_final = valor_en_usd * tasas.TASAS[moneda_destino]

    return round(valor_final)