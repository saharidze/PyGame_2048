# Оглавление

1. [Модуль общих мутаций для взаимодействия с сущностями выпадающего списка](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-выпадающего-списка)
2. [Модуль запросов для взаимодействия с сущностями выпадающего списка](#модуль-запросов-для-взаимодействия-с-сущностями-выпадающего-списка)
3. [Модуль общих мутаций для взаимодействия с сущностями атрибута "Избранное"](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-атрибута-"избранное")
4. [Модуль общих мутаций для взаимодействия с сущностями атрибута "Мульти атрибут"](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-атрибута-"мульти-атрибут")
5. [Модуль запросов для взаимодействия с сущностями атрибута "Мульти атрибут"](#модуль-запросов-для-взаимодействия-с-сущностями-атрибута-"мульти-атрибут")
6. [Модуль общих мутаций для взаимодействия с сущностями атрибута "Приоритет"](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-атрибута-"приоритет")
7. [Модуль запросов для взаимодействия с сущностями атрибута "Приоритет"](#модуль-запросов-для-взаимодействия-с-сущностями-атрибута-"приоритет")
8. [Модуль общих мутаций для взаимодействия с сущностями ролей](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-ролей)
9. [Модуль запросов для взаимодействия с сущностями ролей](#модуль-запросов-для-взаимодействия-с-сущностями-ролей)
10. [Модуль общих мутаций для взаимодействия с сущностями атрибута "Таблица"](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-атрибута-"таблица")
11. [Модуль запросов для взаимодействия с сущностями атрибута "Таблица"](#модуль-запросов-для-взаимодействия-с-сущностями-атрибута-"таблица")
12. [Модуль общих мутаций для взаимодействия с сущностями атрибута "Статус"](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-атрибута-"статус")
13. [Модуль запросов для взаимодействия с сущностями атрибута "Статус"](#модуль-запросов-для-взаимодействия-с-сущностями-атрибута-"статус")
14. [Модуль общих мутаций для взаимодействия с сущностями фильтра](#модуль-общих-мутаций-для-взаимодействия-с-сущностями-фильтра)
15. [Модуль запросов для взаимодействия с сущностями фильтра](#модуль-запросов-для-взаимодействия-с-сущностями-фильтра)
16. [Модуль общих мутаций для взаимодействия с сервисом задачника](#модуль-общих-мутаций-для-взаимодействия-с-сервисом-задачника)
17. [Модуль запросов для взаимодействия с сервисом задачника](#модуль-запросов-для-взаимодействия-с-сервисом-задачника)

# Модуль общих мутаций для взаимодействия с сущностями выпадающего списка

## [createDropDown](dropdown_attribute/mutations.graphql) Класс мутации на создание выпадающего списка
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Элементы выпадающего списка.
### Возвращаемое значение
- <span style="color: orange;">DropDownInfoType</span>: Информация о выпадающем списке.


### Пример использования
```graphql
mutation {
  createDropDown(
    input: {name: "string" isRelated: true}
  ) {
    DropDownInfoType {
    id
    name
    description
    isRelated
    }
  }
}
```


## [patchDropDown](dropdown_attribute/mutations.graphql) Класс мутации на изменение выпадающего списка
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Идентификатор выпадающего списка.
- <span style="color: orange;">input</span> (default_value=None): Элементы выпадающего списка.
### Возвращаемое значение
- <span style="color: orange;">DropDownInfoType</span>: Информация о выпадающем списке.


### Пример использования
```graphql
mutation {
  patchDropDown(id: 10, input: { name: "string", isRelated: true }) {
    DropDownInfoType {
      id
      name
      description
      isRelated
    }
  }
}
```


## [deleteDropDown](dropdown_attribute/mutations.graphql) Класс мутации на удаление выпадающего списка
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Идентификатор выпадающего списка.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteDropDown(id: 10) {
    Boolean
    }
  }
}
```


## [bindDropDown](dropdown_attribute/mutations.graphql) Класс мутации на удаление выпадающего списка
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Идентификатор выпадающего списка.
- <span style="color: orange;">input</span> (default_value=None): Инпут по задаче.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteDropDown(id: 10) {
    Boolean
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями выпадающего списка

## [getDropDown](dropdown_attribute/query.graphql) Получение выпадающего списка
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Элементы выпадающего списка.
- <span style="color: orange;">input</span> (default_value=None): Элементы выпадающего списка.
### Возвращаемое значение
- <span style="color: orange;">DropDownInfoType</span>: Информация о выпадающем списке.


### Пример использования
```graphql
query {
  getDropDown(
    input: {name: "string" isRelated: true}
  ) {
    DropDownInfoType {
      id
      name
      description
      isRelated
    }
  }
}
```


## [getDropDowns](dropdown_attribute/query.graphql) Получение всех выпадающих списков
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">DropDownInfoType</span>: Информация о выпадающем списке.


### Пример использования
```graphql
query {
  getDropDowns {
    DropDownInfoType {
      id
      name
      description
      isRelated
    }
  }
}
```


## [getDropDownItems](dropdown_attribute/query.graphql) Получение элементов выпадающего списка
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Идентификатор выпадающего списка.
- <span style="color: orange;">input</span> (default_value=None): Поиск по задаче.
### Возвращаемое значение
- <span style="color: orange;">DropDownItem</span>: Информация о выпадающем списке.


### Пример использования
```graphql
query {
  getDropDownItems(id: 10, input: { taskType: "string", attribute: "string" }) {
    DropDownItem {
      id
      label
      color
      order
    }
  }
}
```


## [getFilteredDropDownItems](dropdown_attribute/query.graphql) Получение элементов выпадающего списка с фильтрацией
### Аргументы
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">fields</span> (обязательный): Поля для которых нужно получить элементы выпадающего списка.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">returnDefault</span> (default_value=True): Вернуть дефолтные значения, если нет по проекту.
### Возвращаемое значение
- <span style="color: orange;">DropDownItem</span>: Информация о выпадающем списке.


### Пример использования
```graphql
query {
  getFilteredDropDownItems(
    typename: "string"
    fields: { field: "string", filterItemsId: [10] }
  ) {
    FilteredDropDownItemsType {
      field
      isRelated
    }
    values {
      id
      label
      color
      order
    }
    DropDownItemFieldAutocompleteType {
      entityId
      entityType
      entityValue
      projectId
      typename
      field
    }
  }
}
```


## [getDropDownBinds](dropdown_attribute/query.graphql) Получение выпадающих списков привязанных к полям типов задач
### Аргументы
- <span style="color: orange;">typenames</span> (обязательный): Типы задач.
- <span style="color: orange;">projectId</span> (default_value=None): Поля для которых нужно получить элементы выпадающего списка.
### Возвращаемое значение
- <span style="color: orange;">DropDownItem</span>: Информация о выпадающем списке.


### Пример использования
```graphql
query {
  getDropDownBinds(typenames: ["string"]) {
    DropDownTaskTypeBindType {
      typename
      binds
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями атрибута "Избранное"

## [getDropDown](favourites_attribute/mutation.graphql) Класс мутации на добавление карточки в избранное
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (обязательный): Наименование типа задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  getDropDown(id: 10, taskType: "string") {
    Boolean
  }
}
```


## [deleteTaskFromFavorites](favourites_attribute/mutation.graphql) Класс мутации на удаление карточки из избранного
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (обязательный): Наименование типа задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  deleteTaskFromFavorites(id: 10, taskType: "string") {
    Boolean
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями атрибута "Мульти атрибут"

## [patchMultiAttributeUserValue](multi_attribute/mutation.graphql) Класс мутации на редактирование пользовательского значения атрибута "Мульти атрибут"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор значения.
- <span style="color: orange;">name</span> (default_value=None): Наименование значения.
- <span style="color: orange;">color</span> (default_value=None): Цвет атрибута.
- <span style="color: orange;">publicVisible</span> (default_value=False): Видимость для всех пользователей.
### Возвращаемое значение
- <span style="color: orange;">MultiAttributeUserValueType</span>: Значение поля "Мульти атрибут".


### Пример использования
```graphql
query {
  patchMultiAttributeUserValue(
    name: "String"
    entityType: JournalRowType
    projectId: 10
    color: "black"
  ) {
    MultiAttributeUserValueType {
      id
      name
      entityId
      entityType
      entityValue
      userId
      publicVisible
      projectId
      color
    }
  }
}
```


## [deleteMultiAttributeUserValue](multi_attribute/mutation.graphql) Класс мутации на удаление пользовательского значения атрибута "Мульти атрибут"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор значения.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  deleteMultiAttributeUserValue(id: 10) {
    Boolean
  }
}
```


## [setProjectsForMultiAttributeUserValue](multi_attribute/mutation.graphql) Класс мутации на сопоставления проектов в таблице
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  setProjectsForMultiAttributeUserValue{
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сущностями атрибута "Мульти атрибут"

## [patchMultiAttributeUserValue](multi_attribute/mutation.graphql) Получение пользовательского значения атрибута "Мульти атрибут"
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">searchName</span> (default_value=None): Строка поиска значения по имени.
- <span style="color: orange;">onlyUserValues</span> (default_value=False): Значения только текущего пользователя.
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">ignoreIds</span> (default_value=None): Игнорируемые идентификаторы.
### Возвращаемое значение
- <span style="color: orange;">MultiAttributeUserValueType</span>: Значение поля "Мульти атрибут".


### Пример использования
```graphql
query {
  getMultiAttributeUserValues(
    projectId: 10
  ) {
    MultiAttributeUserValueType {
      id
      name
      entityId
      entityType
      entityValue
      userId
      publicVisible
      projectId
      color
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями атрибута "Приоритет"

## [createPriorityItem](priority_attribute/mutation.graphql) Класс мутации на создание атрибута "Приоритет"
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Данные элемента атрибута Приоритет.
### Возвращаемое значение
- <span style="color: orange;">PriorityItemType</span>: Приоритет.


### Пример использования
```graphql
query {
  createPriorityItem(input: { name: "string" }) {
    PriorityItemType {
      id
      name
      color
      isActive
      priority
    }
  }
}
```


## [patchPriorityItem](priority_attribute/mutation.graphql) Класс мутации на обновление атрибута "Приоритет"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор элемента атрибута Приоритет.
- <span style="color: orange;">input</span> (обязательный): Данные элемента атрибута Приоритет.
### Возвращаемое значение
- <span style="color: orange;">PriorityItemType</span>: Приоритет.


### Пример использования
```graphql
query {
  patchPriorityItem(id: 10, input: { name: "string" }) {
    PriorityItemType {
      id
      name
      color
      isActive
      priority
    }
  }
}
```


## [deletePriorityItem](priority_attribute/mutation.graphql) Класс мутации на удаление атрибута "Приоритет"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор элемента атрибута Приоритет.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  deletePriorityItem(id: 10) {
    Boolean
  }
}
```


## [bindPriorityItems](priority_attribute/mutation.graphql) Класс мутации на привязку элементов атрибута "Приоритет" к полю и типу задачи
### Аргументы
- <span style="color: orange;">taskType</span> (обязательный): Наименование типа задачи.
- <span style="color: orange;">field</span> (обязательный): Наименование поля.
- <span style="color: orange;">priorityItemIds</span> (обязательный): Идентификаторы элементов атрибута Приоритет.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
query {
  bindPriorityItems(taskType: 10, field: "string", priorityItemIds: [10]) {
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сущностями атрибута "Приоритет"

## [getPriorityItems](priority_attribute/query.graphql) Получение всех приоритетов
### Аргументы
- <span style="color: orange;">filter</span> (default_value=None): Фильтрация по типу и полю.
- <span style="color: orange;">onlyActive</span> (default_value=True): Только активные.
### Возвращаемое значение
- <span style="color: orange;">[PriorityItemType]</span>: Список приоритетов.


### Пример использования
```graphql
query {
  getPriorityItems {
    PriorityItemType {
      id
      name
      color
      isActive
      priority
    }
  }
}
```


## [getPriorityItemBinds](priority_attribute/query.graphql) Получение приоритетов привязанных к полям типов задач
### Аргументы
- <span style="color: orange;">taskTypes</span> (обязательный): Фильтрация по типу и полю.
- <span style="color: orange;">onlyActive</span> (default_value=True): Только активные.
### Возвращаемое значение
- <span style="color: orange;">[PriorityItemTaskTypeBindType]</span>: Список связей типа задачи, поля и приорите.


### Пример использования
```graphql
query {
  getPriorityItemBinds(taskTypes: ["string"], onlyActive: True) {
    PriorityItemTaskTypeBindType {
      typename
      field
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями ролей

## [changeRolesSettings](role_permissions/mutation.graphql) Класс мутации на обновления права на роль
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения разрешений на роль.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeRolesSettings(
    permissions: [
      {
        task_type: "string"
        read: True
        create: False
        patch: False
        delete: False
      }
    ]
  ) {
    Boolean
  }
}
```


## [grantPermissionsByRoles](role_permissions/mutation.graphql) Класс мутации на установление прав пользователю
### Аргументы
- <span style="color: orange;">userId</span> (обязательный): Идентификатор пользователя.
- <span style="color: orange;">rolesId</span> (обязательный): Идентификаторы ролей.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  grantPermissionsByRoles(userId: 10, rolesId: [10]) {
    Boolean
  }
}
```


## [changeUserPermissionsByRoles](role_permissions/mutation.graphql) Класс мутации на изменения прав у пользователя
### Аргументы
- <span style="color: orange;">usersId</span> (обязательный): Идентификаторы пользователей.
- <span style="color: orange;">addedRolesId</span> (обязательный): Идентификаторы назначенных ролей.
- <span style="color: orange;">removedRolesId</span> (обязательный): Идентификаторы отобранных ролей.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeUserPermissionsByRoles(
    usersId: [10]
    addedRolesId: [20]
    removedRolesId: [10]
  ) {
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сущностями ролей

## [getRolesSettings](role_permissions/query.graphql) Получение настройки прав ролей
### Аргументы
- <span style="color: orange;">ids</span> (обязательный): Идентификаторы ролей.
- <span style="color: orange;">taskTypes</span> (default_value=None): Типы задач.
### Возвращаемое значение
- <span style="color: orange;">[RoleSettingsType]</span>: Список настроек прав ролей.


### Пример использования
```graphql
query {
  getRolesSettings(ids: [10]) {
    RoleSettingsType {
      id
      roleId
      taskType
      read
      create
      patch
      delete
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями атрибута "Таблица"

## [migrateSheets](sheet_attribute/mutation.graphql) Класс мутации на миграцию таблиц на новую схему 
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  migrateSheets {
    Boolean
  }
}
```


## [convertSheetToAdvancedSheet](sheet_attribute/mutation.graphql) Класс мутации на конвертацию структуры обычных таблиц в структуру расширенных таблиц
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[RoleSettingsType]</span>: Список настроек прав ролей.


### Пример использования
```graphql
mutation {
  convertSheetToAdvancedSheet {
    Boolean
  }
}
```


## [createSheet](sheet_attribute/mutation.graphql) Класс мутации на создание атрибута "Таблица"
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут создания таблицы атрибута.
### Возвращаемое значение
- <span style="color: orange;">SheetStructureType</span>: Структура атрибута "Таблица".


### Пример использования
```graphql
mutation {
  createSheet(input: { name: "string", description: "string" }) {
    SheetStructureType {
      id
      name
      parentId
      childrenId
    }
  }
}
```


## [patchSheet](sheet_attribute/mutation.graphql) Класс мутации на обновление атрибута "Таблица"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор таблицы.
- <span style="color: orange;">input</span> (обязательный): Инпут создания таблицы атрибута.
### Возвращаемое значение
- <span style="color: orange;">SheetStructureType</span>: Структура атрибута "Таблица".


### Пример использования
```graphql
mutation {
  patchSheet(id: 10, input: { name: "string", description: "string" }) {
    SheetStructureType {
      id
      name
      parentId
      childrenId
    }
  }
}
```


## [deleteSheet](sheet_attribute/mutation.graphql) Класс мутации на удаление атрибута "Таблица"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор таблицы.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteSheet(id: 10) {
    Boolean
  }
}
```


## [bindSheet](sheet_attribute/mutation.graphql) Класс мутации на привязку таблицы атрибута "Таблица" к типу задачи и полю
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут привязки.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  bindSheet(input: { id: 10, taskType: "string", fieldId: 10 }) {
    Boolean
  }
}
```


## [unbindSheet](sheet_attribute/mutation.graphql) Класс мутации на отвязку таблицы атрибута "Таблица" от типа задачи и поля
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут привязки.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  unbindSheet(input: { id: 10, taskType: "string", fieldId: 10 }) {
    Boolean
  }
}
```


## [setSheetStructure](sheet_attribute/mutation.graphql) Класс мутации на определение структуры таблицы атрибута "Таблица"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор таблицы.
- <span style="color: orange;">input</span> (default_value=None): Список полей для добавления.
### Возвращаемое значение
- <span style="color: orange;">SheetStructureType</span>: Структура атрибута "Таблица".


### Пример использования
```graphql
mutation {
  setSheetStructure(id: 10, fields: [{ id: 10, order: 1 }]) {
    SheetStructureType {
      id
      name
      parentId
      childrenId
    }
  }
}
```


# Модуль запросов для взаимодействия с сущностями атрибута "Таблица"

## [getSheetStructure](sheet_attribute/query.graphql) Получение структуры таблицы привязанных к типу задачи и полю
### Аргументы
- <span style="color: orange;">sheetType</span> (обязательный): Название типа таблицы.
### Возвращаемое значение
- <span style="color: orange;">[SheetStructureType]</span>: Список структур атрибутов "Таблица".


### Пример использования
```graphql
query {
  getSheetStructure(sheetType: "string") {
    SheetStructureType {
      id
      name
      parentId
      childrenId
    }
  }
}
```


## [getSheetBinds](sheet_attribute/query.graphql) Получение структуры таблицы привязанных к типу задачи и полю
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[SheetBindType]</span>: Список типов связей таблиц с типами задач.


### Пример использования
```graphql
query {
  getSheetBinds {
    SheetBindType {
    taskType
    fieldId
    }
  }
}
```


## [getSheetBinds](sheet_attribute/query.graphql) Пересчет итога у таблицы
### Аргументы
- <span style="color: orange;">field</span> (обязательный): Наименование поля.
- <span style="color: orange;">task</span> (обязательный): Объект задачи.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.


### Пример использования
```graphql
query {
  getSheetBinds(field: "string" task: JSONTask) {
    JSONTask
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями атрибута "Статус"

## [createStatusItem](status_attribute/mutation.graphql) Класс мутации на создание атрибута "Статус"
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании атрибута "Статус".
### Возвращаемое значение
- <span style="color: orange;">StatusItemType</span>: Объект атрибута "Статус".


### Пример использования
```graphql
mutation {
  createStatusItem(input: { name: "string" }) {
    StatusItemType {
      id
      name
      color
      order
      isActive
      category
    }
  }
}
```


## [patchStatusItem](status_attribute/mutation.graphql) Класс мутации на обновление атрибута "Статус"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор статуса.
- <span style="color: orange;">input</span> (обязательный): Объект обмена данными о создании атрибута "Статус".
### Возвращаемое значение
- <span style="color: orange;">StatusItemType</span>: Объект атрибута "Статус".


### Пример использования
```graphql
mutation {
  patchStatusItem(id: 10, input: { name: "string" }) {
    StatusItemType {
      id
      name
      color
      order
      isActive
      category
    }
  }
}
```


## [deleteStatusItem](status_attribute/mutation.graphql) Класс мутации на обновление атрибута "Статус"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор статуса.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteStatusItem(id: 10) {
    Boolean
  }
}
```


## [createStatusItemCategory](status_attribute/mutation.graphql) Класс мутации на создание категории атрибута "Статус"
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Данные для создания категории статуса.
### Возвращаемое значение
- <span style="color: orange;">StatusItemCategoryType</span>: Категория статуса.


### Пример использования
```graphql
mutation {
  createStatusItemCategory(input: {name: "string"}) {
    StatusItemCategoryType {
      id
      name
      color
    }
  }
}
```


## [patchStatusItemCategory](status_attribute/mutation.graphql) Класс мутации на обновление категории атрибута "Статус"
### Аргументы
- <span style="color: orange;">шв</span> (обязательный): Идентификатор категории статуса.
- <span style="color: orange;">input</span> (обязательный): Данные для создания категории статуса.
### Возвращаемое значение
- <span style="color: orange;">StatusItemCategoryType</span>: Категория статуса.


### Пример использования
```graphql
mutation {
  patchStatusItemCategory(id: 10, input: {name: "string"}) {
    StatusItemCategoryType {
      id
      name
      color
    }
  }
}
```


## [deleteStatusItemCategory](status_attribute/mutation.graphql) Класс мутации на удаление категории атрибута "Статус"
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор категории статуса.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteStatusItemCategory(id: 10) {
    Boolean
  }
}
```


## [bindStatusItems](status_attribute/mutation.graphql) Класс мутации на привязку атрибута "Статус" к полю и типу задачи
### Аргументы
- <span style="color: orange;">taskType</span> (обязательный): Наименование типа задачи.
- <span style="color: orange;">field</span> (обязательный): Наименование поля.
- <span style="color: orange;">statusItemIds</span> (обязательный): Идентификаторы статусов.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  bindStatusItems(taskType: "string", field: "string", statusItemIds: [10]) {
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сущностями атрибута "Статус"

## [getStatusItemCategories](status_attribute/query.graphql) Получение всех категорий статуса
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[StatusItemCategoryType]</span>: Список категорий статуса.


### Пример использования
```graphql
query {
  getStatusItemCategories {
    StatusItemCategoryType {
      id
      name
      color
    }
  }
}
```


## [getStatusItems](status_attribute/query.graphql) Получение всех категорий статуса (с возможной фильтрацией по типу и полю)
### Аргументы
- <span style="color: orange;">filter</span> (default_value=None): Фильтрация по типу и полю.
- <span style="color: orange;">onlyActive</span> (default_value=True): Только активные.
### Возвращаемое значение
- <span style="color: orange;">[StatusItemType]</span>: Список статусов.


### Пример использования
```graphql
query {
  getStatusItems {
    StatusItemType {
      id
      name
      color
      order
      isActive
      category
    }
  }
}
```


## [getStatusItemBinds](status_attribute/query.graphql) Получение статусов привязанных к полям типов задач
### Аргументы
- <span style="color: orange;">taskTypes</span> (обязательный): Типы задач.
- <span style="color: orange;">onlyActive</span> (default_value=True): Только активные.
### Возвращаемое значение
- <span style="color: orange;">[StatusItemTaskTypeBindType]</span>: Список связей типа задачи, поля и статусов.


### Пример использования
```graphql
query {
  getStatusItemBinds(taskTypes: ["string"]) {
    StatusItemTaskTypeBindType {
      typename
      field
      bind
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сущностями фильтра

## [createFilter](user_filters/mutation.graphql) Класс мутации на создание фильтра
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Типы задач.
- <span style="color: orange;">users</span> (default_value=True): Только активные.
- <span style="color: orange;">groups</span> (обязательный): Типы задач.
- <span style="color: orange;">projects</span> (default_value=True): Только активные.
### Возвращаемое значение
- <span style="color: orange;">Filter</span>: Список категорий статуса.


### Пример использования
```graphql
mutation {
  createFilter(
    input: {
      name: "string"
      conditions: [{ attribute: "string", operation: eq }]
    }
    users: [{ id: 10 }]
    groups: [20]
    projects: [10]
  ) {
    Filter {
      id
      parentId
      childrenId
      name
      taskType
      creatorId
      category
      groupedFilters
      count
      onlyActualRevision
      showCompleted
      isSystemFilter
      isGlobalFilter
      showCounter
      groupByField
      excludedUsersId
      usersId
      projectsId
      isDelimiter
      filterDelimiterId
      filtersWithDelimeterId
    }
  }
}
```


## [patchFilter](user_filters/mutation.graphql) Класс мутации на обновление фильтра
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор фильтра.
- <span style="color: orange;">input</span> (обязательный): Типы задач.
- <span style="color: orange;">users</span> (обязательный): Только активные.
- <span style="color: orange;">groups</span> (обязательный): Типы задач.
- <span style="color: orange;">projects</span> (обязательный): Только активные.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  patchFilter(
    id: 10  
    input: {
      name: "string"
      conditions: [{ attribute: "string", operation: eq }]
    }
    users: [{ id: 10 }]
    groups: [20]
    projects: [10]
  ) {
    Boolean
  }
}
```


## [deleteFilter](user_filters/mutation.graphql) Класс мутации на удаление фильтра
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор фильтра.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteFilter(id: 10) {
    Boolean
  }
}
```


## [assignFilters](user_filters/mutation.graphql) Класс мутации на назначение фильтра
### Аргументы
- <span style="color: orange;">ids</span> (обязательный): Идентификатор фильтра.
- <span style="color: orange;">users</span> (обязательный): Только активные.
- <span style="color: orange;">groups</span> (обязательный): Типы задач.
- <span style="color: orange;">projects</span> (обязательный): Только активные.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  assignFilters(
    ids: [10]
    users: [{ id: 10 }]
    groups: [20]
    projects: [10]
  ) {
    Boolean
  }
}
```


## [createUserFilter](user_filters/mutation.graphql) Класс мутации на создание пользовательского фильтра
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для создания пользовательского фильтра.
### Возвращаемое значение
- <span style="color: orange;">Filter</span>: Список категорий статуса.


### Пример использования
```graphql
mutation {
  createFilter(
    input: {
      name: "string"
      conditions: [{ attribute: "string", operation: eq }]
    }
  ) {
    Filter {
      id
      parentId
      childrenId
      name
      taskType
      creatorId
      category
      groupedFilters
      count
      onlyActualRevision
      showCompleted
      isSystemFilter
      isGlobalFilter
      showCounter
      groupByField
      excludedUsersId
      usersId
      projectsId
      isDelimiter
      filterDelimiterId
      filtersWithDelimeterId
    }
  }
}
```


## [patchUserFilter](user_filters/mutation.graphql) Класс мутации на обновление пользовательского фильтра
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор фильтра.
- <span style="color: orange;">input</span> (обязательный): Инпут для обновления пользовательского фильтра.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  patchUserFilter(
    id: 10  
    input: {
      name: "string"
      conditions: [{ attribute: "string", operation: eq }]
    }
  ) {
    Boolean
  }
}
```


## [deleteUserFilter](user_filters/mutation.graphql) Класс мутации на удаление пользовательского фильтра
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор фильтра.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteUserFilter(id: 10) {
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сущностями фильтра

## [getFilters](user_filters/query.graphql) Получение всех фильтров
### Аргументы
- <span style="color: orange;">usersId</span> (default_value=None): Типы задач.
- <span style="color: orange;">projectsId</span> (default_value=None): Только активные.
### Возвращаемое значение
- <span style="color: orange;">[Filter]</span>: Список фильтров.


### Пример использования
```graphql
query {
  getFilters {
    Filter {
      id
      parentId
      childrenId
      name
      taskType
      creatorId
      category
      groupedFilters
      count
      onlyActualRevision
      showCompleted
      isSystemFilter
      isGlobalFilter
      showCounter
      groupByField
      excludedUsersId
      usersId
      projectsId
      isDelimiter
      filterDelimiterId
      filtersWithDelimeterId
    }
  }
}
```


## [getUserFilters](user_filters/query.graphql) Получение всех пользовательских фильтров
### Аргументы
- <span style="color: orange;">projectsId</span> (обязательный): Только активные.
- <span style="color: orange;">category</span> (default_value=None): Типы категории.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[Filter]</span>: Список фильтров.


### Пример использования
```graphql
query {
  getUserFilters(projectsId: [10]) {
    Filter {
      id
      parentId
      childrenId
      name
      taskType
      creatorId
      category
      groupedFilters
      count
      onlyActualRevision
      showCompleted
      isSystemFilter
      isGlobalFilter
      showCounter
      groupByField
      excludedUsersId
      usersId
      projectsId
      isDelimiter
      filterDelimiterId
      filtersWithDelimeterId
    }
  }
}
```


# Модуль общих мутаций для взаимодействия с сервисом задачника

## [createTask](mutation.graphql) Класс мутации на создание задачи
### Аргументы
- <span style="color: orange;">typename</span> (обязательный): Тип создаваемой задачи.
- <span style="color: orange;">input</span> (обязательный): Информация для изменения задачи.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.


### Пример использования
```graphql
mutation {
  createTask(typeName: "string", input: JSONTask) {
    JSONTask
  }
}
```


## [patchTask](mutation.graphql) Класс мутации на обновление задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор изменяемой задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип создаваемой задачи.
- <span style="color: orange;">input</span> (обязательный): Информация для изменения задачи.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.


### Пример использования
```graphql
mutation {
  patchTask(id:10, typeName: "string", input: JSONTask) {
    JSONTask
  }
}
```


## [deleteTask](mutation.graphql) Класс мутации на удаление задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор изменяемой задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип создаваемой задачи.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.


### Пример использования
```graphql
mutation {
  deleteTask(id:10, typeName: "string") {
    JSONTask
  }
}
```


## [deleteTasks](mutation.graphql) Класс мутации на удаление задач
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Список удаляемых задач.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteTasks(input: [{ id:10, typeName: "string" }]) {
    Boolean
  }
}
```


## [deleteJobTasksByShiftWorks](mutation.graphql) Класс мутации на удаление задач по сменным работам
### Аргументы
- <span style="color: orange;">ids</span> (обязательный): Список идентификаторов сменных работ.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteJobTasksByShiftWorks(ids: [10]) {
    Boolean
  }
}
```


## [changeProjectSettings](mutation.graphql) Класс мутации на удаление задач
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">taskTypes</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeProjectSettings(id: 10, taskTypes: "string") {
    Boolean
  }
}
```


## [changeUserSettings](mutation.graphql) Класс мутации на обновление прав у пользователя
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">permissions</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeUserSettings(id: 10 permissions: [{taskType: "string", read: True, create: True, patch: True, delete: True}]) {
    Boolean
  }
}
```


## [changeUsersSettingsPermissions](mutation.graphql) Класс мутации на обновление прав у пользователей
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут настройки разрешений пользователя.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeUsersSettingsPermissions(
    input: [
      {
        id: 10
        permissions: [
          {
            taskType: "string"
            read: True
            create: True
            patch: True
            delete: True
          }
        ]
      }
    ]
  ) {
    Boolean
  }
}
```


## [changeGroupSettings](mutation.graphql) Класс мутации на обновление прав у группы
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор группы.
- <span style="color: orange;">input</span> (обязательный): Инпут настройки разрешений группы.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  changeGroupSettings(id: 10 permissions: [{taskType: "string", read: True, create: True, patch: True, delete: True}]) {
    Boolean
  }
}
```


## [addComment](mutation.graphql) Класс мутации на добавление комментария
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">attribute</span> (обязательный): Атрибут.
- <span style="color: orange;">comment</span> (обязательный): Комментарий.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  addComment(
    id: 10
    typename: "string"
    attribute: "string"
    comment: "string"
  ) {
    Boolean
  }
}
```


## [createTaskCategory](mutation.graphql) Класс мутации на создание категории
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для создания категории.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  createTaskCategory(
    input: {name: "string", description: "string"}
  ) {
    TaskCategory {
      id
      name
      description
      url_path
    }
  }
}
```


## [patchTaskCategory](mutation.graphql) Класс мутации на обновление категории
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор категории.
- <span style="color: orange;">input</span> (обязательный): Инпут для создания категории.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  patchTaskCategory(id: 10, input: { name: "string", description: "string" }) {
    Boolean
  }
}
```


## [deleteTaskCategory](mutation.graphql) Класс мутации на удаление категории
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор категории.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteTaskCategory(id: 10) {
    Boolean
  }
}
```


## [createModule](mutation.graphql) Класс мутации на создание модуля
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для создания модуля.
### Возвращаемое значение
- <span style="color: orange;">Module</span>: Объект модуля.


### Пример использования
```graphql
mutation {
  createModule(input: {name: "string" description: "string"}) {
    Module {
      id
      name
      description
      url_path
    }
  }
}
```


## [patchModule](mutation.graphql) Класс мутации на обновление модуля
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор модуля.
- <span style="color: orange;">input</span> (обязательный): Инпут для обновления модуля.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  patchModule(id: 10, input: {name: "string" description: "string"}) {
    Boolean
  }
}
```


## [deleteModule](mutation.graphql) Класс мутации на удаление модуля
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор модуля.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteModule(id: 10) {
    Boolean
  }
}
```


## [createTaskType](mutation.graphql) Класс мутации на создание типа задачи
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения типа задачи.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.


### Пример использования
```graphql
mutation {
  createTaskType(
    input: { description: "string", name: "string", isAbstract: true }
  ) {
    TaskType {
      id
      description
      name
      parent
      children
      dependencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [patchTaskType](mutation.graphql) Класс мутации на обновление типа задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор типа задачи.
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения типа задачи.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.


### Пример использования
```graphql
mutation {
  patchTaskType(
    id: 10  
    input: { description: "string", name: "string", isAbstract: true }
  ) {
    TaskType {
      id
      description
      name
      parent
      children
      dependencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [deleteTaskType](mutation.graphql) Класс мутации на удаление типа задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор типа задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteTaskType(id: 10) {
    Boolean
  }
}
```


## [createField](mutation.graphql) Класс мутации на удаление поля задачи
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">FieldType</span>: Поле задачи.


### Пример использования
```graphql
mutation {
  createField(input: { name: "string", description: "string" }) {
    FieldType {
      fieldId
      name
      description
      fullDescription
      userHint
      valueAttribute
      attribute
      valueType
      type
      isSystemField
      clearWhenClone
      clearWhenRevision
    }
  }
}
```


## [patchField](mutation.graphql) Класс мутации на обновление поля задачи
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Название поля типа задачи.
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">FieldType</span>: Поле задачи.


### Пример использования
```graphql
mutation {
  patchField(name :"string", input: { name: "string", description: "string" }) {
    FieldType {
      fieldId
      name
      description
      fullDescription
      userHint
      valueAttribute
      attribute
      valueType
      type
      isSystemField
      clearWhenClone
      clearWhenRevision
    }
  }
}
```


## [deleteField](mutation.graphql) Класс мутации на удаление поля задачи
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Название поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteField(name :"string") {
    Boolean
  }
}
```


## [createAttribute](mutation.graphql) Класс мутации на создание атрибута
### Аргументы
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения атрибута.
### Возвращаемое значение
- <span style="color: orange;">AttributeType</span>: Атрибут.


### Пример использования
```graphql
mutation {
  createAttribute(
    input: {
      name: "string"
      description: "string"
      fields: [
        {
          description: "string"
          name: "string"
          readOnly: true
          required: true
          isList: true
        }
      ]
    }
  ) {
    AttributeType {
      id
      description
      name
      fields
    }
  }
}
```


## [patchAttribute](mutation.graphql) Класс мутации на обновления атрибута
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор атрибута.
- <span style="color: orange;">input</span> (обязательный): Инпут для изменения атрибута.
### Возвращаемое значение
- <span style="color: orange;">AttributeType</span>: Атрибут.


### Пример использования
```graphql
mutation {
  patchAttribute(
    id: 10  
    input: {
      name: "string"
      description: "string"
      fields: [
        {
          description: "string"
          name: "string"
          readOnly: true
          required: true
          isList: true
        }
      ]
    }
  ) {
    AttributeType {
      id
      description
      name
      fields
    }
  }
}
```


## [addTaskTypeFields](mutation.graphql) Класс мутации на изменения свойства полей в типе задачи
### Аргументы
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">fields</span> (обязательный): Инпут для изменения поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.


### Пример использования
```graphql
mutation {
  addTaskTypeFields(typename: "string", fields: [{name: "string"}]) {
    TaskType {
      id
      description
      name
      parent
      children
      dependencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [addTaskTypeFields](mutation.graphql) Класс мутации на изменения свойства полей в типе задачи
### Аргументы
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">fields</span> (обязательный): Инпут для изменения поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.


### Пример использования
```graphql
mutation {
  addTaskTypeFields(typename: "string", fields: [{name: "string"}]) {
    TaskType {
      id
      description
      name
      parent
      children
      dependencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [patchTaskTypeFields](mutation.graphql) Класс мутации на изменения свойства полей в типе задачи
### Аргументы
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">fields</span> (обязательный): Инпут для изменения поля типа задачи.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.


### Пример использования
```graphql
mutation {
  patchTaskTypeFields(typename: "string", fields: [{name: "string"}]) {
    TaskType {
      id
      description
      name
      parent
      children
      dependencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [generateTaskEnumerator](mutation.graphql) Класс мутации на генерирование номера задачи
### Аргументы
- <span style="color: orange;">input</span> (default_value=None): Объект генерации номера задачи.
### Возвращаемое значение
- <span style="color: orange;">[GenerateTaskEnumeratorResult]</span>: Объект генерации номера задачи.


### Пример использования
```graphql
mutation {
  generateTaskEnumerator(input: {id: 10, typename: "string", projectId: 10}) {
    GenerateTaskEnumeratorResult {
      field
      value
    }
  }
}
```


## [saveUserSettingsColumns](mutation.graphql) Класс мутации на сохранение пользовательских настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">filterId</span> (default_value=None): Идентификатор настроек.
- <span style="color: orange;">module</span> (обязательный): Название модуля.
- <span style="color: orange;">columns</span> (обязательный): Атрибуты столбцов.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  saveUserSettingsColumns(filterId: 10, module: "string", columns: [{field: "string"}]) {
    Boolean
  }
}
```


## [resetUserSettingsColumns](mutation.graphql) Класс мутации на сброс пользовательских настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">filterId</span> (default_value=None): Идентификатор настроек.
- <span style="color: orange;">module</span> (обязательный): Название модуля.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetUserSettingsColumns(filterId: 10, module: "string") {
    Boolean
  }
}
```


## [saveSystemSettingsColumns](mutation.graphql) Класс мутации на сохранение системных настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">filterId</span> (default_value=None): Идентификатор настроек.
- <span style="color: orange;">module</span> (обязательный): Название модуля.
- <span style="color: orange;">columns</span> (обязательный): Атрибуты столбцов.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  saveSystemSettingsColumns(filterId: 10, module: "string", columns: [{field: "string"}]) {
    Boolean
  }
}
```


## [resetSystemSettingsColumns](mutation.graphql) Класс мутации на сброс системных настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">filterId</span> (default_value=None): Идентификатор настроек.
- <span style="color: orange;">module</span> (обязательный): Название модуля.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetSystemSettingsColumns(filterId: 10, module: "string") {
    Boolean
  }
}
```


## [deleteReport](mutation.graphql) Класс мутации на удаление отчета
### Аргументы
- <span style="color: orange;">id</span> (default_value=None): Идентификатор отчета.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteReport(id: 10) {
    Boolean
  }
}
```


## [deleteReports](mutation.graphql) Класс мутации на удаление отчетов
### Аргументы
- <span style="color: orange;">taskType</span> (default_value=None): Тип задач.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
- <span style="color: orange;">startDate</span> (default_value=None): Начало интервала.
- <span style="color: orange;">dueDate</span> (default_value=None): Конец интервала.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  deleteReports(projectId: 10) {
    Boolean
  }
}
```


## [cloneTask](mutation.graphql) Класс мутации на копирование задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (обязательный): Тип задач.
### Возвращаемое значение
- <span style="color: orange;">ID</span>: Идентификатор задачи.


### Пример использования
```graphql
mutation {
  cloneTask(id: 10, taskType: "string") {
    ID
  }
}
```


## [createRevision](mutation.graphql) Класс мутации на создание версии задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (обязательный): Тип задач.
- <span style="color: orange;">oldRevisionState</span> (default_value=None): Состояние старой версии задачи.
- <span style="color: orange;">newRevisionState</span> (default_value=None): Состояние новой версии задачи.
### Возвращаемое значение
- <span style="color: orange;">ID</span>: Идентификатор задачи.


### Пример использования
```graphql
mutation {
  createRevision(id: 10, taskType: "string") {
    ID
  }
}
```


## [addNestedTask](mutation.graphql) Класс мутации на добавление вложенной задачи
### Аргументы
- <span style="color: orange;">parentId</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">parentTaskType</span> (обязательный): Тип задач.
- <span style="color: orange;">nestedId</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">nestedTaskType</span> (обязательный): Тип задач.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  addNestedTask(parentId: 10, parentTaskType: "string", nestedId: 10, nestedTaskType: "string") {
    Boolean
  }
}
```


## [updateRelationFieldsInTask](mutation.graphql) Класс мутации на обновление вложенной задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (обязательный): Тип задач.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateRelationFieldsInTask(id: 10, taskType: "string") {
    Boolean
  }
}
```


## [parseFromFileStorage](mutation.graphql) Класс мутации на массовое создание документов по структуре папок файлового хранилища
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">projectDirGuid</span> (обязательный): GUID корневой директории хранилища проекта.
- <span style="color: orange;">dirPath</span> (обязательный): Директория со структурой для парсинга.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseFromFileStorage(projectId: 10, projectDirGuid: "string", dirPath: "string") {
    Boolean
  }
}
```


## [createTasksFromChart](mutation.graphql) Класс мутации на создание задач по графику
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">projectTransactionId</span> (обязательный): Идентификатор транзакции.
- <span style="color: orange;">startDate</span> (обязательный): Начало интервала.
- <span style="color: orange;">dueDate</span> (обязательный): Конец интервала.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">description</span> (обязательный): Описание задачи.
- <span style="color: orange;">createForWorksWithTasks</span> (обязательный): Флаг повторного создания задач.
- <span style="color: orange;">createInProcess</span> (default_value=None): Флаг, что нужно создавать в состоянии process.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.


### Пример использования
```graphql
mutation {
  createTasksFromChart(
    projectId: 10
    projectTransactionId: 10
    startDate: "2024-01-01"
    dueDate: "2024-01-01"
    typename: "string"
    description: "string"
    createForWorksWithTasks: false
  ) {
    Boolean
  }
}
```


## [uploadAllPrescription](mutation.graphql) Класс мутации на выгрузку всех предписания
### Аргументы
- <span style="color: orange;">cleanBefore</span> (default_value=False): Предварительно очистить таблицу с предписаниями.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  uploadAllPrescription(cleanBefore: false) {
    Boolean
  }
}
```


## [uploadWeeklyFundingData](mutation.graphql) Класс мутации на принудительную выгрузку данных из отчета WeeklyFundingReport в postgres
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  uploadWeeklyFundingData {
    Boolean
  }
}
```


## [uploadWeeklyFundingDetailedPaymentData](mutation.graphql) Класс мутации на принудительную выгрузку данных по платежам в postgres
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  uploadWeeklyFundingDetailedPaymentData {
    Boolean
  }
}
```


## [uploadAvtodorDashboardData](mutation.graphql) Класс мутации на принудительную выгрузку данных дашборда для Автодор в postgres
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  uploadAvtodorDashboardData {
    Boolean
  }
}
```


## [updateGraphQLSchema](mutation.graphql) Класс мутации на обновление схемы GraphQL
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateGraphQLSchema {
    Boolean
  }
}
```


## [resetCache](mutation.graphql) Класс мутации на сброс кэша
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  resetCache {
    Boolean
  }
}
```


## [grantAllPrivileges](mutation.graphql) Класс мутации на получение привилегий всех пользователей
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  grantAllPrivileges {
    Boolean
  }
}
```


## [dropSchemaCache](mutation.graphql) Класс мутации на сброс кэша схемы
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  dropSchemaCache {
    Boolean
  }
}
```


## [updateDropdownValuesInMongo](mutation.graphql) Класс мутации на обновление имени во всех выпадающих полях во всех задачах
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  updateDropdownValuesInMongo {
    Boolean
  }
}
```


## [startMachineApplicationLoader](mutation.graphql) Класс мутации на запуск процесса выгрузки заявок в задачник
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  startMachineApplicationLoader {
    Boolean
  }
}
```


## [manualCreateRequisitionMB](mutation.graphql) Класс мутации на создание заявки для Мостового Бюро вручную
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  manualCreateRequisitionMB(id: 10, typename: "string") {
    Boolean
  }
}
```


## [parseRelatedDropdownItems](mutation.graphql) Класс мутации на парсинг связанных выпадающих элементов
### Аргументы
- <span style="color: orange;">count</span> (обязательный): Количество.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseRelatedDropdownItems(count: 10) {
    Boolean
  }
}
```


## [parseWorkDocumentationItems](mutation.graphql) Класс мутации на парсинг полей из excel файла для черновиков БАМ
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">userId</span> (обязательный): Идентификатор пользователя.
- <span style="color: orange;">fileName</span> (обязательный): Наименование файла.
- <span style="color: orange;">cellStart</span> (обязательный): Начальная ячейка файла.
- <span style="color: orange;">cellEnd</span> (обязательный): Последняя ячейка файла.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  parseWorkDocumentationItems(projectId: 10, userId: 10, fileName: "string", cellStart: "A1", cellEnd: "J100") {
    Boolean
  }
}
```


## [migrateFilesToS3](mutation.graphql) Класс мутации на миграцию файлов и медиа на хранилище S3
### Аргументы
- <span style="color: orange;">typenames</span> (обязательный): Список наименований файлов.
- <span style="color: orange;">projectIds</span> (обязательный): Список идентификаторов проектов.
- <span style="color: orange;">deleteOld</span> (обязательный): Флаг удаления старых файлов.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.


### Пример использования
```graphql
mutation {
  migrateFilesToS3(typenames: ["string"], projectIds: [10], deleteOld: true) {
    Boolean
  }
}
```


## [cleanupMigratedFiles](mutation.graphql) Класс мутации на удаление мигрированных файлов 
### Аргументы
- <span style="color: orange;">typenames</span> (обязательный): Список наименований файлов.
- <span style="color: orange;">projectIds</span> (обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">Boolean</span>: Успешность операции.

### Пример использования
```graphql
mutation {
  cleanupMigratedFiles(typenames: ["string"], projectIds: [10]) {
    Boolean
  }
}
```


# Модуль запросов для взаимодействия с сервисом задачника

## [getVersion](query.graphql) Получение версии схемы
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">DateTime</span>: Объект даты и времени.

### Пример использования
```graphql
query {
  getVersion {
    DateTime
  }
}
```


## [myDraftTasks](query.graphql) Получение черновиков
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myDraftTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myFavoriteTasks](query.graphql) Получение избранных
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myFavoriteTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myIncomingTasks](query.graphql) Получение входящих задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myIncomingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myProcessIncomingTasks](query.graphql) Получение входящих задач в работе
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myProcessIncomingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myCompleteIncomingTasks](query.graphql) Получение выполненных входящих задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myCompleteIncomingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myOutgoingTasks](query.graphql) Получение исходящих задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myOutgoingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myDraftOutgoingTasks](query.graphql) Получение исходящих черновиков
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myDraftOutgoingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myProcessOutgoingTasks](query.graphql) Получение исходящих задач в работе
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myProcessOutgoingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myCompleteOutgoingTasks](query.graphql) Получение выполненных исходящих задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myCompleteOutgoingTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allTasks](query.graphql) Получение всех задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allProcessTasks](query.graphql) Получение всех задач в работе
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allProcessTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allCompleteTasks](query.graphql) Получение всех завершенных задач
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allCompleteTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myDraftDocuments](query.graphql) Получение документов в черновике
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myDraftDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myOutgoingDocuments](query.graphql) Получение документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myOutgoingDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myEditedDocuments](query.graphql) Получение правленных документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myEditedDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myAgreedOutgoingDocuments](query.graphql) Получение исходящих на согласовании документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myAgreedOutgoingDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myAgreedIncomingDocuments](query.graphql) Получение входящих ожидающие согласование документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myAgreedIncomingDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [myAgreedIncomingProcessedDocuments](query.graphql) Получение входящих согласованных/несогласованных мной документы
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  myAgreedIncomingProcessedDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [mySignedOutgoingDocuments](query.graphql) Получение исходящих на подписание документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  mySignedOutgoingDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [mySignedIncomingDocuments](query.graphql) Получение входящих ожидающих подписание документы
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  mySignedIncomingDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [mySignedIncomingProcessedDocuments](query.graphql) Получение входящих подписанных/неподписанных мной документы
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  mySignedIncomingProcessedDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allDocuments](query.graphql) Получение всех документов
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allDocuments(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allDraftTasks](query.graphql) Получение всех черновиков
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allDraftTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [allTasksWithError](query.graphql) Получение всех задач с ошибками процесса
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  allTasksWithError(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [filteredTasks](query.graphql) Получение задач пользовательского фильтра
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  filteredTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [groupedFilteredTasks](query.graphql) Получение всех задач пользовательского фильтра
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  groupedFilteredTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [filteredRelationTasks](query.graphql) Получение всех задач пользовательского фильтра
### Аргументы
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
- <span style="color: orange;">searchString</span> (default_value=None): Строка поиска задач по имени.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">sortBy</span> (default_value=None): Сортировка по полю.
- <span style="color: orange;">taskType</span> (default_value=None): Тип задачи.
- <span style="color: orange;">parentRelations</span> (default_value=None): Идентификаторы и типы родительских задач из родительского поля "Связь".
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
- <span style="color: orange;">filterTaskTypes</span> (default_value=None): Фильтрация по типу задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  filteredRelationTasks(page: 1, projectsId: [10]) {
    JSONTask
  }
}
```


