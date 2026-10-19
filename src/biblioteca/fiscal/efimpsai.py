# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimpsai (Impostos das notas de saída) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimpsai"
MODULO = "fiscal"
ENTIDADES = ['imposto_nota_saida']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
