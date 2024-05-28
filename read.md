# Модуль общих мутаций для взаимодействия с сущностями авторизации пользователей

## [LoginUser](auth.py) Класс мутации на авторизацию пользователя
### Аргументы
- <span style="color: orange;">email</span> (обязательный): Адрес электронный почты для привязки учетной записи.
- <span style="color: orange;">password</span> (обязательный): Пароль пользователя.
- <span style="color: orange;">username</span> (default_value=None): Имя пользователя в системе.
- <span style="color: orange;">login_ip</span> (default_value=None): IP адрес, с которого пользователь входит в систему.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">user</span>: Сущность пользователя.
- <span style="color: orange;">token</span>: Токен для входа в систему.
- <span style="color: orange;">message</span>: Сообщение о результате операции.


### Пример использования
```graphql
mutation {
  loginUser(
    email: "mail@mail.ru"
    password: "string"
  ) {
    ok
    user {
      rowId
    }
    token
    message
  }
}
```


## [LogoutUser](auth.py) Класс мутации на выход пользователя из системы
### Аргументы
- <span style="color: orange;">auth_token</span> (обязательный): Токен для входа в систему.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">message</span>: Сообщение о результате операции.


### Пример использования
```graphql
mutation {
  logoutUser(authToken: "string") {
    ok
    message
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями авторизации пользователей

## [CreatePackOfUserByFile](user.py) Класс мутации на создание файла с группами пользователей
### Аргументы
- <span style="color: orange;">input_file</span> (обязательный): Объект обмена данными о создании файла с группами пользователей.
- <span style="color: orange;">role_ids</span> (обязательный): Пароль пользователя.
### Возвращаемое значение
- <span style="color: orange;">users</span>: Список сущностей созданных пользователей.
- <span style="color: orange;">errors</span>: Текст ошибки.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createUserByFile(inputFile: "file.xslx") {
    users {
      rowId
      username
    }
    errors
    ok
  }
}
```


## [CreateUser](user.py) Класс мутации на создание пользователя
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании файла с группами пользователей.
### Возвращаемое значение
- <span style="color: orange;">user</span>: Сущность пользователя.
- <span style="color: orange;">email_validate</span>: Результат валидации электронной почты пользователя.
- <span style="color: orange;">username_validate</span>: Результат валидации логина пользователя.
- <span style="color: orange;">phone_number_validate</span>: Результат валидации номера телефона пользователя.
- <span style="color: orange;">result</span>: Результат создания пользователя.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createUser(
    input: {
      newPassword: "string"
      username: "string"
      email: "mail@mail.ru"
      userType: USER
    }
  ) {
    user {
      rowId
      username

    }
    emailValidate
    usernameValidate
    phoneNumberValidate
    result
    ok
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями авторизации пользователей

## [DeleteUserMutation](user.py) Класс мутации на удаление пользователя
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор пользователя.
### Возвращаемое значение
- <span style="color: orange;">user</span>: Сущность пользователя.


### Пример использования
```graphql
mutation {
  deleteUser(rowId: 100) {
    user {
      rowId
      username
    }
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями авторизации пользователей

## [UpdateUser](user.py) Класс мутации на обновление пользователя
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении пользователя типа GraphQL.
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор пользователя.
### Возвращаемое значение
- <span style="color: orange;">user</span>: Сущность пользователя.
- <span style="color: orange;">password_status</span>: Результат обновление пароля.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateUser(input: {username:"string"}, rowId: 100) {
    user {
      rowId
      username
    }
    passwordStatus
    ok
  }
}
```


## [SetActiveStatusToUsers](user.py) Класс мутации на обновление поля "active" у пользователей
### Аргументы
- <span style="color: orange;">user_ids</span> (обязательный): Идентификаторы пользователей.
- <span style="color: orange;">active_status</span> (обязательный): Статус активации пользователя.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setActiveStatusToUsers(activeStatus: true, userIds: [100]) {
    ok
  }
}
```


# Модуль запросов для взаимодействия с сущностями типа авторизации пользователей

## [allUsers](user.py) Получение пользователей
### Аргументы
- <span style="color: orange;">row_id</span> (default_value=None): Список идентификаторов заявок.
- <span style="color: orange;">filters</span> (default_value=None): Флаг включения работников в результат запроса.
- <span style="color: orange;">ignore_deleted</span> (default_value=False): Список идентификаторов заявок.
- <span style="color: orange;">ignore_inactive</span> (default_value=False): Флаг включения работников в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[User]</span>: Список пользователей.


### Пример использования
```graphql 
query {
  allUsers(
    ignoreDeleted: false
    ignoreInactive: false
  ) {
    rowId
    username
    photo {
      extension
      rowId
    }
    roles {
      rowId
      name
    }
    organization {
      title

      rowId
    }
    workers {
      rowId
    }
  }
}
```

## [getUserByRowId](user.py) Получение пользователя по идентификатору
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Список идентификаторов заявок.
- <span style="color: orange;">ignore_deleted</span> (default_value=False): Список идентификаторов заявок.
- <span style="color: orange;">ignore_inactive</span> (default_value=False): Флаг включения работников в результат запроса.
- <span style="color: orange;">with_worker</span> (default_value=False): Фильтр на получение работников в сущности пользователя.
### Возвращаемое значение
- <span style="color: orange;">TList[User]</span>: Список пользователей.


### Пример использования
```graphql 
query {
  getUserByRowId(
    rowId: 90
    ignoreDeleted: false
    ignoreInactive: false
    withWorker: false
  ) {
    rowId
    username
    photo {
      extension
      rowId
    }
    roles {
      rowId
      name
    }
    organization {
      title
      rowId
    }
    workers {
      rowId
      firstName
    }
  }
}
```

## [getUserByRowId](user.py) Получение пользователей для страницы 'Управление пользователями'
### Аргументы
- <span style="color: orange;">filters</span> (default_value=None): Фильтры для взаимодействия с сущностями пользователей типа GraphQL.
- <span style="color: orange;">ignore_deleted</span> (default_value=False): Список идентификаторов заявок.
- <span style="color: orange;">ignore_inactive</span> (default_value=False): Флаг включения работников в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[User]</span>: Список пользователей.


### Пример использования
```graphql 
query {
  allUsersForControl(filters: {}, ignoreDeleted: false, ignoreInactive: false) {
    rowId
    username
    photo {
      extension
      rowId
    }
    roles {
      rowId
      name
    }
    organization {
      title
      rowId
    }
  }
}
```


## [getUserByTableNumber](user.py) Получение пользователей пользователя по табельному номеру
### Аргументы
- <span style="color: orange;">table_number</span> (обязательный): Фильтры для взаимодействия с сущностями пользователей типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[User]</span>: Список пользователей.


### Пример использования
```graphql 
query {
  getUserByTableNumber(tableNumber: "string") {
    rowId
    username
    photo {
      extension
      rowId
    }
    roles {
      rowId
      name
    }
    organization {
      title
      rowId
    }
    workers {
      rowId
      firstName
    }
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями машин


## [RegisterInterval](interval_create.py) Класс мутации на регистрацию интервала ТИС
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о регистрации интервала ТИС типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">interval</span>: Интервал ТИС.


### Пример использования
```graphql
mutation {
  registerInterval(input: {}) {
    ok
    interval {
      rowId
    }
  }
}
```


## [CreateMachineApplication](machine_application_create.py) Класс мутации на создание заявки для машины
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании заявки для машины типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">machine_application</span>: Заявка на машину.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createMachineApplication(createInput: {guid:"string" applicationNumber:"string" projectId:100 machineType:"string" service:"string" totalSum:1 startDate:"2024-01-01T14:00:00+01:00" finishDate:"2024-01-01T19:00:00+01:00" customerId:100 performerId:100 orderProvider:"string" price:100 measureUnit:"string" amount:100}) {
    machineApplication {
      rowId
      guid
    }
    okStatus
  }
}
```


## [CreateRouteList](route_list_create.py) Класс мутации на создание путевого листа
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании путевого листа типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">route_list</span>: Путевой лист.


### Пример использования
```graphql
mutation {
  createRouteList(input: {tisId:100 dateOutPlan:"2024-01-01T14:00:00+01:00" dateInPlan:"2024-01-01T15:00:00+01:00" status:CLOSED organizationId:100 dateOutFact:"2024-01-01T16:00:00+01:00" dateInFact:"2024-01-01T17:00:00+01:00" tsType:"string" driverIds:100 closeDate:"2024-02-01T15:00:00+01:00" machineIds:100}) {
    ok
    routeList {
      rowId
      organizationId
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями машин

## [DeleteRouteList](route_list_delete.py) Класс мутации на удаление путевого листа
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о удалении путевого листа типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">route_list</span>: Путевой лист.


### Пример использования
```graphql
mutation {
  deleteRouteList(input: {id:100}) {
    ok
    routeList {
      rowId
      organizationId
    }
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями машин

## [UpdateFuelConsumption](fuel_consumption_update.py) Класс мутации на обновление причины расхода топлива
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор причины расхода топлива.
- <span style="color: orange;">notes</span> (default_value=None): Причина отклонения расхода топлива.
- <span style="color: orange;">accepted_action</span> (default_value=None): Принятые меры по отклонению расхода топлива.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateFuelConsumption(
    acceptedAction: "string"
    notes: "string"
    rowId: 100
  ) {
    ok
  }
}
```


## [UpdateMachineApplication](machine_application_update.py) Класс мутации на обновление данных заявки для машины
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении заявки для машины типа GraphQL.
- <span style="color: orange;">row_id</span> (default_value=None): Идентификатор заявки на машину.
### Возвращаемое значение
- <span style="color: orange;">machine_application</span>: Заявка на машину.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateMachineApplication(rowId: 100, updateInput: {service:"string"}) {
    machineApplication {
      rowId
      guid
    }
    okStatus
  }
}
```


## [UpdateMachineTask](machine_task_update.py) Класс мутации на обновление задачи для машины
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении задачи для машины типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">machine_task</span>: Задача для машины.


### Пример использования
```graphql
mutation {
  updateMachineTask(input: {id:100}) {
    ok
    machineTask {
      rowId
      description
    }
  }
}
```


## [UpdateMachine](machine_update.py) Класс мутации на обновление машины
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении машины типа GraphQL.
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор машины.
### Возвращаемое значение
- <span style="color: orange;">machine</span>: Машина.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateMachine(input: {model:"string"}, rowId: 100) {
    machine {
      rowId
      vin
    }
    ok
  }
}
```


## [UpdateRouteList](route_list_update.py) Класс мутации на обновление путевого листа
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении путевого листа типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">route_list</span>: Путевой лист.


### Пример использования
```graphql
mutation {
  updateRouteList(input: {id:100}) {
    ok
    routeList {
      rowId
      tsType
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями машин

## [GetAllMachine](machine.py) Получение машин
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Machine]</span>: Список объектов машин типа GraphQL.


### Пример использования
```graphql 
query {
  getAllMachine {
    rowId
    vin
  }
}
```


## [GetMachineType](machine.py) Получение типов машин
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[MachineType]</span>: Список объектов типов машин типа GraphQL.


### Пример использования
```graphql 
query {
  getMachineType {
    rowId
    name
  }
}
```


## [GetAllMachineApplication](machine_application.py) Получение заявок на машины из 1С
### Аргументы 
- <span style="color: orange;">is_correctly</span> (default_value=False): Флаг корректности заполнения заявки.
### Возвращаемое значение
- <span style="color: orange;">TList[MachineApplication]</span>: Список объектов заявок для машин типа GraphQL.


### Пример использования
```graphql 
query {
  getAllMachineApplication(isCorrectly: false) {
    rowId
    guid
    customerContragent {
      rowId
      name
    }
  }
}
```


## [MyMachineTasks](machine_task.py) Получение задач для машины
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[MachineTask]</span>: Список объектов задач для машины типа GraphQL.


### Пример использования
```graphql 
query {
  myMachineTasks {
    rowId
    description
    route {
      rowId
    }
    routeList {
      rowId
    }
  }
}
```



## [GetTisObjects](tis_objects.py) Получение объектов ТИС
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[TisObject]</span>: Список объектов ТИС типа GraphQL.


### Пример использования
```graphql 
query {
  getTisObjects {
    id
    code
    name
    description
    archived
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями контрактов

## [TransferStatementPosition](contract_statement.py) Класс мутации на перенос позиций ведомости
### Аргументы
- <span style="color: orange;">id_transfer_from</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">transfer_input</span> (обязательный): Объект обмена данными о переносе позиций ведомости типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement</span>: Ведомость контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  TransferStatementPosition(
    idTransferFrom: 1
    transferInput: { name: "string", number: "string" contractVersionId: 1}
  ) {
    contractStatement {
      rowId
      name
    }
    okStatus
  }
}
```



## [RecalcStatementByTransaction](contract_statement.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">recalc_statement_id</span> (обязательный): Идентификатор ведомости для перерасчета.
- <span style="color: orange;">project_transaction_from</span> (обязательный): Идентификатор версии графика.
- <span style="color: orange;">recalc_input</span> (обязательный): Объект обмена данными о пересчете ведомости по транзакции типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement</span>: Ведомость контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Описание ошибки.


### Пример использования
```graphql
mutation {
  RecalcStatementByTransaction(
    projectTransactionFrom: 5
    recalcInput: { name: "string", number: "string" contractVersionId: 100}
    recalcStatementId: 10
  ) {
    contractStatement {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [UploadAndParseContractStatement](contract_statement_parser.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">file</span> (обязательный): Файл контрактной ведомости.
- <span style="color: orange;">contract_version_id</span> (обязательный): Идентификатор версии контракта.
- <span style="color: orange;">name</span> (default_value=None): Наименование версии контракта.
- <span style="color: orange;">number</span> (default_value=""): Номер ведомости контракта.
- <span style="color: orange;">ks_source_contract_statement_id</span> (default_value=None): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">contract_statement</span>: Ведомость контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Описание ошибки.
- <span style="color: orange;">err_msg</span>: Список позиций ведомости контракта.


### Пример использования
```graphql
mutation {
  UploadAndParseContractStatement(
    contractVersionId: 100
    file: "file.txt"
    ksSourceContractStatementId: 10
    name: "string"
    number: "string"
  ) {
    contractStatement {
      rowId
      name
    }
    ok
    error
    statementPositions {
      rowId
      name
    }
  }
}
```


## [RecalculateWorkWeightsByCostComponents](contract_statement_position.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">statement_position_ids</span> (обязательный): Список идентификаторов позиций ведомости контракта.
- <span style="color: orange;">cost_codes</span> (обязательный): Коды стоимостных составляющих.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">statement_positions</span>: Список позиций ведомости контракта.
- <span style="color: orange;">err_msg</span>: Описание ошибки.


### Пример использования
```graphql
mutation {
  RecalculateWorkWeightsByCostComponents(
    contractStatementId: 10
    costCodes: ["string"]
    statementPositionIds: [10]
  ) {
    statementPositions {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями контрактов

## [CreateContractStatement](contract_create.py) Класс мутации на создание контракта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract</span>: Созданный контракт.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractStatement(createInput: { name: "string", number: "string" contractVersionId: 1 }) {
    contractStatement {
      rowId
      name
    }
    okStatus
  }
}
```


## [CreateContractStatementColumn](contract_statement_column_create.py) Класс мутации на создание дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании дополнительного столбца ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement_column</span>: Список созданных столбцов КС.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractStatementColumn(input: { columnName: "string" contractStatementId: 1 }) {
    contractStatementColumn {
      rowId
      columnName
      contractStatementId
    }
    ok
  }
}
```


## [CreateContractStatementColumnValue](contract_statement_column_value_create.py) Класс мутации на создание значения дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании значения дополнительного столбца ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement_column</span>: Записанное значение столбца для позиции ведомости контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractStatementColumnValue(input: { columnValue: "string" contractStatementColumnId:1 contractStatementPositionId: 1 }) {
    contractStatementColumnValue {
      contractStatementPositionId
      contractStatementColumnId
      columnValue
    }
    ok
  }
}
```


## [CreateContractStatement](contract_statement_create.py) Класс мутации на создание ведомости контракта
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement</span>: Ведомость контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractStatement(createInput: { name: "string", number: "string" contractVersionId: 1 }) {
    contractStatement {
      rowId
      name
    }
    okStatus
  }
}
```


## [ManuallyCreateContractStatementKSColumns](contract_statement_ks_column_create.py) Класс мутации на создание столбцов КС вручную
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании столбцов КС типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">contract_statement_ks_column</span>: Список созданных столбцов КС.


### Пример использования
```graphql
mutation {
  createContractStatementKsColumn(input: {contractStatementId: 1 ksMonth:"2024-01-01"}) {
    ok
    contractStatementKsColumn {
      rowId
      ksMonth
      contractStatementId
      columnType
    }
  }
}
```


## [CreateStatementPosition](contract_statement_position_create.py) Класс мутации на создание позиций ведомости контракта
### Аргументы
- <span style="color: orange;">create_inputs</span> (обязательный): Объект обмена данными о создании позиции ведомости контракта типа GraphQL.
- <span style="color: orange;">with_delete_force</span> (default_value=False): Флаг удаления значений КС2 и привязанных позиций для родительской строки.
### Возвращаемое значение
- <span style="color: orange;">statement_positions</span>: Список позиций ведомости контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createStatementPosition(
    createInputs: [{ name: "string", statementPositionType: CHAPTER contractStatementId: 1 }]
    withDeleteForce: false
  ) {
    statementPositions {
      rowId
      name
    }
    okStatus
  }
}
```


## [SetResponsibleForPositions](contract_statement_position_create.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">position_ids</span> (обязательный): Список идентификаторов позиций ведомости контракта.
- <span style="color: orange;">set_input</span> (обязательный): Объект обмена данными об установке ответственного для позиций ведомости типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  SetResponsibleForPositions(positionIds: [1], setInput: {responsibleName: "string"}) {
    okStatus
  }
}
```


## [CreateContractStatementResponsiblePermission](contract_statement_responsible_permission_create.py) Класс мутации на создание разрешения доступа ответственного к ведомости контракта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании разрешения доступа ответственного к ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">statement_resp_permission</span>: Объект разрешения на доступ ответственного к ведомости контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractStatementResponsiblePermission(input: {contractStatementId: 1 responsibleId: 1}) {
    statementRespPermission {
      rowId
      contractStatementId
      responsibleId
      canReadWholeStatement
      canEditWholeStatement
    }
    ok
  }
}
```


## [CreateContractVersionMutation](contract_version_create.py) Класс мутации на создание версии контракта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании версии контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_version</span>: Созданная версия контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContractVersion(
    input: { name: "string", contractVersionType: ACTUAL contractId: 1 }
  ) {
    contractVersion {
      rowId
      name
    }
    ok
  }
}
```


## [CreateKS3SignActMutation](ks3_sign_act_create.py) Класс мутации на создание акта подписания КС3
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании акта подписания КС3 типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ks3_sign_act</span>: Акт подписания КС3.
- <span style="color: orange;">error_msg</span>: Описание ошибки.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createKs3SignAct(input: { actNumber: "string" reportPeriodStart: "2023-01-01" reportPeriodFinish: "2024-01-01" contractStatementId: 1 compilationDate: "2023-01-01T10:00:00Z" }) {
    ks3SignAct {
      rowId
    }
    errorMsg
    ok
  }
}
```


## [LinkContractsToProjects](project_contract_create.py) Класс мутации на создание акта подписания КС3
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными о создании связи проекта с контрактом типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  linkContractsToProjects(inputs: [{contractId: 1 projectId: 1}]) {
    ok
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями контрактов

## [DeleteContract](contract_delete.py) Класс мутации на удаление контракта
### Аргументы
- <span style="color: orange;">contract_id</span> (обязательный): Идентификатор контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContract(contractId: 1) {
    ok
  }
}
```


## [DeleteContractStatementColumn](contract_statement_column_delete.py) Класс мутации на удаление дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_column_id</span> (обязательный): Идентификатор дополнительного столбца ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContractStatementColumn(contractStatementColumnId: 1) {
    ok
  }
}
```


## [DeleteContractStatementColumnValue](contract_statement_column_value_delete.py) Класс мутации на удаление значения дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_position_id</span> (обязательный): Идентификатор позиции ведомости контракта.
- <span style="color: orange;">contract_statement_column_id</span> (обязательный): Идентификатор дополнительного столбца ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContractStatementColumnValue(
    contractStatementColumnId: 1
    contractStatementPositionId: 1
  ) {
    ok
  }
}
```


## [DeleteContractStatement](contract_statement_delete.py) Класс мутации на удаление ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContractStatement(contractStatementId: 1) {
    okStatus
  }
}
```


## [DeleteContractStatementKSColumns](contract_statement_ks_column_delete.py) Класс мутации на удаление столбцов КС
### Аргументы
- <span style="color: orange;">column_ids</span> (обязательный): Список идентификаторов столбцов КС ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContractStatementKsColumn(columnIds: [1]) {
    ok
  }
}
```


## [DeleteStatementPosition](contract_statement_position_delete.py) Класс мутации на удаление позиций ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">statement_position_ids</span> (обязательный): Список идентификаторов позиций ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">recalculated_parent_positions</span>: Список позиций ведомости контракта.


### Пример использования
```graphql
mutation {
  deleteContractStatementKsColumn(columnIds: [1]) {
    ok
  }
}
```


## [ResetResponsibleForPositions](contract_statement_position_delete.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">position_ids</span> (обязательный): Список идентификаторов позиций ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  ResetResponsibleForPositions(positionIds: [1]) {
    okStatus
  }
}
```


## [DeleteContractVersion](contract_version_delete.py) Класс мутации на удаление версии контракта
### Аргументы
- <span style="color: orange;">contract_id</span> (обязательный): Идентификатор контракта.
- <span style="color: orange;">contract_version_id</span> (обязательный): Идентификатор версии контракта.
### Возвращаемое значение
- <span style="color: orange;">actual_contract_version</span>: Актуальная версия контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContractVersion(contractId: 1, contractVersionId: 1) {
    actualContractVersion {
      rowId
      name
      contractVersionType
      contractId
      createdAt
    }
    ok
  }
}
```


## [DeleteKS3SignAct](ks3_sign_act_delete.py) Класс мутации на удаление акта подписания КС3
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор акта подписания КС3.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteKs3SignAct(contractStatementId: 1, rowId: 1) {
    ok
  }
}
```


## [DeleteKS3SignAct](ks3_sign_act_delete.py) Класс мутации на удаление акта подписания КС3
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор акта подписания КС3.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteKs3SignAct(contractStatementId: 1, rowId: 1) {
    ok
  }
}
```


## [DeleteLinkContractsToProjects](project_contract_delete.py) Класс мутации на удаление связей контрактов с проектами
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">contract_ids</span> (обязательный): Список идентификаторов контрактов.
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об удалении связи проекта с контрактом типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteLinkContractsToProjects(contractIds: [], inputs: [{contractId:1 projectId:1}], projectIds: []) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями контрактов

## [UpdateContractStatementColumn](contract_statement_column_update.py) Класс мутации на обновление дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_column_id</span> (обязательный): Идентификатор дополнительного столбца ведомости контракта.
- <span style="color: orange;">column_name</span> (обязательный): Наименование дополнительного столбца ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">contract_statement_column</span>: Список обновленных столбцов КС.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractStatementColumn(
    columnName: "string"
    contractStatementColumnId: 1
  ) {
    contractStatementColumn {
      rowId
      columnName
      contractStatementId
    }
    ok
  }
}
```


## [UpdateContractStatementColumnValue](contract_statement_column_value_update.py) Класс мутации на обновление дополнительного столбца ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_position_id</span> (обязательный): Идентификатор позиции ведомости контракта.
- <span style="color: orange;">contract_statement_column_id</span> (обязательный): Идентификатор дополнительного столбца ведомости контракта.
- <span style="color: orange;">column_value</span> (обязательный): Значение дополнительного столбца ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">contract_statement_column_value</span>: Записанное значение столбца для позиции ведомости контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractStatementColumnValue(
    columnValue: "string"
    contractStatementColumnId: 1
    contractStatementPositionId: 1
  ) {
    contractStatementColumnValue {
      contractStatementPositionId
      contractStatementColumnId
      columnValue
    }
    ok
  }
}
```


## [UpdateStatementPosition](contract_statement_position_update.py) Класс мутации на обновление позиции ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">statement_position_id</span> (обязательный): Идентификатор позиции ведомости контракта.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении позиции ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">statement_positions</span>: Список позиций ведомости контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateStatementPosition(
    contractStatementId: 1
    statementPositionId: 1
    updateInput: {name: "string"}
  ) {
    statementPositions {
      rowId
      name
    }
    okStatus
  }
}
```


## [BatchUpdateWBSStatementPositions](contract_statement_position_update.py) Класс мутации на обновление позиции ведомости контракта
### Аргументы
- <span style="color: orange;">update_inputs</span> (обязательный): Объект обмена данными о массовом обновлении вбс кодов позиций ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">statement_positions</span>: Список позиций ведомости контракта.


### Пример использования
```graphql
mutation {
  batchUpdateWbsStatementPositions(updateInputs: [{rowId: 1 wbsCode: "string"}]) {
    okStatus
    statementPositions {
      rowId
      wbsCode
    }
  }
}
```


## [BatchBindingWorksToContractStatement](contract_statement_position_update.py) Класс мутации на пересчет ведомости по транзакции
### Аргументы
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">phase_ids</span> (default_value=[]): Список идентификаторов этапов проекта.
- <span style="color: orange;">work_ids</span> (default_value=[]): Список идентификаторов работ позиции ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">statement_positions</span>: Список позиций ведомости контракта.
- <span style="color: orange;">err_msg</span>: Описание ошибки.


### Пример использования
```graphql
mutation {
  BatchBindingWorksToContractStatement(
    contractStatementId: 11
    phaseIds: [1]
    transactionId: 117
    workIds: [1]
  ) {
    statementPositions {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [UpdateContractStatementResponsiblePermission](contract_statement_responsible_permission_update.py) Класс мутации на обновление разрешения доступа ответственного к ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
- <span style="color: orange;">can_read_whole_statement</span> (default_value=False): Флаг просмотра ответственным всей контрактной ведомости.
- <span style="color: orange;">can_edit_whole_statement</span> (default_value=False): Флаг редактирования ответственным всей контрактной ведомости.
### Возвращаемое значение
- <span style="color: orange;">statement_resp_permission</span>: Объект разрешения на доступ ответственного к ведомости контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractStatementResponsiblePermission(
    canEditWholeStatement: false
    canReadWholeStatement: false
    contractStatementId: 1
    responsibleId: 1
  ) {
    statementRespPermission {
      rowId
      contractStatementId
      responsibleId
      canReadWholeStatement
      canEditWholeStatement
    }
    ok
  }
}
```


## [UpdateContractStatementResponsiblePermission](contract_statement_responsible_permission_update.py) Класс мутации на обновление разрешения доступа ответственного к ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
- <span style="color: orange;">can_read_whole_statement</span> (default_value=False): Флаг просмотра ответственным всей контрактной ведомости.
- <span style="color: orange;">can_edit_whole_statement</span> (default_value=False): Флаг редактирования ответственным всей контрактной ведомости.
### Возвращаемое значение
- <span style="color: orange;">statement_resp_permission</span>: Объект разрешения на доступ ответственного к ведомости контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractStatementResponsiblePermission(
    canEditWholeStatement: false
    canReadWholeStatement: false
    contractStatementId: 1
    responsibleId: 1
  ) {
    statementRespPermission {
      rowId
      contractStatementId
      responsibleId
      canReadWholeStatement
      canEditWholeStatement
    }
    ok
  }
}
```


## [UpdateContractStatement](contract_statement_responsible_permission_update.py) Класс мутации на обновление разрешения доступа ответственного к ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении ведомости контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract_statement</span>: Ведомость контракта.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractStatement(contractStatementId: 1, updateInput: {name:"string"}) {
    contractStatement {
      rowId
      name
    }
    okStatus
  }
}
```


## [UpdateContract](contract_update.py) Класс мутации на обновление контракта
### Аргументы
- <span style="color: orange;">contract_id</span> (обязательный): Идентификатор контракта.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract</span>: Обновленный контракт.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContract(contractId: 1, input: {name:"String"}) {
    contract {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateContractVersion](contract_version_update.py) Класс мутации на обновление версии контракта
### Аргументы
- <span style="color: orange;">contract_version_id</span> (обязательный): Идентификатор версии контракта.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении версии контракта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">contract</span>: Обновленная версия контракта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContractVersion(contractVersionId: 1, input: {name:"string"}) {
    contractVersion {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateKS3SignAct](ks3_sign_act_update.py) Класс мутации на обновление акта подписания КС3
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор акта подписания КС3.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении акта подписания КС3 типа GraphQL.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">ks3_sign_act</span>: Акт подписания КС3.
- <span style="color: orange;">error_msg</span>: Описание ошибки.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateKs3SignAct(contractStatementId: 1, input: {actNumber:"string"}, rowId: 1) {
    ks3SignAct {
      rowId
    }
    errorMsg
    ok
  }
}
```


# Модуль запросов для взаимодействия с сущностями типа доступа контрактов

## [GetContractsByProjectId](contract.py) Получение контракта по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[Contract]</span>: Список контрактов.


### Пример использования
```graphql 
query {
  getContractsByProjectId(projectId: 1) {
    rowId
    name
    }
}
```


## [GetAllContracts](contract.py) Получение контрактов
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Contract]</span>: Список контрактов.


### Пример использования
```graphql 
query {
  getAllContracts {
    rowId
    name
  }
}
```


## [GetContractStatementsByContractVersionIds](contract_statement.py) Получение ведомостей контрактов по идентификаторам версий контрактов
### Аргументы
- <span style="color: orange;">contract_version_ids</span> (обязательный): Список идентификаторов версий контрактов.
### Возвращаемое значение
- <span style="color: orange;">TList[ContractStatement]</span>: Список ведомостей контрактов.


### Пример использования
```graphql 
query {
  getContractStatementsByContractVersionIds(contractVersionIds: [1]) {
    rowId
    name
  }
}
```


## [GetContractStatementsColumnsByStatementId](contract_statement_column.py) Получение дополнительных столбцов ведомости контракта по идентификатору ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[ContractStatementColumn]</span>: Список дополнительных столбцов ведомости контракта.


### Пример использования
```graphql 
query {
  getContractStatementsColumnsByStatementId(contractStatementId: 1) {
    rowId
    columnName
    contractStatementId
  }
}
```


## [GetTemplateForParseContractStatement](contract_statement_parser.py) Получение шаблона для импорта сметы контракта
### Аргументы (нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ временного файла.


### Пример использования
```graphql 
query {
  getTemplateForParseContractStatement
}
```


## [GetStatementPositionsByStatementId](contract_statement_position.py) Получение позиций ведомости контракта по идентификатору ведомости контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">responsible_ids</span> (default_value=None): Список идентификаторов организаций исполнителей работ.
### Возвращаемое значение
- <span style="color: orange;">TList[StatementPosition]</span>: Список позиций ведомости контракта.


### Пример использования
```graphql 
query {
  getStatementPositionsByStatementId(
    contractStatementId: 1
    responsibleIds: []
  ) {
    rowId
    name
  }
}
```


## [GetStatementPositionsToLevelByStatementId](contract_statement_position.py) Получение позиций ведомости контракта по id ведомости до определенного уровня в иерархии
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">level</span> (обязательный): Тип позиции ведомости контракта.
- <span style="color: orange;">responsible_ids</span> (default_value=None): Список идентификаторов организаций исполнителей работ.
### Возвращаемое значение
- <span style="color: orange;">TList[StatementPosition]</span>: Список позиций ведомости контракта.


### Пример использования
```graphql 
query {
  getStatementPositionsToLevelByStatementId(
    contractStatementId: 1
    level: CHAPTER
    responsibleIds: []
  ) {
    rowId
    name
  }
}
```


## [GetStatementPositionsByParentId](contract_statement_position.py) Получение позиций ведомости контракта до заданного уровня по идентификатору ведомости
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">level</span> (default_value=[]): Тип позиции ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[StatementPosition]</span>: Список позиций ведомости контракта.


### Пример использования
```graphql 
query {
  getStatementPositionsByParentId(
    parentId: 1
    responsibleIds: []
  ) {
    rowId
    name
  }
}
```


## [GetStatementPositionsByPositionIds](contract_statement_position.py) Получение позиций ведомости контракта по списку идентификаторов позиций ведомости контракта
### Аргументы
- <span style="color: orange;">statement_position_ids</span> (обязательный): Список идентификаторов позиций ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[StatementPosition]</span>: Список позиций ведомости контракта.


### Пример использования
```graphql 
query {
  getStatementPositionsByPositionIds(statementPositionIds: [1]) {
    rowId
    name
  }
}
```


## [GetKsValsByPosAndColumn](contract_statement_position.py) Получение значений КС столбцов по позиции и столбцу КС
### Аргументы
- <span style="color: orange;">statement_position_id</span> (обязательный): Идентификатор позиции ведомости контракта.
- <span style="color: orange;">statement_ks_column_id</span> (обязательный): Идентификатор столбца КС ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[ContractStatementKSColumnValue]</span>: Список столбцов КС ведомостей контрактов.


### Пример использования
```graphql 
query {
  getKsValsByPosAndColumn(
    statementPositionId: 1
    statementKsColumnId: 1
  ) {
    contractStatementPositionId
    contractStatementKsColumnId
    columnValue
    ks3SignActId
    defaultColumnValue
    reductionRatio
  }
}
```


## [GetPosWorksByKsActId](contract_statement_position.py) Получение позиций с типом WORK с суммарными стоимостями и объемами по акту КС3
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">ks3_sign_act_id</span> (обязательный): Идентификатор акта подписания КС3.
### Возвращаемое значение
- <span style="color: orange;">TList[StatementPositionWithVolume]</span>: Список позиций ведомости контракта с общей стоимостью и общим объемом.


### Пример использования
```graphql 
query {
  getPosWorksByKsActId(contractStatementId: 1, ks3SignActId: 1) {
    position {
      rowId
      name
    }
    volumeSum
    costSum
  }
}
```


## [GetPosWorksByKsActId](contract_statement_position.py) Получение родительских позиций ведомости контракта по идентификатору операции
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы позиции ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[VersionContractStatementPositions]</span>: Список позиций ведомости контракта с названием ведомости и названием контракта.


### Пример использования
```graphql 
query {
  getParentsStatementPositionByWorkId(workId: 1) {
    contractName
    statementName
    positions {
      rowId
      name
    }
  }
}
```


## [GetPermissionsForResponsible](contract_statement_responsible_permission.py) Получение родительских позиций ведомости контракта по идентификатору операции
### Аргументы
- <span style="color: orange;">contract_statement_ids</span> (default_value=[]): Список идентификаторов ведомостей контрактов.
- <span style="color: orange;">responsible_ids</span> (default_value=[]): Список идентификаторов организаций исполнителей работ.
### Возвращаемое значение
- <span style="color: orange;">TList[ContractStatementResponsiblePermission]</span>: Список разрешений на доступ ответственного к ведомости контракта.


### Пример использования
```graphql 
query {
  getPermissionsForResponsible(
    contractStatementIds: []
    responsibleIds: []
  ) {
    rowId
    contractStatementId
    responsibleId
    canReadWholeStatement
    canEditWholeStatement
  }
}
```


## [GetKs3SignActs](ks3_sign_act.py) Получение актов подписания КС3
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов акта подписания КС3.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">with_deleted</span> (default_value=False): Флаг получения с удаленными объектами.
- <span style="color: orange;">with_sum</span> (default_value=True): Флаг получения с общими суммами фактических стоимостей.
### Возвращаемое значение
- <span style="color: orange;">TList[KS3SignAct]</span>: Список разрешений на доступ ответственного к ведомости контракта.


### Пример использования
```graphql 
query {
  getKs3SignActs(
    rowIds: [1]
    contractStatementId: 1
    withDeleted: false
    withSum: true
  ) {
    rowId
  }
}
```


## [GetProjectsByContractId](project_contract.py) Получение списка проектов по идентификатору контракта
### Аргументы
- <span style="color: orange;">contract_id</span> (обязательный): Идентификатор контракта.
### Возвращаемое значение
- <span style="color: orange;">TList[Project]</span>: Список проектов.


### Пример использования
```graphql 
query {
  getProjectsByContractId(contractId: 1) {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями маяков

## [CreateMarker](marker.py) Класс мутации на создание маяка
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании маяка типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">marker</span>: Объект маяка типа GraphQL.


### Пример использования
```graphql
mutation {
  createMarker(input: {minor: 10 bleuuid: "string" latitude: 1.0 longitude: 1.0 projectZoneId: 10 markerType: office}) {
    ok
    marker {
      rowId
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями маяков

## [DeleteMarker](marker.py) Класс мутации на удаление маяка
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об удалении маяка типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">marker</span>: Объект маяка типа GraphQL.


### Пример использования
```graphql
mutation {
  deleteMarker(input: { id: 40 }) {
    ok
    marker {
      rowId
      minor
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями маяков

## [GetAllBids](marker.py) Получение всех маяков
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Marker]</span>: Список объектов маяков типа GraphQL.


### Пример использования
```graphql 
query {
  allMarkers {
    rowId
    minor
    project {
      rowId
      name
    }
    projectZone {
      id
      name
    }
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями доступа сотрудников

## [CreateBid](bid_create.py) Класс мутации на создание заявки
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании заявки типа GraphQL.
    - <span style="color: orange;">worker_ids</span> (обязательный): Список идентификаторов работников.
    - <span style="color: orange;">bid_type</span> (обязательный): Тип заявки.
### Возвращаемое значение
- <span style="color: orange;">bid</span>: Заявка.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createBid(createInput: { workerIds: [59163], bidType: INNER_EDUCATION }) {
    bid {
      rowId
      bidType
    }
    okStatus
  }
}
```


## [CreateBidResponsible](bid_responsible_create.py) Класс мутации на создание ответственного по заявке
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании ответственного по заявке типа GraphQL.
    - <span style="color: orange;">user_id</span> (обязательный): Идентификатор системного пользователя ответственного по заявке.
    - <span style="color: orange;">bid_id</span> (обязательный): Идентификатор заявки.
    - <span style="color: orange;">status</span> (обязательный): Статус ответственного по заявке.
    - <span style="color: orange;">create_input</span> (обязательный): Тип ответственного по заявке.
    - <span style="color: orange;">create_input</span> (обязательный): Порядковый номер в цепочке согласования ответственного по заявке.
### Возвращаемое значение
- <span style="color: orange;">bid_responsible</span>: Заявка.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createBidResponsible(
    createInput: { status: START, bidResponsibleType: INITIATOR, order: 1 userId: 10 bidId : 5}
  ) {
    bidResponsible {
      rowId
      userId
      bidId
      status
      bidResponsibleType
      order
    }
    okStatus
  }
}
```


## [CreateEducation](education_create.py) Класс мутации на создание обучения
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании обучения типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование обучения.
    - <span style="color: orange;">education_type</span> (обязательный): Тип обучения.
    - <span style="color: orange;">required_worker_signature</span> (обязательный): Требуется подпись сотрудника.
### Возвращаемое значение
- <span style="color: orange;">education</span>: Обучение.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createEducation(createInput: { name: "string", educationType: MAIN }) {
    education {
      rowId
      name
      educationType
      requiredWorkerSignature
    }
    okStatus
  }
}
```


## [CreateEquipment](equipment_create.py) Класс мутации на создание оборудования
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании оборудования типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование оборудования.
    - <span style="color: orange;">grsi_number</span> (обязательный): Номер ГРСИ оборудования.
    - <span style="color: orange;">factory_number</span> (обязательный): Заводской номер оборудования.
    - <span style="color: orange;">status</span> (обязательный): Статус оборудования.
### Возвращаемое значение
- <span style="color: orange;">equipment</span>: Оборудование.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createEquipment(
    createInput: { name: "string", factoryNumber: "string", status: ACTIVE grsiNumber: "string" }
  ) {
    equipment {
      rowId
      name
      grsiNumber
      factoryNumber
      status
    }
    okStatus
  }
}
```


## [CreateEquipmentVerification](equipment_verification_create.py) Класс мутации на создание поверки оборудования
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании поверки оборудования типа GraphQL.
- <span style="color: orange;">content</span> (default_value=None): Файл документа поверки оборудования.
- <span style="color: orange;">with_documents</span> (default_value=False): Флаг включения документов в результат запроса.
- <span style="color: orange;">with_equipments</span> (default_value=False): Флаг включения оборудований в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">equipment_verification</span>: Поверка оборудования.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createEquipmentVerification(
    createInput: {
      equipmentId: 100
      verificationSubject: "string"
      name: "string"
      number: "string"
      startDate:"2022-02-02"
      expiryDate:"2023-03-03"
    }
    withDocuments: false
    withEquipments: false
  ) {
    equipmentVerification {
      rowId
    }
    okStatus
  }
}
```


## [CreateProtectiveEquipment](protective_equipment_create.py) Класс мутации на создание средства индивидуальной защиты
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными для создания средства индивидуальной защиты типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование средства индивидуальной защиты.
### Возвращаемое значение
- <span style="color: orange;">protective_equipment</span>: Средство индивидуальной защиты.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProtectiveEquipment(createInput: { name: "string" }) {
    protectiveEquipment {
      rowId
      name
    }
    okStatus
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями доступа сотрудников

## [DeleteBids](bid_delete.py) Класс мутации на удаление заявок
### Аргументы
- <span style="color: orange;">bid_ids</span> (обязательный): Список идентификаторов заявок.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteBids(bidIds: [2]) {
    okStatus
  }
}
```


## [DeleteBidResponsible](bid_responsible_delete.py) Класс мутации на удаление ответственных по заявкам
### Аргументы
- <span style="color: orange;">bid_responsible_ids</span> (обязательный): Список идентификаторов ответственных по заявкам.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteBidResponsible(bidResponsibleIds: [2]) {
    okStatus
  }
}
```


## [DeleteEducation](education_delete.py) Класс мутации на удаление обучений
### Аргументы
- <span style="color: orange;">education_ids</span> (обязательный): Список идентификаторов обучений.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteEducations(educationIds: [2]) {
    okStatus
  }
}
```


## [DeleteEquipment](equipment_delete.py) Класс мутации на удаление оборудования
### Аргументы
- <span style="color: orange;">equipment_ids</span> (обязательный): Список идентификаторов оборудования.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteEquipments(equipmentIds: [2]) {
    okStatus
  }
}
```


## [DeleteEquipmentVerifications](equipment_verification_delete.py) Класс мутации на удаление поверок оборудования
### Аргументы
- <span style="color: orange;">equipment_verification_ids</span> (обязательный): Список идентификаторов поверок оборудования.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteEquipmentVerifications(equipmentVerificationIds: [100]) {
    okStatus
  }
}
```


## [DeleteProtectiveEquipments](protective_equipment_delete.py) Класс мутации на удаление средств индивидуальной защиты
### Аргументы
- <span style="color: orange;">protective_equipment_ids</span> (обязательный): Список идентификаторов средств индивидуальной защиты.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProtectiveEquipments(protectiveEquipmentIds: [1]) {
    okStatus
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями доступа сотрудников

## [UpdateBidResponsible](bid_responsible_update.py) Класс мутации на обновление ответственного по заявке
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении ответственного по заявке типа GraphQL.
- <span style="color: orange;">bid_responsible_id</span> (обязательный): Идентификатор ответственного по заявке.
### Возвращаемое значение
- <span style="color: orange;">bid_responsible</span>: Ответственный по заявке.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateBidResponsible(bidResponsibleId: 1 , updateInput: { comment: "string" }) {
    bidResponsible {
      rowId
      userId
      bidId
      status
    }
    okStatus
  }
}

```


