from fastapi import FastAPI, Depends
from routes.routes import router, verify_token
from db import init_db
from routes.auth_routes import auth_router
from fastapi.openapi.utils import get_openapi
from fastapi_mcp import FastApiMCP, AuthConfig


app = FastAPI(title="ClimateWatch API Gateway")


init_db()
app.include_router(router)
app.include_router(auth_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description="API Gateway for ClimateWatch",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    # Aplica globalmente
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema


mcp = FastApiMCP(
    app,
    include_operations=[
        "weather-by-city",
        "add-favorite",
        "list-favorites",
        "check-alerts",
        "register-user",
        "login-user",
    ],
    name="Weather API MCP",
    description="MCP server for the Weather API",
    describe_full_response_schema=True,
    describe_all_responses=True,
)

mcp.mount()

app.openapi = custom_openapi
