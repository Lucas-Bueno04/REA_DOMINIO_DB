# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efpagimp_publicar_documento (Pagamentos de Impostos - Publicação) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efpagimp_publicar_documento"
MODULO = "fiscal_outros"
ENTIDADES = ['efpagimp_publicar_documento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
