# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdespesa_plano_saude_dependentes (Dependentes dos Beneficiários da Despesa com Plano de Saúde) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdespesa_plano_saude_dependentes"
MODULO = "fiscal_outros"
ENTIDADES = ['efdespesa_plano_saude_dependentes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
