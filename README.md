# 📊 Gerenciador Financeiro Simples (Terminal)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Uma aplicação prática em Python para controle de finanças pessoais. Este projeto simula uma "mini base de dados" financeira, permitindo registrar, analisar e exportar seus gastos diários diretamente pelo terminal.

## 🎯 Objetivo
Desenvolvido para consolidar conceitos fundamentais de lógica de programação, manipulação de estruturas de dados compostas e persistência de dados (I/O).

---

## 🛠️ Funcionalidades

O sistema oferece uma interface interativa com as seguintes opções:

* **➕ Adicionar Gasto:** Registro de descrição, valor e categoria com validação (impede valores negativos e erros de digitação).
* **📜 Listar Gastos:** Exibição organizada e numerada de todos os registros (formato de extrato).
* **💰 Mostrar Total:** Cálculo instantâneo da soma de todos os gastos.
* **🔍 Filtrar por Categoria:** Busca segmentada ignorando diferenciação entre maiúsculas e minúsculas.
* **📂 Exportar Dados:** Geração de um arquivo `.txt` com o relatório completo para uso externo.
* **🏆 Estatísticas (Bônus):** Insight de média aritmética, identificação do maior e do menor gasto.

---

## 🧱 Modelo de Dados

Os dados são organizados em uma estrutura de lista contendo dicionários, o que facilita a análise futura para Data Science ou IA:

```python
lista_de_gastos = [
    {
        "descrição": "Exemplo",
        "valor": 50.00,
        "categoria": "Alimentação"
    }
]
```
## 
🪜 Etapas de Desenvolvimento
O desenvolvimento foi dividido em fases para garantir a robustez do código:

- Estrutura Inicial: Criação do loop principal e tratamento de erros com try/except.
- Captura de Dados: Validação para impedir valores negativos ou tipos de dados incorretos.
- Visualização: Uso de enumerate para listar os itens de forma legível.
- Análise: Implementação de cálculos matemáticos sobre a lista de dicionários.
- Filtragem: Normalização de strings (lower()) para buscas precisas.
- Persistência: Manipulação de arquivos para salvamento do relatório final.

## 🚀 Como Rodar o Projeto

1. Clone o repositório
```
git clone [https://github.com/seu-usuario/gerenciador-financeiro.git](https://github.com/seu-usuario/gerenciador-financeiro.git)
```
2. Acesse a pasta
```
cd gerenciador-financeiro
```
3. Execute o programa
```
python gerenciador.py
```
## 💻 Exemplo de Uso (Preview)
```
--- MENU FINANCEIRO ---
1. Adicionar Gasto
2. Listar Gastos
3. Mostrar Total
4. Filtrar por Categoria
5. Exportar Relatório
6. Sair
-----------------------
Escolha: 1
Descrição: Café
Valor: 5.50
Categoria: Alimentação
✅ Gasto adicionado com sucesso!
```

## 🧠 Conceitos Aplicados

- Python Essentials: Variáveis, listas, dicionários e loops (while).
- Robustez: Tratamento de exceções para evitar crashes.
- Data Handling: Filtragem e agregação de valores.
- I/O de Arquivos: Leitura e escrita em arquivos de texto.

## 👨‍💻 Autor
Arthur Lanzoni
