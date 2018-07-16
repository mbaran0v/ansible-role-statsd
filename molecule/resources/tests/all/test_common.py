
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
statsd = {
    'version': 'v0.8.0',
    'root': '/opt/statsd',
    'user': '_statsd',
    'service': 'statsd',
    'socket': 'udp://0.0.0.0:8125'
}


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_release_directory(host):
    f = host.file('{root}/releases/{version}'.format(**statsd))

    assert f.exists
    assert f.is_directory
    assert f.user == '{user}'.format(**statsd)
    assert f.group == '{user}'.format(**statsd)


def test_release_config(host):
    f = host.file('{root}/releases/{version}/config.js'.format(**statsd))

    assert f.exists
    assert f.user == '{user}'.format(**statsd)
    assert f.group == '{user}'.format(**statsd)


def test_release_symlink(host):
    f = host.file('{root}/current'.format(**statsd))

    assert f.exists
    assert f.is_symlink


def test_socket(host):
    s = host.socket('{socket}'.format(**statsd))

    assert s.is_listening


def test_serice(host):
    s = host.service('{service}'.format(**statsd))

    assert s.is_enabled
    assert s.is_running
