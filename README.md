# Objetivo Geral
Criar um sistema bancário com as operações básicas: **sacar**, **depositar** e **visualizar extrato**.

## Desafio
### Funcionalidades:

1. **Depósito**:
   - Permitir o depósito de valores positivos na conta bancária.
   - Armazenar os valores depositados em uma variável.
   - Exibir os valores depositados na operação de extrato, no formato R$ xxx.xx.

2. **Saque**:
   - Permitir a realização de **3 saques diários**.
   - Limitar o valor máximo de cada saque em **R$ 500,00**.
   - Informar ao usuário a falta de saldo em caso de tentativa de saque sem saldo disponível.
   - Armazenar os valores sacados em uma variável.
   - Exibir os valores sacados na operação de extrato, no formato R$ xxx.xx.

3. **Extrato**:
   - Listar todos os depósitos e saques realizados na conta.
   - Exibir o saldo atual da conta ao final da listagem.
   - Exibir a mensagem "**Não foram realizadas movimentações**" se o extrato estiver em branco.

### Requisitos:
- A versão 1 do projeto trabalha apenas com um único usuário, dispensando a necessidade de identificação de agência e conta.

