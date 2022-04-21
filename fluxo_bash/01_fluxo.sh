#!/bin/bash

python3 gera_dataset.py -i 1 -nd 'nomeação e classificação prefeitura de maceio e ama v1' -td 'texto'

python3 gera_versoes.py -i 1 2 2 2 2 -nc 'EventSearch' 'SGDClassifier' -pc '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/classificacao/EventSearch.py'  '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/sgd_pipeline.pkl' -tc 'regex' 'classificador sklearn' -mv '' '' '' 1 '' -nv 'versão regex v1' 'versao modelo SGD v1' 'versão modelo diff v1' 'versao rubrix v1' 'versao merge modelo SGD v1 e rubrix v1' -tv 'texto' 'texto' 'texto' 'texto' 'texto' -dv 'classificação fraca com regex versao v1' 'classificação com SGDClassifier v1' 'diff entre regex e SGDClassifier' 'correção feita manualmente usando o rubrix' 'dataset corrigido com a classificação manual  rubrix v1'

python3 classificador.py -d 1 -r erro_rubrix_v1 -i 1 2 3