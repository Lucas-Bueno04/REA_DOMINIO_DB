# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrole_entrega_equipamentos_protecao_individual (Equipamento de proteção individual - Empregado) - módulo pessoal_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrole_entrega_equipamentos_protecao_individual"
MODULO = "pessoal_controle"
ENTIDADES = ['focontrole_entrega_equipamentos_protecao_individual']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
