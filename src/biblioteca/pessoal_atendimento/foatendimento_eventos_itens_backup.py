# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foatendimento_eventos_itens_backup (Tabela apenas para backup de dados) - módulo pessoal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foatendimento_eventos_itens_backup"
MODULO = "pessoal_atendimento"
ENTIDADES = ['foatendimento_eventos_itens_backup']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
