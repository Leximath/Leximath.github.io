SELECT
    lat as lat, lng as lon
FROM
    contratos
    inner join instalacoes on instalacoes.id = contratos.instalacao 
    inner join (
        select distinct 
            contrato as id 
        from 
            partes 
        where 
            extract(year from data_distribuicao) >= 2011 
            and
            extract(year from data_distribuicao) <= 2011 
    ) as proc on proc.id = contratos.id
WHERE
    extract(year from contratos.data_fim) >= 2011 
    and
    extract(year from contratos.data_inicio) <= 2011 
    and lat != 0 and lng !=0
    ;
