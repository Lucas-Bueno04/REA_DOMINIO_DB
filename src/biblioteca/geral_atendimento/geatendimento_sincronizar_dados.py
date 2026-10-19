# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_sincronizar_dados (Tabela para sincronizar dados com o atendimento) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_sincronizar_dados"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_sincronizar_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