## [getTaskById](query.graphql) Получение задачи по ID
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">disablePermissionCheck</span> (default_value=False): Отключить проверку прав (работает только для определенных типов).
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.

### Пример использования
```graphql
query {
  getTaskById(id: 1, typename: "string") {
    JSONTask
  }
}
```


## [getTasksByCipher](query.graphql) Получение задачи по шифру и номеру изменения
### Аргументы
- <span style="color: orange;">documentNumber</span> (default_value=None): Номер документа.
- <span style="color: orange;">changeName</span> (default_value=None): Наименование изменения.
- <span style="color: orange;">changeNumber</span> (default_value=False): Номер изменения.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">documentDate</span> (default_value=None): Дата документа.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  getTasksByCipher(typename: "string") {
    JSONTask
  }
}
```


## [getTasksById](query.graphql) Получение задач по ID
### Аргументы
- <span style="color: orange;">ids</span> (default_value=None): Идентификаторы задач.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  getTasksById(typename: "string") {
    JSONTask
  }
}
```


## [getTasksStatusesById](query.graphql) Получение информации о статусах задач по списку ID
### Аргументы
- <span style="color: orange;">ids</span> (default_value=None): Идентификаторы задач.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">page</span> (default_value=None): Номер страницы.
- <span style="color: orange;">perPage</span> (default_value=None): Количество элементов на странице.
### Возвращаемое значение
- <span style="color: orange;">[TaskStatusType]</span>: Информация о статусе задачи и его цвете.

