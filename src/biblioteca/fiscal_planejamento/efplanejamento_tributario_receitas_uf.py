# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efplanejamento_tributario_receitas_uf (Planejamento Tributário - Receitas por estado) - módulo fiscal_planejamento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efplanejamento_tributario_receitas_uf"
MODULO = "fiscal_planejamento"
ENTIDADES = ['efplanejamento_tributario_receitas_uf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
