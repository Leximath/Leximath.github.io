\set ano 2011

SELECT
    municipio, count(contratos.id) as qtd, count(distinct(aux.id)) as qtd_notas, count(proc.id) as qtd_proc 
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    left join (
        select distinct 
            negociacoes_ren.instalacao as id 
        from 
            negociacoes_ren, notas_ren
        where
            negociacoes_ren.notas = notas_ren.id
            and
            extract(year from data_de_criacao_da_nota) >= 2009 
            and
            extract(year from data_de_criacao_da_nota) <= 2010 

    ) as aux on aux.id = contratos.instalacao
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
