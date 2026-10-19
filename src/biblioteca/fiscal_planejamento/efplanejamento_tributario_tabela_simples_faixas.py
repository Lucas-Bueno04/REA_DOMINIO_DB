# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efplanejamento_tributario_tabela_simples_faixas (Planejamento Tributário - Tabela Simples Faixas) - módulo fiscal_planejamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efplanejamento_tributario_tabela_simples_faixas"
MODULO = "fiscal_planejamento"
ENTIDADES = ['efplanejamento_tributario_tabela_simples_faixas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
