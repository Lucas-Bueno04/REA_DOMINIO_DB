# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fointegcontlanc (Lançamentos contábeis gerados pela integração da folha) - módulo folha_contabil."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fointegcontlanc"
MODULO = "folha_contabil"
ENTIDADES = ['lancamento_integracao_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
