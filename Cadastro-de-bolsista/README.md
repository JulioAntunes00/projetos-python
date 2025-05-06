# Cadastro de Alunos com Herança – POO em Python

Este projeto foi criado com o objetivo de praticar os fundamentos da Programação Orientada a Objetos (POO) em Python, utilizando herança, atributos e métodos.

---

## O que o projeto faz

- Cria objetos do tipo `Aluno` com nome, curso, idade e mensalidade.
- Cria objetos do tipo `AlunoBolsista` (que herdam de `Aluno`) e permite aplicar um desconto na mensalidade com o método `aplicar_desconto`.
- Exibe todos os dados do aluno no terminal com o método `mostrar_dados`.

---

## Classes

### `Aluno`
- Atributos:
  - `nome`
  - `curso`
  - `idade`
  - `mensalidade`
- Métodos:
  - `mostrar_dados()`: exibe todos os dados do aluno

### `AlunoBolsista` (herda de `Aluno`)
- Métodos:
  - `aplicar_desconto(porcentagem)`: aplica um desconto percentual sobre a mensalidade

---

## Exemplo de uso.

```python
aluno1 = Aluno("Marcos", "ADM", 22, 450.00)
aluno1.mostrar_dados()

aluno2 = AlunoBolsista("André", "Psicologia", 19, 630.00)
aluno2.aplicar_desconto(50)
aluno2.mostrar_dados()
