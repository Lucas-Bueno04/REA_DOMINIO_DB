# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focontrole_busca_tabelas_calculo_sgd (Tabela de controle para buscar atualizações das tabelas de cálculo da Folha no SGD por dia.) - módulo pessoal_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focontrole_busca_tabelas_calculo_sgd"
MODULO = "pessoal_controle"
ENTIDADES = ['focontrole_busca_tabelas_calculo_sgd']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
