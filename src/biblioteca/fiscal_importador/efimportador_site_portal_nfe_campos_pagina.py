# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_site_portal_nfe_campos_pagina (Importação da NF-e pelo site da Receita Federal - Campos da página) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_site_portal_nfe_campos_pagina"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_site_portal_nfe_campos_pagina']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
