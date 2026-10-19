# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrtipo_contrato (Tipo de contrato) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrtipo_contrato"
MODULO = "financeiro_outros"
ENTIDADES = ['hrtipo_contrato']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
