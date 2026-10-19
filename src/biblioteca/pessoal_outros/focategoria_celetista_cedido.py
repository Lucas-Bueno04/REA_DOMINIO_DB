# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focategoria_celetista_cedido (Tabela de catálogo das categorias do tipo Celetista Cedido/ Trabalhador Cedido) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focategoria_celetista_cedido"
MODULO = "pessoal_outros"
ENTIDADES = ['focategoria_celetista_cedido']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
