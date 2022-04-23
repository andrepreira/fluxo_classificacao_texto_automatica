import sqlalchemy as db
import pandas as pd
 
def import_table(table_name, conn):
    metadata = db.MetaData()
    return db.Table(table_name, metadata, autoload=True, autoload_with=conn)

def insert_db(table_name,conn, value_list):
    table = import_table(table_name, conn)
    query = db.insert(table)
    conn.execute(query, value_list)

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = False)

def select_itens_modelo_versao(conn, id_dataset, id_versao):
    item = import_table('item', conn)
    classificados = import_table('classificados', conn)

    query = db.select([item.columns.texto, classificados.columns.label, 
    item.columns.id]).where(item.columns.id == classificados.columns.id_item 
    and item.columns.id_dataset == id_dataset and classificados.columns.id_versao == id_versao)

    r =  conn.execute(query).fetchall()
    df = pd.DataFrame(r)
    df.columns = r[0].keys()
    df.rename(columns={"label": "label_regex"}, inplace = True)
    df['status'] = df['label_regex'].apply(lambda x: 'classified' if x else 'unclassified')
    return  df
    
def select_labels(table_name, conn, id_versao):
    table = import_table(table_name, conn)
    query = db.select([table.columns.label, table.columns.id_item]).where(table.columns.id_versao == id_versao)
    r =  conn.execute(query).fetchall()
    df = pd.DataFrame(r)
    df.columns = r[0].keys()
    return  df
    
def popula_tabelas_iniciais(conn, table_name, values_list):
    classificador = import_table(table_name, conn)
    insert_db(classificador, conn, values_list)