# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela forescisoes_termo_ferias_vencidas (Discriminação das verbas rescisórias do TRCT - (férias vencidas)) - módulo pessoal_rescisoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "forescisoes_termo_ferias_vencidas"
MODULO = "pessoal_rescisoes"
ENTIDADES = ['forescisoes_termo_ferias_vencidas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
