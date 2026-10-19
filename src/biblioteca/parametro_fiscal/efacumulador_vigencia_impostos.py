# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efacumulador_vigencia_impostos (Impostos de cada acumulador por vigência) - módulo parametro_fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efacumulador_vigencia_impostos"
MODULO = "parametro_fiscal"
ENTIDADES = ['acumulador_vigencia_imposto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
