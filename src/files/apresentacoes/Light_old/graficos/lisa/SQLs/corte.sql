SELECT
    lat as lat, lng as lon
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    inner join (
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
WHERE
    extract(year from contratos.data_fim) >= 2011 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and lat != 0 and lng !=0
    ;
