#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Genera un dataset exclusivo de CABA a partir de tabla_ciudad_bsas.csv.

Salida:
    caba_codigos_postales.csv

Columnas finales:
    provincia
    id
    localidad
    partido
    municipio
    cp
    latitud
    longitud
    id_prov_mstr
"""

import os
import sys
import csv
import pandas as pd


def main() -> None:
    """
    Punto de entrada principal.
    """

    # Archivo fuente esperado en la misma carpeta que el script
    input_file = "tabla_ciudad_bsas.csv"
    output_file = "caba_codigos_postales.csv"

    # Validación simple de existencia del archivo fuente
    if not os.path.isfile(input_file):
        print(f'Error: no se encontró el archivo "{input_file}" en la carpeta actual.')
        sys.exit(1)

    # Leemos el CSV fuente como texto para evitar conversiones raras
    df = pd.read_csv(input_file, dtype="string")

    # Validamos que existan las columnas mínimas esperadas
    columnas_requeridas = {
        "cod",
        "cod_description",
        "id_provincia",
        "provincia_descripcion",
    }

    faltantes = columnas_requeridas - set(df.columns)
    if faltantes:
        print("Error: faltan columnas requeridas en tabla_ciudad_bsas.csv:")
        for col in sorted(faltantes):
            print(f" - {col}")
        sys.exit(1)

    # Renombramos columnas para alinearlas con el formato nacional
    df = df.rename(
        columns={
            "cod": "cp",
            "cod_description": "localidad",
            "id_provincia": "id_prov_mstr",
            "provincia_descripcion": "provincia",
        }
    )

    # Normalizamos valores fijos para CABA
    # id: usamos el mismo valor que manejaba el script histórico
    # partido: Capital Federal
    # municipio: CABA unificado
    df["id"] = "5001"
    df["partido"] = "CAPITAL FEDERAL"
    df["municipio"] = "CIUDAD AUTONOMA DE BUENOS AIRES"

    # Este CSV auxiliar no trae coordenadas; las dejamos vacías
    df["latitud"] = pd.NA
    df["longitud"] = pd.NA

    # Normalización defensiva de textos
    for col in ["provincia", "localidad", "partido", "municipio", "id", "id_prov_mstr", "cp"]:
        df[col] = df[col].astype("string").str.strip()

    # Forzamos provincia estandarizada para evitar variantes del archivo fuente
    df["provincia"] = "Ciudad Autonoma de Buenos Aires"
    df["id_prov_mstr"] = "02"

    # Reordenamos columnas para que sean compatibles con el CSV nacional
    columnas_finales = [
        "provincia",
        "id",
        "localidad",
        "partido",
        "municipio",
        "cp",
        "latitud",
        "longitud",
        "id_prov_mstr",
    ]
    df = df[columnas_finales]

    # Eliminamos filas sin código postal, por si hubiera basura
    df = df[df["cp"].notna() & (df["cp"].str.strip() != "")].copy()

    # Eliminamos duplicados exactos por si el archivo los trae repetidos
    df = df.drop_duplicates(subset=["provincia", "localidad", "cp"]).reset_index(drop=True)

    # Guardamos salida
    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
    )

    print(f'Se generó "{output_file}" con {len(df)} registros.')


if __name__ == "__main__":
    main()