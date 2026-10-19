# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_ecf_od (ECF - Parâmetros da escrituração (Outros Dados)) - módulo sped_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_ecf_od"
MODULO = "sped_ecf"
ENTIDADES = ['ecf_outros_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
