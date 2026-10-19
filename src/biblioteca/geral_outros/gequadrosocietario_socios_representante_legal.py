# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gequadrosocietario_socios_representante_legal (Empresa - Cadastro - Quadro Societario - Socios - Representante Legal) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gequadrosocietario_socios_representante_legal"
MODULO = "geral_outros"
ENTIDADES = ['gequadrosocietario_socios_representante_legal']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
