# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabela_exames (Código do exame.) - módulo pessoal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabela_exames"
MODULO = "pessoal_tabela"
ENTIDADES = ['fotabela_exames']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
