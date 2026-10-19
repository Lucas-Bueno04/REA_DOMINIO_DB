# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foatendimento_eventos_itens_filiais (ITENS DOS EVENTOS DOMINIO ATENDIMENTO) - módulo pessoal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foatendimento_eventos_itens_filiais"
MODULO = "pessoal_atendimento"
ENTIDADES = ['foatendimento_eventos_itens_filiais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
