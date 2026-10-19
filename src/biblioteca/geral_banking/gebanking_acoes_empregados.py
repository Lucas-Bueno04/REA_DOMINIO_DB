# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebanking_acoes_empregados (Controle de acoes de empregados para integracao com FinTech) - módulo geral_banking."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebanking_acoes_empregados"
MODULO = "geral_banking"
ENTIDADES = ['gebanking_acoes_empregados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
