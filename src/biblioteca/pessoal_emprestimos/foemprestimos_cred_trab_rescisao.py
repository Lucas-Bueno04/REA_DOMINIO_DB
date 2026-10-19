# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foemprestimos_cred_trab_rescisao (Dados do ultimo calculo da rescisao para o Credito do Trabalhador) - módulo pessoal_emprestimos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foemprestimos_cred_trab_rescisao"
MODULO = "pessoal_emprestimos"
ENTIDADES = ['foemprestimos_cred_trab_rescisao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
