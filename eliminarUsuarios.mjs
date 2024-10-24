import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  ScanCommand,
  PutCommand,
  GetCommand,
  DeleteCommand,
} from "@aws-sdk/lib-dynamodb";

const client = new DynamoDBClient({});

const dynamo = DynamoDBDocumentClient.from(client);

const tableName = "usuarios_tabla";

export const handler = async (event) => {

  const id = event.id;
  const idString = id.toString();


  // Validaciones
  if (!id) {
    return {
      statusCode: 400,
      body: JSON.stringify("Error: El id es requerido"),
    };
  }

  var telefonoString = "3026468094";

  await dynamo.send(
    new DeleteCommand({
      TableName: tableName,
      Key: {
        id: idString,        // Clave primaria
        telefono: telefonoString // Segunda clave para la clave compuesta
      },
    })
  );
  
  

  return {
    statusCode: 200,
    body: JSON.stringify("Usuario eliminado exitosamente"),
  };

};
