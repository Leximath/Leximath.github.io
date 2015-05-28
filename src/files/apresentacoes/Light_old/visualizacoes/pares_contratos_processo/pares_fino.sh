psql -h  dir-rj -U oangelo sap_light -t -A -F ","  -c "
select 
    para_tipo_desc, 
    para_cod_desc,    
    de_tipo_desc, 
    de_cod_desc,    
    count(de_tipo_desc) as percentual_pares,
    count(distinct(contrato)) as percentual_contratos
from 
    pares_processo
where 
    dias < 121  and 
    ano < 2012 and
    ano > 2008 
group by 
    de_tipo_desc, para_tipo_desc, para_cod_desc, de_cod_desc   
order by 
count(de_tipo_desc) desc;
"
