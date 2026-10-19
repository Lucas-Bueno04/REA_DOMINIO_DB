# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalculos_eventos_bases (Contém as bases que não estão vinculadas a eventos para o consulta recibo) - módulo pessoal_calculos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalculos_eventos_bases"
MODULO = "pessoal_calculos"
ENTIDADES = ['focalculos_eventos_bases']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
