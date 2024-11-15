import sys
from ci_test.main import main


def cli():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json>")
        sys.exit(1)

    json_path = sys.argv[1]
    main(json_path=json_path)


if __name__ == "__main__":
    cli()
