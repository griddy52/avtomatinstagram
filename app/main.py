from . import create_app
from .api.accounts import accounts_bp
from .api.content import content_bp
from .api.schedule import schedule_bp
from .api.stats import stats_bp

app = create_app()

app.register_blueprint(accounts_bp)
app.register_blueprint(content_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(stats_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 