## [UpdateBid](bid_update.py) Класс мутации на обновление заявки
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении заявки типа GraphQL.
- <span style="color: orange;">bid_id</span> (обязательный): Идентификатор заявки.
### Возвращаемое значение
- <span style="color: orange;">bid_responsible</span>: Ответственный по заявке.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateBid(bidId: 4, updateInput: {bidType: PROTECTIVE_EQUIPMENT}) {
    bid {
      rowId
      bidType
    }
    okStatus
  }
}
```


## [UpdateEducation](education_update.py) Класс мутации на обновление обучения
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении обучения типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование обучения.
    - <span style="color: orange;">education_type</span> (обязательный): Тип обучения.
- <span style="color: orange;">education_id</span> (обязательный): Идентификатор обучения.
### Возвращаемое значение
- <span style="color: orange;">education</span>: Ответственный по заявке.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateEducation(
    educationId: 1
    updateInput: { name: "string", educationType: MAIN }
  ) {
    education {
      rowId
      name
      educationType
    }
    okStatus
  }
}
```


## [UpdateEquipment](equipment_update.py) Класс мутации на обновление оборудования
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении оборудования типа GraphQL.
- <span style="color: orange;">equipment_id</span> (обязательный): Идентификатор оборудования.
### Возвращаемое значение
- <span style="color: orange;">equipment</span>: Оборудование.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateEquipment(equipmentId: 103, updateInput: { name: "string" factoryNumber: "string" status: ACTIVE }) {
    equipment {
      rowId
    }
    okStatus
  }
}
```


## [UpdateProtectiveEquipment](equipment_verification_update.py) Класс мутации на обновление оборудования
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении поверки оборудования типа GraphQL.
- <span style="color: orange;">equipment_verification_id</span> (обязательный): Идентификатор поверки оборудования.
### Возвращаемое значение
- <span style="color: orange;">equipment_verification</span>: Средство поверок оборудования.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateEquipmentVerification(
    equipmentVerificationId: "10"
    updateInput: { verificationSubject: "string" startDate: "2022-02-02" expiryDate: "2023-03-03" name: "string" number: "string" }
    withDocuments: false
    withEquipments: false
  ) {
    equipmentVerification {
      rowId
    }
    okStatus
  }
}
```


## [UpdateProtectiveEquipment](protective_equipment_update.py) Класс мутации на обновление оборудования
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении оборудования типа GraphQL.
- <span style="color: orange;">protective_equipment_id</span> (обязательный): Идентификатор средства индивидуальной защиты.
### Возвращаемое значение
- <span style="color: orange;">protective_equipment</span>: Средство индивидуальной защиты.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProtectiveEquipment(protectiveEquipmentId: 1, updateInput: {name: "string"}) {
    protectiveEquipment {
      rowId
      name
    }
    okStatus
  }
}
```


# Модуль запросов для взаимодействия с сущностями типа доступа сотрудников

## [GetAllBids](bid.py) Получение заявок
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов заявок.
- <span style="color: orange;">with_workers</span> (default_value=False): Флаг включения работников в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[Bid]</span>: Список заявок.


### Пример использования
```graphql 
query {
  getAllBids(rowIds: [5], withWorkers: false) {
    rowId
    bidType
    createdAt
    workers {
      rowId
      firstName
      surname
      lastName
    }
  }
}
```


## [MyIncomingBids](bid.py) Получение входящих заявок
### Аргументы
- <span style="color: orange;">with_workers</span> (default_value=False): Флаг включения работников в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[Bid]</span>: Список заявок.


### Пример использования
```graphql 
query {
  myIncomingBids(withWorkers: false) {
    rowId
    bidType
    createdAt
    workers {
      rowId
      firstName
      surname
      lastName
    }
  }
}
```


## [MyOutgoingBids](bid.py) Получение исходящих заявок
### Аргументы
- <span style="color: orange;">with_workers</span> (default_value=False): Флаг включения работников в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[Bid]</span>: Список заявок.


### Пример использования
```graphql 
query {
  myOutgoingBids(withWorkers: false) {
    rowId
    bidType
    createdAt
    workers {
      rowId
      firstName
      surname
      lastName
    }
  }
}
```


## [GetAllBidResponsible](bid_responsible.py) Получение ответственных по заявкам
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов ответственных по заявкам.
- <span style="color: orange;">bid_ids</span> (default_value=[]): Список идентификаторов заявок.
- <span style="color: orange;">order</span> (default_value=1): Порядковый номер в цепочке согласования ответственного по заявке.
### Возвращаемое значение
- <span style="color: orange;">TList[BidResponsible]</span>: Список ответственных по заявкам.


### Пример использования
```graphql 
query {
  getAllBidResponsible(rowIds: [100], bidIds: [10], order: 1) {
    rowId
    userId
    bidId
    user {
      username
      email
    }
  }
}
```


## [GetAllEducations](education.py) Получение обучений
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов обучений.
### Возвращаемое значение
- <span style="color: orange;">TList[Education]</span>: Список обучений.


### Пример использования
```graphql 
query {
  getAllEducations(rowIds: [1]) {
    rowId
    name
    educationType
  }
}
```


## [GetAllEquipments](equipment.py) Получение оборудований
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов оборудований.
### Возвращаемое значение
- <span style="color: orange;">TList[Equipment]</span>: Список обучений.


### Пример использования
```graphql 
query {
  getAllEquipments(rowIds: [3]) {
    rowId
    name
    factoryNumber
    status
    user {
      rowId
      username
      email
    }
  }
}
```


## [GetAllEquipmentVerifications](equipment_verification.py) Получение поверок оборудования
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов поверок оборудования.
- <span style="color: orange;">with_documents</span> (default_value=[]): Флаг включения документов в результат запроса.
- <span style="color: orange;">with_equipments</span> (default_value=[]): Флаг включения оборудований в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[EquipmentVerification]</span>: Список поверок оборудования.


### Пример использования
```graphql 
query {
  getAllEquipmentVerifications(
    rowIds: [10]
    withDocuments: false
    withEquipments: false
  ) {
    rowId
    name
    equipment {
      rowId
      name
    }
    document {
      id
      name
    }
  }
}
```


## [GetAllProtectiveEquipments](protective_equipment.py) Получение средств индивидуальной защиты
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов средств индивидуальной защиты.
### Возвращаемое значение
- <span style="color: orange;">TList[ProtectiveEquipment]</span>: Список средств индивидуальной защиты.


### Пример использования
```graphql 
query {
  getAllProtectiveEquipments(rowIds: [10]) {
    rowId
    name
  }
}
```


# Модуль общих мутаций для взаимодействия с файловым хранилищем

## [copyDirectory](directory.py) Класс мутации на копирование директории
### Аргументы
- <span style="color: orange;">p</span> (обязательный): Путь до папки.
- <span style="color: orange;">target_p</span> (обязательный): Путь до целевой папки.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
- <span style="color: orange;">target_guid</span> (default_value=None): GUID директории назначения.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект скопированной папки типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyDirectory(
    p: "path/from/directory"
    targetP: "path/to/directory"
  ) {
    d {
      id
    }
    ok
  }
}
```


## [moveDirectory](file.py) Класс мутации на перемещение директории
### Аргументы
- <span style="color: orange;">p</span> (обязательный): Путь до папки.
- <span style="color: orange;">target_p</span> (обязательный): Путь до целевой папки.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
- <span style="color: orange;">target_guid</span> (default_value=None): GUID директории назначения.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект скопированной папки типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  moveDirectory(
    p: "path/from/directory"
    targetP: "path/to/directory"
  ) {
    d {
      id
    }
    ok
  }
}
```


## [copyFile](file.py) Класс мутации на копирование файла
### Аргументы
- <span style="color: orange;">file_p</span> (обязательный): Путь до файла.
- <span style="color: orange;">target_p</span> (обязательный): Путь до целевой папки.
- <span style="color: orange;">guid</span> (обязательный): GUID директории.
- <span style="color: orange;">target_guid</span> (default_value=None): GUID директории назначения.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект нового файла типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyFile(
    fileP: "path/to/file"
    targetP: "path/to/target"
  ) {
    f {
      id
    }
    ok
  }
}
```


## [moveFile](file.py) Класс мутации на перемещение файла
### Аргументы
- <span style="color: orange;">file_p</span> (обязательный): Путь до файла.
- <span style="color: orange;">target_p</span> (обязательный): Путь до целевой папки.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
- <span style="color: orange;">target_guid</span> (default_value=None): GUID директории назначения.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект нового файла типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  moveFile(
    fileP: "path/to/file"
    targetP: "path/to/target"
  ) {
    f {
      id
    }
    ok
  }
}
```


# Модуль мутаций создания для взаимодействия с файловым хранилищем

## [attachDirectoryToProject](attach_mutations.py) Класс мутации на привязку файла к проекту
### Аргументы
- <span style="color: orange;">by_path</span> (default_value=None): Объект обмена данными (p,guid,project_id) для привязки файла к проекту.
- <span style="color: orange;">by_id</span> (default_value=None): Объект обмена данными (file_object_id,project_id) для привязки файла к проекту.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат привязки файлового объекта к проекту.


### Пример использования
```graphql
mutation {
  attachDirectoryToProject(byPath: {fileObjectId: 10 projectId: 10}) {
    result
  }
}
```


## [createDirectory](directory.py) Класс мутации на создание директории
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Название файла.
- <span style="color: orange;">p</span> (обязательный): Путь до файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект созданной директории типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createDirectory(name: "file", p: "path/to/file") {
    d {
      id
    }
    ok
  }
}
```


## [makeDirectory](directory.py) Класс мутации на создание директории
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Название файла.
- <span style="color: orange;">p</span> (обязательный): Путь до файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект созданной директории типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  makeDirectory(name: "file", p: "path/to/file") {
    d {
      id
    }
    ok
  }
}
```


# Модуль мутаций удаления для взаимодействия с файловым хранилищем

## [detachDirectoryFromProject](attach_mutations.py) Класс мутации на отвязку файла к проекту
### Аргументы
- <span style="color: orange;">by_path</span> (default_value=None): Объект обмена данными (p,guid,project_id) для привязки файла к проекту.
- <span style="color: orange;">by_id</span> (default_value=None): Объект обмена данными (file_object_id,project_id) для привязки файла к проекту.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат отвязки файлового объекта к проекту.


### Пример использования
```graphql
mutation {
  detachDirectoryFromProject(byPath: {fileObjectId: 10 projectId: 10}) {
    result
  }
}
```


## [deleteDirectory](directory.py) Класс мутации на удаление директории
### Аргументы
- <span style="color: orange;">p</span> (обязательный): Путь до папки.
- <span style="color: orange;">recursive</span> (default_value=False): Флаг рекурсивного удаления.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект удаленной директории типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteDirectory(p: "path/to/directory") {
    d {
      id
      name
    }
    ok
  }
}
```


## [deleteFile](file.py) Класс мутации на удаление файла
### Аргументы
- <span style="color: orange;">file_p</span> (обязательный): Путь до файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект удаленного файла типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteFile(fileP: "path/to/file") {
    f {
      id
      name
    }
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с файловым хранилищем

## [renameDirectory](directory.py) Класс мутации на переименование директории
### Аргументы
- <span style="color: orange;">p</span> (обязательный): Путь до папки.
- <span style="color: orange;">new_name</span> (default_value=None): Новое имя папки.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">d</span>: Объект созданной директории.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  renameDirectory(newName: "string", p: "path/to/file") {
    d {
      id
      name
    }
    ok
  }
}
```


## [setActualFile](file.py) Класс мутации на установку актуальной версии для файла
### Аргументы
- <span style="color: orange;">file_path</span> (обязательный): Путь до файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект созданной файла.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setActualFile(filePath: "path/to/file", guid: "6b841741-fa4e-4710-9d4b-c4ce92b3c5dc") {
    ok
  }
}
```


## [updateFile](file.py) Класс мутации на перезапись файла
### Аргументы
- <span style="color: orange;">p</span> (обязательный): Путь до файла.
- <span style="color: orange;">name</span> (обязательный): Название файла.
- <span style="color: orange;">data</span> (обязательный): Данные файла.
- <span style="color: orange;">comment</span> (default_value=None): Комментарий к новой версии файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект перезаписанного файла.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateFile(
    data: "string"
    name: "string"
    p: "path/to/file"
  ) {
    f {
      id
      name
    }
    ok
  }
}
```


## [renameFile](file.py) Класс мутации на переименование файла
### Аргументы
- <span style="color: orange;">file_p</span> (обязательный): Путь до файла.
- <span style="color: orange;">new_name</span> (обязательный): Новое имя файла.
- <span style="color: orange;">guid</span> (default_value=None): GUID директории.
### Возвращаемое значение
- <span style="color: orange;">f</span>: Объект перезаписанного файла.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  renameFile(fileP: "path/to/file", newName: "string") {
    f {
      id
      name
    }
    ok
  }
}
```


# Модуль запросов для взаимодействия с сущностями файлов и директорий

## [getFile](file_management.py) Получение файла
### Аргументы
- <span style="color: orange;">path</span> (обязательный): Путь до файла.
- <span style="color: orange;">guid</span> (default_value=None): Guid директории с файлом.
### Возвращаемое значение
- <span style="color: orange;">File</span>: Объект файла типа GraphQL


### Пример использования
```graphql 
query {
  getFile(path: "path/to/file") {
    id
    name
    }
}
```


## [getDirectory](file_management.py) Получение директории
### Аргументы
- <span style="color: orange;">path</span> (обязательный): Путь до директории.
- <span style="color: orange;">guid</span> (default_value=None): Guid директории.
### Возвращаемое значение
- <span style="color: orange;">Directory</span>: Объект директории типа GraphQL


### Пример использования
```graphql 
query {
  getDirectory(path: "path/to/directory") {
    id
    name
  }
}
```


## [listDirectory](file_management.py) Получение объектов директории
### Аргументы
- <span style="color: orange;">path</span> (обязательный): Путь до директории.
- <span style="color: orange;">guid</span> (default_value=None): Guid директории.
### Возвращаемое значение
- <span style="color: orange;">DirectoryListing</span>: Все элементы в папке


### Пример использования
```graphql 
query {
  listDirectory(path: "Development of Task Manager (Управление задачами)") {
    directories(before: "string", after: "string", first: 1, last: 1) {
      pageInfo{
        hasNextPage
        hasPreviousPage
      }
    }
    files(before: "string", after: "string", first: 1, last: 1) {
      pageInfo{
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
```


## [projectFileListing](file_management.py) Получение всех директорий и файлов проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ProjectDirectoryListing</span>: Все директории и файлы для проекта


### Пример использования
```graphql 
query {
  projectFileListing(projectId: 10) {
    directories(before: "string", after: "string", first: 1, last: 1) {
      pageInfo{
        hasNextPage
        hasPreviousPage
      }
    }
    files(before: "string", after: "string", first: 1, last: 1) {
       pageInfo{
        hasNextPage
        hasPreviousPage
      }
    }
    projectId
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями платформы Mstroy

## [AddDirectoryToProject](attachment.py) Класс мутации на добавление директории в проект
### Аргументы
- <span style="color: orange;">dir_input</span> (обязательный): Объект обмена данными о добавлении указанной директории в проект типа GraphQL.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  addDirectoryToProject(dirInput: { p: "string" }, projectId: 10) {
    result
  }
}
```


## [AddFileToProjectElement](attachment.py) Класс мутации на добавление файла к проекту
### Аргументы
- <span style="color: orange;">file_input</span> (обязательный): Объект обмена данными о добавлении указанного файла к элементу проекта типа GraphQL.
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента проекта.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  addFileToProjectElement(
    fileInput: { p: "string" }
    projectElementId: 10
  ) {
    result
  }
}
```


## [CreateProjectImage](project_image.py) Класс мутации на добавление изображения для проекта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о добавлении изображения для проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_image</span>: Фото проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectImage(input: {photo: "photo.jpg" projectId: 10}) {
    projectImage {
      rowId
      extension
      projectId
    }
    ok
  }
}
```


## [SetProjectRoleScenarios](project_scenario.py) Класс мутации на установку новых сценариев для роли с перезаписыванием старых
### Аргументы
- <span style="color: orange;">set_input</span> (обязательный): Объект обмена данными о установке новых сценариев для роли, с перезаписыванием старых типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setProjectRoleScenarios(setInput: {projectRoleId: 10 projectScenariosIds: [10]}) {
    okStatus
  }
}
```


## [CopyManagers](project_structure.py) Класс мутации на копирование менеджеров к другому проектному подразделению
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов менеджеров.
- <span style="color: orange;">project_organization_unit_id</span> (обязательный): Идентификатор проектного подразделения.
### Возвращаемое значение
- <span style="color: orange;">managers</span>: Список сущностей менеджеров.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyManagers(projectOrganizationUnitId: 10, rowIds: [10]) {
    managers {
      rowId
      name
      projectId
    }
    ok
  }
}
```


## [CopyProjectOrganizationUnits](project_structure.py) Класс мутации на копирование проектных подразделений к контрагенту
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов менеджеров.
- <span style="color: orange;">contragent_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">project_organization_units</span>: Список сущностей проектных подразделений.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyProjectOrganizationUnits(contragentId: 10, rowIds: [10]) {
    projectOrganizationUnits {
      rowId
      name
      projectOrgUnitType
      contragentId
    }
    ok
  }
}
```


## [CopyContragents](project_structure.py) Класс мутации на копирование контрагентов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов контрагентов.
- <span style="color: orange;">parent_contragent_id</span> (default_value=None): Идентификатор контрагента.
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">contragents</span>: Список сущностей контрагентов.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyContragents(
    rowIds: [10]
  ) {
    contragents {
      rowId
      name
      projectId
    }
    ok
  }
}
```


## [AddResponsibleOrder](responsible.py) Класс мутации на добавление для ответственного приказа о назначении
### Аргументы
- <span style="color: orange;">responsible_row_ids</span> (обязательный): Идентификатор ответственного.
- <span style="color: orange;">responsible_order_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">responsible</span>: Сущность ответственного.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  addResponsibleOrder(
    responsibleOrderId: 10
    responsibleRowIds: [10]
  ) {
    responsible {
      rowId
      managerId
    }
    ok
  }
}
```


## [SetResponsibleFieldOrder](responsible_field_order.py) Класс мутации на установку порядка полей ответственных для текущего пользователя
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об установке порядка полей ответственных для текущего пользователя типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible_field_order</span>: Сущность порядка полей ответственных.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setResponsibleFieldOrder(input: {fieldOrder:"string"}) {
    responsibleFieldOrder {
      userId
      fieldOrder
      fieldOrderConstructionCabinet
    }
    ok
  }
}
```


## [SetResponsibleDefaultFieldOrder](responsible_field_order.py) Класс мутации на установку порядка полей ответственных по умолчанию
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об установке порядка полей ответственных по умолчанию типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible_field_order</span>: Сущность порядка полей ответственных.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setResponsibleDefaultFieldOrder(input: {fieldOrder:"string"}) {
    responsibleFieldOrder {
      userId
      fieldOrder
      fieldOrderConstructionCabinet
    }
    ok
  }
}
```


## [ResetResponsibleFieldOrder](responsible_field_order.py) Класс мутации на сброс настроек порядка полей по умолчанию
### Аргументы
- <span style="color: orange;">is_field_order</span> (обязательный): Флаг выбора настроек полей ответственных.
- <span style="color: orange;">is_construction_cabinet</span> (обязательный): Флаг выбора настроек полей ответственных на странице кабинет руководителя.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetResponsibleFieldOrder(
    isConstructionCabinet: true
    isFieldOrder: true
  ) {
    ok
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями платформы Mstroy

## [CreateAdditionalProjectProperties](additional_project_properties_create.py) Класс мутации на создание дополнительных настроек проекта
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании дополнительных настроек проекта типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">bi_short_name</span> (default_value=""): Короткое наименование проекта, отображаемое в BI.
### Возвращаемое значение
- <span style="color: orange;">additional_project_properties</span>: Сущность дополнительных настроек проекта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createAdditionalProjectProperties(createInput: { projectId: 10 biShortName: "string" }) {
    additionalProjectProperties {
      projectId
      biShortName
    }
    okStatus
    errMsg
  }
}
```


## [CreateContragent](contragent_create.py) Класс мутации на создание контрагента
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании контрагента типа GraphQL.
    - <span style="color: orange;">contract</span> (обязательный): Контракт.
    - <span style="color: orange;">contragent_role</span> (обязательный): Проектная роль контрагента.
    - <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
    - <span style="color: orange;">show_in_table</span> (обязательный): Флаг отображения контрагента в табеле.
### Возвращаемое значение
- <span style="color: orange;">contragent</span>: Сущность контрагента.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createContragent(
    input: { contract: "string", contragentRole: GENERAL_CONTRACTOR projectId: 10 organizationId: 20}
  ) {
    contragent {
      rowId
      name
    }
    ok
  }
}
```


## [CreateEducationInfo](education_info_create.py) Класс мутации на создание записи об образовании сотрудника
### Аргументы
- <span style="color: orange;">input_data</span> (обязательный): Объект обмена данными о создании записи информации об образовании сотрудника типа GraphQL.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
    - <span style="color: orange;">institution</span> (обязательный): Проектная роль контрагента.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">education_info</span>: Запись об образовании сотрудника.


### Пример использования
```graphql
mutation {
  createEducationInfo(inputData: { institution: "string" workerId: 10 }) {
    ok
    educationInfo {
      rowId
      workerId
    }
  }
}
```


## [CreateManager](manager_create.py) Класс мутации на добавление нового менеджера в проект
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о добавлении нового менеджера в проект типа GraphQL.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
    - <span style="color: orange;">institution</span> (обязательный): Проектная роль контрагента.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">manager</span>: Сущность менеджера.
- <span style="color: orange;">err_msg</span>: Запись об образовании сотрудника.


### Пример использования
```graphql
mutation {
  createManager(createInput: {projectId: 10 projectOrganizationUnitId: 20 userId: 10}) {
    okStatus
    manager {
      rowId
      name
    }
    errMsg
  }
}
```


## [BatchCreatePercoWorkerAccess](perco_worker_access_create.py) Класс мутации на добавление списка назначений шаблонов доступа Perco
### Аргументы
- <span style="color: orange;">dtos</span> (обязательный): Список объектов обмена данными о создании назначения шаблона доступа Perco рабочему типа GraphQL.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">access_id</span> (обязательный): Идентификатор шаблона доступа в Perco.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">perco_workers_access</span>: Список сущностей доступа сотрудников в системе Perco.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  batchCreatePercoWorkerAccess(dtos: [{workerId: 10 projectId: 20 accessId: 10}]) {
    ok
    percoWorkersAccess {
      rowId
    }
    errMsg
  }
}
```


## [CreatePosition](position_create.py) Класс мутации на создание должности работника
### Аргументы
- <span style="color: orange;">with_overtime_accounting</span> (default_value=False): Флаг получения с типом переработки.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании должности типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название должности работника.
    - <span style="color: orange;">base_salary</span> (обязательный): Базовая ставка оплаты труда за час.
    - <span style="color: orange;">position_group_id</span> (обязательный): Идентификатор группы должностей работников.
### Возвращаемое значение
- <span style="color: orange;">position</span>: Должность работника.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createPosition(input: {name: "str" baseSalary: 1.0 positionGroupId: 20}, withOvertimeAccounting: False) {
    position {
      rowId
      name
      baseSalary
    }
    ok
  }
}
```


## [CreateOvertimeAccountingType](position_overtime_accounting_create.py) Класс мутации на создание типа переработки
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании должности типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименования типа переработок.
    - <span style="color: orange;">description</span> (обязательный): Описание типа переработок.
### Возвращаемое значение
- <span style="color: orange;">overtime_accounting_type</span>: Объект типа переработки.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createOvertimeAccountingType(
    input: { name: "string", description: "string" }
  ) {
    overtimeAccountingType {
      rowId
      name
      description
    }
    ok
  }
}
```


## [CreateProject](project_create.py) Класс мутации на создание проекта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании проекта типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название проекта.
    - <span style="color: orange;">short_name</span> (обязательный): Короткое название проекта.
    - <span style="color: orange;">time_zone_offset</span> (обязательный): Смещение часового пояса проекта.
### Возвращаемое значение
- <span style="color: orange;">project</span>: Сущность проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProject(
    input: { name: "string", shortName: "string", timeZoneOffset: 1 }
  ) {
    project {
      rowId
      name
    }
    ok
  }
}
```


## [CreateProjectGroup](project_group_create.py) Класс мутации на создание группы участников проекта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании группы участников проекта типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">name</span> (обязательный): Наименование группы проекта.
### Возвращаемое значение
- <span style="color: orange;">project_group</span>: Сущность группы проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectGroup(input: { name: "string" projectId: 1 }) {
    projectGroup {
      rowId
      projectId
      name
    }
    ok
  }
}
```


## [CreateProjectGroupResponsible](project_group_responsible_create.py) Класс мутации на создание связи группы проекта с ответственными
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании связи группы проекта с ответственными типа GraphQL.
    - <span style="color: orange;">project_group_id</span> (обязательный): Идентификатор группы проекта.
    - <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">project_group_responsible</span>: Сущность связи группы проекта с ответственными.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectGroupResponsible(input: { responsibleId: [10] projectGroupId: 10}) {
    projectGroupResponsible {
      rowId
      projectGroupId
      responsibleId
    }
    ok
  }
}
```


## [CreateProjectObject](project_object_create.py) Класс мутации на создание этапа проекта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании этапа проекта типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование этапа проекта.
### Возвращаемое значение
- <span style="color: orange;">project_object</span>: Сущности этапа проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectObject(input: { name: "string" }) {
    projectObject {
      rowId
      name
    }
    ok
  }
}
```


## [CreateProjectRole](project_role_create.py) Класс мутации на создание проектной роли
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании проектной роли типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название проектной роли.
### Возвращаемое значение
- <span style="color: orange;">project_role</span>: Сущность проектной роли.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectRole(createInput: { name: "string" }) {
    projectRole {
      rowId
      name
    }
    okStatus
  }
}
```


## [CreateProjectScenario](project_scenario_create.py) Класс мутации на создание проектного сценария
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными для создания проектного сценария типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название проектной роли.
### Возвращаемое значение
- <span style="color: orange;">project_scenario</span>: Сущность проектного сценария.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">error</span>: Текст ошибки.


### Пример использования
```graphql
НА ДОРАБОТКЕ
```


## [CreateResponsible](responsible_create.py) Класс мутации на создание ответственного
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании ответственного типа GraphQL.
    - <span style="color: orange;">manager_id</span> (обязательный): Идентификатор менеджера.
    - <span style="color: orange;">responsible_order_id</span> (обязательный): Идентификатор приказа назначения ответственного.
    - <span style="color: orange;">job_type</span> (обязательный): Вид выполняемых работ.
    - <span style="color: orange;">nrc_number</span> (обязательный): Идентификационный номер НРС.
### Возвращаемое значение
- <span style="color: orange;">responsible</span>: Сущность ответственного.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createResponsible(
    input: { jobType: "string" nrcNumber: "string" managerId: 10 responsibleOrderId : 10 }
  ) {
    responsible {
      rowId
      managerId
      responsibleOrderId
      jobType
      nrcNumber
    }
    ok
  }
}
```


## [CreateResponsibleOrder](responsible_create.py) Класс мутации на создание приказа назначения ответственного лица
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании приказа назначения ответственного лица типа GraphQL.
    - <span style="color: orange;">contragent_id</span> (обязательный): Идентификатор контрагента.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">date_start</span> (обязательный): Дата начала периода приказа.
### Возвращаемое значение
- <span style="color: orange;">responsible_order</span>: Сущность приказа назначения ответственного лица.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
НА ДОРАБОТКЕ
```


## [CreateResponsiblePowerAttorney](responsible_power_attorney_create.py) Класс мутации на создание ведомости ответственного
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании доверенности ответственного типа GraphQL.
    - <span style="color: orange;">id_mchd</span> (обязательный): Единый регистрационный номер доверенности.
    - <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">responsible_power_attorney</span>: Сущность доверенности ответственного.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createResponsiblePowerAttorney(createInput: { idMchd: "string" responsibleId: 10 }) {
    responsiblePowerAttorney {
      rowId
      idMchd
    }
    okStatus
  }
}
```


## [CreateTag](tag_create.py) Класс мутации на создание тега
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании доверенности ответственного типа GraphQL.
    - <span style="color: orange;">id_mchd</span> (обязательный): Единый регистрационный номер доверенности.
    - <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">name_parse_error</span>: Текст ошибки.
- <span style="color: orange;">tag</span>: Сущность тега.


### Пример использования
```graphql
mutation {
  createTag(input: { type: STANDART projectId: 10 name: "string" }) {
    ok
    nameParseError
    tag {
      rowId
      name
      projectId
    }
  }
}
```


## [CreateTimeResource](time_resource_create.py) Класс мутации на создание тайм-ресурса
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании тайм-ресурса типа GraphQL.
    - <span style="color: orange;">id_mchd</span> (обязательный): Единый регистрационный номер доверенности.
    - <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">time_resource</span>: Сущность тайм-ресурса.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createTimeResource(input: { projectId: 10 workerId: 10 }) {
    timeResource {
      rowId
      name
      projectId
    }
    ok
  }
}
```


## [SetUserSettings](user_settings_create.py) Класс мутации на сохранение строки текущих настроек пользователя
### Аргументы
- <span style="color: orange;">user_id</span> (обязательный): Идентификатор пользователя.
- <span style="color: orange;">settings</span> (обязательный): Строка текущих настроек пользователя по проектам.
### Возвращаемое значение
- <span style="color: orange;">settings</span>: Настройки назначенные пользователю.


### Пример использования
```graphql
mutation {
  setUserSettings( settings: "string" userId: 10 ) {
    settings
  }
}
```


## [CreateWorkerDocument](worker_document_create.py) Класс мутации на создание документа работника
### Аргументы
- <span style="color: orange;">content</span> (default_value=None): Строка текущих настроек пользователя по проектам.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании документа работника типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название документа работника.
    - <span style="color: orange;">worker_document_type</span> (обязательный): Тип документа работника.
    - <span style="color: orange;">start_date</span> (обязательный): Дата начала действия документа работника.
    - <span style="color: orange;">expiry_date</span> (обязательный): Дата окончания действия документа работника.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">worker_document</span>: Данные о документах работника.


### Пример использования
```graphql
mutation {
  createWorkerDocument(
    input: { name: "string" workerDocumentType: EDUCATION workerId: 10 startDate: "2024-01-01T10:00:00Z" expiryDate: "2030-01-01T10:00:00Z" description: "string" }
  ) {
    ok
    workerDocument {
      rowId
      name
      description
      workerDocumentType
      startDate
      expiryDate
      workerId
      documentId
    }
  }
}
```


## [CreateWorkersEducations](worker_education_create.py) Класс мутации на назначение инструктажей сотрудникам
### Аргументы
- <span style="color: orange;">worker_ids</span> (обязательный): Список идентификаторов сотрудников.
- <span style="color: orange;">video_instructions_ids</span> (обязательный): Список идентификаторов видео-инструктажей.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">workers_educations</span>: Данные об обучении сотрудников.


### Пример использования
```graphql
mutation {
  createWorkersEducations(
    videoInstructionsIds: [10]
    workerIds: [10]
  ) {
    ok
    workersEducations {
      rowId
      appointDate
      workerId
      videoInstructionId
    }
  }
}
```


## [CreateWorkerPassport](worker_passport_create.py) Класс мутации на создание паспортных данных работника
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании паспорта работника типа GraphQL.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
    - <span style="color: orange;">passport_serial</span> (обязательный): Серия.
    - <span style="color: orange;">passport_number</span> (обязательный): Номер.
    - <span style="color: orange;">issue_date</span> (обязательный): Дата выдачи.
    - <span style="color: orange;">issuer_name</span> (обязательный): Отделение выдачи.
    - <span style="color: orange;">issuer_code</span> (обязательный): Код подразделения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">worker_passport</span>: Паспортные данные работника.


### Пример использования
```graphql
mutation {
  createWorkerPassport(
    input: {
      passportSerial: "12 34"
      passportNumber: "567890"
      issuerName: "string"
      issuerCode: "123-456"
      issueDate: "2024-01-01"
      workerId: 10
    }
  ) {
    ok
    workerPassport {
      rowId
      workerId
      passportSerial
      passportNumber
      issueDate
      issuerName
      issuerCode
    }
  }
}
```


## [CreateWorkerVaccination](worker_vaccination_create.py) Класс мутации на сохранение данных о вакцинации сотрудника
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании паспорта работника типа GraphQL.
    - <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
    - <span style="color: orange;">vaccination_status</span> (обязательный): Статус вакцинации.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkerVaccination(input: { vaccinationStatus: VACCINATED workerId: 10 }) {
    ok
  }
}
```




## [CreateSpanMutation](span_create.py) Класс мутации на создание перегона
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании перегона типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название.
    - <span style="color: orange;">project_object_id</span> (обязательный): Идентификатор этапа.
### Возвращаемое значение
- <span style="color: orange;">span</span>: Созданный перегон.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql 
mutation {
  createSpan(createInput: { name: "string", projectObjectId: 14}) {
    span {
      rowId
      name
      projectObjectId
    }
    ok
    err_msg
  }
}
```

## [CreatePicketMutation](picket_create.py) Класс мутации на создание пикета
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании пикета типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название.
    - <span style="color: orange;">span_id</span> (обязательный): Идентификатор перегона.
### Возвращаемое значение
- <span style="color: orange;">span</span>: Созданный пикет.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql 
mutation {
  createPicket(createInput: { name: "string", spanId: 6}) {
    picket {
      rowId
      name
      projectObjectId
    }
    ok
    err_msg
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями платформы Mstroy

## [RemoveDirectoryFromProject](attachment_delete.py) Класс мутации на удаление указанной директории из проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">dir_input</span> (обязательный): Объект обмена данными об удалении указанной директории из проекта типа GraphQL.
    - <span style="color: orange;">p</span> (обязательный): Путь до папки.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  removeDirectoryFromProject(dirInput: { p: "string" }, projectId: 10) {
    result
  }
}
```


## [RemoveFileFromProjectElement](attachment_delete.py) Класс мутации на удаление указанной директории из проекта
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента проекта.
- <span style="color: orange;">file_input</span> (обязательный): Объект обмена данными об удалении файла из элемента проекта типа GraphQL.
    - <span style="color: orange;">p</span> (обязательный): Путь до папки.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  removeFileFromProjectElement(
    fileInput: { p: "string" }
    projectElementId: 10
  ) {
    result
  }
}
```


## [DeleteContragent](contragent_delete.py) Класс мутации на удаление контрагента
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">contragent</span>: Сущность контрагента.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteContragent(rowId: 10) {
    contragent {
      rowId
      name
    }
    ok
  }
}
```


## [DeleteEducationInfo](education_info_delete.py) Класс мутации на удаление записи об образовании сотрудника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор записи об образовании.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteEducationInfo(rowId: 10) {
    ok
  }
}
```


## [DeleteManager](manager_delete.py) Класс мутации на удаление менеджера проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор записи об образовании.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">manager</span>: Идентификатор менеджера.


### Пример использования
```graphql
mutation {
  deleteManager(rowId: 10) {
    okStatus
    manager {
      rowId
      name
    }
  }
}
```


## [BatchDeletePercoWorkerAccess](perco_worker_access_delete.py) Класс мутации на удаление списка назначений шаблонов доступа Perco
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Список идентификаторов назначения доступа Perco рабочим.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  batchDeletePercoWorkerAccess(rowIds: [10]) {
    ok
    errMsg
  }
}
```


