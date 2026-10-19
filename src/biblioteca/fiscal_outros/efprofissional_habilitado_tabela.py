# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efprofissional_habilitado_tabela (Profissionais Habilitados - Tabelas) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efprofissional_habilitado_tabela"
MODULO = "fiscal_outros"
ENTIDADES = ['efprofissional_habilitado_tabela']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
