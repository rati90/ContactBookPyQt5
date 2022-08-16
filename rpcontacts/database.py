from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createCotactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
         CREATE TABLE IF NOT EXISTS contacts (
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
             name VARCHAR(40) NOT NULL,
             job VARCHAR(50),
             email VARCHAR(40) NOT NULL
         )
         """
    )


def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Erro: {connection.lastError().text()}",
        )
        return False

    _createCotactsTable()
    return True




