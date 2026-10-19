# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo_irpj_real (Apuração do IRPJ pelo lucro real) - módulo lalur."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo_irpj_real"
MODULO = "lalur"
ENTIDADES = ['apuracao_irpj_real']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
