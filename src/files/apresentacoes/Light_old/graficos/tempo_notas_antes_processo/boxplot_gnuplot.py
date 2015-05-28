#!/usr/bin/python2.7
from collections import OrderedDict
import psycopg2 
from sys import argv
from collections import Counter
from collections import defaultdict
nota_data = defaultdict(list)
import numpy as np

ano = argv[1]

"script que relaciona a data de distribuicao do processo com a nota antiga proxima"

sql_instalacoes = """ 
select instalacao, data_distribuicao, data_inicio, data_fim
from partes
where extract(year from data_distribuicao) = {}
"""

sql_data_notas = """
select  descricao_do_tipo_de_nota, data_de_criacao_da_nota 
from notas
where 
notas.instalacao = {}
and
notas.data_de_criacao_da_nota < to_date('{}','YYYY-MM-DD')
and
notas.data_de_criacao_da_nota > to_date('{}','YYYY-MM-DD')
order by data_de_criacao_da_nota desc;
"""

sql_data_notas_ren = """
select  descricao_do_tipo_de_nota, data_de_criacao_da_nota 
from notas_ren
where 
notas_ren.instalacao = {}
and
notas_ren.data_de_criacao_da_nota < to_date('{}','YYYY-MM-DD')
and
notas_ren.data_de_criacao_da_nota > to_date('{}','YYYY-MM-DD')
order by data_de_criacao_da_nota desc;
"""

sql_negativacao = """
select 
orgao_negativador,
data_negativacao
from 
negativacoes, contratos 
where 
contratos.id_parceiro = negativacoes.id_parceiro and 
contratos.instalacao = {} and
negativacoes.data_negativacao < to_date('{}','YYYY-MM-DD') and
negativacoes.data_negativacao > to_date('{}','YYYY-MM-DD')
"""


connection = psycopg2.connect(user="oangelo", password="angelo123", host="dir-rj", database="sap_light")
cursor = connection.cursor()

tipos = [] 

cursor.execute(sql_instalacoes.format(ano))
instalacoes = cursor.fetchall()
for instalacao, data_distribuicao, data_inicio, data_fim in instalacoes:
    if instalacao:
        cursor.execute(sql_data_notas.format(instalacao, data_distribuicao, data_inicio))
        data_nota_tipo = cursor.fetchall()	
        cursor.execute(sql_data_notas_ren.format(instalacao, data_distribuicao, data_inicio))
        data_nota_ren_tipo = cursor.fetchall()	
        cursor.execute(sql_negativacao.format(instalacao, data_distribuicao, data_inicio))
        data_negativacao = cursor.fetchall()	


        data_nota_tipo.extend(data_nota_ren_tipo)
        data_nota_tipo.extend(data_negativacao)
        sorted(data_nota_tipo, key=lambda nota: nota[1])
        if len(data_nota_tipo) > 0:
            tipo_nota, data_nota = data_nota_tipo[0]
            tipos.append(tipo_nota)  
            nota_data[tipo_nota].append(abs((data_nota - data_distribuicao).days)) 
            #print """'{}'""".format(tipo_nota),"," ,abs((data_nota - data_distribuicao).days)
        else:
            tipos.append("NULL")
            #print "'NULL' , -1"

counter = Counter(tipos)
total = float(sum(counter.values()))
c_sorted = sorted(counter.items(), key=lambda nota: nota[1], reverse=True)
for item, qtd in c_sorted:
    lista = sorted(nota_data[item])
    if qtd / total > 0.009:
        for i in lista:
            if i < 1460: 
                print """"{}",{}""".format(item, i)

