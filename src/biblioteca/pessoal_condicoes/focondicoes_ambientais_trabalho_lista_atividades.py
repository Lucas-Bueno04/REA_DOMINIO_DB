# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focondicoes_ambientais_trabalho_lista_atividades (Lista de atividades perigosas e insalubres.) - módulo pessoal_condicoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focondicoes_ambientais_trabalho_lista_atividades"
MODULO = "pessoal_condicoes"
ENTIDADES = ['focondicoes_ambientais_trabalho_lista_atividades']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
