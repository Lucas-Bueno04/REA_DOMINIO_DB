# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempreg_campolivres (Empregados - Cadastro - Campos livres) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempreg_campolivres"
MODULO = "pessoal_outros"
ENTIDADES = ['foempreg_campolivres']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
