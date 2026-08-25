# poo-finance-atv-

Sistema financeiro desenvolvido para a disciplina de **Programação Orientada a Objetos II (POO II)**.

O projeto tem como objetivo aplicar, na prática, conceitos de Programação Orientada a Objetos por meio da construção de um pequeno domínio financeiro, utilizando classes, objetos, relacionamentos, regras de negócio e testes automatizados.

---

##  Objetivo do trabalho 

O **POO Financeiro** foi desenvolvido para representar operações básicas de um sistema financeiro.

O projeto permite:

- Criar e controlar contas;
- Criar categorias financeiras;
- Registrar lançamentos de crédito e débito;
- Validar regras de negócio;
- Realizar fechamentos financeiros;
- Calcular créditos, débitos e saldo;
- Verificar se um fechamento está conciliado;
- Gerar um extrato a partir de diferentes fechamentos;
- Testar automaticamente os comportamentos do sistema.

O foco desse meu projeto não é criar uma aplicação financeira completa e complexa, mas sim utilizar um domínio simples para demonstrar os conceitos estudados em POO até o momento.

---

# Domínio do sistema

O domínio financeiro é composto pelas seguintes classes:

- `Conta`
- `Categoria`
- `Lancamento`
- `Fechamento`
- `Conciliacao`
- `Extrato`

Cada classe possui uma responsabilidade específica dentro do sistema.

### Visão geral do projeto 


Conta
 │
 └── Representa uma conta financeira
       
Categoria
 │
 └── Classifica lançamentos

Lancamento
 │
 └── Representa uma movimentação financeira
       
Fechamento
 │
 └── Consolida lançamentos de um período
       │
       └── Calcula créditos, débitos e saldo
       
Conciliacao
 │
 └── Verifica se um fechamento está conciliado

Extrato
 │
 └── Consolida informações de diferentes fechamentos

 # Autora

**Ellen Martins**

Projeto acadêmico — **POO Financeiro**

Desenvolvido para a disciplina de Programação Orientada a Objetos II.