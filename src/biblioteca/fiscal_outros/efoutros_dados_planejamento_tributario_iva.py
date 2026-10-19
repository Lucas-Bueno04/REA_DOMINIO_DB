# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutros_dados_planejamento_tributario_iva (Outros Dados - Planejamento Tributário - IVA) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutros_dados_planejamento_tributario_iva"
MODULO = "fiscal_outros"
ENTIDADES = ['efoutros_dados_planejamento_tributario_iva']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
