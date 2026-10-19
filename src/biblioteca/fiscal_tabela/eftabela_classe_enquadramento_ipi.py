# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_classe_enquadramento_ipi (Tabela de Classe Enquadramento - IPI) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_classe_enquadramento_ipi"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_classe_enquadramento_ipi']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
