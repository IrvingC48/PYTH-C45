from generador_datos import obtener_df
from graficador_plt import crear_grafica_barras

def main():
    print("---Iniciando App---")

    try:
        #1 Obtener los datos del primer modulo
        df_diabetes = obtener_df()

        #2 Generar una validación simple
        if not df_diabetes.empty:

            #3 Pasar el df al modulo de graficación
            crear_grafica_barras(df_diabetes, 'Glucose', 'Insulin')
        else:
            print("Error: El Dataframe está vacío.")

    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')

    print('---Fin de la ejecución---')

if __name__ == "__main__":
    main()