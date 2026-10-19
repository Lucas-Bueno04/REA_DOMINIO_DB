# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efacumulador_vigencia_pis_cofins_entradas (Acumuladores - Cadastro - PIS/COFINS - Entradas) - módulo fiscal_acumulador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efacumulador_vigencia_pis_cofins_entradas"
MODULO = "fiscal_acumulador"
ENTIDADES = ['efacumulador_vigencia_pis_cofins_entradas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
