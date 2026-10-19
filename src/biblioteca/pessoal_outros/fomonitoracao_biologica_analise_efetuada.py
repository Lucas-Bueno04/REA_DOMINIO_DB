# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomonitoracao_biologica_analise_efetuada (Agente químico.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomonitoracao_biologica_analise_efetuada"
MODULO = "pessoal_outros"
ENTIDADES = ['fomonitoracao_biologica_analise_efetuada']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
