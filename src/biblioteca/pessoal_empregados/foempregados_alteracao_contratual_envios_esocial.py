# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_alteracao_contratual_envios_esocial (Envios das alterações contratuais ao eSocial) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_alteracao_contratual_envios_esocial"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_alteracao_contratual_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
