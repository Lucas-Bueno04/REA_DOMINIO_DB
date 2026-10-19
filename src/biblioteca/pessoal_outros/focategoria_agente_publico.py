# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focategoria_agente_publico (Tabela de catálogo das categorias do tipo Agente público) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focategoria_agente_publico"
MODULO = "pessoal_outros"
ENTIDADES = ['focategoria_agente_publico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