## [DeleteOvertimeAccountingType](position_overtime_accounting_delete.py) Класс мутации на удаление типов переработок
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов типов переработок.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteOvertimeAccountingType(rowIds: [10]) {
    ok
  }
}
```


## [DeleteProject](project_delete.py) Класс мутации на удаление проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProject(projectId: 10) {
    ok
  }
}
```


## [DeleteProjectGroup](project_group_delete.py) Класс мутации на удаление группы участников проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор группы проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectGroup(rowId: 10) {
    ok
  }
}
```


## [DeleteProjectGroupResponsible](project_group_responsible_delete.py) Класс мутации на удаление связи группы проекта с ответственными
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор связи группы проекта с ответственными.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectGroupResponsible(rowId: 10) {
    ok
  }
}
```


## [DeleteProjectImage](project_image_delete.py) Класс мутации на удаление изображения из проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectImageMutation(projectId: 10) {
    ok
  }
}
```


## [DeleteProjectObject](project_object_delete.py) Класс мутации на удаление изображения из проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор этапа проекта.
### Возвращаемое значение
- <span style="color: orange;">project_object</span>: Сущность этапа проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectObject(rowId: 10) {
    projectObject {
      rowId
      name
    }
    ok
  }
}
```


## [DeleteProjectOrganizationUnit](project_org_unit_delete.py) Класс мутации на удаление проектного подразделения
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор проектного подразделения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectOrganizationUnit(rowId: 10) {
    ok
  }
}
```


## [DeleteProjectRole](project_role_delete.py) Класс мутации на удаление проектной роли
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор проектного подразделения.
### Возвращаемое значение
- <span style="color: orange;">project_role</span>: Сущность проектной роли.
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectRole(rowId: 10) {
    projectRole {
      rowId
      name
    }
    errMsg
    okStatus
  }
}
```


## [DeleteProjectScenario](project_scenario_delete.py) Класс мутации на удаление проектного сценария
### Аргументы
- <span style="color: orange;">project_scenario_id</span> (обязательный): Идентификатор сценария.
### Возвращаемое значение
- <span style="color: orange;">project_scenario</span>: Сущность проектного сценария.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectScenario(projectScenarioId: 10) {
    projectScenario {
      rowId
      name
    }
    okStatus
  }
}
```


## [DeleteResponsible](responsible_delete.py) Класс мутации на удаление ответственного
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">responsible</span>: Сущность ответственного.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResponsible(rowId: 10) {
    responsible {
      rowId
      managerId
    }
    ok
  }
}
```


## [DeleteResponsibleOrder](responsible_order_delete.py) Класс мутации на удаление приказа назначения ответственного лица
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор приказа назначения ответственного.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResponsibleOrder(rowId: 10) {
    ok
  }
}
```


## [DeleteResponsiblePowerAttorney](responsible_power_attorney_delete.py) Класс мутации на удаление доверенности ответственного
### Аргументы
- <span style="color: orange;">responsible_power_attorney_id</span> (обязательный): Идентификатор доверенности ответственного.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResponsiblePowerAttorney(responsiblePowerAttorneyId: 10) {
    okStatus
  }
}
```


## [EndWorkingInBrigade](tag_delete.py) Класс мутации на завершение работы бригады
### Аргументы
- <span style="color: orange;">tag_id</span> (обязательный): Идентификатор тега.
- <span style="color: orange;">resource_id</span> (обязательный): Идентификатор тайм-ресурса.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  endWorkingInBrigade(resourceId: 10, tagId: 10) {
    result
  }
}
```


## [EndWorkingInBrigade](tag_delete.py) Класс мутации на завершение работы бригады
### Аргументы
- <span style="color: orange;">tag_id</span> (обязательный): Идентификатор тега.
- <span style="color: orange;">resource_id</span> (обязательный): Идентификатор тайм-ресурса.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  endWorkingInBrigade(resourceId: 10, tagId: 10) {
    result
  }
}
```


## [DeleteTimeResource](time_resource_delete.py) Класс мутации на удаление тайм-ресурса
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор тега.
### Возвращаемое значение
- <span style="color: orange;">time_resource</span>: Сущность тайм-ресурса.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteTimeResource(rowId: 10) {
    timeResource {
      rowId
      name
      projectId
    }
    ok
  }
}
```


## [DeleteCombiningWorker](worker_delete.py) Класс мутации на удаление совмещенного работника
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатора совмещенного работника.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteCombiningWorker(projectId: 10, workerId: 10) {
    ok
  }
}
```


## [DeleteWorkerDocument](worker_document_delete.py) Класс мутации на удаление документа работника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор документа работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkerDocument(rowId: 10) {
    ok
  }
}
```


## [DeleteWorkerPassport](worker_passport_delete.py) Класс мутации на удаление паспортных данных работника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор паспортных данных работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkerPassport(rowId: 10) {
    ok
  }
}
```


## [DeleteSpansMutation](span_delete.py) Класс мутации на массовое удаление перегонов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов перегонов.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  deleteSpans(row_ids: [1]) {
    ok
    err_msg
  }
}
```

## [DeletePicketsMutation](picket_delete.py) Класс мутации на массовое удаление пикетов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов пикетов.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  deletePickets(row_ids: [1]) {
    ok
    err_msg
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями платформы Mstroy

## [UpdateAdditionalProjectProperties](additional_project_properties_update.py) Класс мутации на обновление дополнительных настроек проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">with_return</span> (default_value=False): Флаг возврата результата мутации.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении дополнительных настроек проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">additional_project_properties</span>: Сущность дополнительных настроек проекта.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  updateAdditionalProjectProperties(
    projectId: 10
    updateInput: {biShortName:"string"}
    withReturn: false
  ) {
    additionalProjectProperties {
      projectId
      biShortName
    }
    okStatus
    errMsg
  }
}
```


## [UpdateContragent](contragent_update.py) Класс мутации на обновление контрагента
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении контрагента типа GraphQL.
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">contragent</span>: Сущность контрагента.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateContragent(input: {contract:"string"}, rowId: 10) {
    contragent {
      rowId
      name
      projectId
    }
    ok
  }
}
```


## [UpdateEducationInfo](education_info_update.py) Класс мутации на обновление записи об образовании сотрудника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор записи об образовании.
- <span style="color: orange;">input_data</span> (обязательный): Объект обмена данными для обновления информации об образовании сотрудника типа GraphQL.
    - <span style="color: orange;">institution</span> (обязательный): Наименование образовательного учреждения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">education_info</span>: Сущность контрагента.


### Пример использования
```graphql
mutation {
  updateEducationInfo(inputData: { institution: "string" }, rowId: 6) {
    ok
    educationInfo {
      rowId
      workerId
      institution
    }
  }
}
```


## [UpdateEducationInfo](education_info_update.py) Класс мутации на обновление записи об образовании сотрудника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор записи об образовании.
- <span style="color: orange;">input_data</span> (обязательный): Объект обмена данными для обновления информации об образовании сотрудника типа GraphQL.
    - <span style="color: orange;">institution</span> (обязательный): Наименование образовательного учреждения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">education_info</span>: "Запись об образовании сотрудника.


### Пример использования
```graphql
mutation {
  updateEducationInfo(inputData: { institution: "string" }, rowId: 10) {
    ok
    educationInfo {
      rowId
      workerId
      institution
    }
  }
}
```


## [UpdateManager](manager_update.py) Класс мутации на обновление существующего менеджера
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор менеджера.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении менеджера типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">manager</span>: Сущность менеджера.


### Пример использования
```graphql
mutation {
  updateManager(rowId: 10, updateInput: {projectRoleId: 10}) {
    okStatus
    manager {
      rowId
      name
      projectId
    }
  }
}
```


## [UpdateOvertimeAccountingType](position_overtime_accounting_update.py) Класс мутации на обновление типа переработки
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор типа переработок.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении типа переработки типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">overtime_accounting_type</span>: Сущность типа переработки.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateOvertimeAccountingType(input: {name:"string"}, rowId: 10) {
    overtimeAccountingType {
      rowId
      name
      description
    }
    ok
  }
}
```


## [UpdateProject](project_update.py) Класс мутации на обновление проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project</span>: Сущность проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProject(input: {name:"string" contractIds:[10]}, projectId: 10) {
    project {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateProjectGroup](project_group_update.py) Класс мутации на обновление группы участников проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор группы проекта.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении группы участников проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_group</span>: Сущность группы проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectGroup(input: {name:"string"}, rowId: 10) {
    projectGroup {
      rowId
      projectId
      name
      isConstructionCabinet
    }
    ok
  }
}
```


## [UpdateProjectGroupResponsibleSort](project_group_responsible_update.py) Класс мутации на обновление группы участников проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор связи группы проекта с ответственными.
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об обновление порядка вывода ответственных в группе проекта типа GraphQL.
    - <span style="color: orange;">responsible_id</span> (обязательный): Порядковый номер для вывода в иерархии участников.
    - <span style="color: orange;">serial_number_to_output</span> (обязательный): Примечание к связи группы проекта с ответственными.
### Возвращаемое значение
- <span style="color: orange;">project_group_responsible</span>: Сущность связи группы проекта с ответственными.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectGroupResponsibleSort(
    inputs: [{ serialNumberToOutput: 10 responsibleId: 10 }]
    rowId: 20
  ) {
    projectGroupResponsible {
      rowId
      projectGroupId
      responsibleId
      serialNumberToOutput
    }
    ok
  }
}
```


## [UpdateProjectObject](project_object_update.py) Класс мутации на обновление этапа проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор этапа проекта.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении этапа проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_object</span>: Сущность этапа проекта.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectObject(input: {name:"string"}, rowId: 10) {
    projectObject {
      rowId
      name
      shortName
    }
    ok
  }
}
```


## [UpdateProjectOrganizationUnit](project_org_unit_update.py) Класс мутации на обновление проектного подразделения
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор проектного подразделения.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении проектного подразделения типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_organization_unit</span>: Сущность проектного подразделения.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectOrganizationUnit(input: {name:"string"}, rowId: 10) {
    projectOrganizationUnit {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateProjectRole](project_role_update.py) Класс мутации на обновление проектной роли
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор проектной роли.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении проектной роли типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_role</span>: Сущность проектной роли.
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectRole(rowId: 10, updateInput: {name:"string"}) {
    projectRole {
      rowId
      name
    }
    errMsg
    okStatus
  }
}
```


## [BatchUpdateProjectRolesScenarios](project_role_update.py) Класс мутации на обновление проектной роли
### Аргументы
- <span style="color: orange;">roles_ids</span> (обязательный): Список идентификаторов ролей.
- <span style="color: orange;">scenarios_ids</span> (обязательный): Список идентификаторов проектных сценариев.
- <span style="color: orange;">with_delete</span> (default_value=False): Флаг удаления сценариев для ролей.
### Возвращаемое значение
- <span style="color: orange;">project_roles</span>: Список проектных ролей.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  batchUpdateProjectRolesScenarios(
    rolesIds: [10]
    scenariosIds: [10]
    withDelete: false
  ) {
    projectRoles {
      rowId
      name
    }
    okStatus
  }
}
```


## [UpdateProjectScenario](project_scenario_update.py) Класс мутации на обновление проектного сценария
### Аргументы
- <span style="color: orange;">project_scenario_id</span> (обязательный): Идентификатор сценария.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными для обновления проектного сценария типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_scenario</span>: Сущность проектного сценария.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">error</span>: Текст ошибки.


### Пример использования
```graphql
НА ДОРАБОТКЕ
```


## [UpdateResponsible](responsible_update.py) Класс мутации на обновление ответственного
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении ответственного типа GraphQL.
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор ответственного.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">responsible</span>: Сущность ответственного.


### Пример использования
```graphql
mutation {
  updateResponsible(input: {jobType:"string"}, rowId: 10) {
    ok
    responsible {
      rowId
      managerId
    }
  }
}
```


## [UpdateResponsibleSort](responsible_update.py) Класс мутации на обновление порядка вывода ответственных
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об обновлении порядка вывода ответственных типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible</span>: Сущность ответственного.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateResponsibleSort(inputs: [{ serialNumberToOutput: 10 responsibleId: 10 }]) {
    responsible {
      rowId
      managerId
      responsibleOrderId
    }
    ok
  }
}
```


## [SetResponsibleFieldOrder](responsible_field_order_update.py) Класс мутации на обновление порядка полей ответственных для текущего пользователя
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об установке порядка полей ответственных для текущего пользователя типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible_field_order</span>: Сущность порядка полей ответственных.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setResponsibleFieldOrder(input: {fieldOrder:"string"}) {
    responsibleFieldOrder {
      userId
      fieldOrder
      fieldOrderConstructionCabinet
    }
    ok
  }
}
```


## [UpdateResponsibleOrder](responsible_order_update.py) Класс мутации на обновление приказа назначения ответственного лица
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор приказа назначения ответственного.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об установке порядка полей ответственных для текущего пользователя типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible_order</span>: Сущность приказа назначения ответственного лица.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateResponsibleOrder(input: {orderNumber:"string"}, rowId: 12) {
    responsibleOrder {
      rowId
      contragentId
      projectId
    }
    ok
  }
}
```


## [UpdateResponsiblePowerAttorney](responsible_power_attorney_update.py) Класс мутации на обновление доверенности ответственного
### Аргументы
- <span style="color: orange;">responsible_power_attorney_id</span> (обязательный): Идентификатор доверенности ответственного.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении доверенности ответственного типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">responsible_power_attorney</span>: Сущность доверенности ответственного.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateResponsiblePowerAttorney(
    responsiblePowerAttorneyId: 10
    updateInput: {idMchd: "string"}
  ) {
    responsiblePowerAttorney {
      rowId
      idMchd
    }
    okStatus
  }
}
```


## [TransferInOtherBrigade](tag_update.py) Класс мутации на перевод в другую бригаду
### Аргументы
- <span style="color: orange;">old_tag_id</span> (обязательный): Идентификатор старого тега.
- <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор тайм-ресурса.
- <span style="color: orange;">new_tag_id</span> (обязательный): Идентификатор нового тега.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  transferInOtherBrigade(
    newTagId: 10
    oldTagId: 10
    timeResourceId: 10
  ) {
    result
  }
}
```


## [UpdateWorker](worker_update.py) Класс мутации на обновление работника
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении работника типа GraphQL.
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор сущности работника.
### Возвращаемое значение
- <span style="color: orange;">worker</span>: Сущность работника.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateWorker(input: {surname:"string"}, workerId: 10) {
    worker {
      rowId
      firstName
    }
    ok
  }
}
```


## [FireWorker](worker_update.py) Класс мутации на увольнение работника
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор сущности работника.
- <span style="color: orange;">firing_date</span> (default_value=None): Дата увольнения работника.
### Возвращаемое значение
- <span style="color: orange;">worker</span>: Сущность работника.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  fireWorker(firingDate: "2024-01-01", workerId: 10) {
    worker {
      rowId
      firstName
      surname
    }
    ok
  }
}
```


## [UnFireWorker](worker_update.py) Класс мутации на восстановление в должности уволенного работника
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор сущности работника.
### Возвращаемое значение
- <span style="color: orange;">worker</span>: Сущность работника.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  unfireWorker(workerId: 10) {
    worker {
      rowId
      firstName
      surname
    }
    ok
  }
}
```


## [SetWorkerRfid](worker_update.py) Класс мутации на установление нового значения rfid для работника
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">new_rfid</span> (обязательный): rfid работника.
### Возвращаемое значение
- <span style="color: orange;">result</span>: Результат выполнения запроса.


### Пример использования
```graphql
mutation {
  setWorkerRfid(newRfid: "string", workerId: 10) {
    result
  }
}
```


## [UpdateWorkerDocument](worker_document_update.py) Класс мутации на обновление документа работника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор документа работника.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновления документа работника типа GraphQL.
- <span style="color: orange;">content</span> (default_value=None): Контент документа работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">worker_document</span>: Данные о документах работника.


### Пример использования
```graphql
mutation {
  updateWorkerDocument(input: {name:"string"}, rowId: 10) {
    ok
    workerDocument {
      rowId
      name
    }
  }
}
```


## [FinishWorkerEducation](worker_education_update.py) Класс мутации на завершение инструктажа сотрудником
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификаторов видео-инструктажа.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновления документа работника типа GraphQL.
- <span style="color: orange;">content</span> (default_value=None): Контент документа работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">worker_education</span>: Данные об обучении сотрудника.


### Пример использования
```graphql
mutation {
  finishWorkerEducation(rowId: 10) {
    ok
    workerEducation {
      rowId
      appointDate
    }
  }
}
```


## [UpdateWorkerPassport](worker_passport_update.py) Класс мутации на обновление паспортных данных работника
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор паспортных данных работника.
- <span style="color: orange;">input</span> (обязательный): Объект данных об обновлении паспорта работника типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">worker_passport</span>: Паспортные данные работника.


### Пример использования
```graphql
mutation {
  updateWorkerPassport(input: {passportSerial:"12 34" passportNumber:"567890" issuerCode:"123-456"}, rowId: 1) {
    ok
    workerPassport {
      rowId
      workerId
    }
  }
}
```


## [UpdateSpanMutation](span_update.py) Класс мутации на обновление перегона
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор перегона.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении перегона типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">span</span>: Перегон.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  updateSpan(
    row_id: 2
    updateInput: { name: "update"}
  ) {
    span {
      rowId
      name
      projectObjectId
    }
    ok
    err_msg
  }
}
```


## [UpdatePicketMutation](picket_update.py) Класс мутации на обновление пикета
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор пикета.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении пикета типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">picket</span>: Пикет.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  updatePicket(
    row_id: 2
    updateInput: { name: "update"}
  ) {
    picket {
      rowId
      name
      spanId
    }
    ok
    err_msg
  }
}
```


# Модуль запросов для взаимодействия с сущностями модуля mstroy

## [getAdditionalProjectProperties](additional_project_properties.py) Получение дополнительных настроек проекта по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">AdditionalProjectProperties</span>: Дополнительные настройки проекта.


### Пример использования
```graphql
query {
  getAdditionalProjectProperties(projectId: 10) {
    projectId
    biShortName
  }
}
```


## [getClassifierFile](classifier.py) Получение дополнительных настроек проекта по идентификатору проекта
### Аргументы
- <span style="color: orange;">directory_id</span> (обязательный): Идентификатор директории, по которой будет сформирован файл.
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getClassifierFile(directoryId: 10)
}
```


## [getVdcFromCode](classifier.py) Получение кода ВДЦ(Смет) из кода работы
### Аргументы
- <span style="color: orange;">code</span> (обязательный): Код работы.
### Возвращаемое значение
- <span style="color: orange;">TList[str]</span>: Список кодов ВДЦ.


### Пример использования
```graphql
query {
  getVdcFromCode(code: "string")
}
```


## [getProjectContragentsByProjectIds](contragent.py) Получение контрагентов по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">has_project_organization_unit_types</span> (default_value=None): Список типов подразделений.
- <span style="color: orange;">root_should_present</span> (default_value=False): Флаг присутствия родительского элемента в результатах.
- <span style="color: orange;">show_in_table</span> (default_value=False): Флаг отображения контрагентов в табеле.
### Возвращаемое значение
- <span style="color: orange;">TList[Contragent]</span>: Список контрагентов.


### Пример использования
```graphql
query {
  getProjectContragentsByProjectIds(projectIds: [10]) {
    projectContragents {
      rowId
      name
      projectId
      contract
      contragentRole
      organizationId
      parentContragentId
      responsibleForControlId
      isConstructionCabinet
      showInTable
    }
    projectId
  }
}
```


## [getContragents](contragent.py) Получение контрагентов по списку идентификаторов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов контрагентов.
### Возвращаемое значение
- <span style="color: orange;">TList[Contragent]</span>: Список контрагентов.


### Пример использования
```graphql
query {
  getContragents(rowIds: [10]) {
    rowId
    name
    projectId
    project {
      rowId
      name
    }
    contract
    contragentRole
    organizationId
    parentContragentId
    responsibleForControlId
    organizationUnits {
      rowId
      name
      projectOrgUnitType
      contragentId
    }
    organization {
      title
      fullTitle
    }
    managers {
      rowId
      name
      projectId
    }
    responsibleForControl {
      rowId
      name
      projectId
    }
    isConstructionCabinet
    showInTable
  }
}
```


## [getProjectContragentsByProjectIds](contragent.py) Получение контрагентов по списку идентификаторов проектов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectContragentsObject]</span>: Список контрагентов проектов.


### Пример использования
```graphql
query {
  getProjectContragentsByProjectIds(projectIds: [10]) {
    projectContragents {
      rowId
      name
      projectId
      contract
      contragentRole
      organizationId
      parentContragentId
      responsibleForControlId
      isConstructionCabinet
      showInTable
    }
    projectId
  }
}
```


## [getEducationInfoByWorkerId](education_info.py) Получение информацию об образовании по сотруднику
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор сотрудника.
### Возвращаемое значение
- <span style="color: orange;">TList[EducationInfo]</span>: Список с информацией об образовании.


### Пример использования
```graphql
query {
  getEducationInfoByWorkerId(workerId: 10) {
    rowId
    workerId
    institution
    speciality
    endYear
  }
}
```


## [projectManagers](manager.py) Получение менеджеров по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор сотрудника.
- <span style="color: orange;">project_org_unit_types</span> (default_value=None): Идентификатор сотрудника.
### Возвращаемое значение
- <span style="color: orange;">TList[Manager]</span>: Список менеджеров.


### Пример использования
```graphql
query {
  projectManagers(projectId: 10) {
    rowId
    name
    projectId
    project {
      rowId
      name
    }
    userId
    projectOrganizationUnitId
    projectRoleId
    contragentId
    user {
      rowId
      username
    }
    projectRole {
      rowId
      name
    }
    projectOrganizationUnit {
      rowId
      name
    }
    contragent {
      rowId
      name
    }
  }
}
```


## [userManagers](manager.py) Получение менеджеров пользователя
### Аргументы
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[Manager]</span>: Список менеджеров.


### Пример использования
```graphql
query {
  userManagers {
    rowId
    name
    projectId
    project {
      rowId
      name
    }
    userId
    projectOrganizationUnitId
    projectRoleId
    contragentId
    user {
      rowId
      username
    }
    projectRole {
      rowId
      name
    }
    projectOrganizationUnit {
      rowId
      name
    }
    contragent {
      rowId
      name
    }
  }
}
```


## [getProjectManagersByProjOrgUnitId](manager.py) Получение менеджеров подразделений по идентификатору подразделения
### Аргументы
- <span style="color: orange;">project_organization_unit_id</span> (обязательный): Список менеджеров подразделений по идентификатору подразделения.
### Возвращаемое значение
- <span style="color: orange;">TList[Manager]</span>: Список менеджеров.


### Пример использования
```graphql
query {
  getProjectManagersByProjOrgUnitId(projectOrganizationUnitId: 10) {
    rowId
    name
    projectId
    project {
      rowId
      name
    }
    userId
    projectOrganizationUnitId
    projectRoleId
    contragentId
    user {
      rowId
      username
    }
    projectRole {
      rowId
      name
    }
    projectOrganizationUnit {
      rowId
      name
    }
    contragent {
      rowId
      name
    }
  }
}
```


## [getProjectOrganizationUnitByType](manager.py) Получение менеджеров подразделений по идентификатору подразделения
### Аргументы
- <span style="color: orange;">contragent_role</span> (обязательный): Роль контрагента.
- <span style="color: orange;">project_organization_unit_type</span> (обязательный): Тип подразделения.
- <span style="color: orange;">user_id</span> (default_value=None): Идентификатор пользователя.
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectOrganizationUnit]</span>: Список подходящих проектных подразделений.


### Пример использования
```graphql
query {
  getProjectOrganizationUnitByType(
    contragentRole: GENERAL_CONTRACTOR
    projectOrganizationUnitType: LABORATORY
  ) {
    rowId
    name
    projectOrgUnitType
    contragentId
    managers {
      rowId
      name
    }
  }
}
```


## [allOrganizationUnitProjectRoles](manager.py) Получение проектных ролей подразделения
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationUnitProjectRole]</span>: Список проектных ролей подразделения.


### Пример использования
```graphql
query {
  allOrganizationUnitProjectRoles {
    rowId
    name
    description
    organizations {
      title
      fullTitle
      opfFull
    }
    projectScenarios {
      rowId
      name
    }
    contragentRole
    projectOrganizationUnitType
  }
}
```


## [getOrgUnitProjectRoleByTypes](manager.py) Получение проектных ролей подразделения
### Аргументы
- <span style="color: orange;">project_org_unit_type</span> (обязательный): Тип проектной роли.
- <span style="color: orange;">contragent_role</span> (обязательный): Роль контрагента.
### Возвращаемое значение
- <span style="color: orange;">OrganizationUnitProjectRole | None</span>: Проектная роль подразделения.


### Пример использования
```graphql
query {
  getOrgUnitProjectRoleByTypes(
    projectOrgUnitType: LABORATORY
    contragentRole: GENERAL_CONTRACTOR
  ) {
    rowId
    name
    description
    organizations {
      title
      fullTitle
      opfFull
    }
    projectScenarios {
      rowId
      name
    }
    contragentRole
    projectOrganizationUnitType
  }
}
```


## [allPositionGroups](position_group.py) Получение кадровых должностей
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[PositionGroup]</span>: Список кадровых должностей.


### Пример использования
```graphql
query {
  allPositionGroups {
    rowId
    name
    staffPosition
    serialNumber
  }
}
```


## [getAllOvertimeAccountingType](position_overtime_accounting.py) Получение типов переработок
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов переработок.
### Возвращаемое значение
- <span style="color: orange;">TList[PositionOvertimeAccounting]</span>: Список переработок.


### Пример использования
```graphql
query {
  getAllOvertimeAccountingType(rowIds: [10]) {
    rowId
    name
    description
  }
}
```


## [supervisionProjects](project.py) Получение всех проектов, к которым пользователь имеет сущность строй-контроля
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Project]</span>: Список проектов.


### Пример использования
```graphql
query {
  supervisionProjects {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
    shortName
    tags {
      rowId
      name
    }
    objects {
      rowId
      name
    }
    region {
      id
      name
    }
    incidentCounts {
      total
    }
    inspectionCounts {
      total
      notAccepted
      new
      onCheck
    }
    actualProjectTransaction {
      rowId
      name
    }
    factProjectTransaction {
      rowId
      name
    }
    organization {
      title
      fullTitle
      opfFull
    }
    organizationUnit {
      rowId
      title
    }
    additionalProjectProperties {
      projectId
      biShortName
    }
  }
}
```


## [allProjects](project.py) Получение всех проектов
### Аргументы
- <span style="color: orange;">row_id</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">ignore_deleted</span> (default_value=None): Игнорировать удаленные проекты.
- <span style="color: orange;">project_enum_filters</span> (default_value=None): Объект фильтров по перечислениям полей сущности проекта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[Project] | ProjectCollection</span>: Список проектов | коллекция проектов.


### Пример использования
```graphql
query {
  allProjects {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
    tags {
      rowId
      name
    }
    objects {
      rowId
      name
    }
    region {
      id
      name
    }
    incidentCounts {
      total
    }
    inspectionCounts {
      total
      notAccepted
      new
      onCheck
    }
    actualProjectTransaction {
      rowId
      name
    }
    factProjectTransaction {
      rowId
      name
    }
    organization {
      title
      fullTitle
    }
    organizationUnit {
      rowId
      title
    }
    additionalProjectProperties {
      projectId
      biShortName
    }
  }
}
```

## [getProjectByIds](project.py) Получение списка проектов по списку идентификаторов
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">with_perco</span> (default_value=False): Флаг участия проектов в перке.
- <span style="color: orange;">with_tags</span> (default_value=False): Флаг получения тегов.
### Возвращаемое значение
- <span style="color: orange;">TList[Project] | ProjectCollection</span>: Список проектов | коллекция проектов.


### Пример использования
```graphql
query {
  getProjectByIds(projectIds: [10]) {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
    tags {
      rowId
      name
    }
    objects {
      rowId
      name
    }
    region {
      id
      name
    }
    incidentCounts {
      total
    }
    inspectionCounts {
      total
    }
    actualProjectTransaction {
      rowId
      name
    }
    factProjectTransaction {
      rowId
      name
    }
    organization {
      title
      fullTitle
      opfFull
    }
    organizationUnit {
      rowId
      title
    }
    additionalProjectProperties {
      projectId
      biShortName
    }
  }
}
```


## [getProjectByOrganizationIds](project.py) Получение списка проектов по списку идентификаторов организаций
### Аргументы
- <span style="color: orange;">org_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[Project] | ProjectCollection</span>: Список проектов | коллекция проектов.


### Пример использования
```graphql
query {
  getProjectByOrganizationIds(orgIds: [10]) {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
    tags {
      rowId
      name
    }
    objects {
      rowId
      name
    }
    region {
      id
      name
    }
    incidentCounts {
      total
    }
    inspectionCounts {
      total
    }
    actualProjectTransaction {
      rowId
      name
    }
    factProjectTransaction {
      rowId
      name
    }
    organization {
      title
      fullTitle
      opfFull
    }
    organizationUnit {
      rowId
      title
    }
    additionalProjectProperties {
      projectId
      biShortName
    }
  }
}
```


## [getProjectsByProjectObjectIds](project.py) Получение проектов по списку идентификаторов этапов
### Аргументы
- <span style="color: orange;">project_object_ids</span> (обязательный): Список идентификаторов этапов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификатор проектов, которые не будут включены в результат запроса.
### Возвращаемое значение
- <span style="color: orange;">TList[Project]</span>: Список проектов.


### Пример использования
```graphql
query {
  getProjectsByProjectObjectIds(projectObjectIds: [10]) {
    policy {
      read
      create
      update
      delete
    }
    rowId
    name
    tags {
      rowId
      name
    }
    objects {
      rowId
      name
    }
    region {
      id
      name
    }
    incidentCounts {
      total
    }
    inspectionCounts {
      total
    }
    actualProjectTransaction {
      rowId
      name
    }
    factProjectTransaction {
      rowId
      name
    }
    organization {
      title
      fullTitle
      opfFull
    }
    organizationUnit {
      rowId
      title
    }
    additionalProjectProperties {
      projectId
      biShortName
    }
  }
}
```


## [getProjectGroup](project_group.py) Получение списка групп проектов
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=None): Список идентификаторов групп проекта.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проекта.
- <span style="color: orange;">name</span> (default_value=None): Название группы.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectGroup]</span>: Список проектных групп.


### Пример использования
```graphql
query {
  getProjectGroup {
    rowId
    projectId
    name
    isConstructionCabinet
    project {
      rowId
      name
    }
  }
}
```


## [getProjectGroupResponsible](project_group_responsible.py) Получение списка связи группы проекта с ответственными
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=None): Список идентификаторов групп проекта.
- <span style="color: orange;">project_group_ids</span> (default_value=None): Список идентификаторов группы проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectGroupResponsible]</span>: Список связей групп проекта с ответственными.

 
### Пример использования
```graphql
query {
  getProjectGroupResponsible {
    rowId
    projectGroupId
    responsibleId
    serialNumberToOutput
    note
    projectGroup {
      rowId
      name
    }
    responsible {
      rowId
      managerId
    }
  }
}
```


## [allProjectObjects](project_object.py) Получение всех этапов проектов
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectObject]</span>: Список этапов проектов.

 
### Пример использования
```graphql
query {
  allProjectObjects {
    rowId
    name
    shortName
    spans {
      rowId
      name
      projectObjectId
    }
  }
}
```


## [getProjectObjectsByProjectId](project_object.py) Получение списка этапов проекта по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectObject]</span>: Список объектов проекта.

 
### Пример использования
```graphql
query {
  getProjectObjectsByProjectId(projectId: 10) {
    rowId
    name
    shortName
    spans {
      rowId
      name
      projectObjectId
    }
  }
}
```


## [getMatchedProjectObjects](project_object.py) Получение сопоставленных названий этапов проектов с названиями проектов
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[ObjectNameProjectName]</span>: Список объектов сопоставления названия этапа с названием проекта.

 
### Пример использования
```graphql
query {
  getMatchedProjectObjects(projectIds: [10]) {
    projectObjectName
    projectShortName
  }
}
```


## [getProjectObjectsByWorkIds](project_object.py) Получение этапов проекта по идентификаторам работ
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkProjectObject]</span>: Список объектов связей работ и этапов проекта.

 
### Пример использования
```graphql
query {
  getProjectObjectsByWorkIds(workIds: [10]) {
    projectObject {
      rowId
      name
      shortName
    }
    workId
  }
}
```


## [getProjectObjectsByProjectIds](project_object.py) Получение этапов проектов по идентификаторам проектов
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectObject]</span>: Список объектов связей работ и этапов проекта.

 
### Пример использования
```graphql
query {
  getProjectObjectsByProjectIds(projectIds: [10]) {
    rowId
    name
    shortName
    spans {
      rowId
      name
      projectObjectId
    }
  }
}
```


## [getProjectObjectsByTransactionId](project_object.py) Получение этапов проектов, назначенных на операции, по идентификатору транзакции
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectObject]</span>: Список объектов связей работ и этапов проекта.

 
### Пример использования
```graphql
query {
  getProjectObjectsByTransactionId(projectTransactionId: 10) {
    rowId
    name
    shortName
    spans {
      rowId
      name
      projectObjectId
    }
  }
}
```


## [projectOrganizationUnits](project_org_unit.py) Получение проектных подразделений проекта
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectOrganizationUnit]</span>: Список проектных подразделений.

 
### Пример использования
```graphql
query {
  projectOrganizationUnits(projectId: 10) {
    rowId
    name
    projectOrgUnitType
    contragentId
    managers {
      rowId
      name
      projectId
      userId
      projectOrganizationUnitId
      projectRoleId
      contragentId
    }
  }
}
```


## [getProjectZoneVolumeWeight](project_zone_volume_weight.py) Получение объемных весов проектных зон
### Аргументы
- <span style="color: orange;">project_zone_ids</span> (default_value=None): Список идентификаторов проектных зон.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectZoneVolumeWeight]</span>: Список объектов обмена данными об объемном весе проектной зоны типа GraphQL.

 
### Пример использования
```graphql
query {
  getProjectZoneVolumeWeight {
    rowId
    projectZoneId
    projectZone {
      id
      name
      color
      zoneType
      projectZoneType
      projectId
      organizationId
    }
    volumeWeight
    beginDate
    finishDate
  }
}
```


## [getProjectRole](query.py) Получение проектной роли по идентификатору
### Аргументы
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ProjectRole | None</span>: Проектная роль.

 
### Пример использования
```graphql
query {
  getProjectRole(projectId: 10) {
    rowId
    name
    description
    organizations {
      title
      fullTitle
      opfFull
    }
    projectScenarios {
      rowId
      name
    }
  }
}
```


## [getUserProjectScenarios](query.py) Получение сценариев пользователя в контексте проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectScenario]</span>: Список проектных сценариев.

 
### Пример использования
```graphql
query {
  getUserProjectScenarios(projectId: 10) {
    rowId
    name
    description
    rootName
    viewPolicies {
      typeName
      read
      create
      update
      delete
    }
  }
}
```


## [allProjectScenarios](query.py) Получение проектных сценариев
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectScenario]</span>: Список проектных сценариев.

 
### Пример использования
```graphql
query {
  allProjectScenarios {
    rowId
    name
    description
    rootName
    viewPolicies {
      typeName
      read
      create
      update
      delete
    }
  }
}
```


## [getOrganizationsByProjectRole](query.py) Получение проектной роли по идентификатору
### Аргументы
- <span style="color: orange;">project_role_id</span> (обязательный): Идентификатор проектной роли.
### Возвращаемое значение
- <span style="color: orange;">ProjectRole</span>: Проектная роль.

 
### Пример использования
```graphql
query {
  getOrganizationsByProjectRole(projectRoleId: 10) {
    rowId
    name
    description
    organizations {
      title
      fullTitle
      opfFull
    }
    projectScenarios {
      rowId
      name
    }
  }
}
```


## [allRegions](region.py) Получение всех регионов
### Аргументы
- <span style="color: orange;">row_id</span> (default_value=None): Идентификатор региона.
- <span style="color: orange;">order_by</span> (default_value=None): Список фильтров сортировки для возвращаемого ответа.
### Возвращаемое значение
- <span style="color: orange;">TList[Region] | RegionCollection</span>: Список регионов | коллекция регионов.


### Пример использования
```graphql
query {
  allRegions {
    id
    rowId
    name
    code
  }
}
```


## [getRegionsByIds](region.py) Получение регионов по списку идентификаторов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов регионов.
- <span style="color: orange;">order_by</span> (default_value=None): Список фильтров сортировки для возвращаемого ответа.
### Возвращаемое значение
- <span style="color: orange;">RegionCollection</span>: Коллекция регионов.


### Пример использования
```graphql
query {
  getRegionsByIds(rowIds: [10]) {
    id
    rowId
    name
    code
  }
}
```


## [filterRegionByName](region.py) Получение фильтрованной коллекции регионов по переданной подстроке
### Аргументы
- <span style="color: orange;">text</span> (default_value=None): Строка для фильтрации регионов.
- <span style="color: orange;">order_by</span> (default_value=None): Список фильтров сортировки для возвращаемого ответа.
### Возвращаемое значение
- <span style="color: orange;">RegionCollection</span>: Коллекция регионов.


### Пример использования
```graphql
query {
  filterRegionByName {
    id
    rowId
    name
    code
  }
}
```


## [getResponsible](responsible.py) Получение ответственных
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов ответственных.
### Возвращаемое значение
- <span style="color: orange;">TList[Responsible]</span>: Список ответственных.


### Пример использования
```graphql
query {
  getResponsible(rowIds: [10]) {
    rowId
    managerId
    manager {
      rowId
      name
    }
    serialNumberToOutput
    responsibleOrder {
      rowId
    }
    responsiblePowerAttorney {
      rowId
    }
  }
}
```


## [getResponsibleByManagerIds](responsible.py) Получение ответственных по списку идентификаторов менеджеров
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов менеджеров.
### Возвращаемое значение
- <span style="color: orange;">TList[Responsible]</span>: Список ответственных.


### Пример использования
```graphql
query {
  getResponsibleByManagerIds(rowIds: [10]) {
    rowId
    managerId
    manager {
      rowId
      name
    }
    serialNumberToOutput
    responsibleOrder {
      rowId
    }
    responsiblePowerAttorney {
      rowId
    }
  }
}
```


## [getResponsibleByProjectIds](responsible.py) Получение ответственных по списку идентификаторов проектов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[Responsible]</span>: Список ответственных.


### Пример использования
```graphql
query {
  getResponsibleByProjectIds(rowIds: [10]) {
    rowId
    managerId
    manager {
      rowId
      name
    }
    serialNumberToOutput
    responsibleOrder {
      rowId
    }
    responsiblePowerAttorney {
      rowId
    }
  }
}
```


## [getResponsibleByUserIds](responsible.py) Получение ответственных по списку идентификаторов пользователей
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов пользователей.
### Возвращаемое значение
- <span style="color: orange;">TList[Responsible]</span>: Список ответственных.


