from pathlib import Path

from qt_transifex.parameters import (
    find_config_file,
    load_parameters,
    read_config_from_file,
)


def test_find_config_file(fixtures: Path):
    path = find_config_file(fixtures)
    assert path is not None
    assert path.name == "pyproject.toml"

    path = find_config_file(fixtures.parent)
    assert path is None


def test_read_config(fixtures: Path):
    config = read_config_from_file(fixtures.joinpath(".qt-transifex.toml"))
    assert config.get("organization") == "3liz-1"


def test_load_parameters(fixtures: Path):
    parameters = load_parameters(fixtures)
    assert parameters.plugin_path.parent == fixtures
    assert parameters.lrelease_executable.exists()
    assert parameters.organization == "3liz-1"
