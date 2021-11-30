from typing import List
import sys
import requests
from distutils.version import StrictVersion
from pprint import pprint
from dataclasses import dataclass
from packaging.version import parse as parse_version


@dataclass
class Requirement:
    name: str
    version: str

    @classmethod
    def from_req_line(cls, req_line: str):
        req = req_line.strip().split("==")
        return cls(*req)


def parse_line(line: str):
    if "==" in line:
        return Requirement.from_req_line(line)
    else:
        return None


def parse_requirements_file(filename: str = "requirements.txt"):
    with open(filename) as f:
        return [parse_line(l) for l in f.readlines()]


def pypi_versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = requests.get(url).json()
    versions = data["releases"].keys()
    return sorted(versions, key=lambda v: parse_version(v), reverse=True)


def get_requirements_versions(requirements: List[Requirement]):
    return [(r, pypi_versions(r.name)[0]) for r in requirements if r]


def get_outdated_packages(requirements: List[Requirement]):
    req_versions = get_requirements_versions(requirements)
    return [r for r in req_versions if r[0].version < r[1]]


def main():
    requirements_in_file = parse_requirements_file()
    print(get_outdated_packages(requirements_in_file))
