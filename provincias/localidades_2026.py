#!/usr/bin/python3
from requests import Session
import pandas as pd
import csv
import os
import time
import json

print(
    'Este script genera un csv con las localidades de las provincias de Argentina '
    'a partir del formulario presente en la pagina de Correo Argentino en la parte '
    'de "consulta de codigo postal".'
)

cwd = os.getcwd()
pwd = os.path.join(cwd, 'localidades_cp_maestro.csv')

if os.path.isfile(pwd):
    os.remove(pwd)

prov_cod_correo = {
    "Ciudad Autonoma de Buenos Aires": "C",
    "Buenos Aires": "B",
    "Catamarca": "K",
    "Chaco": "H",
    "Chubut": "U",
    "Cordoba": "X",
    "Corrientes": "W",
    "Entre Rios": "E",
    "Formosa": "P",
    "Jujuy": "Y",
    "La Pampa": "L",
    "La Rioja": "F",
    "Mendoza": "M",
    "Misiones": "N",
    "Neuquen": "Q",
    "Rio Negro": "R",
    "Salta": "A",
    "San Juan": "J",
    "San Luis": "D",
    "Santa Cruz": "Z",
    "Santa Fe": "S",
    "Santiago del Estero": "G",
    "Tierra del Fuego": "V",
    "Tucuman": "T"
}

tmp_csv = os.path.join(cwd, 'localidades_cp.csv')
if os.path.isfile(tmp_csv):
    os.remove(tmp_csv)

url = 'https://www.correoargentino.com.ar/sites/all/modules/custom/ca_forms/api/wsFacade.php'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.correoargentino.com.ar/formularios/cpa',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

with open(tmp_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'provincia', 'id', 'localidad', 'partido', 'municipio',
        'cp', 'latitud', 'longitud'
    ])

    for provincia, cod in prov_cod_correo.items():
        data = {
            'action': 'localidades',
            'localidad': 'none',
            'calle': '',
            'altura': '',
            'provincia': cod
        }

        ok = False

        for intento in range(1, 4):
            try:
                with Session() as s:
                    resp = s.post(url, headers=headers, data=data, timeout=30)

                body = resp.text.strip()
                print(f'{provincia} | intento {intento} | status {resp.status_code}')

                if resp.status_code != 200:
                    print(f'  HTTP no esperado para {provincia}')
                    time.sleep(2)
                    continue

                if body.lower() == 'error':
                    print(f'  backend devolvio "error" para {provincia}')
                    time.sleep(2)
                    continue

                body_clean = resp.text.encode('utf-8').decode('utf-8-sig').strip()
                rows = json.loads(body_clean)
                print(f'  {len(rows)} registros')

                for item in rows:
                    writer.writerow([
                        provincia,
                        item.get('id'),
                        item.get('nombre'),
                        item.get('partido'),
                        item.get('municipio'),
                        item.get('cp'),
                        item.get('latitud'),
                        item.get('longitud')
                    ])

                ok = True
                break

            except Exception as e:
                print(f'  fallo en {provincia}: {e}')
                time.sleep(2)

        if not ok:
            print(f'  no se pudo extraer {provincia}')

        time.sleep(1.5)

df = pd.read_csv(tmp_csv, dtype='string')

dtmast = {
    'provincia': [
        'Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Cordoba',
        'Corrientes', 'Entre Rios', 'Formosa', 'Jujuy', 'La Pampa',
        'La Rioja', 'Mendoza', 'Misiones', 'Neuquen', 'Rio Negro',
        'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe',
        'Santiago del Estero', 'Tierra del Fuego', 'Tucuman',
        'Ciudad Autonoma de Buenos Aires'
    ],
    'id_prov_mstr': [
        '06', '10', '22', '26', '14', '18', '30', '34', '38', '42',
        '46', '50', '54', '58', '62', '66', '70', '74', '78', '82',
        '86', '94', '90', '02'
    ]
}

dfprov = pd.DataFrame.from_dict(dtmast, orient='columns')
dfprov['id_prov_mstr'] = dfprov['id_prov_mstr'].astype('string')

local_con_id = pd.merge(df, dfprov, on='provincia', how='left')

df_caba = pd.read_csv(
    'tabla_ciudad_bsas.csv',
    dtype={'id_provincia': 'string'}
).rename(columns={
    'cod': 'cp',
    'cod_description': 'localidad',
    'id_provincia': 'id_prov_mstr',
    'provincia_descripcion': 'provincia'
})

df_final = pd.concat([local_con_id, df_caba], sort=False)
df_final['id'] = df_final['id'].astype('string')
df_final['id_prov_mstr'] = df_final['id_prov_mstr'].astype('string')

df_final.loc[df_final['id_prov_mstr'] == '02', 'localidad'] = 'Ciudad Autonoma de Buenos Aires'
df_final.loc[df_final['id_prov_mstr'] == '02', 'id'] = '5001'

df_final.to_csv(pwd, index=False, quotechar='"', quoting=csv.QUOTE_ALL)

if os.path.isfile(tmp_csv):
    os.remove(tmp_csv)

print('Se ha generado el csv')