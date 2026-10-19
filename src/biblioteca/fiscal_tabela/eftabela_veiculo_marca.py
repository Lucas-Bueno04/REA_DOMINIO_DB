# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_veiculo_marca (Marca de veículos) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_veiculo_marca"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_veiculo_marca']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
