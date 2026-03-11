import os
import asyncio
import re
from playwright.async_api import async_playwright
import pandas as pd

# CONFIGURAÇÕES 
PERFIL_URL = "https://x.com/TechDrop_News"
NOME_ARQUIVO_CSV = "relatorio_techdrop_limpo.csv"
QUANTIDADE_SCROLLS = 10 

def limpar_apenas_numeros(texto):
    """Extrai apenas os números de uma string (ex: '2 Curtidas' -> '2')"""
    if not texto:
        return "0"
    # Remove pontos de milhar e busca o número
    numeros = re.findall(r'\d+', texto.replace('.', '').replace(',', ''))
    return numeros[0] if numeros else "0"

async def run():
    async with async_playwright() as p:
        # 1. Abre o navegador com um User-Agent comum para evitar bloqueios
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # 2. Acessa o perfil
        print(f"Acessando o perfil: {PERFIL_URL}")
        await page.goto(PERFIL_URL)

        # Aguarda os artigos carregarem
        try:
            await page.wait_for_selector('article', timeout=15000)
        except:
            print("Erro: Não foi possível carregar os posts. Verifique a conexão ou se o perfil é público.")
            await browser.close()
            return

        # 3. Rola a página para carregar mais posts
        print(f"Rolando a página ({QUANTIDADE_SCROLLS}x)...")
        for i in range(QUANTIDADE_SCROLLS):
            await page.mouse.wheel(0, 2000)
            await page.wait_for_timeout(2000)
            print(f"  Scroll {i + 1}/{QUANTIDADE_SCROLLS}...")

        # 4. Seleciona todos os posts
        tweets = await page.query_selector_all('article')
        print(f"\n{len(tweets)} posts encontrados. Iniciando extração...\n")

        dados_finais = []

        for i, tweet in enumerate(tweets):
            try:
                # --- AUTOR (Limpando para pegar só o Nome e @) ---
                autor_elemento = await tweet.query_selector('div[data-testid="User-Name"]')
                autor_raw = await autor_elemento.inner_text() if autor_elemento else "Desconhecido"
                autor_final = autor_raw.split('·')[0].strip().replace('\n', ' ')

                # --- DESCRIÇÃO ---
                texto_elemento = await tweet.query_selector('div[data-testid="tweetText"]')
                texto_final = await texto_elemento.inner_text() if texto_elemento else "Sem texto"
                texto_final = texto_final.replace('\n', ' ')

                # --- DATA ---
                data_elemento = await tweet.query_selector('time')
                data_final = await data_elemento.get_attribute('datetime') if data_elemento else "Sem data"

                # --- URL DO TWEET ---
                link_elemento = await tweet.query_selector('a[href*="/status/"]')
                link_href = await link_elemento.get_attribute('href') if link_elemento else None
                link_final = f"https://x.com{link_href}" if link_href else "Sem link"

                # --- MÉTRICAS (Usando a função de limpeza) ---
                curtidas_raw = await tweet.query_selector('button[data-testid="like"]')
                curtidas_txt = await curtidas_raw.get_attribute('aria-label') if curtidas_raw else "0"
                
                reposts_raw = await tweet.query_selector('button[data-testid="retweet"]')
                reposts_txt = await reposts_raw.get_attribute('aria-label') if reposts_raw else "0"
                
                respostas_raw = await tweet.query_selector('button[data-testid="reply"]')
                respostas_txt = await respostas_raw.get_attribute('aria-label') if respostas_raw else "0"
                
                views_raw = await tweet.query_selector('a[href*="/analytics"]')
                views_txt = await views_raw.get_attribute('aria-label') if views_raw else "0"

                # --- MÍDIA ---
                tem_imagem = await tweet.query_selector('div[data-testid="tweetPhoto"]')
                tem_video = await tweet.query_selector('div[data-testid="videoPlayer"]')
                tipo_midia = "imagem" if tem_imagem else ("video" if tem_video else "nenhuma")

                # Monta o objeto com dados LIMPOS
                dados_finais.append({
                    "autor": autor_final,
                    "descricao": texto_final,
                    "data": data_final,
                    "url_tweet": link_final,
                    "curtidas": limpar_apenas_numeros(curtidas_txt),
                    "reposts": limpar_apenas_numeros(reposts_txt),
                    "respostas": limpar_apenas_numeros(respostas_txt),
                    "visualizacoes": limpar_apenas_numeros(views_txt) if "visualização" in views_txt.lower() else "0",
                    "midia": tipo_midia,
                })

                print(f"  ✅ Post {i + 1} extraído.")

            except Exception as e:
                print(f"  ⚠️ Erro no post {i + 1}: {e}")
                continue

        # 5. Salva em CSV
        pasta_destino = 'saidas_scrapings'
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        df = pd.DataFrame(dados_finais)
        df = df.drop_duplicates(subset=['url_tweet']) # Garante que não há repetidos

        caminho_csv = os.path.join(pasta_destino, NOME_ARQUIVO_CSV)
        df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')

        print(f"\n{'='*50}")
        print(f"🎉 SUCESSO! {len(df)} posts salvos em: {caminho_csv}")
        print(f"{'='*50}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())