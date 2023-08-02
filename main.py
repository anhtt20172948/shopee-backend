from fastapi import FastAPI
import uvicorn
from routes.voucher import router as VoucherRouter

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(VoucherRouter)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                ssl_keyfile="./localhost+2-key.pem",
                ssl_certfile="./localhost+2.pem"
                )
