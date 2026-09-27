# 🏊‍♂️ Sistema de Gestão de Toalhas — Escola de Natação

## 👥 Identificação da Equipe
- **Nome do Projeto:** Sistema de Controle e Gestão de Toalhas (SwimTowel Manager)
- **Integrantes da Equipe:**
  - [Daniel Henry]
  - [Luiz Guilherme Costa]
  - [Igor Gabriel Militão]

---

## 💻 Apresentação do Sistema

### 1. Contexto e Problema
Em escolas de natação com grande fluxo diário de alunos, a gestão do enxoval de toalhas é um desafio operacional. A perda de itens, o descontrole sobre quem retirou ou devolveu, a falta de visibilidade da quantidade de toalhas limpas versus em higienização e a ausência de um histórico confiável geram prejuízos financeiros e atrasos no atendimento da recepção.

### 2. Objetivoa
O objetivo do sistema é automatizar e centralizar o controle de empréstimo, devolução e estoque de toalhas da escola de natação. Desenvolvido em **Python** utilizando o paradigma de **Programação Orientada a Objetos (POO)** e integrado a um **banco de dados relacional**, o software garante rastreabilidade total das operações realizadas por atendentes e alunos.

### 3. Cenário de Utilização
1. O **Nadador** chega ao estabelecimento e solicita uma toalha na recepção.
2. O **Atendente** registra a retirada no sistema, vinculando a toalha ao cadastro do aluno e atualizando o status do item para "Em Uso".
3. Após o treino, o aluno devolve a toalha. O atendente registra a devolução, marcando a toalha como "Para Lavagem" ou retornando-a ao estoque de "Disponíveis".
4. A gestão da escola acessa o **histórico de utilizações** e relatórios de disponibilidade em tempo real.

### 4. Principais Características
- **Cadastro e Autenticação:** Gestão de perfis de Nadadores e Atendentes.
- **Controle de Estoque:** Monitoramento do status individual de cada toalha (Disponível, Em Uso, Em Lavagem, Danificada/Perdida).
- **Rastreabilidade de Empréstimos:** Registro detalhado com datas, horários de retirada e devolução.
- **Histórico e Auditoria:** Registro imutável de todas as transações para consulta rápida.
- **Arquitetura Orientada a Objetos:** Código modular, escalável e de fácil manutenção em Python.

---

## 🗄️ Modelo Lógico do Banco de Dados

Abaixo está a representação do **Modelo Lógico** do banco de dados relacional que servirá de referência para a implementação do sistema. O modelo define as tabelas, atributos, chaves primárias (`PK`), chaves estrangeiras (`FK`) e a cardinalidade dos relacionamentos.

### Diagrama ER (Mermaid)

```mermaid
erDiagram
    ATENDENTE {
        int id PK
        string nome
        string cpf
        string matricula
        string email
    }

    NADADOR {
        int id PK
        string nome
        string cpf
        string matricula
        string telefone
        string status_cadastro
    }

    TOALHA {
        int id PK
        string codigo_barras
        string tamanho
        string estado_conservacao
        string status_disponibilidade
    }

    RETIRADA {
        int id PK
        int nadador_id FK
        int atendente_id FK
        int toalha_id FK
        datetime data_hora_retirada
        datetime data_hora_devolucao
        string status_emprestimo
    }

    HISTORICO_TOALHA {
        int id PK
        int toalha_id FK
        int retirada_id FK
        datetime data_evento
        string tipo_evento
        string observacao
    }

    %% Relacionamentos e Cardinalidades
    ATENDENTE ||--o{ RETIRADA : "registra"
    NADADOR ||--o{ RETIRADA : "solicita"
    TOALHA ||--o{ RETIRADA : "é alocada em"
    TOALHA ||--o{ HISTORICO_TOALHA : "possui"
    RETIRADA ||--o| HISTORICO_TOALHA : "gera"
