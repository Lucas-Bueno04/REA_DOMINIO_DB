# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foequipamentos_protecao_individual (Equipamento de proteção individual) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foequipamentos_protecao_individual"
MODULO = "pessoal_outros"
ENTIDADES = ['foequipamentos_protecao_individual']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
