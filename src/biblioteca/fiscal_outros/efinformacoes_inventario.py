# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efinformacoes_inventario (Tabela de Informações do Inventário) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efinformacoes_inventario"
MODULO = "fiscal_outros"
ENTIDADES = ['efinformacoes_inventario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
