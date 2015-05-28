psql -h dir-rj sap_light -A -F "," < SQLs/corte.sql       > CSVs/corte.csv   
psql -h dir-rj sap_light -A -F "," < SQLs/negativacao.sql > CSVs/negativacao.csv  
psql -h dir-rj sap_light -A -F "," < SQLs/reclamacao.sql  > CSVs/reclamacao.csv 
psql -h dir-rj sap_light -A -F "," < SQLs/toi.sql         > CSVs/toi.csv 
psql -h dir-rj sap_light -A -F "," < SQLs/processo.sql        > CSVs/processo.csv 
