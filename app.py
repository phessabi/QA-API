import json
import uvicorn
import sys
from pydantic import BaseModel
from fastapi import FastAPI, Response


app = FastAPI()


class Query(BaseModel):
    message: str


@app.post("/hello")
async def say_hello(query: Query):
    response = "Hello world. your message: " + query.message
    return Response(
        content=json.dumps({
            "result": response
        }),
        status_code=200
    )


def parse_args(argv) -> dict:
    args = {}
    for arg in argv[1:]:
        if "=" in arg:
            key, value = arg.split("=", 1)
            args[key] = value
    return args


if __name__ == "__main__":
    # debug is passed to the "reload" parameter of uvicorn
    # default values
    ARGS: dict[str, str | int | bool] = {
        "host": "0.0.0.0",
        "port": 5001,
        "debug": 1,
    }
    ARGS.update(parse_args(sys.argv))
    ARGS["port"] = int(ARGS["port"])
    ARGS["debug"] = bool(int(ARGS["debug"]))
    uvicorn.run(
        app='app:app',
        host=ARGS['host'],
        port=ARGS['port'],
        reload=ARGS['debug']
    )
