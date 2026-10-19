# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconvocacao_trabalho_intermitente (Convocação para trabalho intermitente.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconvocacao_trabalho_intermitente"
MODULO = "pessoal_outros"
ENTIDADES = ['foconvocacao_trabalho_intermitente']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
