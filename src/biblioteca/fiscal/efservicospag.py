# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicospag (Recebimentos das notas de serviço) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicospag"
MODULO = "fiscal"
ENTIDADES = ['pagamento_nota_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
