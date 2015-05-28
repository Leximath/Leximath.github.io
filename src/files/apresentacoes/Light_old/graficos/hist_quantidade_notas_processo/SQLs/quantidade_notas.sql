select descricao_do_tipo_de_nota, count(distinct(case when extract(year from notas.data_de_criacao_da_nota) = 2009 then contratos.id else NULL end)) as n_2009, count(distinct(case when extract(year from notas.data_de_criacao_da_nota) = 2010 then contratos.id else NULL end)) as n_2010, count(distinct(case when extract(year from notas.data_de_criacao_da_nota) = 2011 then contratos.id else NULL end)) as n_2011 from notas inner join contratos on notas.instalacao = contratos.instalacao and contratos.data_inicio <= notas.data_de_criacao and contratos.data_fim >= notas.data_de_encerramento group by descricao_do_tipo_de_nota order by n_2009;
