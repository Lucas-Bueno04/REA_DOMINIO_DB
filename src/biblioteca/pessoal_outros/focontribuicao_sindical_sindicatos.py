# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontribuicao_sindical_sindicatos (Tabela de valores de contribuições sindicais por sindicato) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontribuicao_sindical_sindicatos"
MODULO = "pessoal_outros"
ENTIDADES = ['focontribuicao_sindical_sindicatos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