### Пример использования
```graphql
query {
  getResponsibleByUserIds(rowIds: [10]) {
    rowId
    managerId
    manager {
      rowId
      name
    }
    serialNumberToOutput
    responsibleOrder {
      rowId
    }
    responsiblePowerAttorney {
      rowId
    }
  }
}
```


## [getResponsibleByContragentIds](responsible.py) Получение ответственных по списку идентификаторов контрагентов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов контрагентов.
### Возвращаемое значение
- <span style="color: orange;">TList[Responsible]</span>: Список ответственных.


### Пример использования
```graphql
query {
  getResponsibleByContragentIds(rowIds: [10]) {
    rowId
    managerId
    manager {
      rowId
      name
    }
    serialNumberToOutput
    responsibleOrder {
      rowId
    }
    responsiblePowerAttorney {
      rowId
    }
  }
}
```


## [checkResponsibleByContragentIds](responsible.py) Проверка наличия ответственных для контрагентов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов контрагентов.
### Возвращаемое значение
- <span style="color: orange;">TList[ResponsibleCheck]</span>: Список объектов проверки наличия ответственных.


### Пример использования
```graphql
query {
  checkResponsibleByContragentIds(rowIds: [10]) {
    rowId
    checkResponsible
  }
}
```


## [getResponsibleFieldOrder](responsible_field_order.py) Получение порядка полей ответственного для пользователя
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">ResponsibleFieldOrder | None</span>: Порядок полей ответственного.


### Пример использования
```graphql
query {
  getResponsibleFieldOrder {
    userId
    fieldOrder
    fieldOrderConstructionCabinet
  }
}
```


## [getResponsibleOrder](responsible_order.py) Получение списка приказов назначения ответственных с различными фильтрами
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов приказов назначения ответственных.
- <span style="color: orange;">contragent_id</span> (default_value=None): Идентификатор контрагента.
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ResponsibleOrder]</span>: Список приказов назначения ответственных.


### Пример использования
```graphql
query {
  getResponsibleOrder(rowIds: [10]) {
    rowId
    contragentId
    projectId
    orderNumber
    dateStart
    dateFinish
    fileId
    file {
      id
      createdAt
      updatedAt
      name
      size
      guid
      fullPath
      parentFolderId
      creatorUsername
      actualVersionFileId
      getUrl
    }
  }
}
```


## [getProjectTags](tag.py) Получение тегов проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[Tag]</span>: Список тегов.


### Пример использования
```graphql
query {
  getProjectTags(projectId: 10) {
    rowId
    name
    projectId
    type
    organizationId
    projectObjectId
    projectObject {
      rowId
      name
      shortName
    }
  }
}
```


## [getTimeResourceByWorker](time_resource.py) Получение тайм-ресурса по идентификатору проекта и идентификатору работника
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TimeResource</span>: Тайм-ресурс.


### Пример использования
```graphql
query {
  getTimeResourceByWorker(workerId: 10 projectId: 10) {
    rowId
    name
    projectId
    project {
      rowId
      name
    }
    workerId
    category
    isActive
    activeTagId
    activeTag {
      rowId
      name
    }
    worker {
      rowId
      firstName
      surname
    }
  }
}
```


## [getTimeResourceIdByUserAndProject](time_resource.py) Получение идентификатора тайм-ресурса по идентификаторам проекта и работника
### Аргументы
- <span style="color: orange;">user_id</span> (обязательный): Идентификатор пользователя.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TimeResourceData</span>: Объект обмена данными о тайм-ресурсах типа GraphQL.


### Пример использования
```graphql
query {
  getTimeResourceIdByUserAndProject(userId: 10, projectId: 10) {
    errMsg
    timeResourceId
  }
}
```


## [getUserSettings](user_settings.py) Получение настроек пользователя по идентификатору пользователя
### Аргументы
- <span style="color: orange;">user_id</span> (обязательный): Идентификатор пользователя.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Строка настроек пользователя.


### Пример использования
```graphql
query {
  getUserSettings(userId: 10)
}
```


## [searchWorker](worker.py) Получение работника по параметрам
### Аргументы
- <span style="color: orange;">text</span> (обязательный): Строка для поиска.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">organization_name</span> (default_value=None): Название организации.
- <span style="color: orange;">row_id</span> (default_value=None): Идентификатор работника.
- <span style="color: orange;">with_fired</span> (default_value=False): Флаг учета уволенных работников при поиске.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
- <span style="color: orange;">day_report_filter</span> (default_value=False): Флаг проверки существования дневных отчетов.
- <span style="color: orange;">only_last_day_reports</span> (default_value=False): Флаг для ограничения количества выдачи дневных отчетов на каждый тайм-ресурс. Если передан, отображается список только последних отчетов, иначе все.
### Возвращаемое значение
- <span style="color: orange;">SearchWorker</span>: Объект связи работника, тайм ресурса, дневных отчетов.


### Пример использования
```graphql
query {
  searchWorker(
    text: "string"
    organizationIds: [10]
  ) {
    workers {
      rowId
      firstName
      surname
      lastName
    }
    timeResources {
      rowId
      name
    }
    dayReports {
      rowId
      factHours
    }
  }
}
```


## [getWorkerByRfid](worker.py) Получение работника по rfid
### Аргументы
- <span style="color: orange;">rfid</span> (обязательный): rfid.
### Возвращаемое значение
- <span style="color: orange;">WorkerWithTimeResourceQuery</span>: Объект связи работника с тайм-ресурсом.


### Пример использования
```graphql
query {
  getWorkerByRfid(rfid: "string") {
    worker {
      rowId
      firstName
      surname
      lastName
      tableNumber
      positionId
      organizationUnitId
      rate
      birthdate
      gender
      northCoefficient
      harmCoefficient
      organizationId
      rfidValue
      isFired
      vaccination
      piece
      userId
      isActualWorker
      notificationText
    }
    timeResourceId
  }
}
```


## [allWorkers](worker.py) Получение работников
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[Worker]</span>: Список работников.


### Пример использования
```graphql
query {
  allWorkers(
    rowId: 10
  ) {
    rowId
    firstName
    surname
    lastName
    firingData {
      hiringDate
      firingDate
    }
    organizationUnit {
      rowId
      title
    }
    organization {
      title
      fullTitle
      opfFull
    }
    position {
      rowId
      name
    }
    timeResources {
      rowId
      name
    }
    workerDocuments {
      rowId
      name
    }
  }
}
```


## [availableForProjectWorkers](worker.py) Получение работников, доступных для добавления в проект
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[Worker]</span>: Список работников.


### Пример использования
```graphql
query {
  availableForProjectWorkers(projectId: 10) {
    rowId
    firstName
    surname
    lastName
    firingData {
      hiringDate
      firingDate
    }
    organizationUnit {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    organization {
      title
      fullTitle
      opfFull
    }
    position {
      rowId
      name
    }
    timeResources {
      rowId
      name
    }
    workerDocuments {
      rowId
      name
    }
  }
}
```


## [getWorkersSampleFile](worker.py) Получение шаблона файла для загрузки рабочих списком с помощью .xlsx файла
### Аргументы
- <span style="color: orange;">for_1520_platform</span> (default_value=False): Флаг получения шаблона для 1520.
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ на временный файл.


### Пример использования
```graphql
query {
  getWorkersSampleFile
}
```


## [getCombiningToWorker](worker.py) Получение отношения совмещения по идентификатору основного работника и проекта
### Аргументы
- <span style="color: orange;">main_worker_id</span> (обязательный): Идентификатор основного работника.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[CombiningWorker]</span>: Список отношений совмещения.


### Пример использования
```graphql
query {
  getCombiningToWorker(mainWorkerId: 10 projectId: 10) {
    rowId
    combiningWorkerId
    mainWorkerId
    projectId
  }
}
```


## [getCombiningToWorkerById](worker.py) Получение отношения совмещения по идентификатору основного работника
### Аргументы
- <span style="color: orange;">main_worker_id</span> (обязательный): Идентификатор основного работника.
### Возвращаемое значение
- <span style="color: orange;">TList[CombiningWorker]</span>: Список отношений совмещения.


### Пример использования
```graphql
query {
  getCombiningToWorkerById(mainWorkerId: 10) {
    rowId
    combiningWorkerId
    mainWorkerId
    projectId
  }
}
```


## [getCombiningToCombiningWorkerById](worker.py) Получение отношения совмещения по идентификатору совмещенного работника и проекта
### Аргументы
- <span style="color: orange;">combining_worker_id</span> (обязательный): Идентификатор основного работника.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">CombiningWorker | None</span>: Отношение совмещения.


### Пример использования
```graphql
query {
  getCombiningToCombiningWorkerById(
    combiningWorkerId: 10
    projectId: 10
  ) {
    rowId
    combiningWorkerId
    mainWorkerId
    projectId
  }
}
```


## [getWorkersByUserIds](worker.py) Получение списка работников по списку идентификаторов пользователей
### Аргументы
- <span style="color: orange;">user_ids</span> (обязательный): Список идентификаторов пользователей.
### Возвращаемое значение
- <span style="color: orange;">TList[Worker]</span>: Список работников.


### Пример использования
```graphql
query {
  getWorkersByUserIds(userIds: [10]) {
    rowId
    firstName
    surname
    lastName
    firingData {
      hiringDate
      firingDate
    }
    organizationUnit {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    organization {
      title
      fullTitle
      opfFull
    }
    position {
      rowId
      name
    }
    timeResources {
      rowId
      name
    }
    workerDocuments {
      rowId
      name
    }
  }
}
```


## [getWorkersByUserIds](worker.py) Получение списка работников по списку идентификаторов пользователей
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[Worker]</span>: Список работников.


### Пример использования
```graphql
query {
  workersForMonthTable(
    rowId: 10
    projectIds: [10]
    organizationIds: [10]
  ) {
    rowId
    firstName
    surname
    lastName
    organization {
      title
      fullTitle
      opfFull
    }
    position {
      rowId
      name
    }
  }
}
```


## [getTemplateForCreateWorkers](worker.py) Получение шаблона для массового создания пользователей
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getTemplateForCreateWorkers
}
```


## [getAllWorkerDocument](worker_document.py) Получение документов работников
### Аргументы
- <span style="color: orange;">filter</span> (default_value=None): Объект фильтра документов.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkerDocument]</span>: Список документов работников.


### Пример использования
```graphql
query {
  getAllWorkerDocument {
    rowId
    name
    description
    workerDocumentType
    startDate
    expiryDate
    workerId
    documentId
    document {
      id
      createdAt
      updatedAt
      name
      size
      guid
      fullPath
      parentFolderId
      creatorUsername
      actualVersionFileId
      getUrl
    }
  }
}
```


## [getExpiredDocumentForWorker](worker_document.py) Получение документов работников
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">day_delta</span> (обязательный): Кол-во дней до окончания срока годности документа.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkerDocument]</span>: Список документов работников.


### Пример использования
```graphql
query {
  getExpiredDocumentForWorker(workerId: 10, dayDelta: 1) {
    rowId
    name
    description
    workerDocumentType
    startDate
    expiryDate
    workerId
    documentId
    document {
      id
      createdAt
      updatedAt
      name
      size
      guid
      fullPath
      parentFolderId
      creatorUsername
      actualVersionFileId
      getUrl
    }
  }
}
```


## [getEducationsByWorkerId](worker_education.py) Получение списка сущностей обучений, назначенных работнику
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkerEducation]</span>: Список сущностей обучений.


### Пример использования
```graphql
query {
  getEducationsByWorkerId(workerId: 10) {
    rowId
    appointDate
    startDate
    expiryDate
    finished
    workerId
    videoInstructionId
    videoInstruction {
      rowId
      name
      description
      duration
      documentId
      imageId
    }
  }
}
```


## [getAllWorkerPassport](worker_education.py) Получение списка сущностей паспортных данных работников
### Аргументы
- <span style="color: orange;">input_filter</span> (обязательный): Фильтр для паспортных данных работников.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkerPassport]</span>: Список паспортных данных сотрудников.


### Пример использования
```graphql
query {
  getAllWorkerPassport(inputFilter: { rowIds: [10], workerIds: [10] }) {
    rowId
    workerId
    passportSerial
    passportNumber
    issueDate
    issuerName
    issuerCode
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями нормы

## [CreateNormAttribute](norm_attribute_create.py) Класс мутации на создание атрибута нормы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании атрибута нормы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название атрибута нормы.
    - <span style="color: orange;">volume</span> (обязательный): Объем.
    - <span style="color: orange;">norm_id</span> (обязательный): Идентификатор нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">norm_attribute</span>: Атрибут нормы.


### Пример использования
```graphql
mutation {
  createNormAttribute(input: { name: "string" volume: 1 normId: 592 }) {
    ok
    normAttribute {
      rowId
      name
      volume
      normId
    }
  }
}
```


## [CreateNorm](norm_create.py) Класс мутации на создание нормы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании нормы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">norm</span>: Норма.


### Пример использования
```graphql
mutation {
  createNorm(input: { name: "string" }) {
    ok
    norm {
      rowId
      name
      currentVersion
    }
  }
}
```


## [AddNormsToOrganization](norm_create.py) Класс мутации на добавление норм в организацию
### Аргументы
- <span style="color: orange;">norm_ids</span> (обязательный): Идентификаторы норм.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  addNormsToOrganization(normIds: [10], organizationId: 10) {
    ok
  }
}
```


## [CreateResourceNorm](resource_norm_create.py) Класс мутации на создание ресурсной нормы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании ресурсной нормы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название ресурсной нормы.
    - <span style="color: orange;">work_norm_id</span> (обязательный): Идентификатор рабочей нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">resource_norm</span>: Ресурсная норма.


### Пример использования
```graphql
mutation {
  createResourceNorm(input: { name: "string" workNormId: 5009 }) {
    ok
    resourceNorm {
      rowId
      name
      isMain
      workNormId
    }
  }
}
```


## [CreateWorkNorm](work_norm_create.py) Класс мутации на создание рабочей нормы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании рабочей нормы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название рабочей нормы.
    - <span style="color: orange;">work_norm_id</span> (обязательный): Идентификатор нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_norm</span>: Рабочая норма.


### Пример использования
```graphql
mutation {
  createWorkNorm(input: { name: "string" normId: 592 }) {
    ok
    workNorm {
      rowId
      name
      normId
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями нормы

## [DeleteNormAttribute](norm_attribute_delete.py) Класс мутации на удаление атрибута нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор атрибута нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteNormAttribute(rowId: 2560) {
    ok
  }
}
```


## [RemoveNormsFromOrganization](norm_delete.py) Класс мутации на удаление норм из организации
### Аргументы
- <span style="color: orange;">norm_ids</span> (обязательный): Идентификаторы норм.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  removeNormsFromOrganization(normIds: [100], organizationId: 10) {
    ok
  }
}
```


## [DeleteNorm](norm_delete.py) Класс мутации на удаление нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteNorm(rowId: 10) {
    ok
  }
}
```


## [DeleteResourceNorm](resource_norm_delete.py) Класс мутации на удаление ресурсной нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор ресурсной нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResourceNorm(rowId: 8888) {
    ok
  }
}
```


## [DeleteWorkNorm](work_norm_delete.py) Класс мутации на удаление рабочей нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор рабочей нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkNorm(rowId: 4920) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями нормы

## [UpdateNormAttribute](norm_attribute_update.py) Класс мутации на обновление атрибута нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор атрибута нормы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении атрибута нормы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">norm_attribute</span>: Атрибут нормы.


### Пример использования
```graphql
mutation {
  updateNormAttribute(input: {name: "string"}, rowId: 2545) {
    ok
    normAttribute {
      rowId
      name
      measureUnit
      volume
      normId
    }
  }
}
```


## [UpdateNorm](norm_update.py) Класс мутации на обновление нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор атрибута нормы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении нормы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">norm</span>: Норма.


### Пример использования
```graphql
mutation {
  updateNorm(input: {name: "string"}, rowId: 572) {
    ok
    norm {
      rowId
      name
    }
  }
}
```


## [UpdateResourceNorm](resource_norm_update.py) Класс мутации на обновление ресурсной нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор атрибута нормы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении ресурсной нормы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название ресурсной нормы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">resource_norm</span>: Ресурсная норма.


### Пример использования
```graphql
mutation {
  updateResourceNorm(input: { name: "string" }, rowId: 8888) {
    ok
    resourceNorm {
      rowId
      name
      classifierCode
      workNormId
    }
  }
}
```


## [UpdateWorkNorm](work_norm_update.py) Класс мутации на обновление рабочей нормы
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор атрибута нормы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении рабочей нормы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_norm</span>: Рабочая норма.


### Пример использования
```graphql
mutation {
  updateWorkNorm(input: {name: "string"}, rowId: 4916) {
    ok
    workNorm {
      rowId
      name
      measureUnit
      totalVolume
      normId
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями нормы

## [GetNorms](norm.py) Получение норм
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов норм.
- <span style="color: orange;">organization_ids</span> (default_value=[]): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[Norm]</span>: Список норм.


### Пример использования
```graphql 
query {
  getNorms(rowIds: [10], organizationIds: [10]) {
    rowId
    name
    normAttributes {
      rowId
      name
    }
    workNorms {
      rowId
      name
    }
  }
}
```


## [GetNormUniqueClassifierCodes](norm.py) Получение списка уникальных кодов классификатора
### Аргументы
- <span style="color: orange;">organization_ids</span> (default_value=[]): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationClassifiers]</span>: Список классификаторов организаций.


### Пример использования
```graphql 
query {
  getNormUniqueClassifierCodes(organizationIds: [90]) {
    organizationId
    classifiers {
      rowId
      name
    }
  }
}
```


## [GetNormByClassifierCodes](norm.py) Получение списка уникальных кодов классификатора
### Аргументы
- <span style="color: orange;">classifier_codes</span> (default_value=[]): Список кодов классификатора.
### Возвращаемое значение
- <span style="color: orange;">TList[Norm]</span>: Список норм.


### Пример использования
```graphql 
query {
  getNormByClassifierCodes(classifierCodes: ["string"]) {
    rowId
    name
    normAttributes {
      rowId
      name
    }
    workNorms {
      rowId
      name
    }
    uniqueResourceNormsAmongNorm {
      resourceNormName
    }
    paceOfWork
  }
}
```


## [GetNormAttributes](norm_attribute.py) Получение атрибутов норм
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов атрибутов норм.
- <span style="color: orange;">norm_ids</span> (default_value=[]): Список идентификаторов норм.
### Возвращаемое значение
- <span style="color: orange;">TList[NormAttribute]</span>: Список атрибутов норм.


### Пример использования
```graphql 
query {
  getNormAttributes(rowIds: [10], normIds: [10]) {
    rowId
    name
  }
}
```


## [GetResourceNorms](resource_norm.py) Получение норм ресурсов
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов ресурсных норм.
- <span style="color: orange;">work_norm_ids</span> (default_value=[]): Список идентификаторов рабочих норм.
### Возвращаемое значение
- <span style="color: orange;">TList[ResourceNorm]</span>: Список ресурсов норм.


### Пример использования
```graphql 
query {
  getResourceNorms(rowIds: [10], workNormIds: [10]) {
    rowId
    name
  }
}
```


## [GetWorkNorms](work_norm.py) Получение рабочих норм
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=[]): Список идентификаторов рабочих норм.
- <span style="color: orange;">norm_ids</span> (default_value=[]): Список идентификаторов норм.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkNorm]</span>: Список рабочих норм.


### Пример использования
```graphql 
query {
  getWorkNorms(rowIds: [10], normIds: [10]) {
    rowId
    name
    resourceNorms {
      rowId
      name
    }
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями организации

## [CreateOrganization](organization_create.py) Класс мутации на создание организации
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании организации типа GraphQL.
    - <span style="color: orange;">title</span> (обязательный): Краткое название.
- <span style="color: orange;">inherit_inn_from_parent</span> (обязательный): Флаг наследования ИНН от родителя.
- <span style="color: orange;">inherit_kpp_from_parent</span> (обязательный): Флаг наследования КПП от родителя.
### Возвращаемое значение
- <span style="color: orange;">new_org</span>: Созданная организация.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  createOrganization(
    inheritInnFromParent: false
    inheritKppFromParent: false
    input: { title: "string" }
  ) {
    newOrg {
      rowId
    }
    ok
  }
}
```


## [CreateOrganizationRelationship](organization_relationship_create.py) Класс мутации на создание связи между организациями
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными о создании связей между организациями типа GraphQL.
    - <span style="color: orange;">sender_organization_id</span> (обязательный): идентификатор организации-отправителя.
    - <span style="color: orange;">receiver_organization_id</span> (обязательный): идентификатор организации-получателя.
### Возвращаемое значение
- <span style="color: orange;">org_relationships</span>: Список объектов связей между организациями.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql 
mutation {
  createOrganizationRelationship(inputs: [{ senderOrganizationId: 10 receiverOrganizationId: 10 }]) {
    orgRelationships {
      senderOrganizationId
      receiverOrganizationId
      status
    }
    okStatus
  }
}
```


## [CreateOrganizationSro](organization_sro_create.py) Класс мутации на создание связей между организациями с организациями СРО
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными о создании связей между организацией с организацией СРО типа GraphQL.
    - <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
    - <span style="color: orange;">parent_sro_id</span> (обязательный): Родительское СРО.
    - <span style="color: orange;">organization_sro_type</span> (обязательный): Статус организации СРО.
### Возвращаемое значение
- <span style="color: orange;">organization_sro</span>: Список объектов связей между организацией с организацией СРО.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql 
mutation {
  createOrganizationSro(inputs: [{ organizationSroType: PLANNING organizationId: 10 parentSroId: 10 }]) {
    organizationSro {
      rowId
      organizationId
      parentSroId
      organizationSroType
    }
    okStatus
  }
}
```


## [CreateOrganizationUnit](organization_unit_create.py) Класс мутации на создание подразделения организации
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании подразделения организации типа GraphQL.
    - <span style="color: orange;">title</span> (обязательный): Краткое название.
    - <span style="color: orange;">code_1c</span> (обязательный): Код 1C.
    - <span style="color: orange;">parent_organization_unit_id</span> (обязательный): Идентификатор родительского подразделения организации.
    - <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">organization_unit</span>: Созданное подразделение организации.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql 
mutation {
  createOrganizationUnit(createInput: { title: "string" }) {
    organizationUnit {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    ok
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями организаций

## [DeleteOrganization](organization_delete.py) Класс мутации на удаление организации
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">org</span>: Организация.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  deleteOrganization( rowId: 1000 ) {
    org {
      rowId
    }
    ok
  }
}
```


## [DeleteOrganizationRelationship](organization_relationship_delete.py) Класс мутации на удаление связи между организациями
### Аргументы
- <span style="color: orange;">sender_organization_id</span> (обязательный): Идентификатор организации отправителя.
- <span style="color: orange;">receiver_organization_id</span> (обязательный): Идентификатор организации получателя.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql 
mutation {
  deleteOrganizationRelationship(
    receiverOrganizationId: 10
    senderOrganizationId: 10
  ) {
    okStatus
  }
}
```


## [DeleteOrganizationSro](organization_sro_delete.py) Класс мутации на удаление связи между организацией с организацией СРО
### Аргументы
- <span style="color: orange;">organization_sro_id</span> (обязательный): Идентификатор связи организации с организацией СРО.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  deleteOrganizationSro( organizationSroId: 10 ) {
    okStatus
  }
}
```


## [DeleteOrganizationUnit](organization_unit_delete.py) Класс мутации на удаление подразделения организации
### Аргументы
- <span style="color: orange;">organization_unit_id</span> (обязательный): Идентификатор подразделения организации.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">organization_unit</span>: Удаленное подразделение организации.

### Пример использования
```graphql 
mutation {
  deleteOrganizationUnit(organizationUnitId: "2156") {
    organizationUnit {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    ok
  }
}
```


## [DeleteOrganizationUnits](organization_unit_delete.py) Класс мутации на массовое удаление подразделений организаций
### Аргументы
- <span style="color: orange;">organization_unit_ids</span> (обязательный): Список идентификаторов подразделений организаций.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">errMsg</span>: Текст ошибки при выполнении операции.

### Пример использования
```graphql 
mutation {
  deleteOrganizationUnits(organizationUnitIds: []) {
    okStatus
    errMsg
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями организации

## [UpdateOrganizationRelationship](organization_relationship_update.py) Класс мутации на обновление связи между организациями
### Аргументы
- <span style="color: orange;">sender_organization_id</span> (обязательный): Идентификатор организации отправителя.
- <span style="color: orange;">receiver_organization_id</span> (обязательный): Идентификатор организации получателя.
- <span style="color: orange;">status</span> (обязательный): Статус связи между организациями.
### Возвращаемое значение
- <span style="color: orange;">org_relationship</span>: Объект связи между организациями.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  updateOrganizationRelationship(
    receiverOrganizationId: 3501
    senderOrganizationId: 1041
    status: ACCEPTED 
  ) {
    orgRelationship {
      status
    }
    okStatus
  }
}
```


## [UpdateOrganizationSro](organization_sro_update.py) Класс мутации на обновление связи между организацией с организацией СРО
### Аргументы
- <span style="color: orange;">organization_sro_id</span> (обязательный): Идентификатор связи организации с организацией СРО.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении связи между организацией с организацией СРО типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">org_relationship</span>: Список объектов связей между организацией с организацией СРО.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  updateOrganizationSro(organizationSroId: 1, updateInput: { parentSroId: 911 }) {
    organizationSro {
      rowId
      organizationId
      parentSroId
      organizationSroType
    }
    okStatus
  }
}
```


## [UpdateOrganization](organization_update.py) Класс мутации на обновление организации
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении организации типа GraphQL.
- <span style="color: orange;">update_input</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">org</span>: Организация.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  updateOrganization(input: { title: "string" }, rowId: 10 ) {
    org {
      title
      fullTitle
      opfFull
      inn
      kpp
      ogrn
      address
      rowId
    }
    ok
  }
}
```


## [UpdateOrganizationUnit](organization_unit_update.py) Класс мутации на обновление подразделения организации
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении подразделения организации типа GraphQL.
- <span style="color: orange;">organization_unit_id</span> (обязательный): Идентификатор подразделения организации.
### Возвращаемое значение
- <span style="color: orange;">organization_unit</span>: Подразделение организации.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  updateOrganizationUnit(
    organizationUnitId: "2145"
    updateInput: { title: "String" }
  ) {
    organizationUnit {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    ok
  }
}
```


## [UpdateOrganizationUnit](organization_unit_update.py) Класс мутации на установку родительского подразделения организации
### Аргументы
- <span style="color: orange;">parent_organization_unit_id</span> (обязательный): Идентификатор родительского подразделения организации.
- <span style="color: orange;">organization_unit_ids</span> (обязательный): Список идентификаторов подразделений организаций.
### Возвращаемое значение
- <span style="color: orange;">organization_units</span>: Подразделения организаций.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  setParentToOrganizationUnit(
    organizationUnitIds: ["2146"]
    parentOrganizationUnitId: "1"
  ) {
    organizationUnits {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    ok
  }
}
```


## [UpdateOrganizationUnit](organization_unit_update.py) Класс мутации на сброс родительского подразделения организации
### Аргументы
- <span style="color: orange;">organization_unit_ids</span> (обязательный): Список идентификаторов подразделений организаций.
### Возвращаемое значение
- <span style="color: orange;">organization_units</span>: Подразделения организаций.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql 
mutation {
  resetParentToOrganizationUnit(
    organizationUnitIds: ["2146"]
  ) {
    organizationUnits {
      rowId
      title
      parentOrganizationUnitId
      organizationId
      code1c
    }
    ok
  }
}
```


# Модуль запросов для взаимодействия с сущностями структур организаций

## [Organizations](organization.py) Получение всех организаций
### Аргументы
- <span style="color: orange;">row_id</span> (default_value=None): Идентификатор организации.
- <span style="color: orange;">row_ids</span> (default_value=None): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[Organization]</span>: Список организаций.


### Пример использования
```graphql 
query {
  organizations(rowIds: [10]) {
    title
    fullTitle
    opfFull
    inn
    kpp
    ogrn
    address
    parentSro {
      rowId
    }
  }
}
```


## [GetActualOrganizationData](organization.py) Получение актуальной информации об организации по ИНН и КПП
### Аргументы
- <span style="color: orange;">inn</span> (обязательный): ИНН организации.
- <span style="color: orange;">kpp</span> (default_value=None): КПП организации.
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationDataType]</span>: Список объектов данных организаций.


### Пример использования
```graphql 
query {
  getActualOrganizationData(inn: "string") {
    title
    fullTitle
    opfFull
    inn
    kpp
    address
  }
}
```


## [GetOrganizationsByInnKpp](organization.py) Получение организации по ИНН и КПП
### Аргументы
- <span style="color: orange;">inn</span> (обязательный): ИНН организации.
- <span style="color: orange;">kpp</span> (default_value=None): КПП организации.
### Возвращаемое значение
- <span style="color: orange;">TList[Organization]</span>: Список объектов данных организаций.


### Пример использования
```graphql 
query {
  getOrganizationsByInnKpp(inn: "string") {
    title
    fullTitle
    opfFull
    inn
    kpp
    address
    parentSro {
      rowId
      organizationId
    }
  }
}
```


## [GetOrgWithChildsParents](organization.py) Получение организации, ее родительских и дочерних элементов
### Аргументы
- <span style="color: orange;">org_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[OrgParentsChilds]</span>: Список объектов данных организаций.


### Пример использования
```graphql 
query {
  getOrgWithChildsParents(orgIds: [2]) {
    reqOrgId
    parentChildsIds
  }
}
```


## [OrganizationRelationships](organization_relationship.py) Получение связей между организациями
### Аргументы
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationRelationship]</span>: Список связей между организациями.


### Пример использования
```graphql 
query {
  organizationRelationships(organizationIds: [110]) {
    senderOrganizationId
    receiverOrganizationId
    status
  }
}
```


## [OrganizationSro](organization_sro.py) Получение связей организации с организациями СРО
### Аргументы
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationRelationship]</span>: Список связей организации с организациями СРО.


### Пример использования
```graphql 
query {
  organizationSro(organizationIds: [2]) {
    rowId
    organizationId
    parentSroId
    organizationSroType
  }
}
```


## [AllOrganizationUnits](organization_units.py) Получение подразделений организаций
### Аргументы (Нет аргументов)

### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationUnit]</span>: Список подразделений организаций.


### Пример использования
```graphql 
query {
  allOrganizationUnits {
    rowId
    title
    parentOrganizationUnitId
    organizationId
    code1c
  }
}
```


## [OrganizationUnitsByOrgId](organization_units.py) Получение подразделений по организации
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">TList[OrganizationUnit]</span>: Список подразделений организации.


### Пример использования
```graphql 
query {
  organizationUnitsByOrgId(organizationId: 2) {
    rowId
    title
    parentOrganizationUnitId
    organizationId
    code1c
  }
}
```


# Модуль мутаций для взаимодействия с Perco

## [ParseWorkersToPerco](perco_common.py) Класс мутации на парсинг данных о работниках в PERCo
### Аргументы
- <span style="color: orange;">worker_ids</span> (обязательный): Список идентификаторов сотрудников.
- <span style="color: orange;">target_project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseWorkersToPerco(targetProjectId: 10, workerIds: [20]) {
    ok
  }
}
```


## [ParseWorkersToPercoByTimeResources](perco_common.py) Класс мутации на парсинг данных о тайм-ресурсах в PERCo
### Аргументы
- <span style="color: orange;">time_resources_ids</span> (обязательный): Список идентификаторов временных ресурсов.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseWorkersToPercoByTimeResources(timeResourcesIds: [10]) {
    ok
  }
}
```


# Модуль запросов для взаимодействия с Perco

## [GetPercoProjectById](perco.py) Проверка наличия у проекта СКУД
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">bool</span>: Результат проверки.


### Пример использования
```graphql 
query {
  getPercoProjectById(projectId: 10)
}
```


## [GetPercoProjectById](perco.py) Получение шаблонов доступа к перке у проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[PercoAccessTemplate]</span>: Список объектов шаблонов доступа Perco типа GraphQL.


### Пример использования
```graphql 
query {
  getPercosWorkerAccesses(projectId: 10) {
    rowId
    name
  }
}
```


# Модуль мутаций создания для взаимодействия с сервисом PowerBI

## [createBiGroup](bi_group.py) Класс мутации на создание группы BI
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании группы BI типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование группы BI.
### Возвращаемое значение
- <span style="color: orange;">bi_group</span>: Объект группы BI типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  createBiGroup(createInput: { name: "string" }) {
    biGroup {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [createProjectBiGroup](project_bi_group.py) Класс мутации на создание объекта связи проекта и группы BI
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании объекта связи проекта и группы BI типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">bi_group_id</span> (обязательный): Идентификатор группы BI.
### Возвращаемое значение
- <span style="color: orange;">project_bi_group</span>: Объект связи проекта и группы BI типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  createProjectBiGroup(createInput: {projectId: 10 biGroupId: 10}) {
    projectBiGroup {
      projectId
      biGroupId
    }
    okStatus
    errMsg
  }
}
```


# Модуль мутаций удаления для взаимодействия с сервисом PowerBI

## [deleteBIGroups](bi_group.py) Класс мутации на удаление групп BI
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов групп BI.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  deleteBiGroups(rowIds: [10]) {
    okStatus
    errMsg
  }
}
```


## [deleteProjectBiGroupsByProjectIds](project_bi_group.py) Класс мутации на удаление объектов связей проектов и групп BI
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  deleteProjectBiGroupsByProjectIds(projectIds: [10]) {
    okStatus
    errMsg
  }
}
```


