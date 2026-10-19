# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geguia_contribuicao_previdenciaria_compensacoes_dcomp (Guia da contribuição previdenciária - Valores compensados do saldo a recolher.) - módulo geral_guia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geguia_contribuicao_previdenciaria_compensacoes_dcomp"
MODULO = "geral_guia"
ENTIDADES = ['geguia_contribuicao_previdenciaria_compensacoes_dcomp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
