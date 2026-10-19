# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentoacoes_erro (Erros gerados ao tentar enviar alguma ação ao Onvio ou ao Domínio Atendimento) - módulo geral_atendimentoacoes."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentoacoes_erro"
MODULO = "geral_atendimentoacoes"
ENTIDADES = ['geatendimentoacoes_erro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
