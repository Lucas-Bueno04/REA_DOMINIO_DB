# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efatendimento_nfe_catalogo_visualizados (Notas já visualizadas pelos usuários - Domínio Atendimento) - módulo fiscal_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efatendimento_nfe_catalogo_visualizados"
MODULO = "fiscal_atendimento"
ENTIDADES = ['efatendimento_nfe_catalogo_visualizados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
