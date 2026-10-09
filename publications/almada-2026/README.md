# Almada: ecologia pública, metabolismo urbano e democracia material
**Caderno de investigação e ensaios independentes · Versão pública 0.1 · outubro de 2026**

**Autor/organização:** Tiago Dinis — Environmental Engineer & Systems Developer (investigação independente).  
**Estado editorial:** *working papers* e ensaios de teoria política. Sem revisão por pares, sem DOI, sem validação oficial, sem afiliação partidária. A disponibilização pública não representa aceitação por revista nem certificação das análises.

Este conjunto liga contabilidade física de resíduos, circularidade de materiais, habitação e reutilização cultural com questões mais amplas sobre tecnologia, trabalho, propriedade e democracia económica. Inclui uma análise com dados de operador, três protocolos de investigação, e um caderno político pessoal. Não há dados inventados para preencher lacunas.

## Trabalhos ambientais e metodológicos

1. **[WP01 — Evolução da recolha seletiva e dos resíduos indiferenciados, 2023–2024](municipal-evidence/WP01-waste-observability.md)**  
   *Análise quantitativa exploratória.* Transcrição de 54 entradas oficiais reportadas pela Amarsul (nove municípios, três séries, dois anos), processamento reproduzível e avaliação de consistência. A comparação adicional com o Relatório e Contas Amarsul revela perímetros operacionais que permanecem por reconciliar.
2. **[WP02 — Da promessa política à medição pública](municipal-evidence/WP02-policy-crosswalk.md)**  
   *Protocolo de auditoria.* Como relacionar programas autárquicos históricos de 2025, roteiro municipal, competências, contratos, execução e medições. Sem avaliação eleitoral de partidos.
3. **[WP03 — Reutilização de edifícios e cultura](municipal-evidence/WP03-cultural-reuse-protocol.md)**  
   *Protocolo de estudo de caso.* ACV, custos de ciclo de vida, acesso e uso real de espaços culturais. Nenhum edifício selecionado nem benefício contabilizado.
4. **[WP04 — Suficiência material e serviços](municipal-evidence/WP04-sufficiency-methods.md)**  
   *Protocolo empírico.* Investigar materiais por serviço útil, efeito de retorno, bem-estar, acesso e justiça distributiva.

## Caderno político-ecológico

- **[Metabolismo, trabalho, tecnologia, poder e comuns](political-ecology/01-metabolismo-trabalho-comuns.md):** 13 teses de uma perspetiva ecossocialista e democrática explicitamente assumida, com observações, alternativas e objeções. Não é o programa de um partido nem uma posição de organizações locais.
- **[Bibliografia crítica: Frey, Saito e outros](political-ecology/02-bibliografia-critica.md):** distinção entre livro, recensão e edição, diferenças intelectuais e limites da extrapolação.
- **[Programa de investigação e medição](political-ecology/03-programa-de-investigacao.md):** perguntas falsificáveis, fontes necessárias, responsabilidade municipal e próximos trabalhos.

## Reproduzir o único artigo quantitativo

Os ficheiros estão em [`municipal-evidence/data`](municipal-evidence/data/amarsul-2023-2024.csv) e [`municipal-evidence/scripts`](municipal-evidence/scripts/amarsul-summary.mjs).

```bash
node publications/almada-2026/municipal-evidence/scripts/amarsul-summary.mjs
node --test publications/almada-2026/municipal-evidence/scripts/amarsul-summary.test.mjs
```

As saídas são diferenças e variações de **indicadores específicos publicados por um operador**. Não se devem converter em «taxa de reciclagem», «pegada ambiental municipal» ou «impacto causal de determinado partido». Ver [fontes, integridade e limitações](SOURCES_AND_LIMITATIONS.md).

## Política editorial

- **Teoria:** declaradamente normativa; valores e argumentos podem ser debatidos.
- **Investigação:** evidência tratada independentemente do enquadramento político. A qualidade do estudo não depende de concordância ideológica.
- **Programas eleitorais:** descritos como documentos de candidatura no tempo, nunca como realizações nem sinais de apoio ao autor. BE–LIVRE em Almada em Comum e PCP–PEV na CDU são contextos de 2025 distintos das posições nacionais dos partidos.
- **Fontes privadas:** relatórios e documentos internos usados como materiais de reflexão foram sintetizados, **não copiados ou republicados**. Informações privadas, contactos e arquivos integrais de terceiros não fazem parte da publicação.
- **Revisões:** a correção de números e hipóteses deverá ser feita publicamente em commits datados. Manuscritos sem revisão independente mantêm a designação de working papers.

## O que ainda não foi concluído

A série do operador foi conferida na tabela web, mas não reconciliada com o RARU/MRRU e os totais de receção do relatório contabilístico. Faltam séries populacionais harmonizadas 2023–2024, avaliação por tratamento final, informação de contratos, séries espaciais, um edifício concreto e revisão de documentos integrais dos programas municipais para citações cláusula a cláusula. A consequência metodológica é simples: **o WP01 é publicável como análise descritiva com estas restrições; os outros três são protocolos**.

**Data da versão:** 9 de outubro de 2026. Texto e ficheiros sujeitos a revisão, sem DOI atribuído. © Tiago Dinis, 2026. Sem licença adicional de reutilização concedida nesta versão.
