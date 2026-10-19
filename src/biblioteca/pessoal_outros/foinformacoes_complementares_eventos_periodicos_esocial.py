# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foinformacoes_complementares_eventos_periodicos_esocial (Controle de envio das informações complementares dos eventos períodicos para o eSocial.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foinformacoes_complementares_eventos_periodicos_esocial"
MODULO = "pessoal_outros"
ENTIDADES = ['foinformacoes_complementares_eventos_periodicos_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
