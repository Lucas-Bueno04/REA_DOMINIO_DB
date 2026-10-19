# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geconsulta_busca (Configuração do modo de consulta) - módulo geral_consulta."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geconsulta_busca"
MODULO = "geral_consulta"
ENTIDADES = ['geconsulta_busca']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
