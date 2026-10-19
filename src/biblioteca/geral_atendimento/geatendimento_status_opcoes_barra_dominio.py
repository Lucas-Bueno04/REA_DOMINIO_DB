# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_status_opcoes_barra_dominio (No Contábil a thread responsável por habilitar/desabilitar os botões da barra da Domino, verifica os valores nesta tabela.) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_status_opcoes_barra_dominio"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_status_opcoes_barra_dominio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
