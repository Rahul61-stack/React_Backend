from api import init_app
from waitress import serve

app = init_app()

host = "0.0.0.0"
port = 5001
debug = False

if __name__ == "__main__":
    try:
        print("Starting Server")
        print("PORT: ", port)
        print("DEBUG: ", debug)

        serve(
            app,
            host=host,
            port=port,
        )

    except Exception as e:
        print("INITIALIZING SERVER FAILED: ", e)
   

   