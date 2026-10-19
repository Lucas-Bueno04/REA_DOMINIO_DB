# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebanking_feature_flag (Controle de Feature Flags da Fintech) - módulo geral_banking."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebanking_feature_flag"
MODULO = "geral_banking"
ENTIDADES = ['gebanking_feature_flag']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
