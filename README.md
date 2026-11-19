# fedimmich

A federation sidecar for [Immich](https://immich.app). It runs next to an Immich
server, reads data from it through Immich's API, and handles the server-to-server
work so people on different Immich instances can share albums with each other.

Status: scaffold only. The only thing it does today is answer `GET /`.

## Develop

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                                # install deps into .venv
uv run uvicorn fedimmich.app:app --reload              # dev server with reload, :8000
uv run fedimmich                                       # plain server, :8000
curl localhost:8000/                                   # {"message":"Hello, world"}
```
