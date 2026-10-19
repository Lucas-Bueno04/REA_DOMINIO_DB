# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofiliais_sindicatos_patronais (Filiais/Contribuição Sindical Patronal - Cadastro) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofiliais_sindicatos_patronais"
MODULO = "pessoal_outros"
ENTIDADES = ['fofiliais_sindicatos_patronais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
