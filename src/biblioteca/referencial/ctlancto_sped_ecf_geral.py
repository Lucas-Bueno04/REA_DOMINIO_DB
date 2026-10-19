# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlancto_sped_ecf_geral (Lançamentos referenciais SPED ECF (Geral)) - módulo referencial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlancto_sped_ecf_geral"
MODULO = "referencial"
ENTIDADES = ['lancamento_referencial_ecf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
