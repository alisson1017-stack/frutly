# Requisitos:

<br>

**Dados:**
- frutas (string)
- ID
- valor (float)
- margem de lucro (float)
- mês (string)
- quantidade vendida (int)
<br>

**Estrutura dos dados:**

- Mês [dict]:
    - mês [dict]:
        - ID da fruta*
            - quantidade vendida

- fruta [dict]:
    - ID [dict]:
        - ID da fruta*
        - nome
        - valor
        - margem de lucro

<br>

**Input:**
- Nome da fruta (string)
- ID da fruta (string)
- N° de vendas (int)
- Valor da fruta (float)
- Margem de lucro (float)

<br>

**Output:**
- **comparação fruta:**
    - unidades vendidas
    - valor total vendido
    - valor líquido vendido
        - *x margem de lucro*

- **comparação mês:**
    - unidades vendidas
    - valor total vendido
    - valor líquido vendido
        - *x margem de lucro*

<br>

# Funcionalidades:

**Todas:**

- adicionar fruta
- adicionar mês
- listar frutas
- listar meses
- alterar info dos meses
- alterar info das frutas
- comparar frutas por quantidade vendida
- comparar frutas por valor total vendido
- comparar frutas por valor líquido vendido
- comparar meses por quantidade vendida
- comparar meses por valor total vendido
- comparar meses por valor líquido vendido

<br>

**Menu:**

- **Listar frutas:**
    - listar frutas( )

<br>

- **Listar Meses:**
    - listar meses( )

<br>

- **Editar frutas:**
    - adicionar fruta( )
    - alterar info das frutas( )
    - excluir fruta( )

<br>

- **Editar meses:**
    - alterar info dos meses( )
    - adicionar mês( )
    - excluir mês( )

<br>

- **Adicionar fruta:**
    - adicionar fruta( )

<br>

- **Adicionar mês:**
    - adicionar mês( )

<br>

- **Comparar:**
    - **Comparar Frutas:**
        - comparar frutas por quantidade vendida
        - comparar frutas por valor total vendido( )
        - comparar frutas por valor líquido vendido( )

    <br>

    - **Comaprar Meses:**
        - comparar meses por quantidade vendida( )
        - comparar meses por valor total vendido( )
        - comparar meses por valor líquido vendido( )
