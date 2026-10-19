# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_sincronizar_empresas_da (Tabela para controla de sincronia das empresas do DA para remarcação do módulo Atendimento) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_sincronizar_empresas_da"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_sincronizar_empresas_da']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
