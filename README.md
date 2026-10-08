# Projeto Nado Livre — Sistema de Gestão e Persistência

Este projeto é um sistema desenvolvido em Python para a disciplina de Programação Orientada a Objetos (POO). O seu objetivo principal é gerir o empréstimo e a devolução de toalhas para nadadores, contando com o suporte dos atendentes.

O sistema utiliza uma arquitetura organizada em camadas, separando as entidades de domínio, os serviços com as regras de negócio, as telas de interface no terminal e a camada de persistência. 

Todos os dados cadastrados (nadadores, atendentes, toalhas e o histórico de utilizações) são gravados automaticamente em ficheiros no formato JSON na pasta `dados` ao fechar o programa, sendo reconstruídos na memória assim que a aplicação é iniciada novamente através do ficheiro `main.py`.

Alunos: Daniel Henry - Igor Gabriel - Luiz guilherme Costa.