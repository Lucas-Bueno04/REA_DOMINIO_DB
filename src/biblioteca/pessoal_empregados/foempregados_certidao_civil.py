# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_certidao_civil (Cadastro de certidão civil do empregado) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_certidao_civil"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_certidao_civil']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
