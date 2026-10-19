# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctgruposdmpl_tipolancto (Estrutura do DMPL - Tipo Lancamento) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctgruposdmpl_tipolancto"
MODULO = "contabil_outros"
ENTIDADES = ['ctgruposdmpl_tipolancto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
