import os
import sys

LINE = "We held a forty-minute meeting to decide whether to send the email \u2014 the one we'd already written before we sat down."

def main():
    if "\n" in LINE or "\r" in LINE:
        sys.stderr.write("entry must be a single line\n")
        sys.exit(1)
    if len(LINE) > 200:
        sys.stderr.write("entry exceeds 200 characters\n")
        sys.exit(1)
    sys.stdout.write(LINE + "\n")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE + "\n")

if __name__ == "__main__":
    main()
