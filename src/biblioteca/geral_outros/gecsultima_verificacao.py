# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecsultima_verificacao (Última verificação da Central de Soluções) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecsultima_verificacao"
MODULO = "geral_outros"
ENTIDADES = ['gecsultima_verificacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
