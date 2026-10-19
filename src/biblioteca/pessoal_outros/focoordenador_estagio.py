# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focoordenador_estagio (Coordenadores de estágio.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focoordenador_estagio"
MODULO = "pessoal_outros"
ENTIDADES = ['focoordenador_estagio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
