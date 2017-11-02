import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_apache_user_group(User, Group, AnsibleDefaults):
    user = User(AnsibleDefaults["apache_user"])
    group = Group(AnsibleDefaults["apache_group"])

    assert user.exists
    assert group.exists
    assert user.group == AnsibleDefaults["apache_group"]


def test_apache_services(File, Service, Socket, AnsibleDefaults):
    http_port = AnsibleDefaults["apache_port"]

    assert File("/lib/systemd/system/apache2.service").exists
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://0.0.0.0:" + str(http_port)).is_listening
