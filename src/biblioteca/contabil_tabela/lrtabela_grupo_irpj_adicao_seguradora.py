# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrtabela_grupo_irpj_adicao_seguradora (Tabela grupos de Adições da IRPJ - Seguradoras ou Entidades Abertas de Previdência Complementar) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrtabela_grupo_irpj_adicao_seguradora"
MODULO = "contabil_tabela"
ENTIDADES = ['lrtabela_grupo_irpj_adicao_seguradora']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
