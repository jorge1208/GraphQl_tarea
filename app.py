from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
import uvicorn

from resolvers import resolve_producto, resolve_actualizar_precio

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()
mutation = MutationType()

query.set_field("producto", resolve_producto)
mutation.set_field("actualizarPrecio", resolve_actualizar_precio)

schema = make_executable_schema(type_defs, query, mutation)

app = GraphQL(schema)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
