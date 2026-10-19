# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosefip_tbtercr (Relacionamento do Codigo de Terceiro com FPAS) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosefip_tbtercr"
MODULO = "pessoal_outros"
ENTIDADES = ['fosefip_tbtercr']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
