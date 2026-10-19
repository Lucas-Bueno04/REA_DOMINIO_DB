# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparametro_vigencia_inscricoes_subtri (Paramentros - Inscricoes de Substituicao Tributaria) - módulo fiscal_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparametro_vigencia_inscricoes_subtri"
MODULO = "fiscal_parametro"
ENTIDADES = ['efparametro_vigencia_inscricoes_subtri']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
