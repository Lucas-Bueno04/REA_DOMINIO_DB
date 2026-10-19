# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foemprestimos_cred_trab_rescisao_api_retorno (Empréstimo Crédito do Trabalhador - Retorno Consulta API) - módulo pessoal_emprestimos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foemprestimos_cred_trab_rescisao_api_retorno"
MODULO = "pessoal_emprestimos"
ENTIDADES = ['foemprestimos_cred_trab_rescisao_api_retorno']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
