# 💵 Conversor de Moedas — Dólar e Real

Projeto desenvolvido em Python com o objetivo de estudar e praticar o consumo de APIs, utilizando a cotação do dólar americano (USD) em relação ao real brasileiro (BRL).

Esta foi minha primeira experiência utilizando uma API em um projeto Python. Durante o desenvolvimento, coloquei em prática conceitos como requisições HTTP, extração de dados em JSON, conversão de valores, funções, módulos e tratamento de entradas inválidas.

O projeto continuará recebendo melhorias conforme avanço nos estudos de programação.

## 🚀 Funcionalidades

- Consulta à cotação do dólar por meio da AwesomeAPI.
- Exibição dos valores de compra e venda.
- Conversão de dólar para real.
- Conversão de real para dólar.
- Menu interativo para selecionar a conversão desejada.
- Validação das opções e dos valores informados pelo usuário.

## 📂 Estrutura do projeto

- `main.py` — Menu principal que integra as funções e permite selecionar a operação.
- `buscar_cotacao.py` — Realiza a requisição à API, extrai os valores de compra e venda e trata possíveis erros.
- `dolar_real.py` — Consulta a cotação e realiza a conversão de dólar para real.
- `real_dolar.py` — Consulta a cotação e realiza a conversão de real para dólar.

## 🛠️ Tecnologias utilizadas

- **Python** — Linguagem de programação.
- **Requests** — Biblioteca utilizada para realizar requisições HTTP.
- **AwesomeAPI** — Serviço utilizado para obter a cotação USD/BRL.
- **JSON** — Formato dos dados retornados pela API.

## 📦 Instalação

É necessário ter o Python instalado na máquina.

**1. Clone o repositório:**

```bash
git clone URL_DO_SEU_REPOSITORIO
```

**2. Acesse a pasta do projeto:**

```bash
cd NOME_DA_PASTA
```

**3. Instale a biblioteca Requests:**

```bash
pip install requests
```

## ▶️ Como executar

Inicie o programa pelo arquivo principal:

```bash
python main.py
```

No menu, escolha uma das opções:

- `1` — Converter dólar para real.
- `2` — Converter real para dólar.
- `0` — Sair do programa.

Informe o valor desejado quando solicitado. O programa utiliza a cotação retornada pela API para calcular a conversão.

## 📚 Conceitos praticados

- Consumo de APIs com Python.
- Requisições HTTP com a biblioteca Requests.
- Extração e conversão de dados JSON.
- Conversões matemáticas entre moedas.
- Criação e utilização de funções.
- Importação e organização de módulos.
- Tratamento de exceções com `try/except`.
- Validação de entradas e construção de menus interativos.

## 🔧 Melhorias futuras

- Reutilizar a função de consulta à cotação nos módulos de conversão.
- Evitar requisições duplicadas à API.
- Aprimorar o tratamento de erros de conexão e respostas inesperadas.
- Melhorar a organização e a apresentação dos resultados no terminal.

---

**Projeto pessoal de estudo — minha primeira experiência com consumo de APIs utilizando Python.**

