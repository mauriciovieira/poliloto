#!/bin/bash

zips=( "D_megase.zip" "D_quina.zip" "d_dplsen.zip" "D_federa.zip" "d_loteca.zip" "D_timema.zip" "D_lotfac.zip" "D_lotoma.zip" "d_lotogo.zip" )
base_url=http://www1.caixa.gov.br/loterias/_arquivos/loterias

for zip in "${zips[@]}"
do
	wget "${base_url}/$zip" && unzip -o $zip &&	rm $zip
done
