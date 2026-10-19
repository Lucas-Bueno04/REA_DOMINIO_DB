# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdesenvolve_media (DESENVOLVE - BA - Media mensal atualizada) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdesenvolve_media"
MODULO = "fiscal_outros"
ENTIDADES = ['efdesenvolve_media']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
