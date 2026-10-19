# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalcinss_movto (Movimento do valor a ser compensado) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalcinss_movto"
MODULO = "pessoal_outros"
ENTIDADES = ['focalcinss_movto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
