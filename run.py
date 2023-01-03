import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        hotst=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
  
