# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pmconfiguracao_integracao_conta (Configurar Integração por Centro de Custos - Contas) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pmconfiguracao_integracao_conta"
MODULO = "contabil_outros"
ENTIDADES = ['pmconfiguracao_integracao_conta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
