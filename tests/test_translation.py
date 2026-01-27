
from contextlib import chdir
from pathlib import Path

from qt_transifex.parameters import load_parameters
from qt_transifex.translation import Translation


def test_update_strings(fixtures: Path):
    parameters = load_parameters(fixtures)

    ts_path = Translation.translation_file_path(parameters)
    qm_path = ts_path.with_suffix(".qm")
    pro_file = parameters.plugin_path.joinpath(f"{parameters.project}.pro")

    with chdir(fixtures):

        ts_path.unlink(missing_ok=True)
        qm_path.unlink(missing_ok=True)
        pro_file.unlink(missing_ok=True)

        Translation.update_strings(parameters)

        assert ts_path.exists()
        assert pro_file.exists()

        # Compile string
        Translation.compile_strings(parameters)
        assert qm_path.exists()
