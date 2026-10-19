# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_alteracao_outros_campos (Registros de alteração contratual para envio ao eSocial.) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_alteracao_outros_campos"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_alteracao_outros_campos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
