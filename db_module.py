def updateRow(updateInfo):

    database = updateInfo["database"]
    table = updateInfo["table"]
    pkValue = updateInfo["pkValue"]
    field = updateInfo["field"]
    newValue = updateInfo["newValue"]

    databases[database][table][pkValue][field] = newValue


def deleteRow(deleteInfo):

    database = deleteInfo["database"]
    table = deleteInfo["table"]
    pkValue = deleteInfo["pkValue"]

    del databases[database][table][pkValue]
    