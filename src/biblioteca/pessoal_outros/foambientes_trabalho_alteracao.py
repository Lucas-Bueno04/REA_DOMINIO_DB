# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foambientes_trabalho_alteracao (Alterações do ambiente de trabalho.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foambientes_trabalho_alteracao"
MODULO = "pessoal_outros"
ENTIDADES = ['foambientes_trabalho_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
