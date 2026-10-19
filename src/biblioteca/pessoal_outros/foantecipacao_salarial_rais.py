# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foantecipacao_salarial_rais (Valores de antecipação calculados por competência) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foantecipacao_salarial_rais"
MODULO = "pessoal_outros"
ENTIDADES = ['foantecipacao_salarial_rais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
