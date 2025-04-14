import argparse
import fitz


def read_toc(filepath: str, pagenum_sep: str = "|") -> list[list]:
    toc = []
    with open(filepath, "r") as f:
        for line in f:
            text, pagenum = line.split(pagenum_sep)
            text = text.rstrip()
            title = text.lstrip()
            level = len(text) - len(title) + 1
            pagenum = int(pagenum)
            toc.append([level, title, pagenum])
    return toc


def set_toc(pdf: str, tocfile: str, pagenum_sep: str, output: str):
    doc = fitz.open(pdf)
    toc = read_toc(filepath=tocfile, pagenum_sep=pagenum_sep)
    doc.set_toc(toc)
    doc.save(output)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--toc", help="text file containing table of content", required=True
    )
    ap.add_argument(
        "--pdf", help="pdf file whose outline has to be overwritten", required=True
    )
    ap.add_argument("--output", help="name of the output pdf file", required=True)
    ap.add_argument(
        "--pagenum-sep",
        help="character that separates page number in toc file",
        required=False,
        default="|",
        type=str,
    )
    args = ap.parse_args()
    set_toc(
        pdf=args.pdf, tocfile=args.toc, output=args.output, pagenum_sep=args.pagenum_sep
    )


if __name__ == "__main__":
    main()
