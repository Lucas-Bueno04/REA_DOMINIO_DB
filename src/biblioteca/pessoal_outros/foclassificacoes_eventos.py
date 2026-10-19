# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foclassificacoes_eventos (Classificações dos eventos - Cadastro de eventos) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foclassificacoes_eventos"
MODULO = "pessoal_outros"
ENTIDADES = ['foclassificacoes_eventos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
