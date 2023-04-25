import argparse
import os
from pathlib import PosixPath
from typing import Any, Dict, List, Optional

import toml


class ReadTomlFile:
    def __init__(self, directory_path: str) -> None:
        self.directory_path = PosixPath(directory_path).expanduser()
        self.path = self.directory_path.joinpath("pyproject.toml")
        self.toml_file = self.read()

    def read(self) -> Dict[str, Any]:
        with self.path.open(encoding="utf-8") as toml_file:
            return toml.load(toml_file)

    @property
    def get_dependencies(
        self,
        toml_file: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not toml_file:
            toml_file = self.toml_file
        return toml_file["tool"]["poetry"]["dependencies"]

    @property
    def get_dev_dependencies(
        self,
        toml_file: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not toml_file:
            toml_file = self.toml_file
        tool_poetry = toml_file["tool"]["poetry"]
        dev_dependencies = tool_poetry.get("dev-dependencies") or tool_poetry.get(
            "group",
        ).get(
            "dev",
        ).get("dependencies")
        if not dev_dependencies:
            dev_dependencies = {}
        return dev_dependencies


class UpdatePackages:
    def __init__(
        self,
        toml_file: ReadTomlFile,
        include_dev: bool = False,
        only_dev: bool = False,
    ) -> None:
        self.toml_file = toml_file
        self.include_dev = include_dev
        self.only_dev = only_dev
        self.dependencies = self.get_dependencies()
        self.update_packages()

    def get_dependencies(self) -> Dict[str, Any]:
        dependencies = {}

        if self.only_dev:
            dependencies["dev"] = self.toml_file.get_dev_dependencies
        else:
            dependencies["main"] = self.toml_file.get_dependencies
            if self.include_dev:
                dependencies["dev"] = self.toml_file.get_dev_dependencies

        return dependencies

    def update_packages(self) -> None:
        package_names_to_update = self.get_package_names_to_update()

        dev_packages = package_names_to_update.get("dev")
        main_packages = package_names_to_update.get("main")
        print(f"Updating {dev_packages} and {main_packages} packages")
        if dev_packages:
            os.system(f"poetry add --group dev {' '.join(dev_packages)}")
        if main_packages:
            os.system(f"poetry add {' '.join(main_packages)}")

    def get_package_names_to_update(self) -> Dict[str, List[str]]:
        package_names_to_update = {}
        packages_to_ignore = ["python", "poetry-core"]
        for dependency_type, dependencies in self.dependencies.items():
            for package_name in dependencies:
                if package_name not in packages_to_ignore:
                    package_names_to_update.setdefault(dependency_type, []).append(
                        f"{package_name}@latest",
                    )

        return package_names_to_update


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update pyproject.toml file")
    parser.add_argument(
        type=str,
        help="Directory path",
        default=".",
        dest="directory_path",
        nargs="?",
    )
    parser.add_argument(
        "--include-dev",
        action="store_true",
        help="Include dev packages",
        dest="include_dev",
        default=False,
    )
    parser.add_argument(
        "--only-dev",
        action="store_true",
        help="Only dev packages",
        dest="only_dev",
        default=False,
    )

    args = parser.parse_args()
    read_toml = ReadTomlFile(args.directory_path)
    UpdatePackages(read_toml, args.include_dev, args.only_dev)
