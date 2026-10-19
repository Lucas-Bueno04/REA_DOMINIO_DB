# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_marca_grupo_bebida (Tabela Grupos por Marca Comercial) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_marca_grupo_bebida"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_marca_grupo_bebida']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