# Модуль мутаций обновления для взаимодействия с сервисом PowerBI
[updateBiGroup](bi_group.py)
##  Класс мутации на обновление группы BI
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор группы BI.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении группы BI типа GraphQL.
- <span style="color: orange;">with_return</span> (default_value=False): Флаг возврата результата мутации.
### Возвращаемое значение
- <span style="color: orange;">bi_group</span>: Объект группы BI типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  updateBiGroup(rowId: 10, updateInput: {name: "string"}) {
    biGroup {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```

[setProjectBiGroupSerialNumbers](project_bi_group.py)
##  Класс мутации на обновление объектов связей проектов и групп BI
### Аргументы
- <span style="color: orange;">update_inputs</span> (обязательный): Объект обмена данными об обновлении группы BI типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_bi_groups</span>: Объект связи проекта и группы BI типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.


### Пример использования
```graphql
mutation {
  setProjectBiGroupSerialNumbers(updateInputs: [{projectId: 10 biGroupId:10}]) {
    projectBiGroups {
      projectId
      biGroupId
      serialNumber
    }
    okStatus
    errMsg
  }
}
```


# Модуль запросов для взаимодействия с сервисом PowerBI 

## [getBiGroups](bi_group.py) Получение групп BI
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов групп BI.
### Возвращаемое значение
- <span style="color: orange;">TList[BIGroup]</span>: Список объектов групп BI типа GraphQL.


### Пример использования
```graphql 
query {
  getBiGroups(rowIds: []) {
    rowId
    parentId
    name
    serialNumber
  }
}
```


## [getBiGroupsByProjectId](bi_group.py) Получение групп BI по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">with_all_parents</span> (default_value=False): Флаг получения сущностей со всеми родителями.
### Возвращаемое значение
- <span style="color: orange;">TList[BIGroup]</span>: Список объектов групп BI типа GraphQL.


### Пример использования
```graphql 
query {
  getBiGroupsByProjectId(projectId: 10) {
    rowId
    name
  }
}
```


## [getProjectsByBiGroupIds](bi_group.py) Получение групп BI по идентификатору проекта
### Аргументы
- <span style="color: orange;">bi_group_ids</span> (обязательный): Идентификатор группы BI.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectBiGroup]</span>: Список объектов связей проектов и групп BI типа GraphQL.


### Пример использования
```graphql 
query {
  getProjectsByBiGroupIds(biGroupIds: [10]) {
    projectId
    biGroupId
    project {
      rowId
      name
    }
    biGroup {
      rowId
      name
    }
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями типа график

## [CreateProjectTransaction](project_transaction_create.py) Класс мутации на создание версии графика
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании версии графика типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">project_transaction</span>: Объект версии графика.


### Пример использования
```graphql 
mutation {
  createProjectTransaction(
    input: { name: "string", transactionType: PLAN, fromParser: true projectId: 1000 userId: 10000 ganttChartId: 10 }
  ) {
    ok
    projectTransaction {
      rowId
    }
  }
}
```


## [CopyProjectTransaction](project_transaction_create.py) Класс мутации на копирование транзакции
### Аргументы
- <span style="color: orange;">source_transaction_id</span> (обязательный): Идентификатор транзакции, которую необходимо скопировать.
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании транзакции (версии) графика типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">project_transaction</span>: Объект версии графика.
- <span style="color: orange;">err_msg</span>: Текст ошибки при выполнении операции.

### Пример использования
```graphql 
mutation {
  copyProjectTransaction(
    projectId: 1000
    sourceTransactionId: 1000
  ){
    ok
    errMsg
    projectTransaction{
      rowId
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями типа график

## Класс мутации на удаление версии графика
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Список идентификаторов транзакций.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectTransactions(projectTransactionId: [ 190308 ]) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями типа график

## Класс мутации на обновление версии графика
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении транзакции (версии) графика типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">project_transaction</span>: Транзакция (версия) графика.


### Пример использования
```graphql
mutation {
  updateProjectTransaction(input: { name: "string" }, projectTransactionId: 190308) {
    ok
    projectTransaction {
      rowId
      name
      date
      transactionType
      projectId
      ganttChartId
      userId
      fromParser
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями типа график

## Получение всех транзакций по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectTransaction]</span>: Список транзакций.


### Пример использования
```graphql 
query {
  getProjectTransactionsByProjectId(projectId: 30) {
    rowId
    name
    date
    transactionType
    projectId
    ganttChartId
    fileVersionGuid
    userId
    fromParser
  }
}
```


## Получение всех транзакций проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">include_actual</span> (обязательный): Флаг на включение актуального плана.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectTransaction]</span>: Список транзакций.


### Пример использования
```graphql 
query {
  projectPlanTransactions(projectId: 30, includeActual: true) {
    rowId
    name
    date
    transactionType
    projectId
    ganttChartId
    fileVersionGuid
    userId
    fromParser
  }
}
```


## Получение фактической транзакции проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ProjectTransaction</span>: Транзакция.


### Пример использования
```graphql 
query {
  projectFactTransaction(projectId: 30) {
    rowId
    name
    date
    transactionType
    projectId
    ganttChartId
    fromParser
  }
}
```


## Получение актуальной транзакции проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ProjectTransaction</span>: Транзакция.


### Пример использования
```graphql 
query {
  projectActualTransaction(projectId: 30) {
    rowId
    name
    date
    transactionType
    projectId
    ganttChartId
    fileVersionGuid
    userId
    fromParser
  }
}
```


## Получение всех транзакций по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectTransaction]</span>: Список транзакций.


### Пример использования
```graphql 
query {
  getProjectTransactionsByProjectId(projectId: 30) {
    rowId
    name
    date
    transactionType
    projectId
    ganttChartId
    fileVersionGuid
    userId
    fromParser
  }
}
```


## Получить максимальный уровень вложенности фаз по идентификатору транзакции
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">int</span>: Уровень вложенности.


### Пример использования
```graphql 
query {
  getMaxPhaseLevelByProjectTransactionId(projectTransactionId: 10)
}
```
# Модуль запросов на получение ролей пользователей

## [usersByRoleIds](role_users.py) Получение ролей пользователей по списку идентификаторов ролей
### Аргументы
- <span style="color: orange;">role_ids</span> (обязательный): Список идентификаторов ролей.
### Возвращаемое значение
- <span style="color: orange;">TList[RoleUsers]</span>: Список ролей.


### Пример использования
```graphql
query {
  usersByRoleIds(roleIds: [10]) {
    role {
      rowId
      name
      description
    }
    users {
      rowId
      username
      email
      userType
      phone
      education
      courses
      position
      passportNumber
      placeOfRegistration
      licensingCertificates
      isSuperuser
      isActive
      organizationId
      photoId
      tableNumber
      compareWithWorker
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с распознаванием лиц

## [RejectFaceRequests](recognition.py) Класс мутации на отклонение заявок на регистрацию лиц работников
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании запроса на создание заявки на регистрацию лица работника типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">face_requests</span>: Список заявок на регистрацию лиц.


### Пример использования
```graphql
mutation {
  rejectFaceRequests(input: { requestsIds: [1] }) {
    ok
    faceRequests {
      rowId
      workerId
      guid
      dateCreated
    }
  }
}
```


## [ApproveFaceRequests](recognition.py) Класс мутации на подтверждение заявок на регистрацию лиц работников
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об подтверждении заявок на регистрацию лиц работников типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">face_requests</span>: Список заявок на регистрацию лиц.
- <span style="color: orange;">failed_requests_ids</span>: Список идентификаторов заявок, которые не удалось принять.


### Пример использования
```graphql
mutation {
  approveFaceRequests(input: { requestsIds: [1] }) {
    ok
    faceRequests {
      rowId
      workerId
      guid
      dateCreated
    }
    failedRequestsIds
  }
}
```


# Модуль мутаций создания для взаимодействия с распознаванием лиц

## [AddFaces](recognition_create.py) Класс мутации на добавление запросов на создание заявок на регистрацию лиц работников
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании запроса на создание заявки на регистрацию лица работника типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">face_requests</span>: Список заявок на регистрацию лиц.


### Пример использования
```graphql
mutation {
  addFaces(input: { images: ["image.jpg"], extensions: ["string"] workerId: 1 }) {
    ok
    faceRequests {
      rowId
      workerId
      guid
      dateCreated
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с распознаванием лиц

## [DeleteRegistrationVector](recognition_delete.py) Класс мутации на удаление вектора регистрации лица
### Аргументы
- <span style="color: orange;">vector_id</span> (обязательный): Идентификатор вектора.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteRegistrationVector(vectorId: 1) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с распознаванием лиц

## [ManualUpdateRegistrationVector](recognition_update.py) Класс мутации на ручное обновление вектора регистрации лица
### Аргументы
- <span style="color: orange;">vector_id</span> (обязательный): Объект обмена данными об обновлении вектора распознавания сотрудника типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  manualUpdateRegistrationVector(input: {workerId: 1 image: "image.jpg"}) {
    vectorId
    ok
  }
}
```


# Модуль запросов для взаимодействия с распознаванием лиц

## [RecognizeWorker](recognition.py) Распознавание рабочего
### Аргументы
- <span style="color: orange;">recognize_input</span> (обязательный): Объект обмена данными о распознавании рабочего типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">RecognizeWorkerQuery</span>: Результат запроса.


### Пример использования
```graphql 
query {
  recognizeWorker(recognizeInput: {imageStream:"image.jpg" kioskId:1}) {
    worker {
      rowId
      firstName
    }
    timeResourceId
    error
  }
}
```


## [GetFaceRequests](recognition.py) Получение списка заявок на регистрацию лиц
### Аргументы
- <span style="color: orange;">face_request_input</span> (обязательный): Объект обмена данными о получении списка заявок на регистрацию лиц типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[FaceRequest]</span>: Список заявок на регистрацию.


### Пример использования
```graphql 
query {
  getFaceRequests(faceRequestInput: {projectId:1}) {
    rowId
    workerId
    guid
    dateCreated
  }
}
```


## [GetVectorIdByWorkerId](recognition.py) Получение идентификатора вектора по идентификатору рабочего
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Объект обмена данными о получении списка заявок на регистрацию лиц типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">Int</span>: Идентификатор вектора.


### Пример использования
```graphql 
query {
  getVectorIdByWorkerId(workerId: 1)
}
```


## [GetFaceRequestsByWorkerId](recognition.py) Получение списка заявок на регистрацию лиц рабочего
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Объект обмена данными о получении списка заявок на регистрацию лиц типа GraphQL.
- <span style="color: orange;">worker_id</span> (обязательный): Объект обмена данными о получении списка заявок на регистрацию лиц типа GraphQL.
- <span style="color: orange;">worker_id</span> (default_value=None): Объект обмена данными о получении списка заявок на регистрацию лиц типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[FaceRequest]</span>: Список заявок на регистрацию.


### Пример использования
```graphql 
query {
  getFaceRequestsByWorkerId(
    workerId: 1
    projectId: 1
  ) {
    rowId
    workerId
    guid
    dateCreated
  }
}
```


# Модуль запросов на получение отчетов

## [getAppendixFourteenReport](appendix_fourteen_report.py) Получение отчетов приложений 14.1-14.9
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">report_date</span> (обязательный): Дата формирования отчета.
### Возвращаемое значение
- <span style="color: orange;">AppendixFourteenReportElement</span>: Объект обмена данными о выгрузки отчетов приложений 14.1-14.9 типа GraphQL.


### Пример использования
```graphql
query {
  getAppendixFourteenReport(projectId: 10, reportDate: "2024-01-01") {
    keyFile
    errMsg
  }
}
```


## [getBdrReport](bdr_report.py) Получение отчета БДР
### Аргументы
- <span style="color: orange;">project_transaction_ids</span> (обязательный): Список идентификаторов транзакций.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">BdrReportElement</span>: Объект обмена данными о выгрузки БДР отчета типа GraphQL.


### Пример использования
```graphql
query {
  getBdrReport(
    projectTransactionIds: [10]
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    keyFile
    errMsg
  }
}
```


## [getBelateReport](be_late_report.py) Получение отчетов по опоздавшим
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">time_resource_ids</span> (default_value=None): Идентификаторы временных ресурсов.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
- <span style="color: orange;">start_time</span> (default_value=None): Промежуток времени для начала смены.
- <span style="color: orange;">end_time</span> (default_value=None): Промежуток времени для конца смены.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getBelateReport(
    projectId: 10
    organizationIds: [20]
    timeResourceIds: [10]
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getChangesHistoryReport](changes_history_report.py) Получение отчета по внесению изменений в табель
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">datetime_range</span> (default_value=None): Временной промежуток.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getChangesHistoryReport(
    projectIds: [10]
    organizationIds: [10]
  )
}
```


## [getHoursChangesHistoryReport](changes_history_report.py) Получение отчета по корректировкам часов в табеле
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">datetime_range</span> (default_value=None): Временной промежуток.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getHoursChangesHistoryReport(
    projectIds: [10]
    organizationIds: [10]
  )
}
```


## [getConstructionStrategyReport](construction_strategy_report.py) Получение стратегии строительства
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">ConstructionStrategyReportElement</span>: Объект обмена данными о выгрузки стратегии строительства типа GraphQL.


### Пример использования
```graphql
query {
  getConstructionStrategyReport(projectIds: [10]) {
    keyFile
    errMsg
  }
}
```


## [getConstructionStrategyReport](dataset_project_element.py) Получение датасета по элементам графика
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getDatasetProjectElement
}
```


## [getDebtCalculationReport](debt_calculation_report.py) Получение отчетов по задолженностям с учетом КC-3
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">date_range</span> (default_value=None): Временной промежуток.
### Возвращаемое значение
- <span style="color: orange;">DebtCalculationReportElement</span>: Объект обмена данными для получения отчета по задолженностям с учетом КC-3 типа GraphQL.


### Пример использования
```graphql
query {
  getDebtCalculationReport(projectIds: [10]) {
    keyFile
    errMsg
  }
}
```


## [getDriverReportTable](driver_reports.py) Получение отчета по статусам водителей
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getDriverReportTable(
    organizationId: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getDriverReport](driver_reports.py) Получение отчета по статусам водителей
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[DriverReports]</span>: Список водителей либо пустой список.


### Пример использования
```graphql
query {
  getDriverReport(
    organizationId: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    organizationId
    driverMark {
      organizationUnits
    }
  }
}
```


## [getDriverHours](driver_reports.py) Получение всех итоговых часов водителей
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[DriverReports]</span>: Список водителей либо пустой список.


### Пример использования
```graphql
query {
  getDriverHours(
    organizationId: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    totalHours
    hoursRanges {
      totalHours
      timeResourceId
      workerId
      isActive
    }
  }
}
```


## [getFaceRequestsReport](face_request_report.py) Получение отчета по заявкам на регистрацию
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">datetime_range</span> (default_value=None): Временной промежуток.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getFaceRequestsReport(
    projectIds: [10]
    organizationIds: [10]
  )
}
```


## [fotReport](fot_report.py) Получение отчета ФОТ
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">plan_project_transaction_id</span> (обязательный): Идентификатор транзакции для получения плановых данных.
- <span style="color: orange;">fact_project_transaction_id</span> (default_value=None): Идентификатор транзакции.
- <span style="color: orange;">use_shiftworks_fact_data</span> (default_value=None): Использовать сменные задания для получения фактических данных.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  fotReport(
    projectId: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    organizationId: 20
    planProjectTransactionId: 10
  )
}
```


## [chordTaskPlan](fot_report.py) Получение отчета Аккордное план-задание
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">plan_project_transaction_id</span> (обязательный): Идентификатор транзакции для получения плановых данных.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  chordTaskPlan(
    projectId: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    organizationId: 20
    planProjectTransactionId: 10
  )
}
```


## [getFuelConsumption](fuel_consumption_report.py) Получение списка отклонения расхода топлива
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[FuelConsumptionReport]</span>: Список отклонения расхода топлива либо пустой список.


### Пример использования
```graphql
query {
  getFuelConsumption(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    rowId
    date
    machine {
      rowId
      vin
      regNumber
      basePlace
      model
      organizationId
      machineTypeId
    }
    fuelState
    fuelStateBegin
    fuelStateEnd
    fuelStateTotal
    projectZone {
      id
      name
    }
    organization {
      title
      fullTitle
    }
    acceptedAction
  }
}
```


## [getFuelConsumptionReport](fuel_consumption_report.py) Получение отчетов по расходу топлива
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getFuelConsumptionReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getKc2ReportTable](ks_reports.py) Получение КС-2 отчета
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getKc2ReportTable(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    projectId: 10
    contractStatementId: 10
  )
}
```


## [getKc3ReportTable](ks_reports.py) Получение КС-3 отчета
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getKc3ReportTable(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    projectId: 10
    contractStatementId: 10
  )
}
```


## [getMachineEventReport](machine_event_report.py) Получение ключа временного файла excel отчета
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_zone_ids</span> (default_value=None): Список идентификаторов рабочих зон.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов организаций.
- <span style="color: orange;">shift</span> (default_value=None): Тип смены.
### Возвращаемое значение
- <span style="color: orange;">str | None</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getMachineEventReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getDailyMachineEventReport](machine_event_report.py) Получение отчета о ежедневных поставках сыпучих грузов на проектной зоне
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_zone_id</span> (обязательный): Идентификатор проектной зоны.
- <span style="color: orange;">loosening_coefficient</span> (обязательный): Коэффициент разрыхления.
### Возвращаемое значение
- <span style="color: orange;">str | None</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getDailyMachineEventReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    projectZoneId: 10
    looseningCoefficient: 0.8
  )
}
```


## [getMachineShiftWorkTable](machine_shift_work.py) Получение ключа временного файла excel отчета машины и механизмы со сменными работами
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">str | None</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getMachineShiftWorkTable(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getOverworkReport](overwork_report.py) Получение отчета по переработкам
### Аргументы
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getOverworkReport(
    organizationIds: [10]
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getPowerbiBamReport](powerbi_bam_report.py) Получение PowerBI отчета
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getPowerbiBamReport(projectIds: [10])
}
```


## [downloadPowerbiBamReport](powerbi_bam_report.py) Получение PowerBI отчета
### Аргументы
- <span style="color: orange;">year</span> (обязательный): Год отчета.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  downloadPowerbiBamReport(year: 2024)
}
```


## [getPowerbiBamV2Report](powerbi_bam_report.py) Получение PowerBI отчета
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов организаций.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getPowerbiBamV2Report(
    projectIds: [10]
  )
}
```


## [downloadPowerbiReport](powerbi_report.py) Получение отчета по ключевым физ показателям
### Аргументы
- <span style="color: orange;">report_year</span> (обязательный): Год, за который нужно получить отчет по ключевым физ показателям.
- <span style="color: orange;">is_short</span> (default_value=None): Флаг генерации отчета в короткой форме.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  downloadPowerbiReport(reportYear: 2024)
}
```


## [getPowerbiReport](powerbi_report.py) Получение PowerBI отчета
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">date_range</span> (default_value=None): Временной промежуток.
- <span style="color: orange;">is_short</span> (default_value=None): Флаг генерации отчета в короткой форме.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getPowerbiReport(projectIds: [10])
}
```


## [getWeeklyFinance](powerbi_report.py) Получение суммы КС-2 для еженедельного финансового отчета
### Аргументы
- <span style="color: orange;">contract_with_objects</span> (обязательный): Фильтр по контракту и этапам.
- <span style="color: orange;">end_week_day</span> (обязательный): День недели для получения сумм КС-2.
### Возвращаемое значение
- <span style="color: orange;">HCWeeklyFinance</span>: Объект обмена данными.


### Пример использования
```graphql
query {
  getWeeklyFinance(
    contractWithObjects: { contractId: 10, projectObjectIds: [10] }
    endWeekDay: "2024-01-01"
  ) {
    constructionBeginningKs2
    ks2PerWeek
  }
}
```


## [getMs11FinanceReport](powerbi_report.py) Получение сводного финансового отчета МС-11
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getMs11FinanceReport(projectIds: [10])
}
```


## [downloadMs11FinanceReport](powerbi_report.py) Получение сводного финансового отчета МС-11
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  downloadMs11FinanceReport
}
```


## [getWeeklyFinanceAnalog](powerbi_report.py) Получение суммы КС-2 для еженедельного финансового отчета (аналог)
### Аргументы
- <span style="color: orange;">end_week_day</span> (обязательный): День недели для получения сумм КС-2.
- <span style="color: orange;">project_with_objects</span> (обязательный): Фильтр по проекту и этапам.
### Возвращаемое значение
- <span style="color: orange;">WeeklyFinanceAnalog</span>: Объект обмена данными для еженедельного финансового отчета (аналог).


### Пример использования
```graphql
query {
  getWeeklyFinanceAnalog(
    projectWithObjects: { projectId: 10, projectObjectIds: [10] }
    endWeekDay: "2024-01-01"
  ) {
    projectId
    constructionBeginningKs2
    ks2PerWeek
  }
}
```


## [getWeeklyFinanceByDays](powerbi_report.py) Получение данных КС2 по дням
### Аргументы
- <span style="color: orange;">project_with_objects</span> (обязательный): Фильтр по проекту и этапам.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getWeeklyFinanceByDays(
    projectWithObjects: { projectId: 10, projectObjectIds: [10] }
  ) {
    ks2SumByDay
    ks2Day
  }
}
```


## [getProdProgramReport](prod_program_report.py) Получение данных КС2 по дням
### Аргументы
- <span style="color: orange;">project_ids</span> (default_value=None): Фильтр по проекту и этапам.
- <span style="color: orange;">report_year</span> (default_value=None): Фильтр по проекту и этапам.
- <span style="color: orange;">organization_ids</span> (default_value=None): Фильтр по проекту и этапам.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getProdProgramReport
}
```


## [getProductionProgramme](production_programe.py) Получение производственной программы
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Фильтр по проекту и этапам.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
- <span style="color: orange;">phase_ids</span> (default_value=None): Список идентификаторов фаз.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getProductionProgramme(
    projectIds: [10]
  ) {
    keyFile
    errMsg
  }
}
```


## [getFiltersForPlanFactReportv](report_query_filter.py) Получение производственного графика
### Аргументы
- <span style="color: orange;">include_suspended_projects</span> (default_value=None): Флаг получения приостановленных проектов.
- <span style="color: orange;">include_completed_projects</span> (default_value=None): Флаг получения завершенных проектов.
### Возвращаемое значение
- <span style="color: orange;">PlanFactReportFilters</span>: Фильтры для отчета план-факт.


### Пример использования
```graphql
query {
  getFiltersForPlanFactReport {
    projects {
      rowId
      name
      shortName
    }
    organizations {
      title
      fullTitle
      opfFull
    }
  }
}
```


## [getPowerBiData](resource_report.py) Получение данных для запроса в даш-борд power bi
### Аргументы
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[PowerBIElement]</span>: Список элементов для powerBI.


### Пример использования
```graphql
query {
  getPowerBiData {
    organizationName
    projectName
    dataType
    productionCode
    volume
    day
    vssVolume
    vsubVolume
    indexVolume
    graphVersion
  }
}
```


## [getPlanFactReport](resource_report.py) Получение отчета план-факт
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getPlanFactReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getSummaryPlanFactReport](resource_report.py) Получение отчета по численности работающих План-Факт
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">with_total</span> (default_value=None): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">PlanFactElementsMappings</span>: Маппинг элементов план-факт по численности.


### Пример использования
```graphql
query {
  getSummaryPlanFactReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    elementId
    parentElementId
  }
}
```


## [shiftWorkJobReport](shift_work_report.py) Получение отчета наряд-задания
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">project_transaction_ids</span> (обязательный): Список идентификаторов транзакции.
- <span style="color: orange;">unaccounted_works</span> (default_value=None): Фильтр по неучтенным работам в графике производства работ.
- <span style="color: orange;">short_format</span> (default_value=None): Флаг, указывающий на необходимость выдачи сокращенной версии.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  shiftWorkJobReport(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    projectTransactionIds: [10]
  )
}
```


## [shiftWorkJobReport](shift_work_report.py) Получение выгрузки сменных заданий
### Аргументы
- <span style="color: orange;">date_range</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">alt_format</span> (default_value=None): Выгрузка сокращённого отчёта (для одного проекта).
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  uploadingShiftWorkReport
}
```


## [spiderFactExportByProject](spider_fact_report.py) Получение данных для выгрузки факта в спайдер
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">works_with_fact_only</span> (default_value=None): Выгружать работы только с введенным фактом.
- <span style="color: orange;">work_ids_not_inclusive</span> (default_value=None): Идентификаторы работ, которые необходимо исключить из выгрузки.
- <span style="color: orange;">phase_ids_not_inclusive</span> (default_value=None): Идентификаторы фаз, внутри которых работы необходимо исключить из выгрузки.
### Возвращаемое значение
- <span style="color: orange;">SpiderFactExportReport</span>: Объект выгрузки факта в спайдер.


### Пример использования
```graphql
query {
  spiderFactExportByProject(
    projectId: 10
  ) {
    ref
  }
}
```


## [tableSummary](table_summary.py) Получение сводной таблицы по численности
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">generalized_statuses</span> (default_value=None): Выгружать работы только с введенным фактом.
- <span style="color: orange;">project_ids</span> (default_value=None): Идентификаторы работ, которые необходимо исключить из выгрузки.
- <span style="color: orange;">position_group_ids</span> (default_value=None): Идентификаторы фаз, внутри которых работы необходимо исключить из выгрузки.
- <span style="color: orange;">position_group_types</span> (default_value=None): Идентификаторы фаз, внутри которых работы необходимо исключить из выгрузки.
### Возвращаемое значение
- <span style="color: orange;">TList[SummaryElement]</span>: Список элементов.


### Пример использования
```graphql
query {
  tableSummary(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    elementId
    parentElementId
    days {
      day
      workersCount
    }
    opened
  }
}
```


## [getWorkersSummaryHours](table_summary.py) Получение сводной таблицы по часам
### Аргументы
- <span style="color: orange;">key</span> (обязательный): Ключ.
- <span style="color: orange;">date_range</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">generalized_statuses</span> (default_value=None): Выгружать работы только с введенным фактом.
- <span style="color: orange;">project_ids</span> (default_value=None): Идентификаторы работ, которые необходимо исключить из выгрузки.
- <span style="color: orange;">position_group_ids</span> (default_value=None): Идентификаторы фаз, внутри которых работы необходимо исключить из выгрузки.
- <span style="color: orange;">position_group_types</span> (default_value=None): Идентификаторы фаз, внутри которых работы необходимо исключить из выгрузки.
### Возвращаемое значение
- <span style="color: orange;">TList[SummaryElement]</span>: Список элементов.


### Пример использования
```graphql
query {
  getWorkersSummaryHours(
    key: 10
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  ) {
    elementId
    parentElementId
    days {
      day
      workersCount
    }
    opened
  }
}
```


## [flatSummaryTable](table_summary.py) Получение сводной таблицы по численности
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов организаций.
- <span style="color: orange;">generalized_statuses</span> (default_value=None): Список обобщенных статусов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">position_group_ids</span> (default_value=None): Список идентификаторов групп должностей.
- <span style="color: orange;">position_group_types</span> (default_value=None): Список типов должностей для фильтрации.
- <span style="color: orange;">accounting_of_number_mo15</span> (default_value=None): Отчет по численности за ден.
- <span style="color: orange;">accounting_of_number_mo36</span> (default_value=None): Учет по МО-36.
- <span style="color: orange;">vacationers_of_number</span> (default_value=None): Отчет по отдыхающим.
- <span style="color: orange;">operational_accounting</span> (default_value=None): Отчет по кадровому составу.
- <span style="color: orange;">accounting_of_number_for_1520</span> (default_value=None): Отчет по численности за день для 1520.
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ на временный файл.


### Пример использования
```graphql
query {
  flatSummaryTable(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [flatSummaryTableForPrepaid](table_summary.py) Получение сводной таблицы по численности
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">organization_ids</span> (default_value=None): Список идентификаторов организаций.
- <span style="color: orange;">generalized_statuses</span> (default_value=None): Список обобщенных статусов.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">position_group_ids</span> (default_value=None): Список идентификаторов групп должностей.
- <span style="color: orange;">position_group_types</span> (default_value=None): Список типов должностей для фильтрации.
### Возвращаемое значение
- <span style="color: orange;">Key</span>: Ключ на временный файл.


### Пример использования
```graphql
query {
  flatSummaryTableForPrepaid(
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
  )
}
```


## [getSummaryTableOrganizations](table_summary.py) Получение списка организаций для фильтра в сводном табеле
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Organization]</span>: Список организаций.


### Пример использования
```graphql
query {
  getSummaryTableOrganizations {
    title
    fullTitle
    opfFull
    inn
    kpp
    ogrn
    address
    contacts
    postcode
    smb
    isBranchMain
    tisId
    isOuterOrganization
    omnicommId
    scoutGpsId
    parentOrganizationId
    serialNumber
    dutyNumber
    databaseAddress1c
    personnelSynchronization1c
    showInSummaryTable
    rowId
    parentSro {
      rowId
      organizationId
      parentSroId
      organizationSroType
      dateRegistration
      associationMembership
    }
  }
}
```


## [tisApplication](tis_application_export.py) Получение ведомости заявок на технику
### Аргументы
- <span style="color: orange;">from_date</span> (обязательный): Дата начала отчета.
- <span style="color: orange;">to_date</span> (default_value=None): Дата завершения отчета.
### Возвращаемое значение
- <span style="color: orange;">TisApplicationExportReport</span>: Объект ссылки на получение временного файла.


### Пример использования
```graphql
query {
  tisApplication(fromDate: "2024-01-01", toDate: "2024-01-01") {
    ref
  }
}
```


## [uploadContractStatement](uploading_contract_statement.py) Получение выгрузки сметы контракта
### Аргументы
- <span style="color: orange;">contract_statement_id</span> (обязательный): Идентификатор ведомости контракта.
- <span style="color: orange;">responsible_ids</span> (default_value=None): Список идентификаторов организаций исполнителей работ.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  uploadContractStatement(
    contractStatementId: 10
  )
}
```


## [getVmpWmReport](vmp_reports.py) Получение отчета по приходу и уходу сотрудников
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
- <span style="color: orange;">tr_ids</span> (default_value=None): Список идентификаторов тайм-ресурсов.
### Возвращаемое значение
- <span style="color: orange;">str</span>: Ключ временного файла.


### Пример использования
```graphql
query {
  getVmpWmReport(
    projectId: 10
    organizationIds: [10]
  )
}
```


# Модуль общих мутаций для взаимодействия с сущностями ресурсов

## [ProjectElementStagesTransfer](project_element_common.py) Класс мутации на перенос назначенных этапов на элементы графика
### Аргументы
- <span style="color: orange;">project_transaction_id_to</span> (обязательный): Идентификатор версии графика куда переносить.
- <span style="color: orange;">project_transaction_id_from</span> (обязательный): Идентификатор версии графика откуда переносить.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  projectElementStagesTransfer(
    projectTransactionIdFrom: 10
    projectTransactionIdTo: 20
  ) {
    ok
  }
}
```

[CopyProjectPhase](project_phase_common.py)
##  Класс мутации на копирование фазы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о копировании фазы типа GraphQL.
    - <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">source_project_transaction_id</span> (обязательный): Идентификатор транзакции.
    - <span style="color: orange;">target_project_transaction_id</span> (обязательный): Объект обмена данными о копировании фазы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">created_phases</span>: Список созданных объектов фаз типа GraphQL.
- <span style="color: orange;">created_works</span>: Список созданных объектов работы типа GraphQL.
- <span style="color: orange;">created_resources</span>: Список созданных объектов ресурсов типа GraphQL.
- <span style="color: orange;">created_resource_assigns</span>: Список созданных объектов связи с ресурсами типа GraphQL.
- <span style="color: orange;">created_costs</span>: Список созданных объектов стоимостных составляющий типа GraphQL.
- <span style="color: orange;">created_work_links</span>: Список созданных объектов связи операций типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyProjectPhase(input: {phaseId: 10 projectId: 30 sourceProjectTransactionId: 30 targetProjectTransactionId: 10}) {
    createdPhases {
      rowId
      name
    }
    createdWorks {
      rowId
      name
    }
    createdResources {
      rowId
      name
    }
    createdResourceAssigns {
      rowId
    }
    createdCosts {
      rowId
    }
    createdWorkLinks {
      rowId
    }
    updatedPhaseVolumes {
      rowId
    }
    ok
  }
}
```


## [UploadAndParseProjectTransaction](project_transaction_parser_common.py) Класс мутации на парсинг версии графика из файла excel
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">project_phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">file</span> (обязательный): Файл графика в формате excel документа.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  uploadAndParseProjectTransaction(
    file: "file.xslx"
    projectId: 10
    projectPhaseId: 20
    projectTransactionId: 10
  ) {
    errMsg
    ok
    worksWithoutOrgs
  }
}
```


## [BulkCopyResourceAssigns](resource_assign_common.py) Класс мутации на массовое копирование связей ресурсов с работой
### Аргументы
- <span style="color: orange;">bulk_copy_input</span> (обязательный): Объект обмена данными о массовом копировании работ типа GraphQL.
    - <span style="color: orange;">resources_assign_ids</span> (обязательный): Список идентификаторов связей ресурса с работой.
    - <span style="color: orange;">target_work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">transaction_id_from</span> (обязательный): Идентификатор версии графика откуда переносить.
    - <span style="color: orange;">transaction_id_target</span> (обязательный): Идентификатор версии графика куда переносить.
### Возвращаемое значение
- <span style="color: orange;">new_resource_assigns</span>: Список созданных объектов связи с ресурсами типа GraphQL.
- <span style="color: orange;">new_resources</span>: Список созданных объектов ресурсов типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  bulkCopyResourceAssigns(bulkCopyInput: { resourcesAssignIds: [10] targetWorkId: 30 transactionIdFrom: 30 transactionIdTarget: 10 }) {
    newResourceAssigns {
      rowId
    }
    newResources {
      rowId
      name
    }
    okStatus
    errMsg
  }
```


## [InputFact](resource_assign_fact_common.py) Класс мутации на массовое копирование связей ресурсов с работой
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о вводе факта на назначение ресурса типа GraphQL.
    - <span style="color: orange;">resource_assign_id</span> (обязательный): Идентификатор связи ресурса с работой.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">resource_assign_fact</span>: Объект связи ресурса с фактом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  inputFact(input: {resourceAssignId: 10 factDate: "2024-01-01T12:00:00" amount: 1.0 volume: 1.0}, projectId: 10) {
    resourceAssignFact {
      rowId
      factDate
      amount
      volume
      projectTransactionId
      resourceAssignId
    }
    ok
  }
}
```


## [CopyShiftWorksToAnotherDays](shift_work_common.py) Класс мутации на копирование сменной работы в другой день
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">shift_works_ids</span> (обязательный): Список идентификаторов сменных работ.
- <span style="color: orange;">date_to_copy</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">shift_works</span>: Список объектов сменных заданий типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  copyShiftWorksToAnotherDays(
    dateToCopy: {dateBegin: "2024-01-01"}
    projectId: 10
    projectTransactionId: 20
    shiftWorksIds: [10]
  ) {
    shiftWorks {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateShiftWorkTimeResourcesWithHierarchy](shift_work_time_resource_hierarchy_common.py) Класс мутации на назначение тайм-ресурсов на сменную работу с возвращением обновленной иерархии тайм-ресурсов назначенных на сменную работу
### Аргументы
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
- <span style="color: orange;">create_inputs</span> (обязательный): Список объектов обмена данными о создании связей тайм-ресурсов со сменной работой типа GraphQL.
    - <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор тайм-ресурса.
- <span style="color: orange;">update_inputs</span> (обязательный): Список объектов данных об обновлении связей тайм-ресурсов со сменной работой типа GraphQL.
    - <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор тайм-ресурса.
- <span style="color: orange;">remove_time_resource_ids</span> (обязательный): Список идентификаторов тайм-ресурсов для удаления связей со сменной работой.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">with_positions</span> (default_value=False): Флаг группировки.
- <span style="color: orange;">with_previous_days</span> (default_value=False): Флаг включения часы по предыдущим 3 дням.
- <span style="color: orange;">shift_type</span> (default_value=None): Тип смены.
### Возвращаемое значение
- <span style="color: orange;">shift_work</span>: Объект сменной работы типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">worker_elements</span>: Список объектов элементов работников в иерархии типа GraphQL.
- <span style="color: orange;">tag_elements</span>: Список объектов элементов тегов в иерархии типа GraphQL.
- <span style="color: orange;">organization_elements</span>: Список объектов элементов в иерархии типа GraphQL.
- <span style="color: orange;">position_elements</span>: Список объектов должностей в иерархии типа GraphQL.
- <span style="color: orange;">position_group_elements</span>: Список объектов элементов групп должностей в иерархии типа GraphQL.
- <span style="color: orange;">affiliation_group_elements</span>: Список объектов элементов групп принадлежности к организации в иерархии типа GraphQL.
- <span style="color: orange;">assign_group_elements</span>: Список объектов элементов групп распределения часов в иерархии типа GraphQL.
- <span style="color: orange;">removed_element_ids</span>: Список удаленных идентификаторов в иерархии тайм-ресурсов назначенных на сменные задания.


### Пример использования
```graphql
mutation {
  updateShiftWorkTimeResourcesWithHierarchy(
    createInputs: [{timeResourceId: 10}]
    dateRange: {dateBegin: "2024-01-01"}
    projectId: 10
    projectTransactionId: 40
    removeTimeResourceIds: [60]
    shiftType: DAY
    shiftWorkId: 40
    updateInputs: [{timeResourceId: 10}]
  ) {
    shiftWork {
      rowId
      name
    }
    okStatus
    workerElements {
      rowId
    }
    tagElements {
      rowId
    }
    organizationElements {
      rowId
    }
    positionElements {
      rowId
    }
    positionGroupElements {
      rowId
    }
    affiliationGroupElements {
      rowId
    }
    assignGroupElements {
      rowId
    }
    removedElementIds
  }
}
```


## [BulkCopyWork](work_common.py) Класс мутации на массовое копирование работ
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о массовом копировании работ типа GraphQL.
    - <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
    - <span style="color: orange;">target_phase_id</span> (обязательный): Идентификатор фазы.
### Возвращаемое значение
- <span style="color: orange;">works</span>: Список созданных объектов работы типа GraphQL.
- <span style="color: orange;">project_resources</span>: Список созданных объектов ресурсов типа GraphQL.
- <span style="color: orange;">resource_assigns</span>: Список созданных объектов связи с ресурсами типа GraphQL.
- <span style="color: orange;">project_element_costs</span>: Список созданных объектов стоимостных составляющий типа GraphQL.
- <span style="color: orange;">work_links</span>: Список созданных объектов связи операций типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL. 
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  bulkCopyWork(input: { workIds: [10] targetPhaseId: 10 }) {
    works {
      rowId
      name
    }
    projectResources {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    projectElementCosts {
      rowId
    }
    workLinks {
      rowId
    }
    updatedCosts {
      rowId
    }
    updatedPhaseVolumes {
      rowId
    }
    ok
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями ресурсов

## [CreateCostComponent](cost_component_create.py) Класс мутации на создание стоимостной составляющей
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании составляющей стоимости типа GraphQL.
    - <span style="color: orange;">class_code</span> (обязательный): Отображаемые код.
    - <span style="color: orange;">code</span> (обязательный): Код компонента стоимости.
    - <span style="color: orange;">name</span> (обязательный): Название составляющей стоимости.
    - <span style="color: orange;">cost_type</span> (обязательный): Тип составляющей стоимости.
    - <span style="color: orange;">order_number</span> (обязательный): Порядковый номер.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">cost_component</span>: Объект стоимостной составляющей типа GraphQL.


### Пример использования
```graphql
mutation {
  createCostComponent(input: {classCode: "string" code: "string" name: "string" costType: COSTS orderNumber: 10}) {
    ok
    costComponent {
      rowId
      name
    }
  }
}
```


## [CreateGanttChart](gantt_chart_create.py) Класс мутации на создание диаграммы Гантта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании диаграммы Гантта типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование диаграммы.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">gantt_chart</span>: Объект диаграммы Гантта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createGanttChart(input: {name: "string" projectId: 10 organizationId: 10}) {
    ganttChart {
      rowId
      name
    }
    ok
  }
}
```


## [CreateGanttOrganizationHierarchies](gantt_organization_hierarchy_create.py) Класс мутации на создание объектов иерархии организаций диаграмм Гантта
### Аргументы
- <span style="color: orange;">create_inputs</span> (обязательный): Список объектов обмена данными о создании иерархии организаций диаграмм Гантта типа GraphQL.
    - <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
    - <span style="color: orange;">parent_id</span> (обязательный): Идентификатор родительской организации.
### Возвращаемое значение
- <span style="color: orange;">gantt_organization_hierarchies</span>: Список объектов иерархии организаций диаграмм Гантта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createGanttOrganizationHierarchies(createInputs: [{organizationId: 10 parentId: 10}]) {
    ganttOrganizationHierarchies {
      organizationId
      parentId
    }
    ok
    errMsg
  }
}
```


## [CreateMaterial](material_create.py) Класс мутации на создание материала
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании материала типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">element_type</span> (обязательный): Тип элемента.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
    - <span style="color: orange;">measure_unit</span> (обязательный): Единица измерения элемента.
### Возвращаемое значение
- <span style="color: orange;">material</span>: Объект материала типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createMaterial(createInput: {measureUnit: "string" projectId: 10 elementType: WORK projectTransactionId: 10}) {
    material {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [CreateMaterialAssign](material_assign_create.py) Класс мутации на создание объекта связи материала с операцией
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании материала типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">material_id</span> (обязательный): Идентификатор материала.
### Возвращаемое значение
- <span style="color: orange;">material_assign</span>: Объект связи материала с операцией типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createMaterialAssign(createInput: {workId: 10 materialId: 10 consumptionPerHour: 1.0}) {
    materialAssign {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [CreateMaterialResourceAssign](material_resource_assign_create.py) Класс мутации на создание объекта связи материала с ресурсом
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании материала типа GraphQL.
    - <span style="color: orange;">project_resource_id</span> (обязательный): Идентификатор ресурса.
    - <span style="color: orange;">material_id</span> (обязательный): Идентификатор материала.
### Возвращаемое значение
- <span style="color: orange;">material_resource_assign</span>: Объект связи материала с ресурсом типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createMaterialResourceAssign(createInput: {projectResourceId: 10 materialId: 10}) {
    materialResourceAssign {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [CreateProjectElementAdditionalColumn](project_element_additional_column_create.py) Класс мутации на создание дополнительного столбца графика
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании дополнительного столбца графика типа GraphQL.
    - <span style="color: orange;">column_name</span> (обязательный): Наименование дополнительного столбца графика.
    - <span style="color: orange;">column_code</span> (обязательный): Код дополнительного столбца графика.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции проекта элемента.
    - <span style="color: orange;">column_type</span> (обязательный): Тип дополнительного столбца графика.
### Возвращаемое значение
- <span style="color: orange;">project_element_additional_column</span>: Объект дополнительного столбца графика типа GraphQL.


### Пример использования
```graphql
mutation {
  createProjectElementAdditionalColumn(
    createInput: {
      columnName: "string"
      columnCode: "string"
      columnType: TEXT
      projectTransactionId: 10
    }
  ) {
    projectElementAdditionalColumn {
      rowId
    }
  }
}
```


## [CreateProjectElementAdditionalColumnValue](project_element_additional_column_value_create.py) Класс мутации на создание значений дополнительного столбца графика
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании дополнительного столбца графика типа GraphQL.
    - <span style="color: orange;">column_name</span> (обязательный): Наименование дополнительного столбца графика.
    - <span style="color: orange;">column_code</span> (обязательный): Код дополнительного столбца графика.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции проекта элемента.
    - <span style="color: orange;">column_type</span> (обязательный): Тип дополнительного столбца графика.
### Возвращаемое значение
- <span style="color: orange;">project_element_additional_column</span>: Объект дополнительного столбца графика типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createProjectElementAdditionalColumnValue(
    createInput: { columnValue: "string" projectElementAdditionalColumnId: 10 projectElementId: 10 }
  ) {
    projectElementAdditionalColumnValue {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [CreateWorkCosts](project_element_cost_create.py) Класс мутации на создание стоимостной составляющей работ
### Аргументы
- <span style="color: orange;">create_inputs</span> (обязательный): Список объектов обмена данными о создании стоимостных составляющих работ типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">cost_component_id</span> (обязательный): Идентификатор составляющей стоимости.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">project_element_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createWorkCosts(createInputs: [{workId: 10 costComponentId: 10}]) {
    okStatus
    projectElementCosts {
      rowId
    }
    errMsg
  }
}
```


## [CreateProjectElementCosts](project_element_cost_create.py) Класс мутации на создание стоимостной составляющей элемента графика
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными о создании стоимостных составляющих работ типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">cost_component_id</span> (обязательный): Идентификатор составляющей стоимости.
- <span style="color: orange;">cost_accounting_in_phases</span> (default_value=False): Флаг учета стоимости элемента графика в фазах.
- <span style="color: orange;">cost_accounting_in_works_for_materials</span> (default_value=False): Флаг учета стоимостей в операциях.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">project_element_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">error_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createProjectElementCosts(
    costAccountingInPhases: false
    costAccountingInWorksForMaterials: false
    inputs: [{projectElementId: 10 costComponentId: 10}]
  ) {
    okStatus
    projectElementCosts {
      rowId
    }
    errorMsg
  }
}
```


## [CreateProjectElementsPlans](project_element_plans_create.py) Класс мутации на создание планов элементов графика по списку идентификаторов транзакций
### Аргументы
- <span style="color: orange;">project_transaction_ids</span> (обязательный): Список идентификаторов транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectElementsPlans(projectTransactionIds: [10, 20]) {
    okStatus
  }
}
```


