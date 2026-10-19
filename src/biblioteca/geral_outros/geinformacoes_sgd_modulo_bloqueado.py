# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geinformacoes_sgd_modulo_bloqueado (Informações das tentativas de acessos aos modulos bloqueados para serem enviadas para o SGD) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geinformacoes_sgd_modulo_bloqueado"
MODULO = "geral_outros"
ENTIDADES = ['geinformacoes_sgd_modulo_bloqueado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
