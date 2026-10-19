# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodiferenca_alteracao_retroativa_piso_salarial (Diferenças referentes a alteração retroativa de piso salarial.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodiferenca_alteracao_retroativa_piso_salarial"
MODULO = "pessoal_outros"
ENTIDADES = ['fodiferenca_alteracao_retroativa_piso_salarial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
