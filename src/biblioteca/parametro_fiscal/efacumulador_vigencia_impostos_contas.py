# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efacumulador_vigencia_impostos_contas (Contas contábeis dos impostos de cada acumulador) - módulo parametro_fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efacumulador_vigencia_impostos_contas"
MODULO = "parametro_fiscal"
ENTIDADES = ['acumulador_vigencia_conta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
