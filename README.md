# web-scraping-eduardod

# Web Scraping do X (Twitter) com Python

## Descrição do Projeto

Este projeto foi desenvolvido para a disciplina com o objetivo de realizar **coleta de dados (Web Scraping)** de publicações do X (antigo Twitter) utilizando **Python**.

O script acessa automaticamente o perfil de um usuário, coleta informações das publicações e salva esses dados em um **arquivo CSV estruturado**, que pode ser aberto no Excel ou utilizado para análise de dados.

O perfil utilizado para coleta foi:
https://x.com/TechDrop_News

---

## Tecnologias Utilizadas

* Python
* Playwright (automação de navegador)
* Pandas (organização e exportação dos dados)
* Asyncio (execução assíncrona)

---

## Informações coletadas

O script coleta várias informações de cada post encontrado no perfil:

* Autor do post
* Texto da publicação
* Data da postagem
* URL do post
* Número de curtidas
* Número de reposts
* Número de respostas
* Número de visualizações
* Tipo de mídia (imagem, vídeo ou nenhuma)

Essas informações são armazenadas em uma estrutura de dados e depois exportadas para um arquivo `.csv`.

---

## Funcionamento do Script

O programa funciona da seguinte forma:

1. Abre automaticamente um navegador usando Playwright.
2. Acessa o perfil do usuário configurado no código.
3. Realiza rolagem da página para carregar mais posts.
4. Localiza os elementos HTML das publicações.
5. Extrai as informações de cada postagem.
6. Armazena os dados em uma lista.
7. Converte os dados para um DataFrame usando Pandas.
8. Salva os dados em um arquivo CSV.

Também é feito um tratamento para **remover posts duplicados** antes de salvar o arquivo.

---

## Arquivo Gerado

Após a execução do script, é criada uma pasta chamada:

saidas_scrapings

Dentro dela é gerado o arquivo:

relatorio_techdrop.csv

Esse arquivo contém todos os dados coletados das publicações.

---

## Observações

A quantidade de posts coletados pode ser alterada modificando a variável:

QUANTIDADE_SCROLLS

Quanto maior o valor, mais posts serão carregados e coletados pelo script.

---

## Autor

Projeto desenvolvido por estudante de Ciência da Computação como atividade prática de **Web Scraping e coleta de dados utilizando Python**.
