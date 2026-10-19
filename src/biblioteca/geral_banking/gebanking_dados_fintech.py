# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebanking_dados_fintech (Configuracao de feature flags para integracao com a Fintech por empresa) - módulo geral_banking."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebanking_dados_fintech"
MODULO = "geral_banking"
ENTIDADES = ['gebanking_dados_fintech']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
