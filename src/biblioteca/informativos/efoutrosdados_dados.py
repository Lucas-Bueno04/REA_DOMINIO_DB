# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efoutrosdados_dados (Campos informados em cada informativo (campo/valor)) - módulo informativos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efoutrosdados_dados"
MODULO = "informativos"
ENTIDADES = ['dado_informativo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
