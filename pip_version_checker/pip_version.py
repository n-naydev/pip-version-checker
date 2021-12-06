import requests
from packaging.version import parse as parse_version
from dparse.filetypes import requirements_txt
from dparse import parse
from dparse.dependencies import Dependency


class Requirement:
    def __init__(self, dependency: Dependency) -> None:
        self.name = dependency.full_name
        self.specs = dependency.specs
        all_pypi_versions = pypi_versions(self.name)
        self.pypi_version = all_pypi_versions[0] if all_pypi_versions else None

    @property
    def outdated(self):
        return (
            not self.specs.contains(self.pypi_version) if self.pypi_version else False
        )

    def __repr__(self) -> str:
        return (
            f"{self.name}, requirement specs {self.specs}, "
            f"pypi version {self.pypi_version}"
        )


def parse_requirements_file(filename: str = "requirements.txt"):
    with open(filename) as f:
        deps = parse(f.read(), requirements_txt).dependencies
    return [Requirement(d) for d in deps]


def pypi_versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    versions = data["releases"].keys()
    return sorted(versions, key=lambda v: parse_version(v), reverse=True)
