# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsaidas_lancto (Contabilização das notas de saída) - módulo contabil."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsaidas_lancto"
MODULO = "contabil"
ENTIDADES = ['contabilizacao_nota_saida']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
