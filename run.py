from backend.auth.app import create_auth_app

app = create_auth_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)