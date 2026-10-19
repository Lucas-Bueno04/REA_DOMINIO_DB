# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomedidas_protecao_emprego_covid_19 (Medidas de proteção ao empregado devido a COVID-19) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomedidas_protecao_emprego_covid_19"
MODULO = "pessoal_outros"
ENTIDADES = ['fomedidas_protecao_emprego_covid_19']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
