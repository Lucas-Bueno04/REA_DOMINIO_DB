# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomensagem_aviso (Tabela para controle de mensagens e avisos do sistema) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomensagem_aviso"
MODULO = "pessoal_outros"
ENTIDADES = ['fomensagem_aviso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
