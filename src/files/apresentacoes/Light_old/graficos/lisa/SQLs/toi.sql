SELECT
    lat as lat, lng as lon
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    inner join (
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
WHERE
    extract(year from contratos.data_fim) >= 2011 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and lat != 0 and lng !=0
;
