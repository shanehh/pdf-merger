from pathlib import Path
from title_page import create_pdf_title_page

from PyPDF2 import PdfFileWriter, PdfFileReader


def read_pdfs(pdfs_dir: Path):
    lectures_path = list(pdfs_dir.glob("*.pdf"))
    lectures_path.sort()
    return lectures_path


def title_page(title: str):
    path = create_pdf_title_page(title)
    reader = PdfFileReader(open(path, "rb"))
    return reader.getPage(0)


def append_pdf(writer: PdfFileWriter, pdf_path: Path):
    reader = PdfFileReader(open(pdf_path, "rb"))

    n = reader.getNumPages()
    for index in range(n):
        writer.addPage(reader.getPage(index))
    return n


def main(folder_path: Path):
    page_count = -1
    writer = PdfFileWriter()

    for path in read_pdfs(folder_path):
        title = path.stem.replace("-", " ").title()
        print("Read:", path, title)
        # add title page
        writer.addPage(title_page(title))
        page_count += 1
        writer.addBookmark(title, page_count)
        page_count += append_pdf(writer, path)

    # output
    with open(f"{folder_path.name}-compilation.pdf", "wb+") as f:
        writer.write(f)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Error: need to specify the folder path at which your PDFs exist.")
        raise SystemExit(1)

    folder_path = Path(sys.argv[1])
    print("Try to process:", folder_path)
    main(folder_path)
