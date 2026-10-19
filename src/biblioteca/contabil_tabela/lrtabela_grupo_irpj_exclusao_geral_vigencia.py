# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrtabela_grupo_irpj_exclusao_geral_vigencia (TABELA DESCRICAO DO GRUPO IRPJ EXCLUSAO GERAL POR VIGENCIA) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrtabela_grupo_irpj_exclusao_geral_vigencia"
MODULO = "contabil_tabela"
ENTIDADES = ['lrtabela_grupo_irpj_exclusao_geral_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
