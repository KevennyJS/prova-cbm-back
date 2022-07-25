
# Prova CBMSE 2022

Projeto desenvolvido para o processo de seleção


## Autor

- [@kevennyjs](https://www.github.com/kevennyjs)


## Funcionalidades

- Signo
- Tipo sanguineo
- Instituicoes
- Competencias
- Perfis
- Competencia
- Competencia Perfil
- Experiencia
- Formação

## Deploy

Caso ainda não possua o Python instalado na sua maquina, Clique [AQUI](https://www.python.org/downloads/) para baixar e instalar a ultima versão.

#### Local:



O primeiro passo para rodar localmente o projeto é instalar as dependencias, para isso, rode:

Depois de instalado, você precisa definir as variaveis de acesso ao banco de dados em "api > app > sql_app > database.py"


***Lembrando, se você for rodar em docker, vai precisar conectar seu mysql ao docker, que irá gerar um host especifico para ser usado nas configurações do "DOCKFILE" do caminho acima, [AQUI](https://www.youtube.com/watch?v=1Zpr1vX0wqk) tem um tutorial de como você pode fazer isso, caso tenha duvidas.***


```bash
  pip install requirements.txt
```

Agora que o ambiente está com tudo instalado, vá para "{raiz do projeto}/api/" e rode:

```bash
    python -m uvicorn app.main:app --reload
```

pronto! Já pode começar a fazer os requests.

#### Docker

Com o terminal na raiz do projeto, execute para gerar a build do nosso docker:

```bash
  docker build -t cbmse .
```

após a build completa, é hora de iniciar o docker que acabamos de criar, rode:

```bash
  docker run -d --name cbmse_container -p 8000:8000 cbmse
```

# OBS:
#### 1- Link Para o Swagger(O Projeto precisa estar rodando): 
http://seu-host:8000/docs

Exemplo:
http://127.0.0.1:8000/docs 
#### 2- Para facilitar o uso, existe um arquivo "" que pode ser importado no "Postman", nele contem todos os requests organizados e documentados.
#### 3- Em atributos do tipo "datetime", você pode enviar valores em datetime como "2000-06-23T00:00:01.001Z" ou datas no formato "yyyymmdd" como "20200101"
## Documentação da API

#### Retorna todos os perfis

```http
  GET /perfis
```

#### Retorna todos os detalhes de um perfil, incluindo experiência, formação e competencias

```http
  GET /perfis/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do perfil que deseja buscar |


#### Cria um novo perfil
```http
  POST /perfis
```

Body (JSON):

```json
  {
    "tipos_sanguineo_id": 1,
    "signo_id": 1,
    "cpf": "12345678909",
    "nome": "fulaninho junior",
    "data_nascimento": "2000-06-23T00:00:01.001Z",
    "email": "fulaninho@gmail.com",
    "telefone": "7998232337",
    "resumo": "olá, meu nome é fulaninho"
  }
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `tipos_sanguineo_id`      | `int` | **Obrigatório**. O ID do tipo sanguineo (na tabela de tipo sanguineo) |
| `signo_id`      | `int` | **Obrigatório**. O ID do signo (na tabela de signos) |
| `cpf`      | `String` | **Obrigatório**. CPF para o perfil |
| `nome`      | `String` | **Obrigatório**. Nome para o perfil |
| `data_nascimento`      | `datetime` | **Obrigatório**. Data de nascimento usuario |
| `email`      | `String` | **Obrigatório**. Email para o perfil |
| `telefone`      | `String` | **Obrigatório**. Telefone para o perfil  |
| `resumo`      | `String` | **Obrigatório**. Um breve resumo para o perfil |


#### Atualiza um perfil existente
```http
  PUT /perfis/1
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do perfil que deseja Atualizar |

Body (JSON):

```json
  {
    "tipos_sanguineo_id": 1,
    "signo_id": 1,
    "cpf": "12345678909",
    "nome": "Kevenny de Jesus Santos",
    "data_nascimento": "2000-06-23T00:00:01.001Z",
    "email": "kevennykeke@gmail.com",
    "telefone": "7998836127",
    "resumo": "olá, meu nome é kevenny"
  }
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `tipos_sanguineo_id`      | `int` | **Obrigatório**. Novo ID do tipo sanguineo (na tabela de tipo sanguineo) |
| `signo_id`      | `int` | **Obrigatório**. Novo ID do signo (na tabela de signos) |
| `cpf`      | `String` | **Obrigatório**. Novo CPF para o perfil |
| `nome`      | `String` | **Obrigatório**. Novo nome para o perfil |
| `data_nascimento`      | `datetime` | **Obrigatório**. Nova Data de nascimento usuario |
| `email`      | `String` | **Obrigatório**. Novo Email para o perfil |
| `telefone`      | `String` | **Obrigatório**. Novo Telefone para o perfil  |
| `resumo`      | `String` | **Obrigatório**. Novo resumo para o perfil |

```http
  DELETE /perfis/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do perfil que deseja deletar |


#### Retorna todos os signos

```http
  GET /signos
```

#### Retorna todos os tipos sanguineos

```http
  GET /tipo-sanguineos
```

#### Retorna todos as instituições

```http
  GET /instituicoes
```

#### Retorna todos as competencias

```http
  GET /competencias
```

#### Cria uma competencia perfil

```http
  POST /competencias-perfis
```
Body (JSON):

```json
  {
      "competencia_id": 1,
      "perfil_id": 1
  }
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `competencia_id`      | `int` | **Obrigatório**. O ID da competencia (na tabela de competencias) |
| `perfil_id`      | `int` | **Obrigatório**. O ID do perfil (na tabela de perfis) |


#### Retorna todos as formações

```http
  GET /formacoes
```

#### Cria uma competencia perfil

```http
  POST /formacoes
```
Body (JSON):

```json
  {
    "instituicao_id": 1,
    "perfil_id": 1,
    "nome": "Formacao 1"
  }
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `instituicao_id`      | `int` | **Obrigatório**. O ID da instituição (na tabela de instituicoes) |
| `perfil_id`      | `int` | **Obrigatório**. O ID do perfil (na tabela de perfis) |
| `nome`      | `String` | **Obrigatório**. Nome da Formação |

#### Retorna todos as Experiências

```http
  GET /experiencias
```

#### Cria uma competencia perfil

```http
  POST /experiencias
```
Body (JSON):

```json
  {
    "perfil_id": 1,
    "empresa": "Empresa 1",
    "inicio": "20200101",
    "fim": "20200101",
    "atual_trabalho": 1,
    "cargo": "Desenvolvedor Back End"
  }
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `perfil_id`      | `int` | **Obrigatório**. O ID do perfil (na tabela de perfis) |
| `empresa`      | `String` | **Obrigatório**. Nome da Empresa |
| `inicio`      | `datetime` | **Obrigatório**. Data de inicio |
| `fim`      | `datetime` | **Obrigatório**. Data de fim |
| `atual_trabalho`      | `int` | **Obrigatório**. valor de verificação de trabalhando atualmente |
| `cargo`      | `String` | **Obrigatório**. Cargo Atual |

