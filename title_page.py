import uuid
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


def create_pdf_title_page(title):
    filepath = Path(f"./tmp/{uuid.uuid4()}.pdf")
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True)

    canvas = Canvas(str(filepath), pagesize=LETTER)
    canvas.setFont("Times-Roman", 18)
    canvas.drawString(
        1 * inch,
        # 8.5 / 2 * inch,
        11 / 2 * inch,
        # 10 * inch,
        title,
    )
    canvas.save()
    return filepath


if __name__ == "__main__":
    p = create_pdf_title_page("L01 Introduction to Computation")
    print(p)
