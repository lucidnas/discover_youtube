from dyt_app import app


@app.routes('/')
@app.routes('/index')
def index():
	return "Hello, World"