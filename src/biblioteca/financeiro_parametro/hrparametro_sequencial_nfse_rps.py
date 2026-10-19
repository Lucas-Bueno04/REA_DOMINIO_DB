# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_sequencial_nfse_rps (Parâmetro Honorarios - Sequência de RPS utilizada para NFS-e) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_sequencial_nfse_rps"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_sequencial_nfse_rps']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
