SELECT
    lat as lat, lng as lon
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    inner join (
        select distinct 
            id_parceiro as id 
        from 
            negativacoes 
        where
            extract(year from data_negativacao) >= 2011 
            and
            extract(year from data_negativacao) <= 2011 
    ) as negativacao on negativacao.id = contratos.id_parceiro
WHERE
    extract(year from contratos.data_fim) >= 2011 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and lat != 0 and lng !=0
;
