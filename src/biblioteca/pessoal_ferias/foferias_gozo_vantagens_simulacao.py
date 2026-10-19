# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foferias_gozo_vantagens_simulacao (Simulação das vantagens do gozo de férias) - módulo pessoal_ferias."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foferias_gozo_vantagens_simulacao"
MODULO = "pessoal_ferias"
ENTIDADES = ['foferias_gozo_vantagens_simulacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
