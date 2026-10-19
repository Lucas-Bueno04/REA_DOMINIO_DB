# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foalteracao_salarial_complementos (Alterações salariais com complementos de cálculos) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foalteracao_salarial_complementos"
MODULO = "pessoal_outros"
ENTIDADES = ['foalteracao_salarial_complementos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
