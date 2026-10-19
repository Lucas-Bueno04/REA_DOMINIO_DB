# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosindicatos_plr (Configuração das regras para pagamento de PLR.) - módulo pessoal_sindicatos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosindicatos_plr"
MODULO = "pessoal_sindicatos"
ENTIDADES = ['fosindicatos_plr']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