## [CreateProjectElementProjectPhase](project_phase_create.py) Класс мутации на создание фазы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании фазы в графике типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">element_type</span> (обязательный): Тип элемента.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">project_phase</span>: Объект созданной фазы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectElementProjectPhase(input: { elementType: PHASE projectId: 10 projectTransactionId: 10 }) {
    projectPhase {
      rowId
      name
    }
    ok
  }
}
```


## [CreateProjectResource](project_resource_create.py) Класс мутации на создание проектного ресурса
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании проектного ресурса типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">element_type</span> (обязательный): Тип элемента.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">project_resource</span>: Объект проектного ресурса типа GraphQL.


### Пример использования
```graphql
mutation {
  createProjectResource(input: { elementType: PHASE projectId: 10 projectTransactionId: 10 }) {
    ok
    projectResource {
      rowId
      name
    }
  }
}
```


## [CreateProjectTransactionMaterial](project_transaction_material_create.py) Класс мутации на формирование графика потребности материалов
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции проекта.
- <span style="color: orange;">only_internal</span> (default_value=False): Флаг формирования графика по внутригрупповым материалам.
### Возвращаемое значение
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createProjectTransactionMaterial(
    onlyInternal: false
    projectId: 10
    projectTransactionId: 10
  ) {
    errMsg
    okStatus
  }
}
```


## [CreateResourceAssign](resource_assign_create.py) Класс мутации на создание связи ресурса с работой
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании связи ресурса с работой типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">resource_id</span> (обязательный): Идентификатор ресурса.
### Возвращаемое значение
- <span style="color: orange;">resource_assign</span>: Объект связи ресурса с работой типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createResourceAssign(createInput: {workId: 10 resourceId: 10}) {
    resourceAssign {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [CreateShiftWork](shift_work_create.py) Класс мутации на создание сменной работы
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными о создании сменной работы типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Имя элемента из SpiderProject.
    - <span style="color: orange;">code</span> (обязательный): Код элемента из SpiderProject.
    - <span style="color: orange;">shift_day</span> (обязательный): Дата смены журнала заданий.
    - <span style="color: orange;">parent_id</span> (обязательный): Идентификатор родителя.
### Возвращаемое значение
- <span style="color: orange;">shift_works</span>: Список объектов сменных заданий типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createShiftWork(
    inputs: [{ name: "string" code: "string" shiftDay: "2024-01-01" parentId: 10}]
    projectId: 10
    projectTransactionId: 10
  ) {
    shiftWorks {
      rowId
      name
    }
    ok
  }
}
```


## [CreateShiftWorkFact](shift_work_create.py) Класс мутации на создание факта по сменной работы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании факта сменной работы типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">fact_date</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">fact_volume</span> (обязательный): Объем элемента.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">shift_work_fact</span>: Объект факта по сменной работе типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">error_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createShiftWorkFact(input: {shiftWorkId: 10 factDate: "2024-01-01" factVolume: 1.0}, projectId: 100) {
    shiftWorkFact {
      rowId
      name
    }
    ok
    errorMsg
  }
}
```


## [CreateWorkFactForFactual](shift_work_create.py) Класс мутации на создание факта с возвратом иерархии фактических фаз и фактических этапов
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании факта по операции типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">fact_date</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">fact_volume</span> (обязательный): Объем элемента.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_classifier</span> (default_value=True): Флаг вывода работ из классификатора.
- <span style="color: orange;">date_job</span> (default_value=None): День, на который необходимо получить сменные задания.
- <span style="color: orange;">future_works_without_fact</span> (default_value=None): Флаг вывода работы из будущего, по которым не вводился факт.
- <span style="color: orange;">with_factual_phases</span> (default_value=True): Флаг включения в результат запроса родительские фазы работ.
### Возвращаемое значение
- <span style="color: orange;">work_fact</span>: Объект факта по выполненным объемам работ типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">error_message</span>: Текст ошибки.
- <span style="color: orange;">smr_fact_on_day</span>: СМР факт на день.
- <span style="color: orange;">wage_fact_on_day</span>: ЗП сотрудников факт на день.
- <span style="color: orange;">factual_project_objects</span>: Список объектов фактических этапов типа GraphQL.
- <span style="color: orange;">factual_phases</span>: Список объектов фактических фаз типа GraphQL.
- <span style="color: orange;">factual_works</span>: Список объектов фактических работ типа GraphQL.


### Пример использования
```graphql
mutation {
  createWorkFactForFactual(
    createInput: {workId: 10 factDate: "2024-01-01" factVolume: 1.0}
    futureWorksWithoutFact: false
    projectId: 10
    dateRange: {dateBegin: "2024-01-01"}
    projectTransactionId: 120
    withClassifier: true
    withFactualPhases: true
  ) {
    workFact {
      rowId
    }
    okStatus
    errorMessage
    smrFactOnDay
    wageFactOnDay
    factualProjectObjects {
      rowId
      name
    }
    factualPhases {
      rowId
      name
    }
    factualWorks {
      rowId
      name
    }
  }
}
```


## [CreateShiftWorkRelationApprovalWork](shift_work_relation_approval_work_create.py) Класс мутации на массовое создание связей сменной работы с выполненными неподписанными работами
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными о создании факта сменной работы типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">task_id</span> (обязательный): Идентификатор задачи.
    - <span style="color: orange;">type_name</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">shift_work_relation_approval_work</span>: Список объектов связей сменных работ с выполненными неподписанными работами типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createShiftWorkRelationApprovalWork(
    inputs: [{ taskId: "string" typeName: "string" shiftWorkId: 10 }]
  ) {
    shiftWorkRelationApprovalWork {
      rowId
    }
    ok
  }
}
```


## [CreateShiftWorkRelationInspection](shift_work_relation_inspection_create.py) Класс мутации на массовое создание связи сменной работы с приемочной инспекцией
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными о создании факта сменной работы типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">task_id</span> (обязательный): Идентификатор задачи.
    - <span style="color: orange;">type_name</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">shift_work_relation_inspection</span>: Список объектов связей сменных работ с приемочными инспекциями типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createShiftWorkRelationInspection(
    inputs: [{ taskId: "string" typeName: "string" shiftWorkId: 10 }]
  ) {
    shiftWorkRelationInspection {
      rowId
    }
    ok
  }
}
```


## [CreateShiftWorkRelationWorkJournal](shift_work_relation_work_journal_create.py) Класс мутации на создание связи сменной работы с работой из общего журнала работ
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании связи сменной работы с работой из общего журнала работ типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">work_journal_id</span> (обязательный): Идентификатор работы из общего журнала работ.
    - <span style="color: orange;">journal_id</span> (обязательный): Идентификатор общего журнала работ.
### Возвращаемое значение
- <span style="color: orange;">shift_work_relation_work_journal</span>: Объект связи сменной работы с работой из общего журнала работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createShiftWorkRelationWorkJournal(input: {shiftWorkId: 10 workJournalId: 10 journalId: 10}) {
    shiftWorkRelationWorkJournal {
      shiftWorkId
      workJournalId
      journalId
      createDate
    }
    ok
  }
}
```


## [CreateProjectElementWork](work_create.py) Класс мутации на создание элемента графика
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании полей работы в графике типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">work_journal_id</span> (обязательный): Идентификатор работы из общего журнала работ.
    - <span style="color: orange;">journal_id</span> (обязательный): Идентификатор общего журнала работ.
### Возвращаемое значение
- <span style="color: orange;">work</span>: Созданный объект работы типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">work_schedule_assigns</span>: Список объектов связей календарей и операций типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
НА ДОРАБОТКЕ
```


## [CreateWorkFact](work_fact_create.py) Класс мутации на создание факта
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании полей работы в графике типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">fact_date</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">fact_volume</span> (обязательный): Объем элемента.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">work_fact</span>: Объект факта по выполненным объемам работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">error_message</span>: Текст ошибки.
- <span style="color: orange;">smr_fact_on_day</span>: СМР факт на день.
- <span style="color: orange;">wage_fact_on_day</span>: ЗП сотрудников факт на день.


### Пример использования
```graphql
mutation {
  createWorkFact(input: {workId: 10 factDate: "2024-01-01" factVolume: 1.0}, projectId: 10) {
    workFact {
      rowId
    }
    ok
    errorMessage
    smrFactOnDay
    wageFactOnDay
  }
}
```


## [CreateJobTaskFact](work_fact_create.py) Класс мутации на ввод факта журнала сменных заданий
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании полей работы в графике типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">fact_date</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">fact_volume</span> (обязательный): Объем элемента.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">work_fact</span>: Объект факта по выполненным объемам работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">error_message</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  createJobTaskFact(input: {workId: 10 factDate: "2024-01-01" factVolume: 1.0}, projectId: 10) {
    workFact {
      rowId
    }
    ok
    errorMessage
  }
}
```


## [BatchCreateWorkFacts](work_fact_create.py) Класс мутации на массовое создание фактов
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о вводе факта журнала сменных заданий типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">fact_date</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">fact_volume</span> (обязательный): Объем элемента.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">work_facts</span>: Список объектов фактов по выполненным объемам работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  batchCreateWorkFacts(inputs: [{workId: 10 factDate: "2024-01-01" factVolume: 1.0}], projectId: 10) {
    workFacts {
      rowId
    }
    ok
  }
}
```


## [WorkFactTransferToAnotherVersion](work_fact_create.py) Класс мутации на перенос факта в другую версию
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id_from</span> (обязательный): Идентификатор транзакции из которой нужно копировать.
- <span style="color: orange;">project_transaction_id_to</span> (обязательный): Идентификатор транзакции в которую нужно копировать.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">error_message</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  workFactTransferToAnotherVersion(
    dateRange: {dateBegin: "2024-01-01"}
    projectId: 10
    projectTransactionIdFrom: 20
    projectTransactionIdTo: 10
  ) {
    ok
    errorMessage
  }
}
```


## [CreateWorkLink](work_link_create.py) Класс мутации на создание взаимосвязи операций
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании взаимосвязи операций типа GraphQL.
    - <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
    - <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
    - <span style="color: orange;">previous_work_id</span> (обязательный): Идентификатор первоочередной работы во взаимосвязи операций.
    - <span style="color: orange;">next_work_id</span> (обязательный): Идентификатор следующей работы во взаимосвязи операций.
    - <span style="color: orange;">work_link_type</span> (обязательный): Тип взаимосвязи операций.
### Возвращаемое значение
- <span style="color: orange;">work_link</span>: Созданный объект взаимосвязи операций типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkLink(createInput: { workLinkType: START_START projectId: 10 projectTransactionId: 30 previousWorkId: 30 nextWorkId: 10}) {
    workLink {
      rowId
      projectId
    }
    errMsg
    okStatus
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями ресурсов

## [DeleteCostComponents](cost_component_delete.py) Класс мутации на удаление стоимостной составляющей
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор составляющей стоимости.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteCostComponents(rowIds: [10]) {
    ok
  }
}
```


## [DeleteGanttCharts](gantt_chart_delete.py) Класс мутации на удаление диаграмм Гантта
### Аргументы
- <span style="color: orange;">gantt_charts_ids</span> (обязательный): Список идентификаторов диаграмм Гантта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteGanttCharts(ganttChartsIds: [10]) {
    ok
  }
}
```


## [DeleteGanttOrganizationHierarchies](gantt_organization_hierarchy_delete.py) Класс мутации на удаление объектов иерархии организаций диаграмм Гантта
### Аргументы
- <span style="color: orange;">organization_ids</span> (обязательный): Список идентификаторов организаций.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteGanttOrganizationHierarchies(organizationIds: [10]) {
    ok
  }
}
```


## [DeleteMaterial](material_delete.py) Класс мутации на удаление материалов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов материалов.
- <span style="color: orange;">cost_accounting_in_works_for_materials</span> (default_value=False): Флаг учета стоимостей в операциях.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">project_element_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.


### Пример использования
```graphql
mutation {
  deleteMaterial(costAccountingInWorksForMaterials: false, rowIds: [10]) {
    okStatus
    errMsg
    projectElementCosts {
      rowId
    }
  }
}
```


## [DeleteMaterialAssign](material_assign_delete.py) Класс мутации на удаление связи материала и операции
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов объектов связей материалов и операций.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteMaterialAssign(rowIds: [10]) {
    okStatus
    errMsg
  }
}
```


## [DeleteMaterialResourceAssigns](material_resource_assign_delete.py) Класс мутации на удаление связей материалов и ресурсов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов объектов связи материалов и ресурсов.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteMaterialResourceAssigns(rowIds: [10]) {
    okStatus
    errMsg
  }
}
```


## [DeleteProjectElements](project_element_delete.py) Класс мутации на удаление элементов графика
### Аргументы
- <span style="color: orange;">project_elements_ids</span> (обязательный): Список идентификаторов элементов графика для удаления.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteProjectElements(projectElementsIds: [10]) {
    ok
    updatedCosts {
      rowId
    }
    updatedPhaseVolumes {
      rowId
    }
    errMsg
  }
}
```


## [DeleteProjectElementAdditionalColumns](project_element_additional_column_delete.py) Класс мутации на массовое удаление дополнительных столбцов графика
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов дополнительных столбцов графика.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteProjectElementAdditionalColumns(rowIds: [10]) {
    okStatus
    errMsg
  }
}
```


## [DeleteWorkCost](project_element_cost_delete.py) Класс мутации на удаление стоимостной составляющей работ
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов стоимостных составляющих работ.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkCost(rowIds: [10]) {
    okStatus
  }
}
```


## [DeleteProjectElementCosts](project_element_cost_delete.py) Класс мутации на удаление стоимостных составляющих элементов графика
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов стоимостных составляющих работ.
- <span style="color: orange;">cost_accounting_in_phases</span> (default_value=False): Флаг учета стоимости элемента графика в фазах.
- <span style="color: orange;">cost_accounting_in_works_for_materials</span> (default_value=False): Флаг учета стоимостей в операциях.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">project_element_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">error_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteProjectElementCosts(
    costAccountingInPhases: false
    costAccountingInWorksForMaterials: false
    rowIds: [10]
  ) {
    okStatus
    projectElementCosts {
      rowId
    }
    errorMsg
  }
}
```


## [DeleteResourceAssigns](resource_assign_delete.py) Класс мутации на удаление стоимостных составляющих элементов графика
### Аргументы
- <span style="color: orange;">row_ids</span> (default_value=None): Список идентификаторов связей ресурса с работой.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResourceAssigns(projectTransactionId: 10) {
    okStatus
  }
}
```


## [DeleteResourceAssigns](resource_assign_delete.py) Класс мутации на удаление стоимостных составляющих элементов графика
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов связей ресурса с работой.
- <span style="color: orange;">project_transaction_id</span> (default_value=False): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResourceAssigns(projectTransactionId: 10) {
    okStatus
  }
}
```


## [DeleteShiftWorkRelationApprovalWork](shift_work_relation_approval_work_delete.py) Класс мутации на массовое удаление связей сменной работы с выполненными неподписанными работами
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об массовом удалении связи сменных работ с выполненными неподписанными работами типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">task_id</span> (обязательный): Идентификатор задачи.
    - <span style="color: orange;">type_name</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteShiftWorkRelationApprovalWork(
    inputs: [{shiftWorkId: 10 taskId: "string" typeName: "string"}]
  ) {
    ok
  }
}
```


## [DeleteShiftWorkRelationInspection](shift_work_relation_inspection_delete.py) Класс мутации на массовое удаление связи сменной работы с приемочной инспекцией
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об массовом удалении связи сменных работ с приемочными инспекциями типа GraphQL.
    - <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">task_id</span> (обязательный): Идентификатор задачи.
    - <span style="color: orange;">type_name</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteShiftWorkRelationInspection(
    inputs: [{shiftWorkId: 10 taskId: "string" typeName: "string"}]
  ) {
    ok
  }
}
```


## [DeleteTimeResourceAssignmentTypes](time_resource_assignment_type_delete.py) Класс мутации на удаление связей ресурса с должностными группами
### Аргументы
- <span style="color: orange;">resource_ids</span> (default_value=[]): Список идентификаторов ресурсов.
- <span style="color: orange;">project_resource_ids</span> (default_value=[]): Список идентификаторов элементов графика.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteResourceAssigns(projectResourceIds: [10]) {
    ok
  }
}
```


## [DeleteProjectElementWork](work_delete.py) Класс мутации на удаление элемента графика
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов элементов графика.
### Возвращаемое значение
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteProjectElementWork(workIds: [10]) {
    updatedCosts {
      rowId
    }
    updatedPhaseVolumes {
      rowId
    }
    ok
  }
}
```


## [DeleteWorkLink](work_link_delete.py) Класс мутации на удаление взаимосвязи операций
### Аргументы
- <span style="color: orange;">work_link_ids</span> (обязательный): Список идентификаторов взаимосвязей операций.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkLink(workLinkIds: [10]) {
    okStatus
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями ресурсов

## [UpdateCostComponent](cost_component_update.py) Класс мутации на обновление стоимостной составляющей
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор составляющей стоимости.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании составляющей стоимости типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">cost_component</span>: Объект стоимостной составляющей типа GraphQL.


### Пример использования
```graphql
mutation {
  updateCostComponent(input: {code: "string"} rowId: 10) {
    ok
    costComponent {
      rowId
      classCode
      code
      name
      costType
      orderNumber
    }
  }
}
```


## [SetWorkIgnoreDateFilters](factual_work_update.py) Класс мутации на обновления флага ignore_date_filters у работы с возвратом иерархии фактических фаз и фактических этапов
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
- <span style="color: orange;">ignore_date_filters</span> (обязательный): Флаг игнорирования фильтраций по датам при получении работ.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_factual_phases</span> (default_value=True): Флаг включения в результат запроса родительские фазы работ.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">factual_project_objects</span>: Список объектов фактических этапов типа GraphQL.
- <span style="color: orange;">factual_phases</span>: Список объектов фактических фаз типа GraphQL.
- <span style="color: orange;">factual_works</span>: Список объектов фактических работ типа GraphQL.


### Пример использования
```graphql
mutation {
  setWorkIgnoreDateFilters(
    dateRange: {dateBegin: "2024-01-01"}
    ignoreDateFilters: true
    projectId: 10
    projectTransactionId: 20
    withFactualPhases: true
    workIds: [10]
  ) {
    okStatus
    factualProjectObjects {
      rowId
      name
    }
    factualPhases {
      rowId
      name
    }
    factualWorks {
      rowId
      name
    }
  }
}
```


## [UpdateGanttChart](gantt_chart_update.py) Класс мутации на обновление диаграммы Гантта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор диаграммы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении диаграммы Гантта типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">gantt_chart</span>: Объект диаграммы Гантта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateGanttChart(input: {name: "string"} rowId: 10) {
    ganttChart {
      rowId
      name
    }
    ok
  }
}
```


## [SetParentToGanttCharts](gantt_chart_update.py) Класс мутации на установку родительской диаграммы Гантта
### Аргументы
- <span style="color: orange;">parent_id</span> (обязательный): Идентификатор родительской диаграммы Гантта.
- <span style="color: orange;">gantt_charts_ids</span> (обязательный): Список идентификаторов диаграмм Гантта.
### Возвращаемое значение
- <span style="color: orange;">gantt_charts</span>: Список объектов диаграмм Гантта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setParentToGanttCharts(ganttChartsIds: [10] parentId: 20) {
    ganttCharts {
      rowId
      name
    }
    ok
  }
}
```


## [ResetParentToGanttCharts](gantt_chart_update.py) Класс мутации на сброс родительской диаграммы Гантта
### Аргументы
- <span style="color: orange;">gantt_charts_ids</span> (обязательный): Список идентификаторов диаграмм Гантта.
### Возвращаемое значение
- <span style="color: orange;">gantt_charts</span>: Список объектов диаграмм Гантта типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetParentToGanttCharts(ganttChartsIds: [10]) {
    ganttCharts {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateMaterial](material_update.py) Класс мутации на обновление материала
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор материала.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении материала типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">material</span>: Объект материала типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  updateMaterial(rowId: 10 updateInput: {code: "str"}) {
    material {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [UpdateMaterialAssign](material_assign_update.py) Класс мутации на обновление связи материала и операции
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор связи ресурса с работой.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении материала типа GraphQL.
- <span style="color: orange;">with_return</span> (default_value=False): Флаг возврата результата мутации.
### Возвращаемое значение
- <span style="color: orange;">material_assign</span>: Объект связи материала с операцией типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  updateMaterialAssign(rowId: 10 updateInput: {planVolume: 1.0} withReturn: false) {
    materialAssign {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [UpdateMaterialResourceAssign](material_resource_assign_update.py) Класс мутации на обновление связи материала и ресурса
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор связи ресурса с работой.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении материала типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">material_resource_assign</span>: Объект связи материала с операцией типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  updateMaterialResourceAssign(rowId: 10 updateInput: {planVolume: 10.0}) {
    materialResourceAssign {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [SetCodeForProjectElement](project_element_update.py) Класс мутации на назначение этапов элементам графика
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента в базе.
- <span style="color: orange;">code</span> (обязательный): Код элемента из SpiderProject.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setCodeForProjectElement(code: "string", projectElementId: 10) {
    ok
  }
}
```


## [SetProjectElementProjectObject](project_element_update.py) Класс мутации на установку кода элемента проекта по идентификатору элемента проекта
### Аргументы
- <span style="color: orange;">project_elements_ids</span> (обязательный): Список идентификаторов элементов графика.
- <span style="color: orange;">project_object_id</span> (обязательный): Идентификатор этапа проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setProjectElementProjectObject(
    projectElementsIds: [10]
    projectObjectId: 10
  ) {
    ok
  }
}
```


## [SetProjectPhaseProjectObject](project_element_update.py) Класс мутации на назначение этапа фазе
### Аргументы
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">project_object_id</span> (обязательный): Идентификатор этапа проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setProjectPhaseProjectObject(
    phaseId: 10
    projectObjectId: 10
    projectTransactionId: 10
  ) {
    okStatus
  }
}
```


## [ResetProjectElementProjectObject](project_element_update.py) Класс мутации на сброс этапа для элементов графика
### Аргументы
- <span style="color: orange;">project_elements_ids</span> (обязательный): Список идентификаторов элементов графика.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetProjectElementProjectObject(projectElementsIds: [10]) {
    ok
  }
}
```


## [ResetProjectPhaseProjectObject](project_element_update.py) Класс мутации на сброс этапа для элементов графика
### Аргументы
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetProjectPhaseProjectObject(
    phaseId: 10
    projectTransactionId: 10
  ) {
    okStatus
  }
}
```


## [SetProjectElementHidden](project_element_update.py) Класс мутации на установку флага скрытия элемента графика
### Аргументы
- <span style="color: orange;">project_elements_ids</span> (обязательный): Список идентификаторов элементов графика.
- <span style="color: orange;">hidden</span> (default_value=False): Флаг скрытого элемента.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  setProjectElementHidden(hidden: true projectElementsIds: [10]) {
    ok
  }
}
```


## [UpdateProjectElementAdditionalName](project_element_update.py) Класс мутации на обновление дополнительного наименования элемента графика
### Аргументы
- <span style="color: orange;">project_elements_ids</span> (обязательный): Список идентификаторов элементов графика.
- <span style="color: orange;">additional_name</span> (обязательный): Флаг скрытого элемента.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateProjectElementAdditionalName(
    additionalName: "string"
    projectElementsIds: [10]
  ) {
    ok
  }
}
```


## [SetResponsibleForProjectElement](project_element_update.py) Класс мутации на обновление дополнительного наименования элемента графика
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента графика.
- <span style="color: orange;">set_input</span> (обязательный): Объект обмена данными о назначении ответственного по элементу типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_phases</span>: Список обновленных объектов фаз типа GraphQL.
- <span style="color: orange;">works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setResponsibleForProjectElement(projectElementId: 10 setInput: {responsibleName: "string"}) {
    projectPhases {
      rowId
      name
    }
    works {
      rowId
      name
    }
    ok
  }
}
```


## [ResetResponsibleForProjectElement](project_element_update.py) Класс мутации на сброс ответственного за исполнение элемента графика
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента графика.
### Возвращаемое значение
- <span style="color: orange;">project_phases</span>: Список обновленных объектов фаз типа GraphQL.
- <span style="color: orange;">works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  resetResponsibleForProjectElement(projectElementId: 10) {
    projectPhases {
      rowId
      name
    }
    works {
      rowId
      name
    }
    ok
  }
}
```


## [SetResponsibleUsingInBI](project_element_update.py) Класс мутации на сброс ответственного за исполнение элемента графика
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента графика.
- <span style="color: orange;">responsible_using_in_bi</span> (default_value=True): Идентификатор элемента графика.
### Возвращаемое значение
- <span style="color: orange;">project_phases</span>: Список обновленных объектов фаз типа GraphQL.
- <span style="color: orange;">works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setResponsibleUsingInBi(
    projectElementId: 10
    responsibleUsingInBi: true
  ) {
    projectPhases {
      rowId
      name
    }
    works {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateProjectElementAdditionalColumn](project_element_additional_column_update.py) Класс мутации на обновление дополнительного столбца графика
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор дополнительного столбца графика.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении дополнительного столбца графика типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_element_additional_column</span>: Объект дополнительного столбца графика типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateProjectElementAdditionalColumn(rowId: 10 updateInput: {columnCode: "string"}) {
    projectElementAdditionalColumn {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [UpdateProjectElementAdditionalColumnValue](project_element_additional_column_value_update.py) Класс мутации на обновление значения дополнительного столбца графика
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор значения дополнительного столбца графика.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении значения дополнительного столбца графика типа GraphQL.
    - <span style="color: orange;">column_value</span> (обязательный): Идентификатор значения дополнительного столбца графика.
### Возвращаемое значение
- <span style="color: orange;">project_element_additional_column_value</span>: Объект значения дополнительного столбца графика типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateProjectElementAdditionalColumnValue(
    rowId: 10
    updateInput: { columnValue: "string" }
  ) {
    projectElementAdditionalColumnValue {
      rowId
    }
    okStatus
    errMsg
  }
}
```


## [UpdateWorkCost](project_element_cost_update.py) Класс мутации на обновление стоимостной составляющей работ
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении стоимостной составляющей работы типа GraphQL.
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
- <span style="color: orange;">cost_component_id</span> (обязательный): Идентификатор стоимостной составляющей.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">updated_cost</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateWorkCost(costComponentId: 10, updateInput: {costPerHour: 20.0}, workId: 10) {
    okStatus
    updatedCost {
      rowId
    }
    errMsg
  }
}
```


## [UpdateProjectElementCost](project_element_cost_update.py) Класс мутации на обновление стоимостной составляющей элемента графика
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента в базе.
- <span style="color: orange;">cost_component_id</span> (обязательный): Идентификатор стоимостной составляющей.
- <span style="color: orange;">old_total_volume</span> (default_value=None): Фактический объем стоимостной до изменения.
- <span style="color: orange;">old_plan_volume</span> (default_value=None): Плановый объем стоимостной до изменения.
- <span style="color: orange;">old_fact_volume</span> (default_value=None): Общий объем стоимостной до изменения.
- <span style="color: orange;">cost_accounting_in_phases</span> (default_value=False): Флаг учета стоимости элемента графика в фазах.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении объемов стоимостной элемента типа GraphQL.
- <span style="color: orange;">cost_accounting_in_works_for_materials</span> (default_value=False): Флаг учета стоимостей в операциях. При передаче true будут также пересчитаны стоимости фаз.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">project_element_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateProjectElementCost(
    costAccountingInPhases: false
    costAccountingInWorksForMaterials: false
    costComponentId: 10
    oldFactVolume: 20
    oldPlanVolume: 30
    oldTotalVolume: 20
    projectElementId: 10
    updateInput: {costPerHour: 10.0}
  ) {
    okStatus
    projectElementCosts {
      rowId
    }
    errorMsg
  }
}
```


## [RecalculateProjectElementCostsP0](project_element_cost_update.py) Класс мутации на пересчет стоимостных работ фазы по составляющей П0
### Аргументы
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">update_p111_flag</span> (default_value=False): Флаг обновления существующих стоимостных составляющих П111.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">created_works</span>: Список объектов операций типа GraphQL.
- <span style="color: orange;">created_costs</span>: Список созданных объектов стоимостных составляющий типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.

### Пример использования
```graphql
mutation {
  recalculateProjectElementCostsP0(
    phaseId: 1
    projectId: 773
    projectTransactionId: 120
    updateP111Flag: false
  ) {
    ok
    errMsg
    createdWorks {
      rowId
      name
    }
    createdCosts {
      rowId
    }
    updatedCosts {
      rowId
    }
  }
}
```


## [RecalculateChartCosts](project_element_cost_update.py) Класс мутации на пересчет стоимостей фаз по стоимостям дочерних работ
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  recalculateChartCosts(projectId: 10 projectTransactionId: 10) {
    ok
    errMsg
  }
}
```


## [SetResponsibleForProjectPhase](project_element_update.py) Класс мутации на назначение ответственного за фазу
### Аргументы
- <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
- <span style="color: orange;">responsible_type</span> (обязательный): Тип ответственного.
- <span style="color: orange;">responsible_name</span> (обязательный): Имя ответственного.
- <span style="color: orange;">phase_ids</span> (обязательный): Список идентификаторов фаз.
- <span style="color: orange;">parent_phase_ids</span> (обязательный): Список идентификаторов родительских фаз.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setResponsibleForProjectPhase(
    parentPhaseIds: [10]
    phaseIds: [20]
    responsibleId: 10
    responsibleName: "string"
    responsibleType: UserType
  ) {
    ok
  }
}
```


## [UpdateProjectPhase](project_element_update.py) Класс мутации на обновление фазы
### Аргументы
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении фазы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_phase</span>: Объект обновленной фазы типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateProjectPhase(input: {level: 1 parentId: 10}, phaseId: 20) {
    projectPhase {
      rowId
      name
    }
    updatedPhaseVolumes {
      rowId
    }
    updatedCosts {
      rowId
    }
    ok
  }
}
```


## [BulkUpdateProjectPhase](project_element_update.py) Класс мутации на массовое обновление фаз
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об массовом обновлении фаз типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">project_phase</span>: Список обновленных объектов фаз типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  bulkUpdateProjectPhase(inputs: [{phaseId:20 phaseInput: {parentId: 10}}]) {
    projectPhases {
      rowId
      name
    }
    updatedPhaseVolumes {
      rowId
    }
    updatedCosts {
      rowId
    }
    ok
  }
}
```


## [RecalculatePhaseVolumes](project_element_update.py) Класс мутации на пересчет объемов фаз по объемам дочерних работ
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_ids</span> (обязательный): Список идентификаторов транзакции.
### Возвращаемое значение
- <span style="color: orange;">err_msg</span>: Текст ошибки.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  recalculatePhaseVolumes(
    projectId: 10
    projectTransactionIds: [10]
  ) {
    errMsg
    ok
  }
}
```


## [UpdateProjectResource](project_resource_update.py) Класс мутации на обновление проектного ресурса
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор элемента в базе.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении проектного ресурса типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">project_resource</span>: Объект проектного ресурса типа GraphQL.

### Пример использования
```graphql
mutation {
  updateProjectResource(input: { elementType: PHASE projectId: 10 projectTransactionId: 10}, rowId: 20) {
    ok
    projectResource {
      rowId
      name
    }
  }
}
```


## [UpdateResourceAssign](resource_assign_update.py) Класс мутации на обновление связи ресурса с работой
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении связи ресурса с работой типа GraphQL.
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор связи ресурса с работой.
### Возвращаемое значение
- <span style="color: orange;">resource_assign</span>: Объект связи ресурса с работой типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateResourceAssign(rowId: 10, updateInput: {amount: 1}) {
    resourceAssign {
      rowId
    }
    okStatus
  }
}
```


## [SetShiftWorkFactHidden](shift_work_update.py) Класс мутации на установку флага скрытности сменной работы
### Аргументы
- <span style="color: orange;">hidden</span> (обязательный): Флаг скрытого элемента.
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
### Возвращаемое значение
- <span style="color: orange;">shift_work_fact</span>: Объект факта по сменной работе типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setShiftWorkFactHidden(hidden: true, shiftWorkId: 10) {
    shiftWorkFact {
      rowId
      name
    }
    ok
  }
}
```


## [SetIssuerForShiftWork](shift_work_update.py) Класс мутации на установление выдавшего сменную работу
### Аргументы
- <span style="color: orange;">shift_work_ids</span> (обязательный): Список идентификаторов сменных работ.
- <span style="color: orange;">input</span> (обязательный): Идентификатор сменной работы.
    - <span style="color: orange;">issuer_of_task_id</span> (обязательный): Идентификатор выдавшего задание.
    - <span style="color: orange;">issuer_of_task_type</span> (обязательный): Тип выдавшего.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setIssuerForShiftWork(
    input: { issuerOfTaskType: UserType issuerOfTaskId: 10 }
    shiftWorkIds: [10]
  ) {
    ok
  }
}
```


## [UpdateShiftWorkMachineResources](shift_work_update.py) Класс мутации на обновление ресурсов машин у сменной работы
### Аргументы
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об обновлении ресурсов машин у сменной работы типа GraphQL.
    - <span style="color: orange;">machine_resource_id</span> (обязательный): Идентификатор машин ресурса.
### Возвращаемое значение
- <span style="color: orange;">shift_work</span>: Объект сменной работы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateShiftWorkMachineResources(inputs: [{machineResourceId: 10}] shiftWorkId: 10) {
    shiftWork {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateShiftWorkTimeResources](shift_work_update.py) Класс мутации на обновление тайм-ресурсов у сменной работы
### Аргументы
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об обновлении ресурсов машин у сменной работы типа GraphQL.
    - <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор тайм-ресурса.
### Возвращаемое значение
- <span style="color: orange;">shift_work</span>: Объект сменной работы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateShiftWorkTimeResources(inputs: [{timeResourceId: 10}], shiftWorkId: 10) {
    shiftWork {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateShiftWorkRentMachine](shift_work_update.py) Класс мутации на обновление арендованных машин у сменной работы
### Аргументы
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными об обновлении арендованных машин у сменной работы типа GraphQL.
    - <span style="color: orange;">machine_application_id</span> (обязательный): Идентификатор заявки на машину.
### Возвращаемое значение
- <span style="color: orange;">shift_work</span>: Объект сменной работы типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateShiftWorkRentMachine(inputs: [{machineApplicationId: 13}], shiftWorkId: 10) {
    shiftWork {
      rowId
      name
    }
    ok
  }
}
```


## [UpdateShiftWorkRelationWorkJournal](shift_work_relation_work_journal_update.py) Класс мутации на обновление связи сменной работы с работой из общего журнала работ
### Аргументы
- <span style="color: orange;">shift_work_id</span> (обязательный): Идентификатор сменной работы.
- <span style="color: orange;">input</span> (обязательный): Список объектов обмена данными об обновлении арендованных машин у сменной работы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">shift_work_relation_work_journal</span>: Объект связи сменной работы с работой из общего журнала работ типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateShiftWorkRelationWorkJournal(input: {journalId: 10}, shiftWorkId: 10) {
    shiftWorkRelationWorkJournal {
      shiftWorkId
      workJournalId
      journalId
      createDate
    }
    ok
  }
}
```


## [SetResponsibleForWork](work_update.py) Класс мутации на установку ответственного за работу
### Аргументы
- <span style="color: orange;">responsible_id</span> (обязательный): Идентификатор ответственного.
- <span style="color: orange;">responsible_type</span> (обязательный): Тип ответственного.
- <span style="color: orange;">responsible_name</span> (default_value=None): Имя ответственного.
- <span style="color: orange;">phase_ids</span> (default_value=None): Список идентификаторов фаз.
- <span style="color: orange;">work_ids</span> (default_value=None): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setResponsibleForWork(
    phaseIds: [10]
    responsibleId: 20
    responsibleName: "string"
    responsibleType: UserType
    workIds: [10]
  ) {
    ok
  }
}
```


## [UpdateTrafficLightWork](work_update.py) Класс мутации на обновление флага светофорной работы
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
- <span style="color: orange;">traffic_light</span> (обязательный): Флаг светофорной работы.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateTrafficLightWork(trafficLight: true, workIds: [10]) {
    ok
  }
}
```


## [SetIssuerForJobTask](work_update.py) Класс мутации на назначение ответственного по задаче
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о назначении ответственного по задаче типа GraphQL.
    - <span style="color: orange;">issuer_of_task_id</span> (обязательный): Идентификатор выдавшего задание.
    - <span style="color: orange;">issuer_of_task_type</span> (обязательный): Тип выдавшего.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  setIssuerForJobTask(input: { issuerOfTaskType: UserType issuerOfTaskId: 10}) {
    ok
  }
}
```


## [UpdateWork](work_update.py) Класс мутации на обновление работы
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о назначении ответственного по задаче типа GraphQL.
    - <span style="color: orange;">issuer_of_task_id</span> (обязательный): Идентификатор выдавшего задание.
    - <span style="color: orange;">issuer_of_task_type</span> (обязательный): Тип выдавшего.
### Возвращаемое значение
- <span style="color: orange;">work</span>: Объект обновленной работы типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">resource_assigns</span>: Список объектов связей работ с ресурсами типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateWork(input: {name: "string"}, workId: 10) {
    work {
      rowId
      name
    }
    updatedPhaseVolumes {
      rowId
    }
    updatedCosts {
      rowId
    }
    resourceAssigns {
      rowId
    }
    ok
  }
}
```


## [BulkUpdateWork](work_update.py) Класс мутации на обновление работы
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о назначении ответственного по задаче типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">work_input</span> (обязательный): Объект обмена данными об обновлении работы типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">updated_phase_volumes</span>: Список объектов объемов работ фазы типа GraphQL.
- <span style="color: orange;">updated_costs</span>: Список объектов стоимостных составляющих элементов графика типа GraphQL.
- <span style="color: orange;">resource_assigns</span>: Список объектов связей работ с ресурсами типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  bulkUpdateWork(inputs: [{workId: 10 workInput: {workTaskCode: "string"}}]) {
    works {
      rowId
      name
    }
    updatedPhaseVolumes {
      rowId
    }
    updatedCosts {
      rowId
    }
    ok
    resourceAssigns {
      rowId
    }
  }
}
```


## [AddCommentWorkFact](work_fact_update.py) Класс мутации на добавление комментария к факту
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о назначении ответственного по задаче типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">day</span> (обязательный): Фактическая дата назначения.
    - <span style="color: orange;">comment</span> (обязательный): Комментарий к факту.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  addCommentWorkFact(input: { comment: "string" workId:10 day: "2024-01-01" }, projectId: 10) {
    ok
  }
}
```


## [UpdateWorkLink](work_link_update.py) Класс мутации на обновление взаимосвязи операций
### Аргументы
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении взаимосвязи операций типа GraphQL.
- <span style="color: orange;">work_link_id</span> (обязательный): Идентификатор взаимосвязи операций.
### Возвращаемое значение
- <span style="color: orange;">work_link</span>: Обновленный объект взаимосвязи операций типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  updateWorkLink(updateInput: {workLinkType: START_START}, workLinkId: 10) {
    workLink {
      rowId
    }
    okStatus
  }
}
```


## [UpdateWorkDatesForWorkLinks](work_link_update.py) Класс мутации на пересчет операций по взаимосвязям
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">with_dates</span> (default_value=True): Флаг получения с макс и мин датами операций.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">updated_works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">updated_phase</span>: Объект обновленной фазы типа GraphQL.
- <span style="color: orange;">updated_resource_assigns</span>: Список объектов обновленных связей работы с ресурсом типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateWorkDatesForWorkLinks(
    phaseId: 10
    projectId: 20
    transactionId: 10
    withDates: true
  ) {
    okStatus
    updatedWorks {
      rowId
      name
    }
    updatedPhase {
      rowId
    }
    updatedResourceAssigns {
      rowId
    }
    errMsg
  }
}
```


