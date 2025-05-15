# Análise de Viés Textual com LLMs.

Este projeto realiza **web scraping de artigos da Wikipédia** e utiliza **modelos da OpenAI** para gerar relatórios críticos sobre **viés textual** de forma estruturada em Markdown.

---

## Objetivo

O objetivo principal é permitir que qualquer pessoa possa **analisar criticamente conteúdos online**, identificando **diferentes tipos de vieses textuais** que moldam a percepção da informação.

---

## Abordagem Conceitual

### O que é Viés Contextual?

Viés textual ou discursivo ocorre quando a apresentação de informações **não é neutra** e reflete, de forma explícita ou sutil, preferências, julgamentos ou intenções ideológicas, emocionais, culturais ou retóricas.

Este projeto se baseia em uma **tipologia multidimensional** de viés:

- **Ideológico/Político**: favorecimento de correntes ou partidos.
- **Emocional/Afetivo**: uso de linguagem que evoca emoções específicas.
- **Confirmatório**: reforço de crenças prévias do leitor.
- **Cultural/Social**: normatização de visões de mundo específicas.
- **Linguístico/Sintático**: forma gramatical e vocabulário enviesado.
- **Omissão**: ausência intencional de informações relevantes.
- **Framing (enquadramento narrativo)**: como os eventos são estruturados.
- **Autoridade/Credibilidade**: fontes utilizadas e sua confiabilidade.
- **Intencionalidade Retórica**: objetivo persuasivo embutido no texto.
- **Viés Industrial/Governamental/Ético**: interesses institucionais ocultos.

---

## Abordagem Técnica

O script combina duas etapas:

1. **Extração de Conteúdo via Web Scraping**  
   Utiliza `requests` e `BeautifulSoup` para coletar e limpar o texto principal de artigos da Wikipédia a partir de uma URL fornecida.

2. **Análise com OpenAI GPT-4**  
   Envia o conteúdo bruto com um prompt cuidadosamente estruturado para o modelo da OpenAI, que retorna:
   - Um **Bias Score Geral** com classificação (forte, moderado, leve);
   - Um **resumo crítico do viés** encontrado;
   - Um **mapa de categorias de viés** com pontuações por dimensão;
   - **Citações com viés identificadas**, explicadas e reformuladas.

A resposta é retornada no formato **Markdown**, pronta para leitura ou publicação.

---

## 🛠️ Como usar

1. No terminal, clone o repositório deste projeto.
   ```
   git clone https://github.com/rafael-arevalo/teste-nuvia-v11.git
   ```
2. Depois, entre na pasta do projeto.
   ```
   cd teste-nuvia-v11.git
   ```
3. Crie um ambiente virtual (opcional, mas recomendado)
   ```
   python venv venv
   ```

   Agora, ative o ambiente virtual criado:
   - No Windows:
       ```
       venv\Scripts\activate
       ```
   - No Mac/Linux:
       ```
       source venv/bin/activate
       ```
       
4. Inclua a chave da API da OpenAI no script `teste-nuvia-v11.py`.
   ```
   client = OpenAI(api_key="insira aqui a chave API da OpenAI")
   ```
   Agora, salve o arquivo `teste-nuvia-v11.py` para salver o script com a chave API da OpenAI.
5. Instale as dependências do projeto contidas no arquivo `requirements.txt`
   ```
   uv pip install -r requirements.txt
   ```
6. Execute o script no terminal :
   ```
   python teste-nuvia-v11.py
   ```
7. Assim que solicitado, insira a URL de um artigo da Wikipédia sobre algum tema de Inteligência Artificial.
8. Aguarde até que o relatório com a análise de viés seja exibido no terminal.

---

## 📋 Exemplo de Saída
- URL da Wikipedia utilizada sobre o DeepSeek (https://pt.wikipedia.org/wiki/DeepSeek)

## 📊 01. Bias Score Geral:
- **Score:** 65/100
- **Classificação:** Moderado

## 🔍 02. Resumo Geral do Viés:
O conteúdo exibe algum grau de viés, especialmente em termos de viés cultural/social e viés industrial. A apresentação da DeepSeek como uma empresa superior a outras, como OpenAI, pode ser considerada um viés. Além disso, a alusão a eventos políticos como sanções pode introduzir um viés ideológico. Existem alguns sinais de viés de omissão, ao excluir certas informações, proporcionando apenas um lado do panorama.

## 🗺️ 03. Mapa de Viés por Categoria:

| Categoria                   | Score (0-100) | Comentário breve          |
|-----------------------------|---------------|---------------------------|
| Ideológico/político         | 60            | Alusão a eventos políticos nas relações internacionais|
| Emocional/afetivo           | 50            | O texto gera uma visão favorável pela DeepSeek |
| Confirmatório               | 50            | Não há indicação clara de viés confirmatório |
| Cultural/social             | 70            | Orientado para a visão positiva de uma empresa chinesa |
| Linguístico/sintático       | 70            | A repetição de comparações favoráveis apresenta viés |
| Omissão                     | 70            | Certas informações parecem ser omitidas |
| Framing                     | 60            | Enquadramento que promove a visão favorável de uma empresa |
| Autoridade/credibilidade    | 60            | Atribuição de autoridade à empresa por meio de conquistas |
| Intencionalidade retórica   | 60            | A intenção parece promover uma visão positiva da empresa |
| Viés industrial             | 70            | A visão positiva de uma única empresa em detrimento de outras |
| Viés governamental          | 60            | Sugestão do apoio governamental à tecnologia chinesa |
| Viés ético                  | 50            | Nenhum viés ético evidente foi encontrado |

## 🧾 04. Citações ou Trechos que Demonstram Viés:

### Trecho:
> "O modelo DeepSeek-R1 apresentou desempenho superior em testes com modelos otimizados para processamento de imagens e análise de dados complexos, quando comparado a outros modelos de linguagem de grande porte contemporâneos, como o GPT-4 da OpenAI."

- **Categoria(s) de Viés:** Viés industrial, Framing, Intencionalidade retórica
- **Explicação:** Este trecho compara diretamente o DeepSeek-R1 ao GPT-4 da OpenAI, afirmando que o primeiro é superior. Isso reflete um viés industrial, pois promove abertamente a superioridade de um produto sobre outro.
- **Sugestão de Reformulação:** "O modelo DeepSeek-R1 mostrou um bom desempenho em testes com modelos otimizados para processamento de imagens e análise de dados complexos, assim como outros modelos contemporâneos de linguagem de grande porte, como o GPT-4 da OpenAI."

### Trecho: 
> "Ele foi treinado a um custo significativamente mais baixo, US$ 6 milhões, em comparação com US$ 100 milhões para o GPT-4 da OpenAI em 2023."

- **Categoria(s) de Viés:** Viés industrial, Framing
- **Explicação:** Este trecho salienta a suposta eficiência de custo do modelo DeepSeek-R1 em comparação ao GPT-4 da OpenAI, criando um viés industrial que favorece o primeiro.
- **Sugestão de Reformulação:** "O custo de treinamento do modelo DeepSeek-R1 foi de US$ 6 milhões, enquanto o custo de treinamento para outros modelos contemporâneos, como o GPT-4 da OpenAI, foi registrado em torno de US$ 100 milhões em 2023."

---

## 📚 Requisitos

- Python 3.8+
- `requests`, `beautifulsoup4`, `openai`

---

## 📄 Licença

Este projeto é open-source sob a licença MIT.