### Пример использования
```graphql
query {
  getTasksStatusesById(typename: "string") {
    TaskStatusType {
      taskId
      status
      color
      statusCategoryPriority
    }
  }
}
```


## [getTasksByPid](query.graphql) Получение информации о статусах задач по списку ID
### Аргументы
- <span style="color: orange;">pid</span> (обязательный): Process Instance Id задачи.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  getTasksByPid(pid: "string") {
    JSONTask
  }
}
```


## [getDocumentByGuid](query.graphql) Получение информации о статусах задач по списку ID
### Аргументы
- <span style="color: orange;">guid</span> (обязательный): GUID документа из 1С.
- <span style="color: orange;">typename</span> (обязательный): Тип документа.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.

### Пример использования
```graphql
query {
  getDocumentByGuid(guid: "string", typename: "string") {
    JSONTask
  }
}
```


## [getTaskHistoryById](query.graphql) Получение истории изменений задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
### Возвращаемое значение
- <span style="color: orange;">[HistoryResult]</span>: Список объектов истории изменений.

### Пример использования
```graphql
query {
  getTaskHistoryById(id: 10) {
    HistoryResult {
      action
      new
      old
      dateChanged
      userId
    }
  }
}
```


## [getProjectHistoryById](query.graphql) Получение истории изменений по проекту
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">page</span> (обязательный): Номер страницы.
- <span style="color: orange;">perPage</span> (обязательный): Количество элементов на странице.
- <span style="color: orange;">categories</span> (default_value=None): Категории задач.
- <span style="color: orange;">filters</span> (default_value=None): Пользовательские фильтры.
### Возвращаемое значение
- <span style="color: orange;">[ProjectHistoryResult]</span>: Список объектов истории изменений по проекту.

### Пример использования
```graphql
query {
  getProjectHistoryById(id: 10, page: 5, perPage: 10) {
    ProjectHistoryResult {
      id
      name
      typename
      category
      action
      dateChanged
      userId
      cipher
    }
  }
}
```


## [getIdsUsersAndTypenamesForProjectHistory](query.graphql) Получение различных идентификаторов пользователей и различных типов документов для запроса getProjectHistoryById
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">categories</span> (default_value=None): Категории задач.
- <span style="color: orange;">filters</span> (default_value=None): Пользовательские фильтры.
### Возвращаемое значение
- <span style="color: orange;">UsersIdsAndTypenames</span>: Типы документов и ids пользователей.

### Пример использования
```graphql
query {
  getIdsUsersAndTypenamesForProjectHistory(id: 10, page: 5, perPage: 10) {
    UsersIdsAndTypenames{
      users_ids
      typenames
    }
  }
}
```


## [getTaskRevisionById](query.graphql) Получение версии задачи
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор задачи.
- <span style="color: orange;">typename</span> (обязательный): Тип задачи.
### Возвращаемое значение
- <span style="color: orange;">JSONTask</span>: Объект JSONTask.

### Пример использования
```graphql
query {
  getTaskRevisionById(id: 10, typename: "string") {
    JSONTask
  }
}
```


## [count](query.graphql) Получение количества задач в системных фильтрах
### Аргументы
- <span style="color: orange;">filters</span> (обязательный): Фильтры, для которых получить количество задач.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[CountResult]</span>: Количество задач по определенному фильтру.

### Пример использования
```graphql
query {
  count(filters: ["string"]) {
    CountResult {
      filter
      count
    }
  }
}
```


## [countUserFilter](query.graphql) Получение количества задач в пользовательских фильтрах
### Аргументы
- <span style="color: orange;">filters</span> (обязательный): Фильтры, для которых получить количество задач.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[CountResult]</span>: Количество задач по определенному фильтру.

### Пример использования
```graphql
query {
  countUserFilter(filters: ["string"]) {
    CountResult {
      filter
      count
    }
  }
}
```


## [countGroupedUserFilter](query.graphql) Получение количества задач в пользовательских фильтрах
### Аргументы
- <span style="color: orange;">parentFilterId</span> (обязательный): Идентификатор родительского пользовательского фильтра.
- <span style="color: orange;">groupedFilterCondition</span> (обязательный): Условия фильтрации.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[CountResult]</span>: Количество задач по определенному фильтру.

### Пример использования
```graphql
query {
  countGroupedUserFilter(
    parentFilterId: 10
    groupedFilterCondition: [{ value: "string", field: "string" }]
  ) {
    CountResult {
      filter
      count
    }
  }
}
```


## [countByProjects](query.graphql) Получение количества задач в системных фильтрах сгруппированное по проектам
### Аргументы
- <span style="color: orange;">filters</span> (обязательный): Идентификатор родительского пользовательского фильтра.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterDate</span> (default_value=None): Значения для фильтрации по столбцам.
### Возвращаемое значение
- <span style="color: orange;">[CountByProjectResult]</span>: Количество задач по определенному фильтру по каждому проекту.

### Пример использования
```graphql
query {
  countByProjects(filters: ["string"]) {
    CountByProjectResult {
      projectId
      filterCount
    }
  }
}
```


## [countUserFilterByProjects](query.graphql) Получение количества задач в пользовательских фильтрах сгруппированное по проектам
### Аргументы
- <span style="color: orange;">filters</span> (обязательный): Идентификатор пользовательского фильтра.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[CountByProjectResult]</span>: Количество задач по определенному фильтру по каждому проекту.

### Пример использования
```graphql
query {
  countUserFilterByProjects(id: 10) {
    CountByProjectResult {
      projectId
      filterCount
    }
  }
}
```


## [countGroupedUserFilterByProjects](query.graphql) Получение количества задач в пользовательских фильтрах сгруппированное по проектам
### Аргументы
- <span style="color: orange;">parentFilterId</span> (обязательный): Идентификатор родительского пользовательского фильтра.
- <span style="color: orange;">groupedFilterCondition</span> (обязательный): Условия фильтрации.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">[CountByProjectResult]</span>: Количество задач по определенному фильтру по каждому проекту.

### Пример использования
```graphql
query {
  countGroupedUserFilterByProjects(
    parentFilterId: 10
    groupedFilterCondition: [{ value: "string", field: "string" }]
  ) {
    CountByProjectResult {
      projectId
      filterCount
    }
  }
}
```


## [getSystemFilterColumnValues](query.graphql) Получение всех уникальных значений (JSON массив) в столбце в системном фильтре (для фильтрации по значениям в столбцах)
### Аргументы
- <span style="color: orange;">filter</span> (обязательный): Фильтр, для которого нужно получить уникальные значения.
- <span style="color: orange;">field</span> (обязательный): Поле, для которого нужно получить уникальные значения.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">Text</span>: JSON массив.

### Пример использования
```graphql
query {
  getSystemFilterColumnValues(filter: "string", field: "string") {
    Text
  }
}
```


## [getUserFilterColumnValues](query.graphql) Получение всех уникальных значений (JSON массив) в столбце в пользовательском фильтре (для фильтрации по значениям в столбцах)
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор пользовательского фильтра.
- <span style="color: orange;">field</span> (обязательный): Поле, для которого нужно получить уникальные значения.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">Text</span>: JSON массив.

### Пример использования
```graphql
query {
  getUserFilterColumnValues(id: 10, field: "string") {
    Text
  }
}
```


## [getGroupedUserFilterColumnValues](query.graphql) Получение всех уникальных значений (JSON массив) в столбце в сгруппированном пользовательском фильтре (для фильтрации по значениям в столбцах)
### Аргументы
- <span style="color: orange;">parentFilterId</span> (обязательный): Идентификатор родительского пользовательского фильтра.
- <span style="color: orange;">groupedFilterCondition</span> (обязательный): Условия фильтрации.
- <span style="color: orange;">field</span> (обязательный): Поле, для которого нужно получить уникальные значения.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
- <span style="color: orange;">category</span> (default_value=None): Категория типов.
- <span style="color: orange;">filterFieldValues</span> (default_value=None): Значения для фильтрации по столбцам.
- <span style="color: orange;">filterDate</span> (default_value=None): Фильтрация по дате.
### Возвращаемое значение
- <span style="color: orange;">Text</span>: JSON массив.

### Пример использования
```graphql
query {
  getGroupedUserFilterColumnValues(
    parentFilterId: 10
    field: "string"
    groupedFilterCondition: [{ value: "string", field: "string" }]
  ) {
    Text
  }
}
```


## [search](query.graphql) Поиск
### Аргументы
- <span style="color: orange;">query</span> (обязательный): Строка для поиска.
- <span style="color: orange;">category</span> (default_value=None): Категория.
- <span style="color: orange;">projectsId</span> (default_value=None): Идентификаторы проектов.
### Возвращаемое значение
- <span style="color: orange;">[JSONTask]</span>: Список объектов JSONTask.

### Пример использования
```graphql
query {
  search(query: "string") {
    JSONTask
  }
}
```


## [getBimStructure](query.graphql) Получение списка элементов БИМ-модели
### Аргументы
- <span style="color: orange;">modelIds</span> (обязательный): Список идентификаторов модели (UUID XKT файла версии модели).
### Возвращаемое значение
- <span style="color: orange;">[BimStructureElement]</span>: Список элементов БИМ с цветом и статусом.

### Пример использования
```graphql
query {
  getBimStructure(modelIds: ["string"]) {
    BimStructureElement {
      elementId
      status
      color
      statusCategoryPriority
    }
  }
}
```


## [searchByBimElementIds](query.graphql) Поиск по элементу БИМ-модели
### Аргументы
- <span style="color: orange;">elementIds</span> (обязательный): Список идентификаторов элементов.
### Возвращаемое значение
- <span style="color: orange;">[BimElementSearchResult]</span>: Список объектов связанные с элементами БИМ, найденные с помощью поиска.

### Пример использования
```graphql
query {
  searchByBimElementIds(elementIds: ["string"]) {
    BimElementSearchResult {
      id
      name
      typename
      typenameDescription
      status
      color
      state
      elementIds
      modelIds
    }
  }
}
```


## [searchByWork](query.graphql) Поиск по Работам
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор работы.
### Возвращаемое значение
- <span style="color: orange;">[WorkSearchResult]</span>: Список объектов связанные с работой, найденные с помощью поиска.

### Пример использования
```graphql
query {
  searchByWork(id: "string") {
    WorkSearchResult {
      id
      name
      typename
      status
      color
      state
      workId
      createDate
      files
      startDate
      dueDate
      projectStage
      contractor
      module
    }
  }
}
```



## [searchByWorks](query.graphql) Поиск по Работам
### Аргументы
- <span style="color: orange;">ids</span> (обязательный): Идентификаторы работ.
- <span style="color: orange;">taskTypes</span> (default_value=None): Типы задач.
- <span style="color: orange;">date</span> (default_value=None): Поиск по дате.
- <span style="color: orange;">returnExpiredNotCompleted</span> (default_value=False): Вернуть просроченные незавершенные задачи.
### Возвращаемое значение
- <span style="color: orange;">[WorkSearchResult]</span>: Список объектов связанные с работой, найденные с помощью поиска.

### Пример использования
```graphql
query {
  searchByWorks(ids: [10]) {
    WorkSearchResult {
      id
      name
      typename
      status
      color
      state
      workId
      createDate
      files
      startDate
      dueDate
      projectStage
      contractor
      module
    }
  }
}
```


## [searchByShiftWork](query.graphql) Поиск по Сменной работе
### Аргументы
- <span style="color: orange;">id</span> (обязательный): Идентификатор сменной работы.
### Возвращаемое значение
- <span style="color: orange;">[ShiftWorkSearchResult]</span>: Список объектов связанные со сменной работой, найденные с помощью поиска.

### Пример использования
```graphql
query {
  searchByShiftWork(ids: [10]) {
    ShiftWorkSearchResult {
      id
      name
      typename
      status
      color
      state
      shiftWorkId
      createDate
      files
      participant
      checker
    }
  }
}
```


## [searchByShiftWorks](query.graphql) Поиск по Сменным работам
### Аргументы
- <span style="color: orange;">ids</span> (обязательный): Список идентификаторов сменных работ.
- <span style="color: orange;">taskTypes</span> (default_value=None): Типы задач.
- <span style="color: orange;">date</span> (default_value=None): Поиск по дате.
### Возвращаемое значение
- <span style="color: orange;">[ShiftWorkSearchResult]</span>: Список объектов связанные со сменной работой, найденные с помощью поиска.

### Пример использования
```graphql
query {
  searchByShiftWorks(ids: [10]) {
    ShiftWorkSearchResult {
      id
      name
      typename
      status
      color
      state
      shiftWorkId
      createDate
      files
      participant
      checker
    }
  }
}
```


## [getProjectWorkDocumentation](query.graphql) Поиск по Сменным работам
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">lastVersion</span> (default_value=False): Вернуть только последнюю версию или нет.
### Возвращаемое значение
- <span style="color: orange;">[ProjectWorkDocumentationType]</span>: Список объектов Проектной и Рабочей документации.

### Пример использования
```graphql
query {
  getProjectWorkDocumentation(projectId: [10]) {
    ProjectWorkDocumentationType {
      id
      type
      name
      date
      url
      version
    }
  }
}
```


## [allAccessGroups](query.graphql) Получение всех групп
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[AccessGroupType]</span>: Список групп доступа.

### Пример использования
```graphql
query {
  allAccessGroups {
    AccessGroupType {
      rowId
      name
      parentAccessGroup_id
      isUserGroup
    }
  }
}
```


## [allUsers](query.graphql) Получение всех пользователей
### Аргументы
- <span style="color: orange;">userId</span> (default_value=None): Идентификатор пользователя.
- <span style="color: orange;">groupId</span> (default_value=None): Идентификатор группы.
### Возвращаемое значение
- <span style="color: orange;">[User]</span>: Список пользователей.

### Пример использования
```graphql
query {
  allUsers {
    User {
      rowId
      username
      email
      education
      active
      courses
      isSuperuser
      phone
      profileImage
      position
      passportNumber
      placeOfRegistration
      licensingCertificates
    }
  }
}
```


## [getProjectSettings](query.graphql) Получение настроек проекта
### Аргументы
- <span style="color: orange;">id</span> (Обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">[ProjectSettingsType]</span>: Список настроек проекта.

### Пример использования
```graphql
query {
  getProjectSettings(id: 10) {
    ProjectSettingsType {
      id
      taskType
    }
  }
}
```


## [getUserSettings](query.graphql) Получение настроек пользователя
### Аргументы
- <span style="color: orange;">id</span> (Обязательный): Идентификатор пользователя.
- <span style="color: orange;">taskTypes</span> (Обязательный): Типы задач.
### Возвращаемое значение
- <span style="color: orange;">[UserSettingsType]</span>: Список настроек пользователя.

### Пример использования
```graphql
query {
  getUserSettings(id: 10, taskTypes: "string") {
    UserSettingsType {
      id
      userId
      taskType
      read
      create
      patch
      delete
    }
  }
}
```


## [getGroupSettings](query.graphql) Получение настроек группы
### Аргументы
- <span style="color: orange;">id</span> (Обязательный): Идентификатор группы.
### Возвращаемое значение
- <span style="color: orange;">[GroupSettingsType]</span>: Список настроек группы.

### Пример использования
```graphql
query {
  getGroupSettings(id: 10) {
    GroupSettingsType {
      id
      taskType
      read
      create
      patch
      delete
    }
  }
}
```


## [getPermissions](query.graphql) Получение настроек группы
### Аргументы
- <span style="color: orange;">projectsId</span> (Обязательный): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">[UserSettingsType]</span>: Список настроек пользователя.

### Пример использования
```graphql
query {
  getPermissions(id: 10) {
    UserSettingsType {
      id
      userId
      taskType
      read
      create
      patch
      delete
    }
  }
}
```


## [createOneTaskReport](query.graphql) Запрос на создание отчета по задаче
### Аргументы
- <span style="color: orange;">id</span> (Обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (Обязательный): Тип задач.
- <span style="color: orange;">projectId</span> (Обязательный): Идентификатор проекта.
- <span style="color: orange;">typeReport</span> (default_value=None): Тип отчета.
- <span style="color: orange;">formatReport</span> (default_value=None): Формат отчета.
- <span style="color: orange;">filter</span> (default_value=None): Фильтр.
### Возвращаемое значение
- <span style="color: orange;">Report</span>: Объект файла отчета по задаче/задачам.

### Пример использования
```graphql
query {
  createOneTaskReport(id: 10, taskType: "string", projectId: 10) {
    Report {
      fileId
      name
      creatorId
      projectId
      taskType
      createDate
      taskId
      extension
      isFileS3
    }
  }
}
```


## [createMultipleTaskReport](query.graphql) Получение журнала по задачам
### Аргументы
- <span style="color: orange;">taskType</span> (Обязательный): Тип задач.
- <span style="color: orange;">projectId</span> (Обязательный): Идентификатор проекта.
- <span style="color: orange;">startDate</span> (default_value=None): Начало интервала.
- <span style="color: orange;">dueDate</span> (default_value=None): Конец интервала.
- <span style="color: orange;">typeReport</span> (default_value=None): Тип отчета.
- <span style="color: orange;">organizationId</span> (default_value=None): Идентификатор организации.
- <span style="color: orange;">filter</span> (default_value=None): Фильтр.
### Возвращаемое значение
- <span style="color: orange;">Report</span>: Объект файла отчета по задаче/задачам.

### Пример использования
```graphql
query {
  createMultipleTaskReport(taskType: "string", projectId: 10) {
    Report {
      fileId
      name
      creatorId
      projectId
      taskType
      createDate
      taskId
      extension
      isFileS3
    }
  }
}
```


## [getAllReports](query.graphql) Получение всех отчетов
### Аргументы
- <span style="color: orange;">taskType</span> (Обязательный): Тип задач.
- <span style="color: orange;">projectId</span> (Обязательный): Идентификатор проекта.
- <span style="color: orange;">creatorId</span> (Обязательный): Идентификатор создавшего пользователя.
### Возвращаемое значение
- <span style="color: orange;">[Report]</span>: Список объектов файла отчета по задаче/задачам.

### Пример использования
```graphql
query {
  getAllReports(taskType: "string", projectId: 10, creatorId: 10) {
    Report {
      fileId
      name
      creatorId
      projectId
      taskType
      createDate
      taskId
      extension
      isFileS3
    }
  }
}
```


## [getReportsById](query.graphql) Получение отчета по идентификатору
### Аргументы
- <span style="color: orange;">id</span> (Обязательный): Идентификатор задачи.
- <span style="color: orange;">taskType</span> (Обязательный): Тип задач.
- <span style="color: orange;">projectId</span> (Обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">[Report]</span>: Список объектов файла отчета по задаче/задачам.

### Пример использования
```graphql
query {
  getAllReports(id: 10, taskType: "string", projectId: 10) {
    Report {
      fileId
      name
      creatorId
      projectId
      taskType
      createDate
      taskId
      extension
      isFileS3
    }
  }
}
```


## [getAllTaskTypes](query.graphql) Получение всех типов отчетов
### Аргументы
- <span style="color: orange;">withoutPermissionCheck</span> (default_value=False): Флаг проверки разрешений.
- <span style="color: orange;">categories</span> (default_value=None): Тип задач.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">[TaskType]</span>: Список типов задач.

### Пример использования
```graphql
query {
  getAllTaskTypes(projectId: 10) {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getTaskTypesByAttributes](query.graphql) Получение типа отчета по идентификатору
### Аргументы
- <span style="color: orange;">attributes</span> (обязательный): Список наименований атрибутов.
### Возвращаемое значение
- <span style="color: orange;">[TaskType]</span>: Список типов задач.

### Пример использования
```graphql
query {
  getTaskTypesByAttributes(projectId: 10) {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getAllFieldTypes](query.graphql) Получение типа отчета по идентификатору
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[FieldType]</span>: Список значений поля задачи/атрибута.

### Пример использования
```graphql
query {
  getAllFieldTypes {
    FieldType {
      fieldId
      name
      description
      fullDescription
      userHint
      valueAttribute
      attribute
      valueType
      type
      isSystemField
      clearWhenClone
      clearWhenRevision
    }
  }
}
```


## [getAllAttributeTypes](query.graphql) Получение типа отчета по идентификатору
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[AttributeType]</span>: Список атрибутов.

### Пример использования
```graphql
query {
  getAllAttributeTypes {
    AttributeType {
      id
      description
      name
      fields
    }
  }
}
```


## [getAllScalarTypes](query.graphql) Получение всех скаляр
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[ScalarType]</span>: Список атрибутов.

### Пример использования
```graphql
query {
  getAllScalarTypes {
    ScalarType {
      id
      description
      name
    }
  }
}
```


## [getAllCategories](query.graphql) Получение всех категорий
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[TaskCategory]</span>: Список категорий задач.

### Пример использования
```graphql
query {
  getAllScalarTypes {
    TaskCategory {
      id
      name
      description
      url_path
    }
  }
}
```


## [getAllModules](query.graphql) Получение всех модулей
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[Module]</span>: Список модулей.

### Пример использования
```graphql
query {
  getAllScalarTypes {
    Module {
      id
      name
      description
      url_path
    }
  }
}
```


## [getTaskType](query.graphql) Получение типа задачи
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Наименование задачи.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.

### Пример использования
```graphql
query {
  getTaskType(name: "string") {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getTaskTypeWithParents](query.graphql) Получение типа задачи с родителями
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Наименование задачи.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.

### Пример использования
```graphql
query {
  getTaskTypeWithParents(name: "string") {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getTaskTypeChildren](query.graphql) Получение типа зависимой задачи
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Наименование задачи.
- <span style="color: orange;">projectId</span> (default_value=None): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.

### Пример использования
```graphql
query {
  getTaskTypeChildren(name: "string") {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getAttribute](query.graphql) Получение атрибута
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Наименование задачи.
### Возвращаемое значение
- <span style="color: orange;">AttributeType</span>: Тип атрибута.

### Пример использования
```graphql
query {
  getAttribute(name: "string") {
    AttributeType {
      id
      description
      name
      fields
    }
  }
}
```


## [getCategory](query.graphql) Получение категории задачи
### Аргументы
- <span style="color: orange;">name</span> (обязательный): Наименование категории.
### Возвращаемое значение
- <span style="color: orange;">TaskCategory</span>: Категория задачи.

### Пример использования
```graphql
query {
  getCategory(name: "string") {
    TaskCategory {
      id
      name
      description
      url_path
    }
  }
}
```


## [getTaskTypesWithFields](query.graphql) Получение типа задачи с полями
### Аргументы
- <span style="color: orange;">fields</span> (обязательный): Наименование полей.
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
### Возвращаемое значение
- <span style="color: orange;">TaskType</span>: Тип задачи.

### Пример использования
```graphql
query {
  getTaskTypesWithFields(name: "string") {
    TaskType {
      id
      fields
      description
      name
      parent
      children
      dpendencies
      category
      isAbstract
      isActive
      isProcess
      isProcessStep
      isSheet
      isReport
      homeProjectId
      kanbanAvailable
      createFromChart
      reportExist
      formExist
      participantAccessModelEnabled
      canPublish
    }
  }
}
```


## [getUserSettingsColumns](query.graphql) Получение пользовательских настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">module</span> (обязательный): Наименование модуля.
- <span style="color: orange;">filterId</span> (обязательный): Идентификатор фильтра.
### Возвращаемое значение
- <span style="color: orange;">[UserSettingsColumnType]</span>: Тип задачи.

### Пример использования
```graphql
query {
  getUserSettingsColumns(module: "string", filterId: 10) {
    UserSettingsColumnType {
      userId
      field
      width
      order
      module
      filterId
    }
  }
}
```


## [getUserSettingsColumns](query.graphql) Получение пользовательских настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">module</span> (обязательный): Наименование модуля.
- <span style="color: orange;">filterId</span> (обязательный): Идентификатор фильтра.
### Возвращаемое значение
- <span style="color: orange;">[UserSettingsColumnType]</span>: Список пользовательских настроек.

### Пример использования
```graphql
query {
  getUserSettingsColumns(module: "string", filterId: 10) {
    UserSettingsColumnType {
      userId
      field
      width
      order
      module
      filterId
    }
  }
}
```


## [getSystemSettingsColumns](query.graphql) Получение системных настроек столбцов списка задач
### Аргументы
- <span style="color: orange;">module</span> (обязательный): Наименование модуля.
- <span style="color: orange;">filterId</span> (обязательный): Идентификатор фильтра.
### Возвращаемое значение
- <span style="color: orange;">[SystemSettingsColumnType]</span>: Список системных настроек.

### Пример использования
```graphql
query {
  getSystemSettingsColumns(module: "string", filterId: 10) {
    SystemSettingsColumnType {
      field
      width
      order
      module
      filterId
    }
  }
}
```


## [getWarningNotifications](query.graphql) Получение предупреждающего уведомления по проекту
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">filters</span> (default_value=None): Пользовательские фильтры.
### Возвращаемое значение
- <span style="color: orange;">[WarningNotificationType]</span>: Список типов предупреждающих уведомлений.

### Пример использования
```graphql
query {
  getWarningNotifications(projectId: 10) {
    SystemSettingsColumnType {
      field
      width
      order
      module
      filterId
    }
  }
}
```


## [getAvailableTimesMB](query.graphql) Получение доступного времени для создания заявки в Мостовом бюро
### Аргументы
- <span style="color: orange;">projectId</span> (обязательный): Идентификатор проекта.
- <span style="color: orange;">sectionId</span> (обязательный): Идентификатор секции.
- <span style="color: orange;">chapterId</span> (обязательный): Идентификатор раздела.
- <span style="color: orange;">date</span> (обязательный): Дата, для которой нужно получить доступное время.
### Возвращаемое значение
- <span style="color: orange;">[AvailableTimeMBType]</span>: Список доступных часов.

### Пример использования
```graphql
query {
  getAvailableTimesMB(projectId: 10, sectionId: 10, chapterId: 10, date: "2024-01-01") {
    AvailableTimeMBType {
      hours
      minutes
    }
  }
}
```


## [getWeeklyFundingDetailedPaymentData](query.graphql) Получение данных выгрузок по платежам
### Аргументы
- <span style="color: orange;">projectsId</span> (default_value=None): Список идентификаторов проектов.
### Возвращаемое значение
- <span style="color: orange;">[WeeklyFundingDetailedPaymentDataType]</span>: Список данных по платежам.

### Пример использования
```graphql
query {
  getWeeklyFundingDetailedPaymentData {
    WeeklyFundingDetailedPaymentDataType {
      region
      projectId
      sellerId
      documentDate
      prepayment
      payment
      ks2Payment
      ks3Payment
      contractId
    }
  }
}
```


## [getS3Projects](query.graphql) Получение проектов, работающих с хранилищем S3
### Аргументы (Нет аргументов)
### Возвращаемое значение
- <span style="color: orange;">[ID]</span>: Список идентификаторов проектов.

### Пример использования
```graphql
query {
  getS3Projects {
    ID
  }
}
```


## [getFieldAutocompleteValues](query.graphql) Получение значений для автозаполнения полей
### Аргументы
- <span style="color: orange;">triggerId</span> (обязательный): ID на основе которого будет автозаполняться.
- <span style="color: orange;">triggerType</span> (default_value=None): Поле на основе которого будет автозаполняться.
- <span style="color: orange;">taskType</span> (обязательный): Тип задачи.
- <span style="color: orange;">triggerField</span> (обязательный): Поле на основе которого будет автозаполняться.
- <span style="color: orange;">projectId</span> (default_value=None): ID проекта.
### Возвращаемое значение
- <span style="color: orange;">[FieldAutocompleteValuesType]</span>: Список типов для автозаполнения полей.

### Пример использования
```graphql
query {
  getFieldAutocompleteValues(triggerId: 10, taskType: "string", triggerField: "string") {
    FieldAutocompleteValuesType {
      taskType
      projectId
      entityId
      entityType
      entityValue
      entityField
      triggerId
      triggerType
      triggerField
    }
  }
}
```


## [getContractsWithContractStages](query.graphql) Получение договоров с этапами по контракту
### Аргументы
- <span style="color: orange;">projectsId</span> (обязательный): Идентификаторы проектов.
### Возвращаемое значение
- <span style="color: orange;">[ContractWithContractStagesType]</span>: Список договоров с этапами по контракту.

### Пример использования
```graphql
query {
  getContractsWithContractStages {
    ContractWithContractStagesType {
      id
      typename
      projectId
      name
      contractStages
    }
  }
}
```
