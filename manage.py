from application import app, manager
from flask_script import Server
import urls  # noqa

# 配置runserver指令
manager.add_command(
    'runserver',
    Server(host='localhost',
           port=app.config['SERVER_PORT'],
           use_debugger=True,
           use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception:
        import traceback
        traceback.print_exc()
