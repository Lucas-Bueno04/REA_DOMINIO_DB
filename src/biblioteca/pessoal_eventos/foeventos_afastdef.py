# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foeventos_afastdef (Eventos pagos em afastamento - padrao) - módulo pessoal_eventos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foeventos_afastdef"
MODULO = "pessoal_eventos"
ENTIDADES = ['foeventos_afastdef']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
