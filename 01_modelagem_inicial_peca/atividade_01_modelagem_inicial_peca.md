# Atividade 01 — Modelagem inicial de peça no Solid Edge

## Objetivo

Modelar a peça proposta.

## Proposta

### Desenho cotado

![Desenho cotado da peça](assets/image2.png)

### Modelo 3D de referência

![Modelo 3D da peça](assets/image1.png)

---

## Passos

### 1. Criar uma nova peça

Clique em **New Part**.

![New Part](assets/image3.png)

### 2. Selecionar o modo de trabalho

Clique em **Continue with Ordered**.

![Continue with Ordered](assets/image4.png)

### 3. Iniciar a extrusão

Clique em **Extrude**.

![Extrude](assets/image5.png)

### 4. Selecionar o plano XY

Selecione o plano **XY** para iniciar o esboço.

![Seleção do plano XY](assets/image6.png)

### 5. Criar um retângulo pelo centro

Selecione a ferramenta **Rectangle by Center**.

![Rectangle by Center](assets/image7.png)

### 6. Posicionar o retângulo

Clique uma vez na referência central, solte o botão do mouse e arraste para definir o retângulo.

![Posicionamento do retângulo](assets/image8.png)

### 7. Definir as dimensões externas

Defina o retângulo com as medidas:

- **150 mm** de largura;
- **100 mm** de altura.

![Retângulo 150 x 100 mm](assets/image9.png)

### 8. Aplicar chanfro

Selecione a ferramenta **Chamfer**.

![Ferramenta Chamfer](assets/image10.png)

### 9. Configurar o chanfro

Defina as medidas do chanfro conforme a proposta.

![Configuração do Chamfer](assets/image11.png)

### 10. Selecionar os lados do chanfro

Clique nos dois lados do canto e, em seguida, na linha diagonal indicada pela ferramenta.

![Seleção dos lados para o chanfro](assets/image12.png)

### 11. Chanfrar todos os cantos

Repita o procedimento nos quatro cantos da peça.

![Contorno externo com chanfros](assets/image13.png)

### 12. Criar o retângulo interno

Selecione novamente **Rectangle by Center**.

![Rectangle by Center](assets/image7.png)

### 13. Definir o retângulo interno

Adicione um novo retângulo central com as dimensões:

- **100 mm** de largura;
- **40 mm** de altura.

![Retângulo interno 100 x 40 mm](assets/image14.png)

### 14. Aplicar filete

Selecione a ferramenta **Fillet** e configure o raio para **5 mm**.

![Ferramenta Fillet](assets/image15.png)

### 15. Filetar todos os cantos internos

Aplique o filete de **5 mm** nos quatro cantos do retângulo interno.

![Retângulo interno com filetes](assets/image16.png)

### 16. Finalizar a extrusão

Finalize a extrusão com espessura de **20 mm**.

![Extrusão da peça](assets/image17.png)

### 17. Iniciar a criação dos furos

Selecione a ferramenta **Hole**.

![Ferramenta Hole](assets/image18.png)

### 18. Selecionar a face da peça

Clique na face frontal da peça para posicionar o furo.

![Seleção da face para o furo](assets/image19.png)

### 19. Criar o primeiro furo

Adicione um furo com:

- **diâmetro de 12 mm**;
- posicionamento de **15 mm x 15 mm** em relação às bordas indicadas.

Finalize o furo.

![Furo de 12 mm posicionado a 15 x 15 mm](assets/image20.png)

### 20. Iniciar o padrão de furos

Abra **Pattern**, selecione o furo criado e confirme a seleção pelo indicador **Selected**.

![Seleção do furo no Pattern](assets/image21.png)

### 21. Selecionar o padrão retangular

Selecione o plano e clique em **Rectangular Pattern**.

![Rectangular Pattern](assets/image22.png)

### 22. Definir a direção do padrão

Posicione o mouse no centro do furo, clique e arraste para definir a direção do padrão.

![Definição da direção do padrão](assets/image23.png)

### 23. Definir os afastamentos

Coloque as cotas de **15 mm** em cada lado indicado.

![Cotas de 15 mm](assets/image24.png)

### 24. Definir a quantidade de furos

Configure a quantidade de ocorrências do padrão:

- **X = 3**;
- **Y = 2**.

Conclua o comando.

![Quantidade de furos em X e Y](assets/image25.png)

---

## Resultado esperado

Ao final da atividade, a peça deverá apresentar:

- contorno externo de **150 x 100 mm**;
- cantos externos chanfrados;
- abertura interna de **100 x 40 mm** com filetes de **5 mm**;
- espessura de **20 mm**;
- furos de **12 mm** distribuídos por padrão retangular.

![Resultado esperado](assets/image1.png)
