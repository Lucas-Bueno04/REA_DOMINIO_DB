# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrole_atualizacao_tabelas_calculo_sgd (Tabela de controle para verificação de novas versões das tabelas de cálculo da folha no SGD.) - módulo pessoal_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrole_atualizacao_tabelas_calculo_sgd"
MODULO = "pessoal_controle"
ENTIDADES = ['focontrole_atualizacao_tabelas_calculo_sgd']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
