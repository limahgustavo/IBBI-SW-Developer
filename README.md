
Projeto X - Docker Compose

Este projeto utiliza Docker Compose para gerenciar serviços e dependências.
Pré-requisitos

Antes de começar, certifique-se de ter o Docker e o Docker Compose instalados na sua máquina local.

Como Usar
Construir e Iniciar os Serviços

Para construir e iniciar os serviços definidos no docker-compose.yml, execute o seguinte comando no terminal:

bash

- docker-compose up --build

Este comando criará e iniciará todos os containers especificados no arquivo docker-compose.yml. Ele também reconstruirá as imagens se necessário.
Encerrar os Serviços

Para parar e remover os containers, redes e volumes associados aos serviços, utilize o comando:

bash

- docker-compose down

Este comando encerrará todos os serviços definidos no docker-compose.yml.