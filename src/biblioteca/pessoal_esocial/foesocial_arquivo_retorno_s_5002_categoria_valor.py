# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_arquivo_retorno_s_5002_categoria_valor (Informações sobre IRRF do retorno do eSocial no arquivo S-5002.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_arquivo_retorno_s_5002_categoria_valor"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_arquivo_retorno_s_5002_categoria_valor']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
