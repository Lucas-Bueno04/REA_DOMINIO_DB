# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foatendimento_solicitacoes_abertas_rubrica (Tabela que indica rubricas com lançamentos no portal do cliente) - módulo pessoal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foatendimento_solicitacoes_abertas_rubrica"
MODULO = "pessoal_atendimento"
ENTIDADES = ['foatendimento_solicitacoes_abertas_rubrica']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
