# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconvocacao_trabalho_intermitente_envios_esocial (Envios de convocação para trabalho intermitente ao esocial) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconvocacao_trabalho_intermitente_envios_esocial"
MODULO = "pessoal_outros"
ENTIDADES = ['foconvocacao_trabalho_intermitente_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
