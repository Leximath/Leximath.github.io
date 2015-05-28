\set ano 2011

SELECT
    municipio, count(contratos.id) as qtd, count(distinct(aux.id)) as qtd_notas, count(proc.id) as qtd_proc 
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    left join (
        select distinct 
            id_parceiro as id 
        from 
            negativacoes 
        where
            extract(year from data_negativacao) >= 2009 
            and
            extract(year from data_negativacao) <= 2010 
    ) as aux on aux.id = contratos.id_parceiro
    left join (
        select distinct 
            contrato as id 
        from 
            partes 
        where 
            extract(year from data_distribuicao) >= 2010 
            and
            extract(year from data_distribuicao) <= 2011 
    ) as proc on contratos.id = proc.id 
WHERE
    extract(year from contratos.data_fim) >= 2009 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and municipio is not null
    and municipio not like '%LEVY GASPARIAN%'
group by 
    municipio 
order by
    qtd;
