# examples/what_got_generated.py
import pkgutil
import importlib
import sys

# change this to the actual package name printed by the generator
PACKAGE = "help_center_api_client"

def list_submodules(package_name: str):
    pkg = importlib.import_module(package_name)
    print(f"Top-level package: {package_name}")
    for m in pkgutil.iter_modules(pkg.__path__):
        print(" -", m.name)

    # The generator usually exposes operations under <pkg>.api.<tag>
    api_pkg_name = f"{package_name}.api"
    try:
        api_pkg = importlib.import_module(api_pkg_name)
        print(f"\nAPI modules in {api_pkg_name}:")
        for m in pkgutil.iter_modules(api_pkg.__path__):
            print(" -", m.name)
    except ModuleNotFoundError:
        print("\nNo .api package found (this can vary by spec and generator version).")

if __name__ == "__main__":
    list_submodules(PACKAGE)
