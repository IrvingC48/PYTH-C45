import matplotlib.pyplot as plt

def crear_grafica_barras(df, column_x, column_y):
    #Crear la fígura y los ejes
    fig, ax = plt.subplots(figsize=(8,5))

    #Generar las barras
    ax.bar(df[column_x], df[column_y], color='skyblue', edgecolor='black')

    #Personalización
    ax.set_title(f'Gráfica de {column_x} por {column_y}')
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)

    #Añadir un grid suave de fondo
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    print('Gráfica generada. Abriendo ventana de visualización...')

    #Mostrar el gráfico
    plt.show()

    return None