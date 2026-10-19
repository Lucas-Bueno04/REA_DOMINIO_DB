# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobasesserv_calculos_rateio_servico (Relacionamento entre o cálculo principal e os cálculos de rateio por serviço.) - módulo pessoal_basesserv."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobasesserv_calculos_rateio_servico"
MODULO = "pessoal_basesserv"
ENTIDADES = ['fobasesserv_calculos_rateio_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
