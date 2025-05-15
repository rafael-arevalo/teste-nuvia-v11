import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
from openai import OpenAI
import os

# Configure sua chave da API da OpenAI (recomendado usar variável de ambiente)
client = OpenAI(api_key="sk-")


# Extrai o título do artigo da URL fornecida
def extrair_titulo(url):
    path = urlparse(url).path
    return unquote(path.split('/')[-1].replace("_", " "))

# Scraping do conteúdo do artigo na Wikipedia
def extrair_conteudo_wikipedia(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragrafos = soup.select("div.mw-parser-output > p")
        texto = "\n".join(p.get_text().strip() for p in paragrafos if p.get_text().strip())
        return texto
    except Exception as e:
        return f"Erro ao acessar URL: {e}"

# Análise do conteúdo usando a API OpenAI com resposta estruturada em Markdown
def analisar_conteudo_com_openai(titulo, texto):
    prompt = f"""
Você é um linguista especializado em análise crítica de discurso e viés textual.

Analise o seguinte artigo da Wikipédia intitulado "{titulo}" com base no conteúdo abaixo:

\"\"\"{texto}\"\"\"

Gere um relatório completo estruturado em Markdown com os seguintes itens:

## 📊 01. Bias Score Geral:
- **Score:** XX/100
- **Classificação:** (viés forte/moderado/leve)

## 🔍 02. Resumo Geral do Viés:
(descrição breve e clara do viés encontrado)

## 🗺️ 03. Mapa de Viés por Categoria:
| Categoria                   | Score (0-100) | Comentário breve          |
|-----------------------------|---------------|---------------------------|
| Ideológico/político         | XX            | Comentário                |
| Emocional/afetivo           | XX            | Comentário                |
| Confirmatório               | XX            | Comentário                |
| Cultural/social             | XX            | Comentário                |
| Linguístico/sintático       | XX            | Comentário                |
| Omissão                     | XX            | Comentário                |
| Framing                     | XX            | Comentário                |
| Autoridade/credibilidade    | XX            | Comentário                |
| Intencionalidade retórica   | XX            | Comentário                |
| Viés industrial             | XX            | Comentário                |
| Viés governamental          | XX            | Comentário                |
| Viés ético                  | XX            | Comentário                |

## 🧾 04. Citações ou Trechos que Demonstram Viés:
Para cada trecho identificado, utilize a estrutura:

### Trecho:
> "Texto do trecho com viés"

- **Categoria(s) de Viés:** Categoria identificada
- **Explicação:** Justificativa clara da categoria atribuída ao trecho
- **Sugestão de Reformulação:** Sugestão objetiva de texto imparcial
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Função principal para realizar a análise completa e exibir o relatório formatado
def executar_analise(url):
    titulo = extrair_titulo(url)
    print(f"\n🔎 **Extraindo conteúdo do artigo:** {titulo}\n")
    conteudo = extrair_conteudo_wikipedia(url)

    if "Erro ao acessar URL" in conteudo:
        print(f"❌ {conteudo}")
        return

    print("📊 **Enviando conteúdo para análise com OpenAI...**\n")
    relatorio_markdown = analisar_conteudo_com_openai(titulo, conteudo)

    print("\n📝 **RELATÓRIO DE ANÁLISE (Markdown):**\n")
    print(relatorio_markdown)

# Exemplo de uso interativo
if __name__ == "__main__":
    url_usuario = input("🔗 Digite a URL de um artigo da Wikipédia sobre IA: ").strip()
    executar_analise(url_usuario)
