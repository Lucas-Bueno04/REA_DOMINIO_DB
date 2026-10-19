# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efacumulador_vigencia_pis_cofins_saidas (Acumuladores - Cadastro - PIS/COFINS - Saídas) - módulo fiscal_acumulador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efacumulador_vigencia_pis_cofins_saidas"
MODULO = "fiscal_acumulador"
ENTIDADES = ['efacumulador_vigencia_pis_cofins_saidas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
