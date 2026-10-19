# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlancto_scp (Lançamentos de SCP (Sociedade em Conta de Participação)) - módulo referencial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlancto_scp"
MODULO = "referencial"
ENTIDADES = ['lancamento_scp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
