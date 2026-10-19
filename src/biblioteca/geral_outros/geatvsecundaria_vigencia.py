# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatvsecundaria_vigencia (Empresa - Cadastro - Atividades secundarias Vigencia) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatvsecundaria_vigencia"
MODULO = "geral_outros"
ENTIDADES = ['geatvsecundaria_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
