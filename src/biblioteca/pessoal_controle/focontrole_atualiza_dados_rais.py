# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrole_atualiza_dados_rais (Controle para atualizar as tabelas da RAIS de acordo com o cálculo.) - módulo pessoal_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrole_atualiza_dados_rais"
MODULO = "pessoal_controle"
ENTIDADES = ['focontrole_atualiza_dados_rais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
