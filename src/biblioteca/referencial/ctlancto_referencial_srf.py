# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlancto_referencial_srf (Lançamentos referenciais SRF) - módulo referencial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlancto_referencial_srf"
MODULO = "referencial"
ENTIDADES = ['lancamento_referencial_srf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
