from sys import stdout, exit
import click

from pip_version_checker.pip_version import parse_requirements_file


@click.command()
@click.option(
    "--filename", default="requirements.txt", help="File with required python packages"
)
@click.option(
    "--fail", type=bool, default=False, help="Fail if there are outdated packages"
)
def main(filename, fail):
    requirements_in_file = parse_requirements_file(filename)
    outdated_packages = [r for r in requirements_in_file if r.outdated]
    if outdated_packages:
        click.echo(f"Outdated packages in {filename}:", file=stdout)
    else:
        click.echo(f"No outdated packages found in {filename}", file=stdout)
    for op in outdated_packages:
        click.echo(op)
    exit(fail and bool(outdated_packages))
