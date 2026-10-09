# Almada — pequenos artigos e protocolos de evidência (2026)

**Estado: working papers em revisão, não artigos revistos por pares, nem pareceres técnicos certificados.** Esta coleção foi publicada como versão de investigação e não altera o código de produção nem a simulação de resíduos do projeto principal.

## Série

1. [WP01 — Evolução da recolha seletiva e tratamento indiferenciado em nove municípios Amarsul (2023–2024)](WP01-waste-observability.md): breve análise empírica com 54 observações anuais, verificações e limites de comparabilidade.
2. [WP02 — Como traduzir propostas municipais e eleitorais em indicadores auditáveis](WP02-policy-crosswalk.md): matriz descritiva entre Almada Circular 2030, BE–LIVRE, CDU, e indicadores testáveis, sem endosso de nenhum partido.
3. [WP03 — Reutilização de edifícios para cultura: protocolo físico, social e económico](WP03-cultural-reuse-protocol.md): desenho de avaliação para uma eventual infraestrutura cultural de Almada, ainda sem imóvel selecionado.
4. [WP04 — Suficiência material e qualidade dos serviços: hipótese falsificável](WP04-sufficiency-methods.md): investigação pré-registada, não evidência observacional.

## Reproduzir WP01

```bash
node research/municipal-evidence/scripts/amarsul-summary.mjs
node --test research/municipal-evidence/scripts/amarsul-summary.test.mjs
```

Entrada: [CSV transcrito da tabela do operador](data/amarsul-2023-2024.csv), 9 municípios × 3 séries × 2 anos = 54 valores. Fonte primária: https://www.amarsul.pt/umbraco/surface/indicadores/IndicadoresRecolhaSeletivaTemplate?PageID=14665 (consulta em 2026-10-09). Sem interpolação. Valor ausente não se converte em zero. Os números não substituem os dados detalhados do MRRU/RARU.

## Regras editoriais

- **Dados:** conservar indicador, unidade, ano, geografia, emissor, URL e data de extração. Os números da série Amarsul são reportados pelo operador, não medições independentes feitas por este projeto.
- **Fronteiras:** recolha seletiva de embalagens/papel/vidro, biorresíduos tratados e indiferenciados tratados **não são mutuamente exclusivos nem representam necessariamente todas as toneladas geradas**. Não somar para calcular taxa oficial de reciclagem, taxa de captura ou balanço completo.
- **Validade:** uma correlação descritiva entre municípios ou dois anos não demonstra causas, efeitos de políticas, diferenças de serviço ou desempenho de partidos.
- **Neutralidade:** programas eleitorais descrevem compromissos de candidaturas numa data. Atribuição e cumprimento requerem registos independentes. Não usar resultados para classificar partidos.
- **Revisão:** confirmar fontes, edição, permissões de reprodução, cálculos, pressupostos e textos com revisão humana; não atribuir contacto institucional, autoria científica externa ou apoio municipal. Publicação pública, DOI e submissão a revista requerem revisão e autorização do autor.
- **Privacidade:** não importar do Google Drive listas de contactos, dados pessoais nem dossiers privados para este repositório. Só referências documentais relevantes e ligações públicas.

## Articulação com outros projetos

Os documentos culturais do Almada Commons e o relatório *From Circular-Economy Strategy to Measurable Urban Metabolism* são referências conceptuais; não são bases observacionais. Este diretório gera os desenhos de estudo, enquanto `strata-lca` só deverá fornecer inventários/LCIA depois de validação das unidades funcionais e fatores de fonte. Ver também a missão do programa ambiental, mantida separadamente em documentação técnica privada e o roteiro de impacto ambiental, mantido separadamente em documentação técnica privada.

## Próximos dados a obter

- RARU 2024 v1.1 + ficheiro detalhado (APA); reconciliar operações e perímetros.
- PORDATA/INE por município: população residente harmonizada 2023/2024 e resíduos recolhidos, metadados e revisões.
- Almada Circular M5/M6: ações executadas, medição por corrente, orçamento, medição de contaminação com protocolo.
- Dados de ocupação/licença, edifícios municipais e despesa cultural para uma proposta cultural concreta.
