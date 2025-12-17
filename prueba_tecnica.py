import pandas as pd

#Salida 1: Ultima Ubicación conocida

documento = pd.read_parquet('yellow_tripdata_2022-07.parquet')

print(documento)
print("--------------------------------")
print(documento.head())

print("Columnas y tipos de datos:")
print(documento.dtypes)

columnas = ['tpep_pickup_datetime','PULocationID'] #'pickup_latitude','pickup_longitude']
seleccionar_columnas = documento[columnas].copy()
print(seleccionar_columnas)

print("Generando reporte de última ubicación...")
ultima_ubicacion = seleccionar_columnas.loc[
    seleccionar_columnas.groupby('PULocationID')['tpep_pickup_datetime'].idxmax()
]

print('Ultima ubicacion')
print(ultima_ubicacion)

ultima_ubicacion = ultima_ubicacion.rename(
    columns={
        'PULocationID': 'vehicle_id',
        'tpep_pickup_datetime': 'ultima_timestamp',
        #'pickup_latitude': 'ultima_latitud',
        #'pickup_longitude': 'ultima_longitud',
    }
)

ultima_ubicacion.to_csv('ultima_ubicacion.csv', index=False)
print('Ubicacion final guardada de manera exitosa')

#Salida 2: Reporte de viajes por hora
print ('Generando reporte de viajes por hora...')
documento['hora_del_dia'] = documento['tpep_pickup_datetime'].dt.hour

viajes_por_hora =(
        documento.groupby('hora_del_dia')
            .size()
            .reset_index(name='total_viajes')
    )

print(viajes_por_hora)

viajes_por_hora.to_csv('viajes_por_hora.csv', index=False)