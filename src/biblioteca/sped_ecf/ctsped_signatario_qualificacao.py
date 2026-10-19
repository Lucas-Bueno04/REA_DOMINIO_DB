# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctsped_signatario_qualificacao (Qualificações de signatário (SPED Contábil e ECF)) - módulo sped_ecf."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctsped_signatario_qualificacao"
MODULO = "sped_ecf"
ENTIDADES = ['qualificacao_signatario']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
