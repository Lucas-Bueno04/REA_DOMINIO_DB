# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimposto_vigencia_recolhimento (Regras de recolhimento por imposto e vigência) - módulo guias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimposto_vigencia_recolhimento"
MODULO = "guias"
ENTIDADES = ['regra_recolhimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
