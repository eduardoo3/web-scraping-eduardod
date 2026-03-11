# Web Scraping do X (Twitter) com Python

## Descrição do Projeto

Este projeto foi desenvolvido como atividade da disciplina para realizar **coleta de dados (Web Scraping)** de publicações do X (Twitter) utilizando Python.

O script acessa automaticamente um perfil, coleta informações das publicações e salva esses dados em um **arquivo CSV estruturado**, que pode ser aberto no Excel ou utilizado para análise de dados.

Perfil utilizado para coleta:
https://x.com/TechDrop_News

## Tecnologias Utilizadas

* Python
* Playwright (automação de navegador)
* Pandas (organização e exportação de dados)
* Asyncio (execução assíncrona)

## Informações Coletadas

O script coleta as seguintes informações de cada postagem:

* Autor do post
* Texto da publicação
* Data da postagem
* URL do post
* Número de curtidas
* Número de reposts
* Número de respostas
* Número de visualizações
* Tipo de mídia (imagem, vídeo ou nenhuma)

Esses dados são armazenados e depois exportados para um arquivo `.csv`.

## Funcionamento do Script

O programa:

1. Abre automaticamente um navegador usando Playwright
2. Acessa o perfil configurado no código
3. Rola a página para carregar mais posts
4. Localiza os elementos HTML das publicações
5. Extrai as informações de cada postagem
6. Armazena os dados em uma lista
7. Converte os dados para um DataFrame com Pandas
8. Salva os dados em um arquivo CSV

Antes de salvar, o script também remove **posts duplicados**.

## Arquivo Gerado

Após a execução do script é criada a pasta:

`saidas_scrapings`

Dentro dela é gerado o arquivo:

`relatorio_techdrop.csv`

## Observação

A quantidade de posts coletados pode ser alterada modificando a variável:

`QUANTIDADE_SCROLLS`

## Autor

Projeto desenvolvido por estudante de **Ciência da Computação** como atividade prática de Web Scraping com Python.
