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





# 📂 <span style="color:cyan">Documentação da API - Doação de Sangue (POST) </span>

##  <span style="color:red">POST /doadores</span>
- Arquivo: estoque.json
- O que faz: Armazena as informações do estoque de sangue.

- Foco: Contém o tipo sanguíneo e a quantidade disponível.
- Uso: Utilizado para controle e atualização do estoque de sangue no sistema.

Este arquivo JSON representa os dados do estoque de sangue, podendo ser atualizado através das rotas POST da API. Cada item informa o tipo sanguíneo e a quantidade disponível, permitindo o gerenciamento e monitoramento do estoque.
![alt text](image-3.png)

![alt text](image-4.png)


##  <span style="color:green">POST /estoque</span>
- Arquivo: estoque.json
- O que faz: Armazena as informações das bolsas de sangue no estoque.
- Foco: Contém dados como doador, tipo sanguíneo, data de vencimento e local de armazenamento (ex: Ala Norte).

- Uso: Utilizado para controle, organização e monitoramento das bolsas de sangue disponíveis.

![alt text](image-5.png)
![alt text](image-6.png)

## <span style="color:blue">POST /sangue</span>
- Arquivo: sangue.json
- O que faz: Armazena os registros de doações de sangue realizadas.
- Foco: Contém o nome do doador, tipo sanguíneo e a quantidade de sangue doada.
- Uso: Utilizado para controlar as doações e acompanhar a quantidade de sangue disponível por tipo.

Este arquivo JSON representa uma lista de doações registradas no sistema através de requisições do tipo POST. Cada item inclui o nome do paciente (doador), o tipo sanguíneo e a quantidade doada. Ele é utilizado para controle das doações e apoio na gestão do estoque de sangue.

![alt text](image-7.png)

![alt text](image-8.png)





## <span style="color:blue"> VALIDAÇÃO/doadores</span>
- Arquivo: Endpoint /doadores (API Flask)
- O que faz: Recebe e valida dados de doadores enviados via requisição POST.
- Foco: Verifica se o campo paciente existe e se é do tipo texto (string), utilizando isinstance.
- Uso: Utilizado para garantir que os dados enviados para o sistema estejam corretos antes de serem processados ou armazenados.

Este trecho de código representa uma rota da API que recebe dados em formato JSON através de requisições do tipo POST. Ele valida se o campo paciente foi informado e utiliza a função isinstance para garantir que o valor seja do tipo string. Caso alguma dessas validações falhe, retorna uma mensagem de erro com código HTTP apropriado. Isso ajuda a manter a integridade e o padrão dos dados no sistema de cadastro de doadores.

![alt text](image-9.png)



## <span style="color:red"> VALIDAÇÃO/sangue</span>
Arquivo: Endpoint /sangue (API Flask)
O que faz: Recebe e valida dados relacionados ao tipo sanguíneo e quantidade doada via requisição POST.
Foco: Verifica se o campo sangue existe e se é do tipo texto (string), utilizando isinstance, além de validar a presença do campo quantidade.
Uso: Utilizado para garantir que as informações sobre o sangue doado estejam corretas antes de serem processadas ou armazenadas no sistema.

Este trecho de código representa uma rota da API que recebe dados em formato JSON através de requisições do tipo POST. Ele valida se o campo sangue foi informado corretamente e utiliza a função isinstance para garantir que o valor seja do tipo string. Também verifica a existência do campo quantidade. Caso alguma validação falhe, retorna uma mensagem de erro com código HTTP apropriado. Isso assegura a integridade dos dados no controle de doações de sangue.

![alt text](image-10.png)
## <span style="color:pink"> VALIDAÇÃO/estoque</span>
Arquivo: Validação de dados de estoque/doação (API Flask)
O que faz: Recebe e valida informações sobre o tipo de sangue e quantidade disponível via requisição POST.
Foco: Verifica se o campo tipo existe, se não está vazio e se é do tipo texto (string), utilizando isinstance, além de validar a presença do campo quantidade.
Uso: Utilizado para garantir que os dados relacionados ao tipo sanguíneo estejam corretos antes de serem registrados no sistema de estoque de sangue.

Este trecho de código representa uma validação dentro de uma rota da API que recebe dados em formato JSON. Ele verifica se o campo tipo foi informado corretamente e utiliza a função isinstance para garantir que o valor seja do tipo string. Também valida se o campo quantidade está presente. Caso alguma dessas verificações falhe, retorna uma mensagem de erro com código HTTP apropriado. Isso assegura a consistência dos dados no controle de estoque de sangue.
![alt text](image-11.png)

































## <span style="color:purple">Tabelas de Validação das Rotas POST</span>




### POST /doadores

| Rota       | Método | Campo    | Tipo esperado | Obrigatório |
|------------|--------|----------|---------------|-------------|
| /doadores  | POST   | paciente | string        | Sim         |
| /doadores  | POST   | idade    | inteiro       | Sim         |

**Exemplo de mensagens de erro para POST /doadores:**

| Campo    | Situação       | Mensagem retornada                  | Status code |
|----------|----------------|-------------------------------------|-------------|
| paciente | ausente        | O campo 'paciente' é obrigatório.   | 400         |
| paciente | tipo inválido  | 'paciente' deve ser um texto (string). | 422      |
| idade    | ausente        | O campo 'idade' é obrigatório.      | 400         |
| idade    | tipo inválido  | 'idade' deve ser um número inteiro. | 422         |

### POST /estoque

| Rota     | Método | Campo      | Tipo esperado | Obrigatório |
|----------|--------|------------|---------------|-------------|
| /estoque | POST   | tipo       | string        | Sim         |
| /estoque | POST   | quantidade | inteiro       | Sim         |

**Exemplo de mensagens de erro para POST /estoque:**

| Campo      | Situação       | Mensagem retornada                  | Status code |
|------------|----------------|-------------------------------------|-------------|
| tipo       | ausente        | O campo 'tipo' é obrigatório.       | 400         |
| tipo       | tipo inválido  | 'tipo' deve ser um texto (string).  | 422         |
| quantidade | ausente        | O campo 'quantidade' é obrigatório. | 400         |
| quantidade | tipo inválido  | 'quantidade' deve ser um número inteiro. | 422      |

### POST /sangue

| Rota    | Método | Campo      | Tipo esperado | Obrigatório |
|---------|--------|------------|---------------|-------------|
| /sangue | POST   | sangue     | string        | Sim         |
| /sangue | POST   | quantidade | inteiro       | Sim         |
| /sangue | POST   | data       | string        | Não         |

**Exemplo de mensagens de erro para POST /sangue:**

| Campo      | Situação       | Mensagem retornada                  | Status code |
|------------|----------------|-------------------------------------|-------------|
| sangue     | ausente        | O campo 'sangue' é obrigatório.     | 400         |
| sangue     | tipo inválido  | 'sangue' deve ser um texto (string).| 422         |
| quantidade | ausente        | O campo 'quantidade' é obrigatório. | 400         |
| quantidade | tipo inválido  | 'quantidade' deve ser um número inteiro. | 422      |
| data       | tipo inválido  | 'data' deve ser um texto (string).  | 422         |

**Status codes utilizados**

| Código | Situação                          |
|--------|-----------------------------------|
| 201    | Recurso criado com sucesso        |
| 400    | Campo obrigatório ausente         |
| 422    | Campo presente, mas com tipo de dado inválido |