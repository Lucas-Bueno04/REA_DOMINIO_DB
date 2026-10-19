# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimposto_padrao_vigencia_recolhimento (Tabela de Imposto Padrão - Vigência - Recolhimento) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimposto_padrao_vigencia_recolhimento"
MODULO = "fiscal_outros"
ENTIDADES = ['efimposto_padrao_vigencia_recolhimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
