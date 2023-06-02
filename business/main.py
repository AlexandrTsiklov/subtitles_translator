from configurer import IAM_TOKEN
from connector import Connector


if __name__ == '__main__':
    if IAM_TOKEN:
        connector = Connector()
        connector.runapp()
    print("Не получилось обновить IAM токен")