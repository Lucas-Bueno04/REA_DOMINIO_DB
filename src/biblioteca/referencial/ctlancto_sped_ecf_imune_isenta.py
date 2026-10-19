# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlancto_sped_ecf_imune_isenta (Lançamentos referenciais SPED ECF - Imunes e Isentas) - módulo referencial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlancto_sped_ecf_imune_isenta"
MODULO = "referencial"
ENTIDADES = ['lancamento_referencial_ecf_imune_isenta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
