from six import PY3

from mock import Mock, MagicMock, patch


if not PY3:
    @patch.multiple('clld.deploy.util',
                    time=Mock(),
                    getpass=Mock(return_value='password'),
                    confirm=Mock(return_value=True),
                    exists=Mock(return_value=True),
                    virtualenv=MagicMock(),
                    sudo=Mock(),
                    run=Mock(return_value='{"status": "ok"}'),
                    local=Mock(),
                    put=Mock(),
                    env=MagicMock(),
                    service=Mock(),
                    cd=MagicMock(),
                    require=Mock(),
                    postgres=Mock())
    def test_deploy():
        from clld.deploy.util import deploy
        from clld.deploy.config import App

        app = App('test', 9999, domain='d')
        assert app.src
        deploy(app, 'test')
        deploy(app, 'test', with_alembic=True)
        deploy(app, 'production')
