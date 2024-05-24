from src.loading_data import load_operations
from src.functions import formatting_date, mask_number


def main():
    operations = load_operations('../operations.json')

    for operation in operations:
        operation["date"] = formatting_date(operation["date"])
        operation['to'] = mask_number(operation['to'])
        operation['from'] = mask_number(operation['from']) if operation.get('from') else None

    for operation in operations:
        print(f"\n{operation['date']} {operation['description']}")
        print(f"{' -> '.join(filter(None, [operation.get('from'), operation['to']]))}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")


if __name__ == '__main__':
    main()
