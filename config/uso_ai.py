import pandas as pd
import operator
import re
import pyodbc
def clean_text(txt):
    txt = re.sub("[^a-záéíóúñüäë]", " ", txt.lower())
    txt = re.sub(' +',' ', txt)
    return txt.strip().split()

def df_to_dict(df, key_column, val_column):
    """convierte dos pandas series en un diccionario"""
    xkey = df[key_column].tolist()
    xval = df[val_column].tolist()
    return dict(zip(xkey,xval))

def get_gender2(names):
    names = clean_text(names)
    names = [x for x in names if gender_list.get(x,'a') != 'a']
    gender ={'m':0, 'f':0, 'a':0}
    for i, name in enumerate(names):
        g = gender_list.get(name,'a')
        gender[g] += 1
        gender[g] += 2 if len(names) > 1 and i == 0 and g != 'a' else 0
    gender['a'] = 0 if (gender['f']+gender['m']) > 0 else 1
    return max(gender.items(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
    server = 'DESKTOP-C4PE698'#'tcp:myserver.database.windows.net'
    database = 'dblamorenita'
    username = ''
    password = ''
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + password)
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (server, database, username, password))
    cursor = conn.cursor()
    #res = pd.read_sql("select  scli_codigo IdCliente, scli_nombre nombre, scli_direccion direccion from [dblamorenita].sis_clientes", con=conn)
    path = 'https://www.dropbox.com/s/edm5383iffurv4x/nombres.csv?dl=1'
    gender_list = pd.read_csv(path)
    gender_list = df_to_dict(gender_list, key_column='nombre', val_column='genero')
    # clientes = cursor.execute("select  scli_codigo IdCliente, scli_nombre nombre, scli_direccion direccion from [dblamorenita].sis_clientes")
    # clients = clientes.fetchall()
    # for cliente in clients:
    #     idCliente = cliente[0]
    #     nombre = cliente[1]
    #     genero = get_gender2(nombre).upper()
    #     sql = f"update [dblamorenita].sis_clientes set scli_genero = '{genero}' where scli_codigo='{idCliente}'"
    #     cursor.execute(sql)
    #     conn.commit()

    # sql_clientes = """
    #     select
    #         scli_codigo IdCliente,
    #         scli_direccion direccion
    #     from
    #        [dblamorenita].sis_clientes  where scli_direccion=''
    # """
    # result = cursor.execute(sql_clientes)
    # clientes = result.fetchall()
    # for cliente in clientes:
    #     sql_direccion = """select top(1)
    #             scli_direccion direccion
    #         from
    #            [dblamorenita].sis_clientes
    #         where scli_direccion!='' and len(scli_direccion)<30
    #         group by
    #            scli_direccion
    #         order by NEWID()
    #         """
    #     result2 = cursor.execute(sql_direccion)
    #     direccion = result2.fetchone()
    #     sql_update = f"""update [dblamorenita].sis_clientes set scli_direccion = '{direccion[0]}' where scli_codigo='{cliente[0]}'"""
    #     cursor.execute(sql_update)
    #     conn.commit()
    import random
    from datetime import datetime

    inicio = datetime(1980, 1, 1)
    final = datetime(2003, 12, 31)

    # results = cursor.execute("select  scli_codigo IdCliente, scli_fecha_nac fecha_nacimiento from [dblamorenita].sis_clientes")
    # clientes = results.fetchall()
    # for cliente in clientes:
    #     random_date = inicio + (final - inicio) * random.random()
    #     fecha_nacimiento = random_date.date().__str__()
    #     sql_update = f"""update [dblamorenita].sis_clientes set scli_fecha_nac = '{fecha_nacimiento}' where scli_codigo='{cliente[0]}'"""
    #     cursor.execute(sql_update)
    #     conn.commit()
    #
    # results = cursor.execute("""select
    #                             susr_codigo IdEmpleado
    #                         from [dblamorenita].sis_usuarios""")
    # empleados = results.fetchall()
    # for empleado in empleados:
    #     random_date = inicio + (final - inicio) * random.random()
    #     fecha_nacimiento = random_date.date().__str__()
    #     sql_update = f"""update [dblamorenita].sis_usuarios set susr_fecha_nac = '{fecha_nacimiento}' where susr_codigo='{empleado[0]}'"""
    #     cursor.execute(sql_update)
    #     conn.commit()
    # print(get_gender2('santos contreras'))
    # print(get_gender2('maria isabel lopez garcia rodriguez'))
    # print(get_gender2('cami lopez'))
    # print(get_gender2('majo garcia'))
    # print(get_gender2('colon cristobal'))
    # print(get_gender2('Cristóbal Colón'))
    print(get_gender2('ARACELY'))