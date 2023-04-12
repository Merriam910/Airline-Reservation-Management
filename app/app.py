import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routers import flight, ticket, passenger

app = FastAPI()

app.include_router(flight.router)
app.include_router(ticket.router)
app.include_router(passenger.router)


@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
