# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrconta_financeira (Contas financeiras do escritório) - módulo honorarios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrconta_financeira"
MODULO = "honorarios"
ENTIDADES = ['conta_financeira']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
