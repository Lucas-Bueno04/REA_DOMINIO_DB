# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcontrole_emissao_relatorio (Controle de relatórios emitidos da Escrita) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcontrole_emissao_relatorio"
MODULO = "fiscal_outros"
ENTIDADES = ['efcontrole_emissao_relatorio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
