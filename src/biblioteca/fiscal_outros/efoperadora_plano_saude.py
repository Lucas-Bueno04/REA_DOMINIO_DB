# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoperadora_plano_saude (Operadoras de Plano de Saúde) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoperadora_plano_saude"
MODULO = "fiscal_outros"
ENTIDADES = ['efoperadora_plano_saude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
