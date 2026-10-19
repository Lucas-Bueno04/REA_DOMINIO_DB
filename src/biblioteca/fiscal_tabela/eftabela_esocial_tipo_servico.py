# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_esocial_tipo_servico (Tabela e_Social Tipo de Serviço) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_esocial_tipo_servico"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_esocial_tipo_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
