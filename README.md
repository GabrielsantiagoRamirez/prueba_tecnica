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

Ejecuta el script con el siguiente comando:

```bash
python pruba_tecnica.py yellow_tripdata_2022-07.parquet