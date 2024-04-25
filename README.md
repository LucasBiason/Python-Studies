# PythonStudies

Mini Projetos de Cursos, Livros e artigos de python.

Aqui tenho projetos desde python puro focado em padrões, tecnicas avançadas ou simples

(Não utilizo para estudos de IA, isso terá o próprio repositório)


## Python - Práticas e Algoritmos


### Design Patterns Python I: Boas práticas de programação
Pasta: Python/DesignerPatterns

Link: https://cursos.alura.com.br/course/design-patterns-python

Sobre: Projeto de uma cálculadora fiscal para demonstração dos padrões. Cada Pasta é uma aula diferente.


### Design Patterns Python II: Boas práticas de programação
Pasta: Python/DesignerPatterns2

Link: https://cursos.alura.com.br/course/design-patterns-python-2

Sobre: Continuação do primeiro curso.


## Django - Projetos e Cases de Estudo


### Python: introdução a ambientes virtuais
Pasta: Django/Environments

Link: https://cursos.alura.com.br/course/python-ambientes-virtuais

Sobre: Configuração de ambiente para python utilizando como base um sistema de controle de estoque. (pipenv, pyenv, virtualenv)

### Python: ambientes virtuais com Docker e ASDF
**Pasta:** Django/Environments

**Link:** https://cursos.alura.com.br/course/python-ambientes-virtuais-docker-asdf

**Sobre:** Configuração de ambiente para o projeto do curso anterior em Docker

### CIDashPyPY - Dashboard with CI, SysAdmin and infraestructure for learning
**Pasta:** Django/RestFlask-Hotels

**Sobre:** Este é o template do dashboard de administração de aplicação desenvolvido no curso 521 - Python para DevOps da 4Linux. Este dashboard gerencia o container aonde a aplicação está rodando (Docker), a esteira de deploy (Jenkins) e oferece informações sobre os usuários cadastrados no GitLab local.

### API for Recipe Book Apps (Study Case) 
**Pasta:** Django/RecipeAppApi

**Sobre:** Training: Django Rest and TDD

-- Install and run:

docker build .
docker-compose build
docker-compose run app sh -c "python manage.py createsuperuser"
docker-compose up

Now you can open: http://0.0.0.0:8000/admin/ and log with super user created.

-- Others commands:

docker-compose run app sh -c "python manage.py test"  // Testing the app
docker-compose run app sh -c "python manage.py runserver 0.0.0.0:8000"


## Testes - Cases de Estudo


### Curso de Testes automatizados: TDD com Python
**Pasta:** Tests/python_tests

**Link:** https://cursos.alura.com.br/course/tdd-com-python

**Sobre:** Projeto de um leilao, aplicando conceitos basicos de testes em python


### Curso de Testes em Python: trabalhando com dublês de testes
**Pasta:** Tests/python_duble

**Link:** [Página Curso](https://cursos.alura.com.br/course/python-testes-com-dubles)

**Sobre:** Projeto que capta informações de livros e armazena em base de dados.


## Flask - Projetos e Cases de Estudo


### Flask parte 1: Crie uma webapp com Python 3
**Pasta:** Flask/jogoteca

**Sobre:** um projeto de uma biblioteca de jogos.


### Flask parte 2: Avançando no desenvolvimento web
**Pasta:** Flask/jogoteca

**Sobre:** continuando e complementando o projeto da biblioteca de jogos.


### Flask Full Series - Web Application Development with Python
**Pasta:** Flask/FlaskSeries

**Link:** [Playlist](https://www.youtube.com/watch?v=p068JokuThU&list=PLOkVupluCIjuPtTkhO6jmA76uQR994Wvi)

**Sobre:** aplicação de loja virtual


### REST APIs com Python e Flask
**Pasta:** Flask/RestFlask-Hotels

**Link:** [Página Curso](https://www.udemy.com/course/rest-apis-com-python-e-flask/)

**Sobre:** aplicação de hoteis com REST API em Flask


## Streamlit - Projetos e Cases de Estudo


### Dashboard simples com Streamlit
**Pasta:** Dashboards/Streamlit/streamlit-quickstart

**Sobre:** um projeto de um dashboard simples com apenas um gráfico, um quickstart para entender melhor a ferramenta


### Dashboard de Vendas com Streamlit
**Pasta:** Dashboards/Streamlit/streamlit-dashboard

**Sobre:** um projeto de um dashboard simples com apenas um gráfico, um quickstart para entender melhor a ferramenta


### Streamlit conectando com postgres (test Case)
**Pasta:** Dashboards/Streamlit/streamlit-postgres

**Sobre:** um projeto de um dashboard simples com apenas um exemplo de como integrar Streamlit e postgres


### Streamlit com Login e MultiPages
**Pasta:** Dashboards/Streamlit/streamlit-multipage

**Sobre:** um projeto de uma pagina de login fixa que leva a uma Home e um menu onde é possivel navegar em três paginas apenas se logado.
Este projeto não utilizou o multipages do Streamlit devido a criação de uma sidebar irritante e pouco configurável onde colocou o nome dos arquivos.
Isso me fez pensar em utilizar o Streamlit apenas para Dashboards pontuais com um login simples.