## [UpdateWorkDatesForWorkLinksTransactions](work_link_update.py) Класс мутации на пересчет операций по взаимосвязям для списка транзакций
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">updated_transaction_works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">updated_phase</span>: Объект обновленной фазы типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateWorkDatesForWorkLinksTransactions(
    projectId: 10
    transactionIds: [10]
  ) {
    okStatus
    updatedTransactionWorks {
      transactionId
    }
    updatedPhases {
      rowId
      name
    }
    errMsg
  }
}
```


## [UpdateWorkDatesForWorkLinksWorksMutation](work_link_update.py) Класс мутации на пересчет дат операций по взаимосвязям для списка работ
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">updated_transaction_works</span>: Список объектов обновленных работ типа GraphQL.
- <span style="color: orange;">updated_phase</span>: Объект обновленной фазы типа GraphQL.
- <span style="color: orange;">err_msg</span>: Текст ошибки.

### Пример использования
```graphql
mutation {
  updateWorkDatesForWorkLinksTransactions(
    projectId: 10
    transactionIds: [10]
  ) {
    okStatus
    updatedTransactionWorks {
      transactionId
    }
    updatedPhases {
      rowId
      name
    }
    errMsg
  }
}
```


# Модуль запросов для взаимодействия с сущностями ресурсов

## [getAllCostComponents](cost_component.py) Получение всех объектов стоимостных составляющих
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[CostComponent]</span>: Список объектов стоимостных составляющих типа GraphQL.


### Пример использования
```graphql
query{
  getAllCostComponents {
    rowId
    name
  }
}
```


## [getFactualWorks](factual_works.py) Получение объектов фактических работ по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">FactualWorkCollection</span>: Список объектов стоимостных составляющих типа GraphQL.


### Пример использования
```graphql
query{
  getFactualWorks(
    projectId: 773
    dateRange: {dateBegin: "2024-01-01"}
  ) {
    phases {
      rowId
      name
    }
    factualWorks {
      date
    }
  }
}
```


## [getAllGanttCharts](factual_works.py) Получение объектов фактических работ по идентификатору проекта
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[GanttChart]</span>: Список объектов диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getAllGanttCharts {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartByRowId](factual_works.py) Получение объектов фактических работ по идентификатору проекта
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор диаграммы.
### Возвращаемое значение
- <span style="color: orange;">GanttChart</span>: Объект диаграммы Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartByRowId(rowId: 10) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartsByProjectId](factual_works.py) Получение объектов диаграмм Гантта по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">project_ids</span> (default_value=None): Список идентификаторов проектов.
- <span style="color: orange;">with_dates</span> (default_value=False): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">without_check_permissions</span> (default_value=False): Флаг без проверки прав доступа.
- <span style="color: orange;">with_check_responsible</span> (default_value=False): Флаг получения диаграмм Гантта, в которых контрагент пользователя является ответственным за работы.
### Возвращаемое значение
- <span style="color: orange;">TList[GanttChart]</span>: Список объектов диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartsByProjectId(
    projectId: 10
  ) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    parentId
    haveChild
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartsByOrganizationId](factual_works.py) Получение объектов диаграмм Гантта по идентификатору организации
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">TList[GanttChart]</span>: Список объектов диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartsByOrganizationId(organizationId: 10) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartByOrgAndProjectId](factual_works.py) Получение объекта диаграммы Гантта по идентификатору проекта и организации
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">GanttChart</span>: Объект диаграммы Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartByOrgAndProjectId(projectId: 10, organizationId: 20) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartsByParentId](factual_works.py) Получение объектов диаграмм Гантта по идентификатору родительской диаграммы
### Аргументы
- <span style="color: orange;">parent_id</span> (обязательный): Идентификатор родительской диаграммы Гантта.
### Возвращаемое значение
- <span style="color: orange;">TList[GanttChart]</span>: Список объектов диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartsByParentId(parentId: 10) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getGanttChartByProjectOrgNames](factual_works.py) Получение объектов диаграмм Гантта по списку фильтров названий проектов и организаций
### Аргументы
- <span style="color: orange;">project_org_names_filters</span> (обязательный): Список фильтров по названиям проекта и организации типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[GanttChart]</span>: Список объектов диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  getGanttChartByProjectOrgNames(
    projectOrgNamesFilters: [
      { projectShortName: "string", organizationName: "string" }
    ]
  ) {
    rowId
    name
    planProjectTransactions {
      rowId
      name
    }
    factProjectTransactions {
      rowId
      name
    }
    actualProjectTransaction {
      rowId
      name
    }
    organization {
      rowId
    }
    project {
      rowId
      name
    }
  }
}
```


## [getMachineReports](machine.py) Получение всех объектов часов и машин по проекту в промежуток дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">MachineWorkHour</span>: Объект часов и машин типа GraphQL.


### Пример использования
```graphql
query{
  getMachineReports(projectId: 10, dateRange: {dateBegin: "2024-01-01"}) {
    projectId
    machineHour {
      projectId
    }
  }
}
```


## [getMachineRentReports](machine.py) Получение всех объектов часов и арендованных машин по проекту в промежуток дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">MachineRentWorkHour</span>: Объект часов и машин типа GraphQL.


### Пример использования
```graphql
query{
  getMachineRentReports(projectId: 10, dateRange: {dateBegin:"2024-01-01"}) {
    projectId
    machineHour {
      day
      totalHours
      machineClassifier
    }
  }
}
```


## [getMachineApplicationRentByProjectId](machine.py) Получение объектов техники по заявкам из 1С за диапазон дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">MachineWorkApplicationHour</span>: Объект часов и машин типа GraphQL.


### Пример использования
```graphql
query{
  getMachineApplicationRentByProjectId(
    projectId: 10
    dateRange: {dateBegin:"2024-01-01"}
  ) {
    projectId
    machineHour {
      rowId
    }
  }
}
```


## [getMaterialsByRowIds](material.py) Получение объектов материалов по списку идентификаторов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов материалов.
### Возвращаемое значение
- <span style="color: orange;">TList[Material]</span>: Список объектов материалов типа GraphQL.


### Пример использования
```graphql
query{
  getMaterialsByRowIds(rowIds: [10]) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
  }
}
```


## [getMaterialsByProjectId](material.py) Получение объектов материалов по идентификатору проекта
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов материалов.
- <span style="color: orange;">transaction_id</span> (default_value=None): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[Material]</span>: Список объектов материалов типа GraphQL.


### Пример использования
```graphql
query{
  getMaterialsByProjectId(projectId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
  }
}
```


## [getMaterialAssignsByProjectId](material_assign.py) Получение объектов связи материалов и операций проекта по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[MaterialAssign]</span>: Список объектов связи материалов и работ типа GraphQL.


### Пример использования
```graphql
query{
  getMaterialAssignsByProjectId(
    projectId: 10
  ) {
    rowId
    material {
      rowId
      name
    }
  }
}
```


## [getMaterialAssignsByWorkIds](material_assign.py) Получение объектов связей материалов с операциями по списку идентификаторов операций
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">TList[MaterialAssign]</span>: Список объектов связи материалов и работ типа GraphQL.


### Пример использования
```graphql
query{
  getMaterialAssignsByWorkIds(workIds: [10]) {
    rowId
    material {
      rowId
      name
    }
  }
}
```


## [getMaterialResourceAssignsByProjectResourceIds](material_resource_assign.py) Получение объекта транзакции и графика по идентификатору элемента
### Аргументы
- <span style="color: orange;">project_resource_ids</span> (обязательный): Список идентификаторов ресурсов.
### Возвращаемое значение
- <span style="color: orange;">TList[MaterialResourceAssign]</span>: Список объектов связи материалов и ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getMaterialResourceAssignsByProjectResourceIds(
    projectResourceIds: [10]
  ) {
    rowId
    material {
      rowId
      name
    }
  }
}
```


## [getTransactionAndChartByElementId](project_element.py) Получение объекта транзакции и графика по идентификатору элемента
### Аргументы
- <span style="color: orange;">project_element_id</span> (обязательный): Идентификатор элемента в базе.
### Возвращаемое значение
- <span style="color: orange;">TransactionAndChart</span>: Список объектов связи материалов и ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getTransactionAndChartByElementId(projectElementId: 10) {
    projectTransaction {
      rowId
      name
    }
    ganttChart {
      rowId
      name
    }
  }
}
```


## [getProjectElementsByTransactionId](project_element.py) Получение объектов элементов графика
### Аргументы
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">parent_id</span> (default_value=None): Идентификатор элемента в базе.
- <span style="color: orange;">for_root</span> (default_value=False): Флаг получения элементов графика для 1 уровня графика.
- <span style="color: orange;">with_dates</span> (default_value=True): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">with_work_links</span> (default_value=False): Флаг получения взаимосвязей операций.
- <span style="color: orange;">with_resource_assign</span> (default_value=False): Флаг получения связей ресурсов с работами.
- <span style="color: orange;">cost_component_codes</span> (default_value=[]): Список кодов стоимостных показателей.
- <span style="color: orange;">with_material_assigns</span> (default_value=False): Флаг получения с объектами связи материалов с операциями.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
- <span style="color: orange;">with_work_work_schedules</span> (default_value=False): Флаг получения календарей операций.
- <span style="color: orange;">with_project_phase_plans</span> (default_value=False): Флаг получения планов фаз.
- <span style="color: orange;">with_work_plans</span> (default_value=False): Флаг получения планов работ.
### Возвращаемое значение
- <span style="color: orange;">ScheduleElement</span>: Вспомогательный объект для объединения типов элемента графика и работы типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementsByTransactionId(
    transactionId: 10
  ) {
    works {
      rowId
      name
    }
    projectPhases {
      rowId
      name
    }
    costComponents {
      rowId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    workPlans {
      rowId
    }
    projectPhasePlans {
      rowId
    }
    error
  }
}
```


## [findProjectElements](project_element.py) Поиск объектов элементов графика по фазе
### Аргументы
- <span style="color: orange;">transaction_ids</span> (обязательный): Список идентификаторов транзакции.
- <span style="color: orange;">find_text</span> (обязательный): Текст для поиска.
- <span style="color: orange;">with_dates</span> (default_value=True): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">cost_component_codes</span> (default_value=[]): Список кодов стоимостных показателей.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
### Возвращаемое значение
- <span style="color: orange;">ScheduleElement</span>: Вспомогательный объект для объединения типов элемента графика и работы типа GraphQL.


### Пример использования
```graphql
query{
  findProjectElements(
    transactionIds: [10]
    findText: "string"
  ) {
    works {
      rowId
      name
    }
    projectPhases {
      rowId
      name
    }
    costComponents {
      rowId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    workPlans {
      rowId
    }
    projectPhasePlans {
      rowId
    }
    error
  }
}
```


## [getProjectElementsHierarchyByWorkId](project_element.py) Получение объектов иерархии родительских элементов для работы
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">with_dates</span> (default_value=False): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">with_work_links</span> (default_value=False): Флаг получения взаимосвязей операций.
- <span style="color: orange;">with_resource_assign</span> (default_value=False): Флаг получения связей ресурсов с работами.
- <span style="color: orange;">cost_component_codes</span> (default_value=[]): Список кодов стоимостных показателей.
- <span style="color: orange;">with_material_assigns</span> (default_value=False): Флаг получения с объектами связи материалов с операциями.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
- <span style="color: orange;">with_work_work_schedules</span> (default_value=False): Флаг получения календарей операций.
- <span style="color: orange;">with_project_phase_plans</span> (default_value=False): Флаг получения планов фаз.
- <span style="color: orange;">with_work_plans</span> (default_value=False): Флаг получения планов работ.
### Возвращаемое значение
- <span style="color: orange;">ScheduleElement</span>: Вспомогательный объект для объединения типов элемента графика и работы типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementsHierarchyByWorkId(
    workId: 773
    transactionId: 120
  ) {
    works {
      rowId
      name
    }
    projectPhases {
      rowId
      name
    }
    costComponents {
      rowId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    workPlans {
      rowId
    }
    projectPhasePlans {
      rowId
    }
    error
  }
}
```


## [getProjectElementsHierarchyByWorkIds](project_element.py) Получение объектов иерархии родительских элементов для списка работ
### Аргументы
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">phase_ids</span> (default_value=[]): Список идентификаторов фаз.
- <span style="color: orange;">work_ids</span> (default_value=[]): Список идентификаторов работ.
- <span style="color: orange;">with_dates</span> (default_value=False): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">with_work_links</span> (default_value=False): Флаг получения взаимосвязей операций.
- <span style="color: orange;">with_resource_assign</span> (default_value=False): Флаг получения связей ресурсов с работами.
- <span style="color: orange;">cost_component_codes</span> (default_value=[]): Список кодов стоимостных показателей.
- <span style="color: orange;">with_material_assigns</span> (default_value=False): Флаг получения с объектами связи материалов с операциями.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
- <span style="color: orange;">with_work_work_schedules</span> (default_value=False): Флаг получения календарей операций.
- <span style="color: orange;">with_project_phase_plans</span> (default_value=False): Флаг получения планов фаз.
- <span style="color: orange;">with_work_plans</span> (default_value=False): Флаг получения планов работ.
### Возвращаемое значение
- <span style="color: orange;">ScheduleElement</span>: Вспомогательный объект для объединения типов элемента графика и работы типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementsHierarchyByWorkIds(
    transactionId: 10
  ) {
    works {
      rowId
      name
    }
    projectPhases {
      rowId
      name
    }
    costComponents {
      rowId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    workPlans {
      rowId
    }
    projectPhasePlans {
      rowId
    }
    error
  }
}
```


## [findProjectElementsByFields](project_element.py) Поиск объектов элементов графика по полям элементов графика
### Аргументы
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">find_values</span> (обязательный): Список объектов обмена данными о фильтрации элементов графика при поиске по столбцам типа GraphQL.
    - <span style="color: orange;">find_text</span> (обязательный): Текст для поиска.
    - <span style="color: orange;">field_name</span> (обязательный): Наименование поля элемента графика.
- <span style="color: orange;">find_by_resources</span> (default_value=False): Флаг для поиска, включая поиск по ресурсам.
- <span style="color: orange;">find_by_materials</span> (default_value=False): Флаг для поиска, включая поиск по материалам.
- <span style="color: orange;">with_dates</span> (default_value=False): Флаг получения с макс и мин датами операций.
- <span style="color: orange;">with_work_links</span> (default_value=False): Флаг получения взаимосвязей операций.
- <span style="color: orange;">with_resource_assign</span> (default_value=False): Флаг получения связей ресурсов с работами.
- <span style="color: orange;">cost_component_codes</span> (default_value=[]): Список кодов стоимостных показателей.
- <span style="color: orange;">with_material_assigns</span> (default_value=False): Флаг получения с объектами связи материалов с операциями.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
- <span style="color: orange;">with_work_work_schedules</span> (default_value=False): Флаг получения календарей операций.
- <span style="color: orange;">with_project_phase_plans</span> (default_value=False): Флаг получения планов фаз.
- <span style="color: orange;">with_work_plans</span> (default_value=False): Флаг получения планов работ.
### Возвращаемое значение
- <span style="color: orange;">ScheduleElement</span>: Вспомогательный объект для объединения типов элемента графика и работы типа GraphQL.


### Пример использования
```graphql
query{
  findProjectElementsByFields(
    transactionId: 10
    findValues: [{ findText: "string", fieldName: NAME }]
  ) {
    works {
      rowId
      name
    }
    projectPhases {
      rowId
      name
    }
    costComponents {
      rowId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    workPlans {
      rowId
    }
    projectPhasePlans {
      rowId
    }
    error
  }
}
```


## [getProjectElementsByProjectObjectIdAndTransactionIds](project_element.py) Получение объектов элементов графика по списку идентификаторов транзакций и списку идентификаторов этапов (сводный график)
### Аргументы
- <span style="color: orange;">transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">project_object_ids</span> (обязательный): Список идентификаторов этапов проекта.
- <span style="color: orange;">with_work_links</span> (default_value=False): Флаг получения взаимосвязей операций.
- <span style="color: orange;">with_resource_assign</span> (default_value=False): Флаг получения связей ресурсов с работами.
- <span style="color: orange;">with_material_assigns</span> (default_value=False): Флаг получения с объектами связи материалов с операциями.
- <span style="color: orange;">with_fact_total_volume</span> (default_value=False): Флаг подсчета у фаз общего введенного объема по дочерним фактическим работам.
- <span style="color: orange;">with_work_work_schedules</span> (default_value=False): Флаг получения календарей операций.
### Возвращаемое значение
- <span style="color: orange;">ProjectObjectScheduleElement</span>: Вспомогательный объект для объединения типов элементов графиков по этапу типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementsByProjectObjectIdAndTransactionIds(
    transactionIds: [10]
    projectObjectIds: [10]
  ) {
    shortScheduleElements {
      projectObjectId
    }
    workLinks {
      rowId
    }
    resourceAssigns {
      rowId
    }
    materialAssigns {
      rowId
    }
    materialCosts {
      rowId
    }
    workWorkSchedules {
      workId
    }
    error
  }
}
```


## [getProjectElementAdditionalColumnValuesByTransactionId](project_element_additional_column_value.py) Получение объектов значений дополнительных столбцов графика по идентификатору транзакции
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectElementAdditionalColumnValue]</span>: Список объектов значений дополнительных столбцов графика типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementAdditionalColumnValuesByTransactionId(
    projectTransactionId: 10
  ) {
    rowId
    projectElementId
    projectElementAdditionalColumnId
    columnValue
  }
}
```


## [getProjectElementAdditionalColumnValuesByColumnId](project_element_additional_column_value.py) Получение объектов значений дополнительных столбцов графика по идентификатору дополнительного столбца 
### Аргументы
- <span style="color: orange;">column_id</span> (обязательный): Идентификатор дополнительного столбца графика.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectElementAdditionalColumnValue]</span>: Список объектов значений дополнительных столбцов графика типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementAdditionalColumnValuesByColumnId(columnId: 10) {
    rowId
    projectElementId
    projectElementAdditionalColumnId
    columnValue
  }
}
```


## [getProjectElementAdditionalColumnValuesByColumnId](project_element_cost.py) Получение объектов стоимостных составляющих элементов по проекту и транзакции 
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">cost_component_code</span> (default_value=None): Код компонента стоимости.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
- <span style="color: orange;">project_element_ids</span> (default_value=None): Список идентификаторов элементов графика.
- <span style="color: orange;">with_resources_costs</span> (default_value=False): Флаг учета стоимостей ресурсов в стоимостях операций.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectElementCost]</span>: Список объектов стоимостных составляющих типа GraphQL.


### Пример использования
```graphql
query{
  getProjectElementCostsByProjectId(
    projectId: 10
  ) {
    rowId
    projectElementId
    costComponentId
    totalVolume
    planVolume
    factVolume
    code
    costPerHour
    costPerUnitVolume
    costFixed
  }
}
```


## [getProjectPhasesByProjectId](project_phase.py) Получение объектов фаз по идентификатору проекта или транзакции 
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
- <span style="color: orange;">project_element_code</span> (default_value=None): Код элемента из SpiderProject.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectPhase]</span>: Список объектов фаз типа GraphQL.


### Пример использования
```graphql
query{
  getProjectPhasesByProjectId(
    projectId: 10
  ) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    responsible {
      responsibleId
    }
    factTotalVolume
  }
}
```


## [getProjectPhaseById](project_phase.py) Получение объекта фазы по идентификатору
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор элемента в базе.
### Возвращаемое значение
- <span style="color: orange;">ProjectPhase</span>: Объект фазы типа GraphQL.


### Пример использования
```graphql
query{
  getProjectPhaseById(rowId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    level
    responsible {
      responsibleId
    }
    factTotalVolume
  }
}
```


## [getRootPhasesByProjectTransactionId](project_phase.py) Получение объекта фазы по идентификатору
### Аргументы
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectPhase]</span>: Список объектов фаз типа GraphQL.


### Пример использования
```graphql
query{
  getRootPhasesByProjectTransactionId(projectTransactionId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    level
    responsible {
      responsibleId
    }
    factTotalVolume
  }
}
```


## [getProjectResourcesByProjectId](project_resource.py) Получение объектов ресурсов по идентификатору проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[ProjectResource]</span>: Список объектов ресурсов типа GraphQL.


### Пример использования
```graphql
query{
  getProjectResourcesByProjectId(
    projectId: 10
  ) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
    }
  }
}
```


## [getProjectResourceById](project_resource.py) Получение объекта ресурса по идентификатору
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор ресурса.
### Возвращаемое значение
- <span style="color: orange;">ProjectResource</span>: Объект ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getProjectResourceById(rowId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
  }
}
```


## [getResourceAssignByParentId](resource_assign.py) Получение объектов ресурсов по идентификатору работы
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
### Возвращаемое значение
- <span style="color: orange;">TList[ResourceAssign]</span>: Список объектов связи ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getResourceAssignByParentId(workId: 10) {
    rowId
    startDate
    finishDate
    parentId
    workId
    resourceId
    resource {
      rowId
      name
    }
    fact {
      rowId
    }
  }
}
```


