# WP01 · Aumento da recolha seletiva sem redução dos indiferenciados? Um teste de observabilidade nos municípios da Amarsul (2023–2024)

**Série:** Almada Municipal Evidence · Working paper 01 · versão 0.1, 9 outubro 2026  
**Tipo:** análise descritiva preliminar, sem revisão por pares. **Autor científico e aprovação:** por confirmar pelo proprietário do repositório.  
**Âmbito:** nove municípios abrangidos pela Amarsul, Portugal, dois anos de atividade reportada pelo operador.

## Resumo

Testa-se a hipótese descritiva de que o crescimento da recolha seletiva é acompanhado, no mesmo período, por menor tonelagem de resíduos indiferenciados tratados. A fonte operacional da Amarsul publica três séries municipais para 2023 e 2024: recolha seletiva multimaterial, tratamento de biorresíduos e tratamento de indiferenciados. A transcrição controlada contém **54 registos** (9 municípios × 3 séries × 2 anos). Para Almada, a recolha seletiva multimaterial passou de **10 757 t para 12 838 t** (+19,35%), o tratamento de biorresíduos de **4 068 t para 4 682 t** (+15,09%) e o tratamento de indiferenciados de **66 267 t para 68 920 t** (+4,00%). Em oito dos nove municípios, seletivos e indiferenciados subiram simultaneamente. Estes números não permitem inferir a taxa de reciclagem, a taxa de captura, o êxito de uma política ou qualquer causalidade. Sugerem a necessidade de monitorização integrada de fluxos físicos, escala demográfica, composição e destinos.

**Palavras-chave:** resíduos urbanos; material flow analysis; Amarsul; Almada; indicadores; observabilidade; transparência de dados.

## 1. Pergunta e antecedentes

A transição circular não é observável apenas pela instalação de infraestruturas ou pelo crescimento de uma série positiva. Uma política pode aumentar simultaneamente a recolha seletiva e o fluxo residual se houver alterações no volume total de resíduos gerados, no perímetro do serviço, na composição ou no registo de entradas. O Roteiro Almada Circular 2030 prevê uma medida de circularidade de recursos e materiais (M5) e outra de construção circular (M6), mas uma estratégia municipal é distinta de uma avaliação de resultados.

Pergunta operacional: entre os dois anos publicados, uma maior recolha seletiva multimaterial coexistiu com menor tratamento de indiferenciados? Hipótese exploratória H1: os municípios mostram redução de indiferenciados quando cresce o seletivo. Hipótese nula descritiva: não existe padrão consistente. Este teste **não** estima o efeito causal da recolha seletiva.

## 2. Material, método e controlo

Fonte primária: tabela «Indicadores — Recolha seletiva Amarsul — Janeiro a dezembro de 2024», que apresenta pares de anos 2023/2024, por município:
https://www.amarsul.pt/umbraco/surface/indicadores/IndicadoresRecolhaSeletivaTemplate?PageID=14665

Os dados foram transcritos manualmente para `data/amarsul-2023-2024.csv`. Todas as entradas têm município, corrente, ano, toneladas, operador e edição. Os ficheiros `scripts/amarsul-summary.mjs` e `scripts/amarsul-summary.test.mjs` implementam transformações e verificações de consistência. O texto desta versão não equivale a prova de execução de testes no CI; antes de divulgação deve existir saída reproduzida num ambiente limpo e cotejo visual integral com a tabela do operador.

A variação absoluta é tonelagem em 2024 menos tonelagem em 2023. A variação relativa é 100 × (2024/2023 − 1). Crescimento simultâneo exige variações estritamente positivas nas duas séries. Um rácio auxiliar de seletivo/(seletivo + indiferenciado) é calculável, mas **não é taxa de reciclagem nem taxa oficial de recolha seletiva** e não é usado como métrica de desempenho.

Não se somam indiscriminadamente as três séries: «tratamento de biorresíduos» pode agregar fluxos cuja relação com outras séries depende das definições de origem/entrada no sistema. Nem todas as operações apresentadas cobrem necessariamente a produção municipal total.

## 3. Resultados

| Município | Seletivo 2023–24 (t) | Δ seletivo (%) | Indiferenciado 2023–24 (t) | Δ indiferenciado (%) |
|---|---:|---:|---:|---:|
| Alcochete | 1 129 → 1 508 | +33,57 | 7 653 → 7 514 | −1,82 |
| Almada | 10 757 → 12 838 | +19,35 | 66 267 → 68 920 | +4,00 |
| Barreiro | 3 801 → 4 585 | +20,63 | 26 209 → 26 993 | +2,99 |
| Moita | 3 034 → 3 762 | +23,99 | 23 524 → 24 477 | +4,05 |
| Montijo | 2 671 → 3 271 | +22,46 | 21 688 → 22 393 | +3,25 |
| Palmela | 3 659 → 4 508 | +23,20 | 26 559 → 28 910 | +8,85 |
| Seixal | 9 323 → 11 039 | +18,41 | 53 809 → 56 090 | +4,24 |
| Sesimbra | 3 405 → 4 116 | +20,88 | 24 083 → 25 418 | +5,54 |
| Setúbal | 6 124 → 7 309 | +19,35 | 49 662 → 49 683 | +0,04 |

**Resultado de sinal, não teste estatístico causal:** nove municípios apresentaram aumento seletivo; oito também cresceram nos indiferenciados; Alcochete foi a exceção neste intervalo. Em Almada, a diferença absoluta foi +2 081 t de seletivo e +2 653 t de indiferenciado. O facto de a recolha seletiva crescer percentualmente mais depressa não garante redução do volume final de resíduos ou melhoria proporcional da reciclagem efetiva.


