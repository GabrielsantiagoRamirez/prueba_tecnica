## Descripción

Este proyecto procesa datos de viajes en taxi a partir de un archivo parquet y genera dos reportes
1. La última ubicación conocida por vehículo.
2. El total de viajes iniciados por hora del dia

## Herramientas utilizadas

- Python 3.14.0
- pandas
- pyarrow
- fastparquet

## Instlación de dependencias

Ejecuta el script con el siguiente comando:

```bash
pip install -r requirements.txt

## Ejecución

Ejecuta el script con el siguiente comando

```bash
python pruba_tecnica.py yellow_tripdata_2022-07.parquet

## Archivos generados

El script genera los siguientes archivos:

- 'ultima_ubicacion.csv'
   Contiene la última ubicación conocida de cada vehículo, basada en el 'tpep_pickupc_datetime'.

- 'viajes_por_hora.csv'
   Contiene el total de viajes iniciados por cada hora del dia (0 a 23).