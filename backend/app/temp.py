import fitz  # PyMuPDF
from fitz import Document, Page


def edit_pdf(
    input_pdf: str,
    output_pdf: str,
) -> None:
    doc: Document = fitz.open(input_pdf)
    page: Page = doc[0]

    # Edit name
    NAME_FONT_FILE = "fonts/Inter_24pt-Medium.ttf"
    NAME_OLD_TEXT = "Henrique Santos de Andrade"
    NAME_FONT_SIZE = 13
    NAME_FONT_NAME = "F1"
    NAME_COLOR = (0, 0, 0)

    text_instance = page.search_for(NAME_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]


    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    page.insert_text(
        (span["bbox"][0], 230),
        "Fernando Sousa Santos",
        fontname=NAME_FONT_NAME,
        fontfile=NAME_FONT_FILE,
        fontsize=NAME_FONT_SIZE,
        color=NAME_COLOR,
    )

    # Edit account
    ACCOUNT_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
    ACCOUNT_OLD_TEXT = "51908076110"
    ACCOUNT_FONT_SIZE = 10
    ACCOUNT_FONT_NAME = "F2"
    ACCOUNT_COLOR = (0, 0, 0)

    text_instance = page.search_for(ACCOUNT_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]


    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    print(span["bbox"])
    page.insert_text(
        (span["bbox"][0], 298),
        "51209067220",
        fontname=ACCOUNT_FONT_NAME,
        fontfile=ACCOUNT_FONT_FILE,
        fontsize=ACCOUNT_FONT_SIZE,
        color=ACCOUNT_COLOR,
    )

    doc.save(output_pdf)
    doc.close()
    return output_pdf


if __name__ == "__main__":
    edit_pdf("templates/mercado_pago.pdf", "templates/mercado_pago_new.pdf")
