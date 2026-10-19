# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efprofissional_habilitado_tabela_faixa (Profissionais Habilitados - Tabelas - Faixas) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efprofissional_habilitado_tabela_faixa"
MODULO = "fiscal_outros"
ENTIDADES = ['efprofissional_habilitado_tabela_faixa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
