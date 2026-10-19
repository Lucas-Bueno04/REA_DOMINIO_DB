# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focategoria_origem_dirigente_sindical (Tabela de catálogo das categorias do tipo Dirigente Sindical) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focategoria_origem_dirigente_sindical"
MODULO = "pessoal_outros"
ENTIDADES = ['focategoria_origem_dirigente_sindical']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
