# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foformas_ajuste_parcelamento_competencias (Formas de ajustes conforme parcelamento - Competências) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foformas_ajuste_parcelamento_competencias"
MODULO = "pessoal_outros"
ENTIDADES = ['foformas_ajuste_parcelamento_competencias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
