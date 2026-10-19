# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrexclusao_conta (Cadastro de Exclusões - Contas contábeis) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrexclusao_conta"
MODULO = "contabil_outros"
ENTIDADES = ['lrexclusao_conta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
