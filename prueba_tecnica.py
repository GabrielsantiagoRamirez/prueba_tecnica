import pandas as pd

#Salida 1: Ultima Ubicación conocida

document= pd.read_parquet('yellow_tripdata_2022-07.parquet')

columns = ['tpep_pickup_datetime','PULocationID', 'pickup_latitude','pickup_longitude']
select_columns = document.reindex(columns=columns)

print("Generando reporte de última ubicación...")
last_location = select_columns.loc[
    select_columns.groupby('PULocationID')['tpep_pickup_datetime'].idxmax()
]

last_location = last_location.rename(
    columns={
        'PULocationID': 'vehicle_id',
        'tpep_pickup_datetime': 'ultimo_timestamp',
        'pickup_latitude': 'ultima_latitud',
        'pickup_longitude': 'ultima_longitud',
    }
)

last_location.to_csv('ultima_ubicacion.csv', index=False)
print('Ubicacion final guardada de manera exitosa')

#Salida 2: Reporte de viajes por hora

print ('Generando reporte de viajes por hora...')
document['hora_del_dia'] = document['tpep_pickup_datetime'].dt.hour

trips_per_hour =(
        document.groupby('hora_del_dia')
            .size()
            .reset_index(name='total_viajes')
    )

trips_per_hour.to_csv('viajes_por_hora.csv', index=False)

print('Reporte de viajes por hora guardado de manera exitosa')