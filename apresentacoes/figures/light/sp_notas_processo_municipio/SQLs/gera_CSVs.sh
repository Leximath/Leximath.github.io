#/bin/bash

# Comente os blocos que não deseja refazer

# Gera CSVs por municío
echo corte-proc
psql -U david -h dir-rj sap_light -A -t -F ',' < municipio_corte_proc.sql > ../CSVs/corte_proc.csv && psql -U david -h dir-rj sap_light -A -t -F ',' < ap_corte_proc.sql >> ../CSVs/corte_proc.csv &

echo neg-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < municipio_negativacao_proc.sql > ../CSVs/negativacao_proc.csv && psql -U david -h dir-rj sap_light -A -t -F ',' < ap_negativacao_proc.sql >> ../CSVs/negativacao_proc.csv &

echo rec-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < municipio_rec_proc.sql > ../CSVs/rec_proc.csv && psql -U david -h dir-rj sap_light -A -t -F ',' < ap_rec_proc.sql >> ../CSVs/rec_proc.csv &

echo toi-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < municipio_toi_processo.sql > ../CSVs/toi_processo.csv && psql -U david -h dir-rj sap_light -A -t -F ',' < ap_toi_processo.sql >> ../CSVs/toi_processo.csv &

# Gera CSVs a partir dos anteriores, apenas com as APs
echo corte-proc
grep ../CSVs/corte_proc.csv -e "AP " >> ../CSVs/corte_proc_AP.csv 

echo neg-proc
grep ../CSVs/negativacao_proc.csv -e "AP "  >> ../CSVs/negativacao_proc_AP.csv 

echo rec-proc
grep ../CSVs/rec_proc.csv -e "AP "  >> ../CSVs/rec_proc_AP.csv

echo toi-proc
grep ../CSVs/toi_processo.csv -e "AP "  >> ../CSVs/toi_processo_AP.csv


# Gera CSVs usando RA
echo * Gerando RA
echo corte-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < ra_corte_proc.sql > ../CSVs/ra_corte_proc.csv &
echo neg-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < ra_negativacao_proc.sql > ../CSVs/ra_negativacao_proc.csv &
echo rec-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < ra_rec_proc.sql > ../CSVs/ra_rec_proc.csv &
echo toi-proc
time psql -U david -h dir-rj sap_light -A -t -F ',' < ra_toi_processo.sql > ../CSVs/ra_toi_processo.csv &

echo geracao de CSVs terminada
