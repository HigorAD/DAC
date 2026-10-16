# Atividade 07 — Suporte para fixação de tubo no Solid Edge

**Disciplina:** Desenho Assistido por Computador (DAC)  
**Software:** Solid Edge  
**Ambientes:** Part / Ordered e Draft  
**Unidades:** milímetros (mm)

## 1. Objetivo

Modelar uma peça a partir de requisitos dimensionais e produzir seu desenho técnico, combinando esboços cotados, extrusões, furos passantes, padrão retangular, furo roscado e chanfros.

## 2. Proposta

Modele um **suporte para fixação de tubo** constituído por uma base retangular e um ressalto central, formando uma única peça. O tubo atravessará um furo horizontal no ressalto. Um furo roscado na face superior permitirá a instalação de um parafuso de travamento.

O tubo e o parafuso são apenas referências de funcionamento: a entrega compreende somente o suporte, sem montagem.

![Vistas superior e frontal cotadas do suporte, mostrando a base, o ressalto e a posição dos furos](assets/01_vistas_cotadas.png)

**Figura 1 — Vistas de referência.** As dimensões representam os contornos nominais antes dos chanfros. São vistas de estudo apresentadas separadamente; sua disposição não estabelece um sistema de projeção. Todas as cotas estão em milímetros.

### 2.1. Dimensões e requisitos

| Elemento | Dimensão / requisito |
|---|---|
| Base | 100 × 60 × 10 mm |
| Ressalto | 40 × 30 × 30 mm, centralizado sobre a base |
| Orientação do ressalto | 40 mm paralelos aos 100 mm da base; 30 mm paralelos aos 60 mm da base |
| Altura total | 40 mm, incluindo base e ressalto |
| Furos de fixação | Quatro furos passantes de Ø8 mm na base |
| Posição dos furos de fixação | Um próximo a cada canto, com centro a 12 mm de cada uma das duas bordas adjacentes |
| Furo para o tubo | Ø16 mm, passante no ressalto, ao longo da dimensão de 30 mm |
| Posição do eixo do furo para o tubo | Centralizado na dimensão de 40 mm do ressalto e a 25 mm da face inferior da base |
| Furo roscado de travamento | M8, padrão ISO Metric, passo normal da tabela do software |
| Posição do furo roscado | No centro da face superior do ressalto, vertical e com eixo que intercepta o eixo do furo de Ø16 mm |
| Extensão do furo roscado | 10 mm a partir da face superior, em direção à base, comunicando-se com o furo de Ø16 mm |
| Chanfros | 1 × 45° em arestas externas escolhidas pelo aluno |

**Referência para a profundidade da rosca:** os 10 mm definem a extensão nominal do recurso a partir da face superior. Parte dessa extensão encontra o vazio do furo horizontal; portanto, não corresponde a 10 mm contínuos de rosca em material.

![Corte didático pelo centro do suporte, mostrando a comunicação do furo vertical M8 com o furo horizontal de Ø16 mm](assets/02_corte_comunicacao.png)

**Figura 2 — Funcionamento do travamento.** O corte está no plano central do suporte, paralelo à direção do furo horizontal. A hachura representa material; as regiões brancas internas representam os furos. A rosca está simplificada. O corte serve para interpretar a peça e não precisa ser reproduzido pelo aluno se esse recurso ainda não tiver sido estudado.

Use as dimensões nominais dos contornos antes dos chanfros como referência para posicionar os furos. Os chanfros não devem modificar suas posições nem eliminar detalhes funcionais.

## 3. Tarefas

1. Crie um arquivo **Part**, no modo **Ordered**, com unidades em milímetros.
2. Modele a base e o ressalto com esboços dimensionados, mantendo a centralização entre eles.
3. Crie os quatro furos de fixação. Utilize um **padrão retangular** para distribuir as ocorrências.
4. Crie o furo horizontal para passagem do tubo.
5. Crie o furo roscado M8 e confira sua comunicação com o furo horizontal.
6. Aplique os chanfros e registre no desenho quais arestas os recebem.
7. Gere o desenho técnico no ambiente **Draft**.
8. Revise o modelo, atualize as vistas e exporte o desenho em PDF.

## 4. Desenho técnico

Apresente as vistas ortográficas necessárias para definir a peça e uma vista isométrica. Escolha como vista principal aquela em que o furo de Ø16 mm aparece como círculo.

O desenho deverá conter:

- dimensões da base e do ressalto, com informações suficientes para estabelecer sua centralização;
- altura total ou indicação inequívoca da altura do ressalto acima da base;
- quantidade, diâmetro e posicionamento dos quatro furos de fixação;
- diâmetro, posição e condição passante do furo para o tubo;
- identificação M8 e profundidade nominal de 10 mm do recurso roscado;
- indicação dos chanfros aplicados;
- linhas de centro, escala e quadro de identificação preenchido.

Organize as vistas conforme o sistema de projeção adotado na disciplina. Evite cotas duplicadas, sobrepostas ou desnecessárias. Se a comunicação entre os furos não ficar clara nas vistas escolhidas, utilize uma anotação explicativa; uma vista em corte pode ser acrescentada como recurso complementar, se já tiver sido trabalhada em aula.

## 5. Entrega

| Arquivo | Nome sugerido |
|---|---|
| Modelo 3D nativo | `Nome_Suporte_Tubo.par` |
| Desenho técnico editável | `Nome_Suporte_Tubo.dft` |
| Desenho técnico exportado | `Nome_Suporte_Tubo.pdf` |

Mantenha os arquivos `.par` e `.dft` na mesma pasta e confira se o desenho continua vinculado ao modelo entregue.

## 6. Critérios de avaliação

| Critério | Peso |
|---|---:|
| Geometria, dimensões e comunicação entre os furos | 40% |
| Esboços dimensionados e organização dos recursos de modelagem | 20% |
| Vistas, cotagem e clareza do desenho técnico | 30% |
| Organização, identificação e apresentação dos arquivos | 10% |

## 7. Conferência antes da entrega

- [ ] Base e ressalto formam uma única peça.
- [ ] O ressalto está centralizado e a altura total é 40 mm.
- [ ] Os quatro furos de Ø8 mm são passantes e estão nas posições solicitadas.
- [ ] O furo de Ø16 mm atravessa a dimensão de 30 mm do ressalto.
- [ ] Seu eixo está a 25 mm da face inferior da base.
- [ ] O furo M8 está centralizado no topo e se comunica com o furo de Ø16 mm.
- [ ] Os chanfros são de 1 × 45° e estão identificados no desenho.
- [ ] As vistas estão atualizadas e as cotas estão legíveis.
- [ ] Os três arquivos solicitados foram entregues.

---

**Material complementar do professor:** [resolução comentada](resolucao_suporte_para_fixacao_de_tubo.md).
