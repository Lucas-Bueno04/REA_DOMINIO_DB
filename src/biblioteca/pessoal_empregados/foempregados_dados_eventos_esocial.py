# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_dados_eventos_esocial (Tabela de relacionamento entre o cadastro de empregados e os registros de envio para o eSocial.) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_dados_eventos_esocial"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_dados_eventos_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
