# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecomunicador_web_parada_processo (Controle de pedido de parada do processo do Busca NF-e) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecomunicador_web_parada_processo"
MODULO = "geral_outros"
ENTIDADES = ['gecomunicador_web_parada_processo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
