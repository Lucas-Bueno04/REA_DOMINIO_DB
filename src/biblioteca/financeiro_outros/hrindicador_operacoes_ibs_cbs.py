# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrindicador_operacoes_ibs_cbs (Indicadores de Operação IBS/CBS) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrindicador_operacoes_ibs_cbs"
MODULO = "financeiro_outros"
ENTIDADES = ['hrindicador_operacoes_ibs_cbs']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