## 3.1. Verificação independente: indicadores de tratamento ≠ receção de indiferenciados

O **Relatório e Contas Amarsul 2024**, na tabela `RI — Recolha Indiferenciada, Receção (ton)`, apresenta para Almada **85 742 t em 2023** e **86 589 t em 2024** de `RU Municipal` (crescimento de 847 t, cerca de 0,99%). São números materialmente distintos dos **66 267 t → 68 920 t** da página pública de indicadores de `tratamento de resíduos indiferenciados` usada nesta análise. A diferença entre os dois documentos é **19 475 t** em 2023 e **17 669 t** em 2024. Não se deve assumir equivalência entre receção de RU municipal e o subconjunto reportado na página de tratamento, nem concluir que se trata de um erro de qualquer fonte. O operador deverá esclarecer a delimitação exata e os fluxos excluídos de cada série.

| Série Amarsul (Almada) | 2023 (t) | 2024 (t) | Δ (t) | Δ (%) | Fonte |
|---|---:|---:|---:|---:|---|
| Indicador web, tratamento de indiferenciados | 66 267 | 68 920 | +2 653 | +4,00 | Página «Indicadores» |
| Relatório e Contas, receção de RU municipal | 85 742 | 86 589 | +847 | +0,99 | Relatório e Contas 2024, secção «Receção de Resíduos», quadro «RI — Recolha Indiferenciada» |

Fonte para a segunda linha: [Amarsul, Relatório e Contas 2024 (PDF), p. 41 no excerto indexado, numeração impressa do relatório a confirmar](https://www.amarsul.pt/media/v0ffpgvu/relatorio-e-contas-amarsul-2024_compressed.pdf). **Estado de verificação:** os valores são apresentados num excerto da fonte identificado por motor de pesquisa, mas a consulta integral do PDF foi limitada pelo tamanho do ficheiro; os números e a numeração exigem cotejo no PDF antes de citar como resultado auditado. A tabela dos indicadores web foi lida diretamente. O relatório também apresenta totais de âmbito Amarsul que não coincidem com o indicador web, reforçando a necessidade de um *data dictionary* oficial.

**Implicação de publicabilidade:** o resultado WP01 é um teste de consistência de publicações operacionais e de variações **dentro da mesma tabela web**. Não constitui um balanço completo de resíduos gerados no município. A reconciliação com RARU/MRRU é uma condição explícita de qualquer artigo que interprete desempenho, captura ou impacto causal.

## 4. Interpretações concorrentes e limites

Há pelo menos seis explicações por distinguir: (i) crescimento populacional/turístico ou da atividade económica; (ii) expansão territorial/operacional da recolha; (iii) maior geração de resíduos por pessoa; (iv) captação de materiais anteriormente não contabilizados; (v) alterações de composição, rejeitados e perdas entre recolha e valorização; (vi) diferenças entre recolha, receção, tratamento e destino final. A análise não isola qualquer delas.

Uma diferença de dois pontos temporais não estabelece tendência. Não foi construída série homogénea por habitante, por freguesia, por material, por domicílio servido nem por tratamento final. Os nove municípios partilham um operador, pelo que as observações não são amostras independentes de políticas municipais. Não se deve apresentar coeficiente de correlação como efeito de uma medida autárquica.

## 5. Que dados permitem uma análise publicável mais forte?

1. APA/RARU 2023 e RARU 2024 (edições e erratas), incluindo indicador municipal de captura de biorresíduos e documentação MRRU; reconciliar fluxos à mesma fronteira.
2. INE/PORDATA: população residente e população flutuante quando sustentada, ano e metodologia; calcular t/hab./ano comparáveis.
3. Amarsul/município: cobertura por recolha porta-a-porta, ecopontos, calendário, tecnologia, contaminação, rejeitados, destinos e biorresíduos de recolha seletiva versus mistura.
4. Contratos/BASE.gov.pt e orçamento municipal: investimento, CAPEX/OPEX, frequência e encargos operacionais, com deflatores e responsabilidades institucionais.
5. Série antes/depois de intervenções delimitadas e municípios/zonas de comparação; explicitar variáveis confundidoras e efeitos de registo antes de tentar inferência quase experimental.

## 6. Conclusão provisória

Nos números reportados pelo operador, **mais recolha seletiva não coincidiu com menos tratamento indiferenciado em Almada**, entre 2023 e 2024. É uma observação restrita, compatível com múltiplas explicações e insuficiente para avaliar o desempenho da política pública. O contributo do estudo é tornar explícita a lacuna entre fluxos publicados e uma avaliação municipal de circularidade que contabilize produção, captura, qualidade, recuperação efetiva, custos e distribuição territorial.

## Fontes e versões

- [Amarsul — Indicadores 2024, comparação com 2023](https://www.amarsul.pt/umbraco/surface/indicadores/IndicadoresRecolhaSeletivaTemplate?PageID=14665). Tabela operacional, consultada em 2026-10-09.
- [CM Almada — Almada Circular 2030](https://www.cm-almada.pt/almada-circular). Programa e medidas M1–M6, consultado em 2026-10-09.
- [APA — RARU 2024](https://apambiente.pt/destaque2/raru-2024-relatorio-anual-de-residuos-urbanos). Fonte de reconciliação futura, não usada para gerar os 54 registos desta análise.
- [APA — dados RARU e correções](https://apambiente.pt/residuos/dados-sobre-residuos-urbanos). A obter antes da versão 1.0.
