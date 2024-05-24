import json


def load_operations(file_operation):
    """
    Получает список последних успешных банковских операций клиента
    :return: list operations
    """
    with open(file_operation, 'rt', encoding='utf') as file:
        operations = [operation for operation in json.load(file) if operation and operation['state'] == "EXECUTED"]

    operations.sort(key=lambda x: str(x.get('date')), reverse=True)
    operations = operations[:5]

    return operations
