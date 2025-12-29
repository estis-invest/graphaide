from pathlib import Path

PROJECT_DIRS = {
    "data": Path("data"),
    "figures": Path("figures")
}

class InitCommand:
    @classmethod
    def name(cls) -> str:
        return "init"

    def run(self, *args:str):
        base_dir = Path.cwd()
        for dir_path in PROJECT_DIRS.values():
            path = base_dir / dir_path
            path.mkdir(parents=True, exist_ok=True)
        print("\nProject directories where created at:")
        print("\n".join(str(base_dir / p) for p in PROJECT_DIRS.values()))



