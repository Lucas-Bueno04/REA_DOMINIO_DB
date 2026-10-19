# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geacoes_suporte_configuracoes (Tabela de configurações de ações exclusivas do suporte) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geacoes_suporte_configuracoes"
MODULO = "geral_outros"
ENTIDADES = ['geacoes_suporte_configuracoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
