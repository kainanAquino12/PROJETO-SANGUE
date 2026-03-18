# 📂 <span style="color:cyan">Documentação da API - Doação de Sangue</span>






##  <span style="color:red">GET /sangue</span>

- Arquivo: sangue.json

- O que faz: Exibe o volume de sangue coletado.

- Foco: Mostra o nome do paciente, o tipo sanguíneo e a quantidade (ml).

Controle de entrada de bolsas por doação.Este arquivo JSON armazena uma lista de pacientes, contendo o nome, tipo sanguíneo e uma quantidade associada a cada um. Ele é utilizado para organizar e facilitar o controle dessas informações dentro do sistema, podendo representar dados como estoque, necessidade ou registros relacionados ao sangue.

![alt text](image.png)

http://127.0.0.1:5000/sangue






##  <span style="color:lawngreen">GET /doadores</span>
- Arquivo: doadores.json

- O que faz: Exibe o cadastro dos voluntários.

- Foco: Mostra o nome, o contato (WhatsApp/Telefone) e a idade.

- Uso: Localizar o doador para triagem ou convocação.

Este arquivo JSON representa a resposta de uma requisição do tipo GET, retornando uma lista de doadores/pacientes com informações como nome, contato e idade. Ele é utilizado para permitir a consulta e visualização desses dados dentro do sistema.

![alt text](image-1.png)

http://127.0.0.1:5000/doadores



## <span style="color:gold">GET /estoque</span>
- Arquivo: estoque.json

- O que faz: Exibe a logística das bolsas no hospital.

- Foco: Mostra o tipo, a data de vencimento e o setor (ex: Ala Norte).

- Uso: Gestão de validade para não desperdiçar sangue.

Este arquivo JSON representa a resposta de uma requisição do tipo GET, contendo uma lista de bolsas de sangue em estoque. Cada item inclui o doador, tipo sanguíneo, data de vencimento e o setor de armazenamento. Ele é utilizado para consulta e monitoramento do estoque.

![alt text](image-2.png)

http://127.0.0.1:5000/estoque