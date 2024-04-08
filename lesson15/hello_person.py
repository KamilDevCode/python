import argparse
parser = argparse.ArgumentParser(
    description='Provides a person greeting'
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required = True, help = "the name of person to greet"
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)