## [getResourceAssignByParentIds](resource_assign.py) Получение объектов ресурсов по списку идентификаторов работ
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">TList[ResourceAssign]</span>: Список объектов связи ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getResourceAssignByParentIds(workIds: [10]) {
    rowId
    startDate
    finishDate
    parentId
    workId
    resourceId
    resource {
      rowId
      name
    }
    fact {
      rowId
    }
  }
}
```


## [getResourceAssignById](resource_assign.py) Получение объектов связей ресурса по идентификатору ресурса
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор ресурса.
### Возвращаемое значение
- <span style="color: orange;">ResourceAssign</span>: Объект связи ресурса типа GraphQL.


### Пример использования
```graphql
query{
  getResourceAssignById(rowId: 10) {
    rowId
    startDate
    finishDate
    parentId
    workId
    resourceId
    resource {
      rowId
      name
    }
    fact {
      rowId
    }
  }
}
```


## [getShiftWorks](shift_work.py) Получение объектов фактических работ и заданий для журнала сменных заданий
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">work_id</span> (default_value=None): Идентификатор работы, по которой надо получить фактические работы.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_classifier</span> (default_value=True): Флаг вывода работ из классификатора.
- <span style="color: orange;">date_job</span> (default_value=None): День, на который необходимо получить сменные задания.
- <span style="color: orange;">future_works_without_fact</span> (default_value=False): Флаг вывода работы из будущего, по которым не вводился факт.
### Возвращаемое значение
- <span style="color: orange;">ShiftJobLog</span>: Журнал сменных работ: список фактических работ, список сменных работ, список фаз.


### Пример использования
```graphql
query{
  getShiftWorks(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
  ) {
    factualWork {
      rowId
      name
    }
    shiftWork {
      rowId
      name
    }
    projectPhase {
      rowId
      name
    }
  }
}
```


## [getShiftWorksByProjectObjects](shift_work.py) Получение объектов фактических работ для журнала сменных работ по идентификаторам этапов проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">work_ids</span> (default_value=None): Список идентификаторов работ.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">project_object_ids</span> (default_value=None): Список идентификаторов этапов проекта.
- <span style="color: orange;">with_no_project_object</span> (default_value=False): Флаг включения в результат запроса работы, на которые не назначен этап проекта.
- <span style="color: orange;">with_factual_phases</span> (default_value=True): Флаг включения в результат запроса родительские фазы работ.
- <span style="color: orange;">with_hidden</span> (default_value=True): Флаг учтения скрытых работ.
- <span style="color: orange;">with_overdue</span> (default_value=None): Флаг учтения просроченных работ.
- <span style="color: orange;">with_date_section_works</span> (default_value=False): Флаг учтения работ за срез дат.
- <span style="color: orange;">shift</span> (default_value=False): Тип смены.
### Возвращаемое значение
- <span style="color: orange;">FactualShiftJobLog</span>: Журнал сменных работ: список фактических работ, список сменных работ, список фактических фаз.


### Пример использования
```graphql
query{
  getShiftWorksByProjectObjects(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
  ) {
    factualWorks {
      rowId
      name
    }
    shiftWorks {
      rowId
      name
    }
    factualPhases {
      rowId
      name
    }
  }
}
```


## [getShiftWorksByFilters](shift_work.py) Получение фактических работ для журнала сменных работ по фильтрам
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">work_ids</span> (default_value=None): Список идентификаторов работ.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_factual_phases</span> (default_value=True): Флаг включения в результат запроса родительские фазы работ.
- <span style="color: orange;">with_hidden</span> (default_value=True): Флаг учтения скрытых работ.
- <span style="color: orange;">with_overdue</span> (default_value=None): Флаг учтения просроченных работ.
- <span style="color: orange;">with_date_section_works</span> (default_value=False): Флаг учтения работ за срез дат.
- <span style="color: orange;">shift</span> (default_value=None): Тип смены.
- <span style="color: orange;">filters</span> (обязательный): Объект фильтров сменных заданий и фактических работ типа GraphQL.
- <span style="color: orange;">element_type</span> (default_value=None): Тип смены.
### Возвращаемое значение
- <span style="color: orange;">FactualShiftJobLog</span>: Журнал сменных работ: список фактических работ, список сменных работ, список фактических фаз.


### Пример использования
```graphql
query{
  getShiftWorksByFilters(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
    filters: {name: "string"}
  ) {
    factualWorks {
      rowId
      name
    }
    shiftWorks {
      rowId
      name
    }
    factualPhases {
      rowId
      name
    }
  }
}
```


## [getFactualProjectObjects](shift_work.py) Получение объектов фактических этапов по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_hidden</span> (default_value=False): Флаг учтения скрытых работ.
- <span style="color: orange;">with_overdue</span> (default_value=None): Флаг учтения просроченных работ.
- <span style="color: orange;">with_date_section_works</span> (default_value=False): Флаг учтения работ за срез дат.
### Возвращаемое значение
- <span style="color: orange;">TList[FactualProjectObject]</span>: Список объектов фактических этапов типа GraphQL.


### Пример использования
```graphql
query{
  getFactualProjectObjects(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
  ) {
    rowId
    name
  }
}
```


## [getShiftWorksByTimeResources](shift_work.py) Получение журнала сменных заданий по идентификаторам тайм-ресурсов
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">with_factual_phases</span> (default_value=True): Флаг включения в результат запроса родительские фазы работ.
- <span style="color: orange;">time_resource_ids</span> (обязательный): Список идентификаторов назначенных тайм-ресурсов.
### Возвращаемое значение
- <span style="color: orange;">FactualShiftJobLog</span>: Журнал сменных работ: список фактических работ, список сменных работ, список фактических фаз.


### Пример использования
```graphql
query{
  getShiftWorksByTimeResources(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 20
    timeResourceIds: [10]
  ) {
    factualWorks {
      rowId
      name
    }
    shiftWorks {
      rowId
      name
    }
    factualPhases {
      rowId
      name
    }
  }
}
```


## [getShiftWorksColumnValues](shift_work.py) Получение объекта значений полей сменных работ и работ
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">date_section</span> (default_value=None): Срез дат.
- <span style="color: orange;">columns</span> (обязательный): Список столбцов.
- <span style="color: orange;">with_date_section_works</span> (default_value=False): Флаг учтения работ за срез дат.
- <span style="color: orange;">with_overdue</span> (default_value=False): Флаг учтения просроченных работ.
- <span style="color: orange;">with_hidden</span> (default_value=False): Флаг учтения скрытых работ.
- <span style="color: orange;">shift</span> (default_value=None): Тип смены.
### Возвращаемое значение
- <span style="color: orange;">ShiftWorkColumnValues</span>: Объект значений полей сменных работ и работ типа GraphQL.


### Пример использования
```graphql
query{
  getShiftWorksColumnValues(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
    dateSection: {dateBegin: "2024-01-01"}
    columns: ["string"]
  ) {
    classifierCode
    issuerOfTaskName
    responsibleName
  }
}
```


## [checkWorksHaveShiftWorksInChildGanttOrgHierarchy](shift_work.py) Проверка наличия сменных работ в дочерних организациях иерархии диаграмм Гантта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">query_filter</span> (обязательный): Фильтр для запроса на проверку наличия сменных работ в дочерних организациях иерархии организаций диаграмм Гантта типа GraphQL.
    - <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
    - <span style="color: orange;">project_object_id</span> (обязательный): Идентификатор этапа проекта.
- <span style="color: orange;">source_organization_id</span> (обязательный): Идентификатор организации, для которой выполняется поиск.
### Возвращаемое значение
- <span style="color: orange;">ResultWorksHaveShiftWorksInChildsGanttOrgHierarchy</span>: Объект обмена данными о результатах проверки наличия сменных работ в дочерних организациях иерархии организаций диаграмм Гантта типа GraphQL.


### Пример использования
```graphql
query{
  checkWorksHaveShiftWorksInChildGanttOrgHierarchy(
    projectId: 10
    queryFilter: [{workId: 30 projectObjectId: 30}]
    sourceOrganizationId: 10
  ) {
    worksData {
      sourceWorkId
      foundedWorkIds
    }
    errMsg
  }
}
```


## [getShiftWorkMachineResourcesByDate](shift_work_machine_resource.py) Получение объектов связей ресурсов машин и фактов по сменным работам по промежутку дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[ShiftWorkMachineResource]</span>: Список объектов связей ресурсов машин и фактов по сменным работам типа GraphQL.


### Пример использования
```graphql
query{
  getShiftWorkMachineResourcesByDate(projectId: 10, dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}) {
    rowId
    shiftWorkId
    machineResourceId
    hours
  }
}
```


## [getShiftWorkRentMachineByDate](shift_work_rent_machine.py) Получение связей арендованных машин и фактов по сменным работам по промежутку дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[ShiftWorkRentMachine]</span>: Список объектов связей арендованных машин и фактов по сменным работам типа GraphQL.


### Пример использования
```graphql
query{
  getShiftWorkRentMachineByDate(projectId: 10, dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}) {
    rowId
    shiftWorkId
    machineApplicationId
    hours
    amount
  }
}
```


## [getShiftWorkTimeResourceHierarchy](shift_work_time_resource_hierarchy.py) Получение объектов иерархии тайм-ресурсов, назначенных на сменные работы
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">with_positions</span> (default_value=False): Флаг группировки по должностям.
- <span style="color: orange;">with_previous_days</span> (default_value=False): Флаг включения часы по предыдущим 3 дням.
- <span style="color: orange;">shift_type</span> (default_value=None): Тип смены.
- <span style="color: orange;">shift_work_id</span> (default_value=None): Идентификатор сменной работы.
### Возвращаемое значение
- <span style="color: orange;">ShiftWorkTimeResourceHierarchyLog</span>: Объект элементы иерархии тайм-ресурсов, назначенных на сменные работы типа GraphQL.


### Пример использования
```graphql
query{
  getShiftWorkTimeResourceHierarchy(
    projectId: 10
    dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}
    projectTransactionId: 10
  ) {
    workerElements {
      rowId
    }
    tagElements {
      rowId
    }
    organizationElements {
      rowId
    }
    positionElements {
      rowId
    }
    positionGroupElements {
      rowId
    }
    affiliationGroupElements {
      rowId
    }
    assignGroupElements {
      rowId
    }
  }
}
```


## [getWorkById](work.py) Получение работы по идентификатору
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
### Возвращаемое значение
- <span style="color: orange;">Work</span>: Объект работы типа GraphQL.


### Пример использования
```graphql
query{
  getWorkById(workId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    responsibleForWork {
      responsibleId
    }
    workFact {
      rowId
    }
  }
}
```


## [getWorkByIds](work.py) Получение работ по идентификаторам
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">TList[Work]</span>: Список объектов работ типа GraphQL.


### Пример использования
```graphql
query{
  getWorksByIds(workIds: [10]) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    responsibleForWork {
      responsibleId
    }
    workFact {
      rowId
    }
  }
}
```


## [getWorksByProjectId](work.py) Получение объектов работы по идентификатору проекта
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
- <span style="color: orange;">with_duration</span> (default_value=False): Флаг получения с длительностью.
### Возвращаемое значение
- <span style="color: orange;">TList[Work]</span>: Список объектов работ типа GraphQL.


### Пример использования
```graphql
query{
  getWorksByProjectId(projectId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    responsibleForWork {
      responsibleId
    }
    workFact {
      rowId
    }
  }
}
```


## [getWorksByParentId](work.py) Получение работы по идентификатору родителя(фазы)
### Аргументы
- <span style="color: orange;">phase_id</span> (обязательный): Идентификатор фазы.
### Возвращаемое значение
- <span style="color: orange;">TList[Work]</span>: Список объектов работ типа GraphQL.


### Пример использования
```graphql
query{
  getWorksByParentId(phaseId: 10) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    responsibleForWork {
      responsibleId
    }
    workFact {
      rowId
    }
  }
}
```


## [getWorksByRange](work.py) Получение работы в промежутке заданных дат
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">project_transaction_id</span> (default_value=None): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[Work]</span>: Список объектов работ типа GraphQL.


### Пример использования
```graphql
query{
  getWorksByRange(projectId: 10 dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"}) {
    rowId
    name
    project {
      rowId
      name
    }
    projectObject {
      rowId
      name
    }
    resourceAssigns {
      rowId
    }
    responsibleForWork {
      responsibleId
    }
    workFact {
      rowId
    }
  }
}
```


## [getTasksByWorkId](work.py) Получение задач, на которые назначена работа
### Аргументы
- <span style="color: orange;">work_id</span> (обязательный): Идентификатор работы.
### Возвращаемое значение
- <span style="color: orange;">TList[Task]</span>: Список объектов задач типа GraphQL.


### Пример использования
```graphql
query{
  getTasksByWorkId(workId: 10) {
    id
    name
    files {
      name
      id
    }
  }
}
```


## [trafficLightWorks](work.py) Получение светофорного отчета по диапазону дат
### Аргументы
- <span style="color: orange;">pass_to_pdf</span> (обязательный): Светофорный отчет в pdf или xlsx.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (default_value=None): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">String</span>: Ключ временного файла.


### Пример использования
```graphql
query{
  trafficLightWorks(passToPdf: true, dateRange: {dateBegin: "2024-01-01" dateFinish: "2025-01-01"})
}
```


## [getEffectiveSolutionData](work.py) Получение объекта данных библиотеки эффективных решений
### Аргументы
- <span style="color: orange;">project_ids</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">organization_ids</span> (default_value=None): Идентификатор организации.
- <span style="color: orange;">date_range</span> (default_value=None): Промежуток дат.
### Возвращаемое значение
- <span style="color: orange;">TList[SolutionLibraryConstructive]</span>: Список объектов элементов таблицы типа GraphQL.


### Пример использования
```graphql
query{
  getEffectiveSolutionData(
    projectIds: 10
  ) {
    organizationName
    projectName
    region
    constructiveName
    elements {
      workName
    }
  }
}
```


## [dataFromTrafficLightReport](work.py) Получение объекта данных из светофорного отчета для создания таблицы
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TrafficLightData</span>: Объект данных светофора типа GraphQL.


### Пример использования
```graphql
query{
  dataFromTrafficLightReport(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2024-02-01"}
    inputs: {projectId: 10 projectTransactionId: 20 organizationId: 10}
  ) {
    trafficLightWork {
      rowId
    }
    trafficLightTimeResource {
      name
    }
    trafficLightMachineResource {
      classificatorModel
    }
    totalOrganizationsPhysicalVolumes {
      rowId
    }
    errorMsg
  }
}
```


## [getSummaryTimeResourcesForTrafficLight](work.py) Получение списка объектов тайм-ресурсов из светофорного отчета для создания таблицы
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[TrafficLightTimeResource]</span>: Список объектов человеческих ресурсов из светофорного отчета типа GraphQL.


### Пример использования
```graphql
query{
  getSummaryTimeResourcesForTrafficLight(dateRange: {dateBegin:"2024-01-01" dateFinish:"2025-01-01"}, inputs: [{projectId: 10 projectTransactionId: 20 organizationId: 10}]) {
    name
    resourcesQuantity {
      day
    }
    completedToStartDateRange
    monthsVolume {
      month
      volume
    }
    monthCompleted {
      planVolume
      factVolume
    }
    monthRemainder {
      planVolume
      factVolume
    }
  }
}
```


## [getTotalOrganizationsPhysicalVolumesFromTrafficLight](work.py) Получение объекта данных итоговых значений ресурсов из светофорного отчета для создания таблицы
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[TotalOrganizationsPhysicalVolumes]</span>: Список объектов итоговых значений ресурсов из светофорного отчета типа GraphQL.


### Пример использования
```graphql
query{
  getTotalOrganizationsPhysicalVolumesFromTrafficLight(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2025-01-01"}
    inputs: [{projectId: 10 projectTransactionId: 20 organizationId: 10}]
  ) {
    rowId
    daysVolume {
      day
    }
    monthlyPlan
    currentDateVolumes {
      planVolume
      factVolume
    }
    organizationsPhysicalVolumes {
      organization
    }
  }
}
```


## [getTotalWorkFromTrafficLight](work.py) Получение объекта данных из светофорного отчета для создания таблицы
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TrafficlightWorksData</span>: Объект обмена данными о работах светофора типа GraphQL.


### Пример использования
```graphql
query{
  getTotalWorkFromTrafficLight(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2025-01-01"}
    inputs: [{projectId: 10 projectTransactionId: 20 organizationId: 10}]
   ) {
    trafficLightWorks {
      rowId
      workId
    }
    errMsg
  }
}
```


## [checkProjectTransactionsByWorks](work.py) Получение объектов транзакции на наличие работ с классификатором по ним
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат.
- <span style="color: orange;">inputs</span> (обязательный): Объект обмена данными для ввода организации и версии графика светофора типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">TList[Key]</span>: Список объектов транзакции типа GraphQL.


### Пример использования
```graphql
query{
  checkProjectTransactionsByWorks(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2025-01-01"}
    inputs: [{projectId: 10 projectTransactionId: 20 organizationId: 10}]
   )
}
```


## [getWorkLinksByProjectId](work_link.py) Получение объектов взаимосвязей операций по идентификатору проекта или транзакции
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkLink]</span>: Список объектов взаимосвязей операций типа GraphQL.


### Пример использования
```graphql
query{
  getWorkLinksByProjectId(projectId: 10) {
    rowId
    projectId
    projectTransactionId
    previousWorkId
    nextWorkId
    workLinkType
    workLinkDelay
    workLinkDelayType
    workScheduleId
  }
}
```


## [getWorksCriticalPath](work_link.py) Получение критического пути операций
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_transaction_id</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">find_by_key_volume_works</span> (default_value=False): Флаг поиска только по ключевым операциям.
### Возвращаемое значение
- <span style="color: orange;">CriticalPathInfo</span>: Список объектов работ кратчайшего пути типа GraphQL.


### Пример использования
```graphql
query{
  getWorksCriticalPath(
    projectId: 10
    projectTransactionId: 10
  ) {
    works {
      rowId
      name
    }
    phasesIds
    errMsg
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями ролей

## [CreateRole](role_create.py) Класс мутации на создание роли
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании роли типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">role</span>: Сущность роли.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createRole(createInput: {}) {
    role {
      rowId
      name
    }
    okStatus
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями ролей

## [DeleteRole](role_delete.py) Класс мутации на удаление роли
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор роли.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  deleteRole(rowId: 10) {
    okStatus
    errMsg
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями ролей

## [UpdateRole](role_update.py) Класс мутации на обновление роли
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор роли.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении роли типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">role</span>: Сущность роли.
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">err_msg</span>: Текст ошибки.


### Пример использования
```graphql
mutation {
  updateRole(rowId: 10, updateInput: {name:"string"}) {
    role {
      rowId
      name
    }
    okStatus
    errMsg
  }
}
```


## [BatchUpdateRolesScenarios](role_update.py) Класс мутации на массовое обновление сценариев для ролей
### Аргументы
- <span style="color: orange;">roles_ids</span> (обязательный): Список идентификаторов ролей.
- <span style="color: orange;">scenarios_ids</span> (обязательный): Список идентификаторов сценариев.
- <span style="color: orange;">with_delete</span> (default_value=False): Флаг удаления сценариев для ролей.
### Возвращаемое значение
- <span style="color: orange;">project_roles</span>: Список сущностей ролей.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  batchUpdateRolesScenarios(
    rolesIds: [10]
    scenariosIds: [10]
    withDelete: false
  ) {
    projectRoles {
      rowId
      name
    }
    okStatus
  }
}
```


# Модуль запросов для взаимодействия с сущностями ролей

## [GetNorms](role.py) Получение норм
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[Role]</span>: Список ролей.


### Пример использования
```graphql 
query {
  getAllRoles {
    rowId
    name
    scenarios {
      name
      rowId
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями доступного времени

## [getAvailableForInspectionDays](available_time.py) Получение свободных дней для инспекций
### Аргументы
- <span style="color: orange;">contragent_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">TList(Date)</span>: Список дат.


### Пример использования
```graphql
query {
  getAvailableForInspectionDays(contragentId: 10, labOrGeoRequired: true)
}
```


## [getAvailableForInspectionTime](available_time.py) Получение инспекции для выбора доступных времен подачи заявки на инспекцию
### Аргументы
- <span style="color: orange;">day</span> (обязательный): Дата.
- <span style="color: orange;">contragent_id</span> (обязательный): Идентификатор контрагента.
### Возвращаемое значение
- <span style="color: orange;">TList(Date)</span>: Список дат.


### Пример использования
```graphql
query {
  getAvailableForInspectionTime(day: "2024-01-01", contragentId: 10) {
    timeBegin
    timeFinish
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями видео-инструкций

## [CreateVideoInstruction](video_instruction_creator.py) Класс мутации на создание видео-инструкции
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании видео-инструкции типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Название видео-инструкции.
    - <span style="color: orange;">duration</span> (обязательный): Продолжительность видео-инструкции.
- <span style="color: orange;">content</span> (default_value=None): Видео-файл.
- <span style="color: orange;">img_content</span> (default_value=None): Файл изображения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">video_instruction</span>: Объект видео-инструкции типа GraphQL.


### Пример использования
```graphql
mutation {
  createVideoInstruction(
    input: { name: "string" duration: 180 }
  ) {
    ok
    videoInstruction {
      rowId
      name
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями видео-инструкций

## [DeleteVideoInstruction](video_instruction_delete.py) Класс мутации на удаление видео-инструкции
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор видео-инструкции.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteVideoInstruction(rowId: 10) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями видео-инструкций

## [UpdateVideoInstruction](video_instruction_update.py) Класс мутации на обновление видео-инструкции
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор видео-инструкции.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении видео-инструкции типа GraphQL.
- <span style="color: orange;">content</span> (default_value=None): Видео-файл.
- <span style="color: orange;">img_content</span> (default_value=None): Файл изображения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">video_instruction</span>: Объект видео-инструкции типа GraphQL.


### Пример использования
```graphql
mutation {
  updateVideoInstruction(
    input: { name:"string" duration: 180 }
    rowId: 10
  ) {
    ok
    videoInstruction {
      rowId
      name
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями видео-инструкции

## [getVideoInstructionById](video_instruction.py) Получение видео инструкций по списку идентификаторов
### Аргументы
- <span style="color: orange;">row_ids</span> (обязательный): Список идентификаторов видео-инструкций.
### Возвращаемое значение
- <span style="color: orange;">TList[VideoInstruction]</span>: Список объектов видео-инструкций типа GraphQL.


### Пример использования
```graphql 
query {
  getVideoInstructionById(rowIds: [10]) {
    rowId
    name
    document {
      id
      name
    }
    image {
      id
      name
    }
  }
}
```


## [getAllVideoInstructions](video_instruction.py) Получение всех видео-инструкций
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[VideoInstruction]</span>: Список объектов видео-инструкций типа GraphQL.


### Пример использования
```graphql 
query {
  getAllVideoInstructions {
    rowId
    name
    document {
      id
      name
    }
    image {
      id
      name
    }
  }
}
```


# Модуль мутаций для взаимодействия с сущностями отчетов по дням

## [SetAdjustHoursMutation](day_worker_report.py) Класс мутации на изменение часов работника
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об изменении часов работнику типа GraphQL.
- <span style="color: orange;">pair</span> (обязательный): Объект обмена данными об идентификации рабочих часов. Составной ключ временной ресурс - день типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">input_errors</span>: Ошибки вводных данных
- <span style="color: orange;">result</span>: Результат для данного дня тайм-ресурса
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql 
mutation {
  setAdjustHours(input: {adjustHours:8}, pair: {timeResourceId:10 day:"2024-01-01"}) {
    inputErrors {
      dayHoursError
    }
    result
    ok
  }
}
```


## [BatchSetAdjustHoursMutation](day_worker_report.py) Класс мутации на массовое изменение часов работникам
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Список объектов обмена данными об изменении часов работникам типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">input_errors</span>: Ошибки вводных данных
- <span style="color: orange;">result</span>: Результат для данного дня тайм-ресурса
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  batchSetAdjustHours(input: [{setAdjustHours:{adjustHours:8} timeResourceDayPair:{timeResourceId:10 day:"2024-01-01"}}]) {
    inputErrors {
      dayHoursError
    }
    result {
      timeResourceId
      day
      result
    }
    ok
  }
}
```


## [MarkVisitWorkMutation](day_worker_report.py) Класс мутации на создание отметки о приходе рабочего на рабочее место
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции
- <span style="color: orange;">result</span>: Результат для данного дня тайм-ресурса
- <span style="color: orange;">day_report</span>: Список дневных отчетов работников


### Пример использования
```graphql
mutation {
  markVisitWorkMutation(
    workerId: 10, projectId: 10
  ) {
    ok
    result
    dayReport {
      rowId
      factHours
      isAdjusted
      adjustHours
      factNightHours
      adjustedNightHours
      isVisible
      status
      timeResourceId
      workerId
      day
      comment
      tsBegin
      tsFinish
      tagId
      previewHours
    }
  }
}
```


## [MarkLeaveWorkMutation](day_worker_report.py) Класс мутации на создание отметки об окончании рабочего дня
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции
- <span style="color: orange;">result</span>: Результат для данного дня тайм-ресурса
- <span style="color: orange;">day_report</span>: Список дневных отчетов работников


### Пример использования
```graphql
mutation {
  markLeaveWorkMutation(
    workerId: 10, projectId: 10
  ) {
    ok
    result
    dayReport {
      rowId
      factHours
      isAdjusted
      adjustHours
      factNightHours
      adjustedNightHours
      isVisible
      status
      timeResourceId
      workerId
      day
      comment
      tsBegin
      tsFinish
      tagId
      previewHours
    }
  }
}
```


## [MoveDayReportToTagMutation](day_worker_report.py) Класс мутации на перемещение дневного отчета в другой тэг (группу)
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о перемещении дневного отчета между тэгами (группами) типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  moveDayReportToTagMutation(input: {dayReportId: 10 tagId: 10}) {
    ok
  }
}
```


## [DayReportChangeProjectMutation](day_worker_report.py) Класс мутации на перемещение дневных отчетов из проекта в проект
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор работника.
- <span style="color: orange;">old_project_id</span> (обязательный): Идентификатор проекта, откуда перемещать дневные отчета.
- <span style="color: orange;">new_project_id</span> (обязательный): Идентификатор проекта, куда перемещать дневные отчеты.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  dayReportChangeProject(
    dateRange:{dateBegin:"2024-01-01" dateFinish:"2024-02-01"}
    newProjectId: 20
    oldProjectId: 10
    workerId: 10
  ) {
    ok
    result
    dayReport {
      rowId
      factHours
      isAdjusted
      adjustHours
      factNightHours
      adjustedNightHours
      isVisible
      status
      timeResourceId
      workerId
      day
      comment
      tsBegin
      tsFinish
      tagId
      previewHours
    }
  }
}
```


# Модуль мутаций для взаимодействия с сущностями отметок о рабочем дне


## [BatchCreatePACSWorkMarkMutation](work_mark.py) Класс мутации на массовое создание списка отметок о рабочем дне из СКУД систем
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов данных о рабочем дне из СКУД системы типа GraphQL.
- <span style="color: orange;">user_id</span> (обязательный): Идентификатор пользователя.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  batchCreatePacsWorkMarks(
    inputs: [
      {
        createdAt: "2024-01-01T12:00:00+05:00"
        timeResourceId: { workerId: 10, projectId: 20, timeResourceId: 10 }
        regId: 10
        breathalyzerResult: 0.0
      }
    ]
  ) {
    ok
  }
}
```


## [CreateShiftEnd](work_mark.py) Класс мутации на создании отметки об окончании вахты типа GraphQL
### Аргументы
- <span style="color: orange;">worker_id</span> (обязательный): Идентификатор сущности работника.
- <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор временного ресурса (тайм-ресурса).
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  createShiftEnd(timeResourceId: 10, workerId: 10) {
    ok
  }
}
```


## [WorkMarkSpoof](work_mark.py) Класс мутации на установку флага спуфа отметок типа GraphQL
### Аргументы
- <span style="color: orange;">work_mark_ids</span> (обязательный): Cписок идентификаторов отметок.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  workMarkSpoof(workMarkIds: [10]) {
    ok
  }
}
```


## [WorkMarkSpoofDayChecker](work_mark.py) Класс мутации на проверку изображений в течении выбранного промежутка времени на спуф типа GraphQL
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат, в котором искать отметки.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции


### Пример использования
```graphql
mutation {
  workMarkSpoofDayChecker(dateRange: {dateBegin:"2024-01-01" dateFinish:"2024-01-02"}) {
    ok
  }
}
```


# Модуль запросов для взаимодействия с сущностями отчетов по дням

## [getWorkersHours](day_worker_report.py) Получение всех итоговых часов работников
### Аргументы
- <span style="color: orange;">filter</span> (обязательный): Параметры фильтрации для получения часов работников.
### Возвращаемое значение
- <span style="color: orange;">TotalWorkReports</span>: Количество итоговых часов


### Пример использования
```graphql 
query {
  getWorkersHours(
    filter: { dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" } }
  ) {
    totalHours
    hoursRanges {
      totalHours
      timeResourceId
      workerId
      isActive
    }
  }
}
```


## [workHoursReport1c](day_worker_report.py) Получение отчета по часам работников в формате 1с
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для получения данных.
### Возвращаемое значение
- <span style="color: orange;">WorkerHoursReport1c</span>: Идентификатор для скачивания отчета


### Пример использования
```graphql 
query {
  workHoursReport1c(
    filter: {
      timeResourceIds: 10
      dateBeginGte: "2024-01-01"
      dateEndLte: "2024-02-01"
    }
  ) {
    ref
    errMsg
  }
}
```


## [form15201cDataDump](day_worker_report.py) Генерация и отправка отчета по часам работников в 1с
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">organization_unit_id</span> (обязательный): Идентификатор подразделения.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для отчета.
### Возвращаемое значение
- <span style="color: orange;">WorkerHours1cResponse</span>: Ответ от 1с


### Пример использования
```graphql 
query {
  form15201cDataDump(
    organizationId: 10
    organizationUnitId: 20
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    timeResourceIds: [10]
  ) {
    ref
  }
}
```


## [anotherWorkHoursReport1c](day_worker_report.py) Генерация и отправка отчета для аванса по работникам в формате 1с
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для отчета.
### Возвращаемое значение
- <span style="color: orange;">WorkerHoursReport1c</span>: Идентификатор для скачивания отчета


### Пример использования
```graphql 
query {
  anotherWorkHoursReport1c(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2024-02-01"}
    organizationId: 10
    blankToDayOff: false
    projectIds: [10]
  ) {
    ref
    errMsg
  }
}
```


## [workHoursReport1cV2](day_worker_report.py) Генерация и отправка отчета по часам работников в формате 1с
### Аргументы
- <span style="color: orange;">filter</span> (обязательный): Параметры фильтрации.
### Возвращаемое значение
- <span style="color: orange;">WorkerHoursReport1c</span>: Идентификатор для скачивания отчета


### Пример использования
```graphql 
query {
  workHoursReport1cV2(
    filter: {
      timeResourceIds: [20561]
      dateBeginGte: "2024-01-01"
      dateEndLte: "2024-02-01"
    }
    excelFile1c: "file.xls"
    fullFio: true
    blankToDayOff: true
    downloadFactHours: false
    downloadNightHours: false
    downloadDayNightHours: false
    downloadHoursByCalendarDays: false
  ) {
    ref
    errMsg
  }
}
```


## [anotherWorkHoursReport1cV2](day_worker_report.py) Генерация и отправка отчета для аванса по работникам в формате 1с
### Аргументы
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для отчета.
### Возвращаемое значение
- <span style="color: orange;">WorkerHoursReport1c</span>: Идентификатор для скачивания отчета


### Пример использования
```graphql 
query {
  anotherWorkHoursReport1cV2(
    dateRange: {dateBegin:"2024-01-01" dateFinish:"2024-02-01"}
    organizationId: 10
    fullFio: true
    blankToDayOff: true
    downloadFactHours: false
    projectIds: [10]
  ) {
    ref
    errMsg
  }
}
```


## [getDayReportsByTimeResources](day_worker_report.py) Получение часов временных ресурсов в промежутке дат
### Аргументы
- <span style="color: orange;">time_resource_ids</span> (обязательный): Список идентификаторов по которым надо получить отчеты.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для отчета.
### Возвращаемое значение
- <span style="color: orange;">TList[DayReport]</span>: Список часов


### Пример использования
```graphql 
query {
  getDayReportsByTimeResources(
    timeResourceIds: [10]
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    onlyLast: true
  ) {
    rowId
    factHours
    isAdjusted
    adjustHours
    factNightHours
    adjustedNightHours
    isVisible
    status
    timeResourceId
    workerId
    worker {
      rowId
      firstName
      surname
      lastName
      tableNumber
    }
    day
    comment
    tsBegin
    tsFinish
    tagId
    previewHours
  }
}
```


## [getDayReportsCoordsByProjectId](day_worker_report.py) Получение дневных отчетов у которых есть координаты по проекту за выбранный период времени
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">date_range</span> (обязательный): Промежуток дат для отчета.
### Возвращаемое значение
- <span style="color: orange;">TotalHours</span>: Отчет


### Пример использования
```graphql 
query {
  getDayReportsCoordsByProjectId(projectId: 1, dateRange: {dateBegin:"2024-01-01" dateFinish:"2024-02-01"}) {
    totalHours
    hoursRanges {
      totalHours
      timeResourceId
      workerId
      isActive
    }
  }
}
```


# Модуль запросов для взаимодействия с линейными ИТР


## [checkExistsItrByProjectIds](linear_itr.py) Проверка существования линейных ИТР по идентификаторам проектов
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">TList[LinearITRCheck]</span>: Список объектов проверки существования линейных ИТР по проектам


### Пример использования
```graphql 
query {
  checkExistsItrByProjectIds(projectIds: [1], checkDate: "2024-01-01") {
    projectId
    checkExist
  }
}
```


## [getLinearItrByProjectId](linear_itr.py) Получение линейных ИТР по проекту
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">project_id</span> (обязательный): Список идентификаторов проектов, среди которых идет поиск линейных ИТР.
### Возвращаемое значение
- <span style="color: orange;">TList[LinearITR]</span>: Список линейных ИТР по проекту


### Пример использования
```graphql 
query {
  getLinearItrByProjectId(
    projectId: 1
    withoutComparedProjectIds: [10]
    checkDate: "2024-01-01"
  ) {
    worker {
      rowId
      firstName
      surname
      lastName
      tableNumber
    }
    contragent {
      rowId
      name
    }
    dayReport {
      rowId
      factHours
      isAdjusted
    }
    user {
      rowId
      username
      email
    }
  }
}
```


# Модуль запросов для взаимодействия с отчетами по табелю проекта и организации


## [getProjectOrganizationDayReport](linear_itr.py) Получение отчета по табелю проекта и организации
### Аргументы
- <span style="color: orange;">project_ids</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">date_range</span> (обязательный): Временной промежуток.
### Возвращаемое значение
- <span style="color: orange;">ProjectOrganizationDayReportElement</span>: Объект обмена данными о выгрузки отчета по табелю проекта и организации типа GraphQL


### Пример использования
```graphql 
query {
  getProjectOrganizationDayReport(
    projectIds: [1]
    dateRange: { dateBegin: "2024-01-01", dateFinish: "2024-02-01" }
    organizationIds: [10]
  ) {
    keyFile
    errMsg
  }
}
```


# Модуль запросов для взаимодействия с рабочим календарем


## [getProjectCalendar](linear_itr.py) Получение календаря по проекту
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Optional[WorkCalendar]</span>: Рабочий календарь


### Пример использования
```graphql 
query {
  getProjectCalendar {
    rules {
      timeBegin
      timeEnd
      ruleType
      minActivityLevel
    }
    name
    projectId
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями календарей

## [parseWorkScheduleShiftDaysCut](work_schedule_shift_day_cut_common.py) Класс мутации на парсинг файла с ограничениями вахтового рабочего календаря
### Аргументы
- <span style="color: orange;">input_file</span> (обязательный): Файл содержащий данные об ограничениях вахтового календаря.
- <span style="color: orange;">work_schedule_shift_id</span> (обязательный): Идентификатор календаря.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_days_cuts</span>: Объект ограничения вахтового календаря типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseWorkScheduleShiftDaysCut(
    inputFile: "file.xlsx"
    workScheduleShiftId: 10
  ) {
    workScheduleDaysCuts {
      rowId
      day
      hours
      workScheduleShiftId
    }
    ok
  }
}
```


# Модуль мутаций создания для взаимодействия с сущностями календарей

## [CreateWorkDaySchedule](work_day_schedule_create.py) Класс мутации на создание рабочего дня календаря
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании рабочего дня типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование рабочего дня.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_day_schedule</span>: Объект рабочего дня календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  createWorkDaySchedule(input: { name: "string" }) {
    ok
    workDaySchedule {
      rowId
      name
    }
  }
}
```


## [CreateWorkPeriods](work_period_create.py) Класс мутации на создание периода рабочего дня
### Аргументы
- <span style="color: orange;">inputs</span> (обязательный): Список объектов обмена данными о создании рабочих периодов типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_periods</span>: Список объектов отрезков времени Обед/Работа.


### Пример использования
```graphql
mutation {
  createWorkPeriods(inputs: [{ workPeriodType: WORK serialNumber: 10 begin: "10:00:00" finish: "20:00:00" }]) {
    ok
    workPeriods {
      rowId
    }
  }
}
```


## [CreateWorkScheduleProjectAssign](work_schedule_assignment_create.py) Класс мутации на назначение рабочего календаря для проекта
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">is_default</span> (default_value=False): Флаг основного календаря.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_assign</span>: Объект связи календаря с элементом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleProjectAssign(
    isDefault: false
    projectId: 10
    workScheduleId: 10
  ) {
    workScheduleAssign {
      elementId
    }
    ok
  }
}
```


## [CreateWorkScheduleOrganizationAssign](work_schedule_assignment_create.py) Класс мутации на назначение рабочего календаря организации
### Аргументы
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">is_default</span> (default_value=False): Флаг основного календаря.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_assign</span>: Объект связи календаря с элементом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleOrganizationAssign(
    isDefault: false
    organizationId: 10
    projectId: 20
    workScheduleId: 10
  ) {
    workScheduleAssign {
      elementId
    }
    ok
  }
}
```


## [CreateWorkScheduleTimeResourceAssign](work_schedule_assignment_create.py) Класс мутации на назначение рабочего календаря тайм-ресурсу
### Аргументы
- <span style="color: orange;">time_resource_ids</span> (обязательный): Список идентификаторов тайм-ресурсов.
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_assign</span>: Объект связи календаря с элементом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleTimeResourceAssign(
    timeResourceIds: [10]
    workScheduleId: 10
  ) {
    workScheduleAssigns {
      elementId
    }
    ok
  }
}
```


## [CreateWorkScheduleResourceAssign](work_schedule_assignment_create.py) Класс мутации на назначение рабочего календаря ресурсу
### Аргументы
- <span style="color: orange;">time_resource_ids</span> (обязательный): Список идентификаторов тайм-ресурсов.
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_assigns</span>: Список объектов связи календаря с элементом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleResourceAssign(
    resourceIds: [10]
    workScheduleId: 10
  ) {
    workScheduleAssigns {
      elementId
    }
    ok
  }
}
```


## [CreateWorkScheduleWorkAssign](work_schedule_assignment_create.py) Класс мутации на назначение рабочего календаря списку работ
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_assigns</span>: Список объектов связи календаря с элементом типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleWorkAssign(workIds: [10], workScheduleId: 10) {
    workScheduleAssigns {
      elementId
    }
    ok
  }
}
```


## [CreateWorkScheduleCommon](work_schedule_common_create.py) Класс мутации на создание обычного календаря
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Список идентификаторов работ.
    - <span style="color: orange;">name</span> (обязательный): Наименование календаря.
    - <span style="color: orange;">work_schedule_type</span> (обязательный): Тип календаря.
    - <span style="color: orange;">using_in_month_table</span> (default_value=False): Флаг использования календаря в табеле.
### Возвращаемое значение
- <span style="color: orange;">work_schedule</span>: Объект обычного рабочего календаря типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleCommon(
    createInput: { name: "string", workScheduleType: COMMON }
    organizationId: 10
  ) {
    workSchedule {
      rowId
      name
    }
    okStatus
  }
}
```


## [CreateWorkScheduleShift](work_schedule_shift_create.py) Класс мутации на создание вахтового рабочего календаря
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Список идентификаторов работ.
    - <span style="color: orange;">name</span> (обязательный): Наименование календаря.
    - <span style="color: orange;">work_schedule_type</span> (обязательный): Тип календаря.
    - <span style="color: orange;">using_in_month_table</span> (default_value=False): Флаг использования календаря в табеле.
### Возвращаемое значение
- <span style="color: orange;">work_schedule</span>: Объект обычного рабочего календаря типа GraphQL.
- <span style="color: orange;">ok_status</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleShift(
    input: {
      name: "string"
      workScheduleType: COMMON
      workDayAmount: 1
      chillDayAmount: 1
    }
    organizationId: 10
  ) {
    workSchedule {
      rowId
      name
    }
    ok
  }
}
```


## [CreateWorkScheduleShiftWorkDayAssign](work_schedule_shift_create.py) Класс мутации на создание связи вахтового календаря с рабочим днем
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">work_day_schedule_id</span> (обязательный): Идентификатор рабочего дня.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkScheduleShiftWorkDayAssign(
    workDayScheduleId: 10
    workScheduleId: 10
  ) {
    ok
  }
}
```


## [CreateWorkScheduleShiftDayCut](work_schedule_shift_day_cut_create.py) Класс мутации на создание ограничения для вахтового рабочего календаря
### Аргументы
- <span style="color: orange;">create_input</span> (обязательный): Объект обмена данными о создании ограничения часов на день типа GraphQL.
    - <span style="color: orange;">day</span> (обязательный): День, на который установлено ограничение по часам.
    - <span style="color: orange;">hours</span> (обязательный): Количество часов, которое является ограничением.
    - <span style="color: orange;">work_schedule_shift_id</span> (обязательный): Флаг использования календаря в табеле.
### Возвращаемое значение
- <span style="color: orange;">work_schedule_day_cut</span>: Объект ограничения вахтового календаря типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">error</span>: Перечисление результатов создания ограничения вахтового календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  createWorkScheduleShiftDayCut(createInput: {day: "2024-01-01" hours: 1 workScheduleShiftId: 10}) {
    workScheduleDayCut {
      rowId
      day
      hours
      workScheduleShiftId
    }
    ok
    error
  }
}
```


## [CreateWorkWeekSchedule](work_week_schedule_create.py) Класс мутации на создание рабочей недели календаря
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании рабочей недели типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование рабочей недели.
### Возвращаемое значение
- <span style="color: orange;">work_week_schedule</span>: Объект рабочей недели календаря типа GraphQL.
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWorkWeekSchedule(input: { name: "string" }) {
    workWeekSchedule {
      rowId
      name
    }
    ok
  }
}
```


## [CreateWorkWeekend](work_weekend_create.py) Класс мутации на создание календарного исключения
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании календарного исключения типа GraphQL.
    - <span style="color: orange;">name</span> (обязательный): Наименование календарного исключения.
    - <span style="color: orange;">date_begin</span> (обязательный): Дата начала календарного исключения.
    - <span style="color: orange;">date_finish</span> (обязательный): Дата окончания календарного исключения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_weekend</span>: Объект календарного исключения типа GraphQL.


### Пример использования
```graphql
mutation {
  createWorkWeekend(input: { name: "string" dateBegin: "2024-01-01" dateFinish: "2024-02-01" }) {
    ok
    workWeekend {
      rowId
      name
    }
  }
}
```


## [BatchCreateWorkScheduleWeekendAssign](work_weekend_create.py) Класс мутации на массовое создание связи календаря с календарными исключениями
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">weekend_ids</span> (обязательный): Список идентификаторов календарных исключений.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  batchCreateWorkScheduleWeekendAssign(
    weekendIds: [10]
    workScheduleId: 10
  ) {
    ok
  }
}
```


## [CreateWeekendPeriods](work_weekend_period_create.py) Класс мутации на создание периода календарного исключения
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
    - <span style="color: orange;">work_weekend_id</span> (обязательный): Идентификатор календарного исключения.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createWeekendPeriods(inputs: [{ workPeriodType: WORK, serialNumber: 1 begin: "2024-01-01" finish: "2024-02-01" workWeekendId: 10 }]) {
    ok
    weekendPeriods {
      rowId
      begin
      finish
      serialNumber
      workPeriodType
      workWeekendId
    }
  }
}
```


# Модуль мутаций удаления для взаимодействия с сущностями календарей

## [DeleteWorkDaySchedule](work_day_schedule_delete.py) Класс мутации на удаление рабочего дня
### Аргументы
- <span style="color: orange;">work_day_schedule_ids</span> (обязательный): Список идентификаторов рабочих дней.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkDaySchedule(workDayScheduleIds: [10]) {
    ok
  }
}
```


## [DeleteWorkPeriod](work_period_delete.py) Класс мутации на удаление рабочих периодов дня
### Аргументы
- <span style="color: orange;">work_period_ids</span> (обязательный): Список идентификаторов периодов рабочих дней.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkPeriods(workPeriodIds: [10]) {
    ok
  }
}
```


## [DeleteWorkSchedules](work_schedule_delete.py) Класс мутации на удаление календаря
### Аргументы
- <span style="color: orange;">work_schedules_ids</span> (обязательный): Список идентификаторов календарей.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkSchedules(workSchedulesIds: [10]) {
    ok
  }
}
```


## [DeleteWorkScheduleAssign](work_schedule_assignment_delete.py) Класс мутации на удаление связи рабочего календаря с организацией/проектом/работником
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkScheduleAssign(
    organizationId: 10
    workScheduleId: 10
  ) {
    ok
  }
}
```


## [DeleteWorkScheduleShiftWorkDayAssign](work_schedule_shift_delete.py) Класс мутации на удаление связи вахтового календаря с рабочим днем
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">work_days_schedule_ids</span> (обязательный): Список идентификаторов рабочих дней.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkScheduleShiftWorkDayAssign(
    workDaysScheduleIds: [10]
    workScheduleId: 10
  ) {
    ok
  }
}
```


## [DeleteWorkScheduleShiftDayCut](work_schedule_shift_delete.py) Класс мутации на удаление списка ограничений вахтового календаря
### Аргументы
- <span style="color: orange;">work_schedule_day_cut_ids</span> (обязательный): Список идентификаторов ограничения по часам.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkScheduleShiftDayCut(workScheduleDayCutIds: [10]) {
    ok
  }
}
```


## [DeleteWorkWeekSchedule](work_week_schedule_delete.py) Класс мутации на удаление рабочей недели календаря
### Аргументы
- <span style="color: orange;">work_week_schedule_ids</span> (обязательный): Список идентификаторов недель.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkWeekSchedule(workWeekScheduleIds: [10]) {
    ok
  }
}
```


## [DeleteWorkWeekends](work_weekend_delete.py) Класс мутации на удаление календарных исключений
### Аргументы
- <span style="color: orange;">work_week_schedule_ids</span> (обязательный): Список идентификаторов календарных исключений.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWorkWeekSchedule(workWeekScheduleIds: [10]) {
    ok
  }
}
```


## [DeleteWeekendPeriods](work_weekend_period_delete.py) Класс мутации на удаление периодов календарных исключений
### Аргументы
- <span style="color: orange;">work_period_ids</span> (обязательный): Список идентификаторов периодов календарных исключений.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteWeekendPeriods(workPeriodIds: [10]) {
    ok
  }
}
```


# Модуль мутаций обновления для взаимодействия с сущностями календарей

## [UpdateWorkDaySchedule](work_day_schedule_update.py) Класс мутации на обновление рабочего дня
### Аргументы
- <span style="color: orange;">work_day_schedule_id</span> (обязательный): Идентификатор рабочего дня.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении рабочего дня типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_day_schedule</span>: Объект рабочего дня календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkDaySchedule(input: {name: "string"} workDayScheduleId: 10) {
    ok
    workDaySchedule {
      rowId
      name
    }
  }
}
```


## [UpdateWorkPeriod](work_period_update.py) Класс мутации на обновление рабочего периода
### Аргументы
- <span style="color: orange;">work_period_id</span> (обязательный): Идентификатор периода рабочего дня.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении рабочего периода типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_day_schedule</span>: Объект отрезка времени Обед/Работа типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkPeriod(input: {begin: "08:00:00"}, workPeriodId: 10) {
    ok
    workPeriod {
      rowId
    }
  }
}
```


## [UpdateWorkScheduleCommon](work_schedule_common_update.py) Класс мутации на обновление обычного календаря
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении обычного календаря типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok_status</span>: Успешность операции.
- <span style="color: orange;">work_schedule</span>: Объект обычного рабочего календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkScheduleCommon(updateInput: {name: "string"}, workScheduleId: 10) {
    okStatus
    workSchedule {
      rowId
      name
    }
  }
}
```


## [UpdateWorkScheduleShift](work_schedule_shift_update.py) Класс мутации на обновление вахтового календаря
### Аргументы
- <span style="color: orange;">work_schedule_id</span> (обязательный): Идентификатор календаря.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении обычного календаря типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_schedule</span>: Объект вахтового рабочего календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkScheduleShift(input: {name:"string"}, workScheduleId: 10) {
    ok
    workSchedule {
      rowId
      name
    }
  }
}
```


## [UpdateWorkScheduleShiftDayCut](work_schedule_shift_day_cut_update.py) Класс мутации на обновление ограничения вахтового рабочего календаря
### Аргументы
- <span style="color: orange;">work_schedule_shift_day_cut_id</span> (обязательный): Идентификатор ограничения по часам.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении ограничения часов на день типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_schedule_shift_day_cut</span>: Объект ограничения вахтового календаря типа GraphQL.
- <span style="color: orange;">error</span>: Перечисление результатов обновления ограничения вахтового календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkScheduleShiftDayCut(
    updateInput: {hours: 1}
    workScheduleShiftDayCutId: 10
  ) {
    ok
    workScheduleShiftDayCut {
      rowId
      day
      hours
      workScheduleShiftId
    }
    error
  }
}
```


## [UpdateWorkWeekSchedule](work_week_schedule_update.py) Класс мутации на обновление рабочей недели
### Аргументы
- <span style="color: orange;">work_week_schedule_id</span> (обязательный): Идентификатор недели.
- <span style="color: orange;">update_input</span> (обязательный): Объект обмена данными об обновлении рабочей недели типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_week_schedule</span>: Объект рабочей недели календаря типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkWeekSchedule(input: {name:"string"}, workWeekScheduleId: 10) {
    ok
    workWeekSchedule {
      rowId
      name
    }
  }
}
```


## [UpdateWorkWeekend](work_weekend_update.py) Класс мутации на обновление календарного исключения
### Аргументы
- <span style="color: orange;">work_weekend_id</span> (обязательный): Идентификатор календарного исключения.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении календарного исключения типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">work_weekend</span>: Объект календарного исключения типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkWeekend(input: {name: "string"}, workWeekendId: 10) {
    ok
    workWeekend {
      rowId
      name
    }
  }
}
```


## [UpdateWeekendPeriod](work_weekend_period_update.py) Класс мутации на обновление календарного исключения
### Аргументы
- <span style="color: orange;">work_weekend_id</span> (обязательный): Идентификатор календарного исключения.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными об обновлении календарного исключения типа GraphQL.
### Возвращаемое значение
- <span style="color: orange;">ok</span>: Успешность операции.
- <span style="color: orange;">weekend_period</span>: Объект периода работы/обеда календарного исключения типа GraphQL.


### Пример использования
```graphql
mutation {
  updateWorkWeekend(input: {name: "string"}, workWeekendId: 10) {
    ok
    workWeekend {
      rowId
      name
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями календарей

## [getWorkDaysScheduleByText](work_day_schedule.py) Получение рабочих дней по наименованию
### Аргументы
- <span style="color: orange;">text</span> (обязательный): Строка для поиска.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkDaySchedule]</span>: Список объектов рабочих дней типа GraphQL


### Пример использования
```graphql 
query {
  getWorkDaysScheduleByText(text: "string") {
    rowId
    name
    periods {
      rowId
    }
    totalHours
  }
}
```


## [getAllWorkSchedules](work_schedule.py) Получение всех календарей
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[WorkSchedulesUnion]</span>: Список объектов календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getAllWorkSchedules{
    ... on WorkSchedule {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkScheduleById](work_schedule.py) Получение календаря по идентификатору
### Аргументы
- <span style="color: orange;">row_id</span> (обязательный): Идентификатор календаря.
### Возвращаемое значение
- <span style="color: orange;">WorkSchedulesUnion</span>: Объект календаря типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkScheduleById(rowId: 10)
  {
    ... on WorkSchedule
    {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkSchedulesByProjectId](work_schedule.py) Получение календарей, назначенных на проект
### Аргументы
- <span style="color: orange;">project_id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">using_in_month_table</span> (default_value=False): Флаг использования календаря в табеле.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkSchedulesUnion]</span>: Список объектов календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkSchedulesByProjectId(projectId: 10)
  {
    ... on WorkSchedule
    {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkSchedulesByOrganizationId](work_schedule.py) Получение календарей, назначенных на организацию
### Аргументы
- <span style="color: orange;">project_id</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">organization_id</span> (обязательный): Идентификатор организации.
- <span style="color: orange;">using_in_month_table</span> (default_value=False): Флаг использования календаря в табеле.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkSchedulesUnion]</span>: Список объектов календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkSchedulesByOrganizationId(
    organizationId: 10
  ) {
    ... on WorkSchedule
    {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkScheduleByTimeResourceId](work_schedule.py) Получение календаря тайм-ресурса
### Аргументы
- <span style="color: orange;">time_resource_id</span> (обязательный): Идентификатор организации.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkSchedulesUnion]</span>: Список объектов календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkScheduleByTimeResourceId(timeResourceId: 10)
  {
    ... on WorkSchedule
    {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkSchedulesByTimeResourceIds](work_schedule.py) Получение календарей тайм-ресурсов
### Аргументы
- <span style="color: orange;">time_resource_ids</span> (обязательный): Список идентификаторов тайм-ресурсов.
### Возвращаемое значение
- <span style="color: orange;">TList[TimeResourceWorkSchedule]</span>: Список объектов производственных календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkSchedulesByTimeResourceIds(timeResourceIds: [10]) {
    timeResourceId
  }
}
```


## [getWorkScheduleByText](work_schedule.py) Получение рабочего календаря по наименованию
### Аргументы
- <span style="color: orange;">text</span> (обязательный): Наименование календаря.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkSchedulesUnion]</span>: Список объектов календарей типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkScheduleByText(text: "string")
  {
    ... on WorkSchedule
    {
      rowId
      name
      workScheduleType
    }
  }
}
```


## [getWorkSchedulesByResourceIds](work_schedule.py) Получение объектов связи рабочих календарей и ресурсов
### Аргументы
- <span style="color: orange;">resource_ids</span> (обязательный): Список идентификаторов ресурсов.
### Возвращаемое значение
- <span style="color: orange;">TList[ResourceWorkSchedule]</span>: Список объектов связей рабочих календарей и ресурсов типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkSchedulesByResourceIds(resourceIds: [10]) {
    resourceId
    workSchedule {
      rowId
      name
    }
  }
}
```


## [getWorkSchedulesByWorkIds](work_schedule.py) Получение объектов связей рабочих календарей и операций
### Аргументы
- <span style="color: orange;">work_ids</span> (обязательный): Список идентификаторов работ.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkWorkSchedule]</span>: Список объектов связей рабочих календарей и операций типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkSchedulesByWorkIds(workIds: [10]) {
    workId
    workSchedule {
      rowId
      name
    }
  }
}
```


## [getCutsForScheduleShift](work_shedule_shift_day_cut.py) Получение ограничений по идентификаторам календарей
### Аргументы
- <span style="color: orange;">work_schedule_shift_ids</span> (обязательный): Список идентификаторов вахтовых календарей.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkScheduleShiftDayCutOnScheduleShift]</span>: Список объектов связи вахтового календаря со списком его ограничений типа GraphQL.


### Пример использования
```graphql 
query {
  getCutsForScheduleShift(workScheduleShiftIds: [10]) {
    workScheduleShiftId
    workScheduleShiftDaysCut {
      rowId
      day
      hours
      workScheduleShiftId
    }
  }
}
```


## [getWorkWeeksScheduleByText](work_week_schedule.py) Получение календарных исключений оп наименованию
### Аргументы
- <span style="color: orange;">text</span> (обязательный): Текст для поиска.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkWeekSchedule]</span>: Список объектов календарных исключений типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkWeeksScheduleByText(text: "string") {
    rowId
    name
    workDaysSchedule {
      rowId
      name
    }
  }
}
```


## [getAllWorkWeekSchedules](work_week_schedule.py) Получение всех недельных расписаний
### Аргументы (Нет Аргументов)
### Возвращаемое значение
- <span style="color: orange;">TList[WorkWeekSchedule]</span>: Список объектов календарных исключений типа GraphQL.


### Пример использования
```graphql 
query {
  getAllWorkWeekSchedules {
    rowId
    name
    workDaysSchedule {
      rowId
      name
    }
  }
}
```


## [getWorkWeekendsByText](work_weekend_schedule.py) Получение календарных исключений по наименованию
### Аргументы
- <span style="color: orange;">text</span> (обязательный): Текст для поиска.
### Возвращаемое значение
- <span style="color: orange;">TList[WorkWeekend]</span>: Список объектов календарных исключений типа GraphQL.


### Пример использования
```graphql 
query {
  getWorkWeekendsByText(text: "string") {
    rowId
    name
    dateBegin
    dateFinish
    periods {
      rowId
    }
  }
}
```
