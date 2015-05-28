SELECT
    municipio_rio.cod_bairro, 
    cast(count(proc.id) as float) * 10000 / count(contratos.id) as qtd_proc, 
    cast(count(distinct(toi.id)) as float) * 10000 / count(contratos.id) as qtd_toi, 
    cast(count(distinct(negativacao.id)) as float) * 10000  / count(contratos.id) as qtd_nega, 
    cast(count(distinct(corte.id)) as float)  * 10000 / count(contratos.id) as qtd_corte, 
    cast(count(distinct(reclamacao.id)) as float)  * 10000 / count(contratos.id) as qtd_reclamacao, 
    count(contratos.id)  as qtd
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    inner join municipio_rio on municipio_rio.bairro_sap = instalacoes.bairro
    left join (
        select distinct 
            negociacoes_ren.instalacao as id 
        from 
            negociacoes_ren, notas_ren
        where
            negociacoes_ren.notas = notas_ren.id
            and
            extract(year from data_de_criacao_da_nota) >= 2011 
            and
            extract(year from data_de_criacao_da_nota) <= 2011 

    ) as toi on toi.id = contratos.instalacao

    left join (
        select distinct 
            instalacao as id, 
            descricao_do_tipo_de_nota  
        from 
            notas 
        where 
            notas.descricao_do_tipo_de_nota   = 'Corte BT'
            and
            extract(year from data_de_criacao_da_nota) >= 2011 
            and
            extract(year from data_de_criacao_da_nota) <= 2011 
    ) as corte on corte.id = contratos.instalacao
    left join (
        select distinct 
            instalacao as id, 
            descricao_do_tipo_de_nota  
        from 
            notas 
        where 
            notas.descricao_do_tipo_de_nota   = 'Reclamação'
            and
            extract(year from data_de_criacao_da_nota) >= 2011 
            and
            extract(year from data_de_criacao_da_nota) <= 2011 
    ) as reclamacao on reclamacao.id = contratos.instalacao

    left join (
        select distinct 
            id_parceiro as id 
        from 
            negativacoes 
        where
            extract(year from data_negativacao) >= 2011 
            and
            extract(year from data_negativacao) <= 2011 
    ) as negativacao on negativacao.id = contratos.id_parceiro
    left join (
        select distinct 
            contrato as id 
        from 
            partes 
        where 
            extract(year from data_distribuicao) >= 2011 
            and
            extract(year from data_distribuicao) <= 2011 
    ) as proc on contratos.id = proc.id 
WHERE
    extract(year from contratos.data_fim) >= 2011 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and 
    municipio = 'RIO DE JANEIRO'
group by 
    municipio_rio.cod_bairro
order by
    qtd_proc
desc;
