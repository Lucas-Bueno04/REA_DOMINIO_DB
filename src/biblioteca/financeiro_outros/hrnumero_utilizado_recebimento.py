# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrnumero_utilizado_recebimento (Tabela para ser usada na geração de números e verificar se os números estão sendo utilizados) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrnumero_utilizado_recebimento"
MODULO = "financeiro_outros"
ENTIDADES = ['hrnumero_utilizado_recebimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
