# poo-finance-atv-

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos II, com o objetivo de aplicar conceitos de POO em um pequeno sistema financeiro ensinado em sala de aula.

O projeto possui as classes `Conta`, `Categoria`, `Lancamento`, `Fechamento`, `Conciliacao` e `Extrato`, além de testes automatizados utilizando o `pytest`.

# Decisões de projeto

# 1. No Fechamento, os Lancamentos são copiados ou referenciados?

Os `Lancamentos` são **referenciados**, e não copiados.

O `Fechamento` em si recebe uma lista de lançamentos e mantém essa mesma referência. Essa decisão foi tomada porque não é necessário criar novos objetos para realizar os cálculos do período. Assim, o fechamento vai  apenas utilizar os lançamentos já existentes para calcular totais, créditos, débitos e saldo.

# 2. Conciliacao é uma classe própria ou um método de Fechamento?

A `Conciliacao` foi criada como uma **classe própria**.

O `Fechamento` é responsável por organizar os lançamentos e realizar os cálculos financeiros, enquanto a `Conciliacao` fica responsável por verificar se esses valores estão ok e equilibrados.

# 3. O que acontece quando não existem Lancamentos no período?

Quando não existem lançamentos, o `Fechamento` continua sendo válido. Os cálculos retornam `0`, pois não há valores para somar.

Exemplo:

* Total = `0`
* Créditos = `0`
* Débitos = `0`
* Saldo = `0`

Não é exatamente considerada uma situação de erro.

# 4. E quando a conciliação não bate?

Quando os créditos e débitos são diferentes, a conciliação retorna `False` através do método `esta_conciliado()`.

Não é lançada uma exceção, pois uma divergência de valores não impede o funcionamento do sistema. Apenas indica que aquele fechamento não está conciliado.

## Testes

Foram criados testes automatizados com `pytest`, incluindo casos de sucesso e situações inválidas para verificar as regras de negócio das classes e fazer com que tudo de certo.

Para executar:

```bash
python3 -m pytes
```

Todos os testes desenvolvidos para o projeto estão passando.


 # Autora

**Ellen Martins**

Projeto acadêmico — **POO Financeiro**

Desenvolvido para a disciplina de Programação Orientada a Objetos II.
