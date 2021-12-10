from sys import stdout, exit
import click

from pip_version_checker.pip_version import parse_requirements_file


@click.command()
@click.option(
    "--filename", default="requirements.txt", help="File with required python packages"
)
def main(filename):
    requirements_in_file = parse_requirements_file(filename)
    outdated_packages = [r for r in requirements_in_file if r.outdated]
    if outdated_packages:
        print(f"Outdated packages in {filename}:", stdout)
    else:
        print(f"No outdated packages found in {filename}", stdout)
    for op in outdated_packages:
        print(op)
