# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_sped_ecf_geral_ref (Mapeamento das contas da empresa para o plano ECF Geral) - módulo referencial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_sped_ecf_geral_ref"
MODULO = "referencial"
ENTIDADES = ['conta_referencial_ecf']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
