# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geguia_contribuicao_previdenciaria_saldos_recolher_valores_compensados (Guia da contribuição previdenciária - Valores compensados do saldo a recolher.) - módulo geral_guia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geguia_contribuicao_previdenciaria_saldos_recolher_valores_compensados"
MODULO = "geral_guia"
ENTIDADES = ['geguia_contribuicao_previdenciaria_saldos_recolher_valores_c']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
