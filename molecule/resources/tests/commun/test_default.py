import os
import pytest
import testinfra
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture
def get_vars(host):
    defaults_files = "file=../../vars/main.yml name=role_defaults"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    return ansible_vars


@pytest.fixture
def get_vars_stuff(host):
    defaults_files = "file=../resources/vars/stuff.yml name=role_defaults"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    return ansible_vars


def test_hosts_file(host, get_vars, get_vars_stuff):
    true_vals = []
    for i in range(1, 2):
        true_vals.append("{} -classpath /tmp/molecule_capping/{}::/tmp/molecule_capping/{} "
                         "org.molecule_capping.launch.commandline.CommandLine updateDatabase "
                         "-config /tmp/molecule_capping/molecule_capping-{}.properties".format(get_vars_stuff['molecule_capping_Xmx'],
                                                                                               get_vars['_molecule_capping_jarname'],
                                                                                               get_vars_stuff['molecule_capping_jdbc_name'],
                                                                                               get_vars_stuff['molecule_capping_properties'][i]['name']))
    f = host.file("/tmp/cap_java/molecule_cap_cmd_file.txt")
    assert f.exists
    for true_val in true_vals:
        assert true_val in f.content_string.split("\n")
