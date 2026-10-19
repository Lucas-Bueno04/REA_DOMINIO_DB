# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efecf_configuracao (ECF - Configuração da redução Z) - módulo fiscal_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efecf_configuracao"
MODULO = "fiscal_ecf"
ENTIDADES = ['efecf_configuracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
