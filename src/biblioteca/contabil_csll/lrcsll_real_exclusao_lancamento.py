# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcsll_real_exclusao_lancamento (Lançamentos de Exclusões da Contribuição Social - Lancamentos Contábeis) - módulo contabil_csll."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcsll_real_exclusao_lancamento"
MODULO = "contabil_csll"
ENTIDADES = ['lrcsll_real_exclusao_lancamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
