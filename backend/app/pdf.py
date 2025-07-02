import fitz  # PyMuPDF
from fitz import Document, Page
from app.utils import get_date_string


def edit_pdf(
    input_pdf: str,
    output_pdf: str,
    new_value: str,
    new_name: str,
    new_cpf: str,
    new_bank: str,
    new_agency: str | None,
    new_account: str | None,
) -> None:
    doc: Document = fitz.open(input_pdf)
    page: Page = doc[0]

    # Edit date
    DATE_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
    DATE_OLD_TEXT = "Sábado, 28 de junho de 2025, às 18:13:36."
    DATE_FONT_SIZE = 10
    DATE_FONT_NAME = "F4"
    DATE_COLOR = (0, 0, 0)

    text_instance = page.search_for(DATE_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]

    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    page.insert_text(
        (span["bbox"][0], span["bbox"][3]),
        get_date_string(),
        fontname=DATE_FONT_NAME,
        fontfile=DATE_FONT_FILE,
        fontsize=DATE_FONT_SIZE,
        color=DATE_COLOR,
    )

    # Edit value
    VALUE_FONT_FILE = "fonts/Inter_24pt-SemiBold.ttf"
    VALUE_OLD_TEXT = "R$ 0,01"
    VALUE_FONT_SIZE = 21
    VALUE_FONT_NAME = "F0"
    VALUE_COLOR = (0, 0, 0)

    text_instance = page.search_for(VALUE_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]
    
    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    page.insert_text(
        (span["bbox"][0], span["bbox"][3]),
        new_value,
        fontname=VALUE_FONT_NAME,
        fontfile=VALUE_FONT_FILE,
        fontsize=VALUE_FONT_SIZE,
        color=VALUE_COLOR,
    )

    # Edit name
    NAME_FONT_FILE = "fonts/Inter_24pt-Medium.ttf"
    NAME_OLD_TEXT = "MARIANA SANTOS DE ANDRADE"
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
        (span["bbox"][0], 353),
        new_name,
        fontname=NAME_FONT_NAME,
        fontfile=NAME_FONT_FILE,
        fontsize=NAME_FONT_SIZE,
        color=NAME_COLOR,
    )

    # Edit CPF
    CPF_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
    CPF_OLD_TEXT = "647.433"
    CPF_FONT_SIZE = 10
    CPF_FONT_NAME = "F2"
    CPF_COLOR = (0, 0, 0)

    text_instance = page.search_for(CPF_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]

    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    page.insert_text(
        (66, 371),
        new_cpf,
        fontname=CPF_FONT_NAME,
        fontfile=CPF_FONT_FILE,
        fontsize=CPF_FONT_SIZE,
        color=CPF_COLOR,
    )

    # Edit Bank
    BANK_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
    BANK_OLD_TEXT = "BANCO BRADESCO S.A."
    BANK_FONT_SIZE = 10
    BANK_FONT_NAME = "F3"
    BANK_COLOR = (0, 0, 0)

    text_instance = page.search_for(BANK_OLD_TEXT)[0]
    
    blocks = page.get_text("dict", clip=text_instance)

    block = blocks["blocks"][0]
    line = block["lines"][0]
    span = line["spans"][0]

    page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

    page.insert_text(
        (span["bbox"][0], 387),
        new_bank,
        fontname=BANK_FONT_NAME,
        fontfile=BANK_FONT_FILE,
        fontsize=BANK_FONT_SIZE,
        color=BANK_COLOR,
    )

    # Edit Agency
    if new_agency is not None:
        AGENCY_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
        AGENCY_OLD_TEXT = "621"
        AGENCY_FONT_SIZE = 10
        AGENCY_FONT_NAME = "F3"
        AGENCY_COLOR = (0, 0, 0)

        text_instance = page.search_for(AGENCY_OLD_TEXT)[0]
        
        blocks = page.get_text("dict", clip=text_instance)

        block = blocks["blocks"][0]
        line = block["lines"][0]
        span = line["spans"][0]

        page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

        page.insert_text(
            (span["bbox"][0], 404),
            new_agency,
            fontname=AGENCY_FONT_NAME,
            fontfile=AGENCY_FONT_FILE,
            fontsize=AGENCY_FONT_SIZE,
            color=AGENCY_COLOR,
        )

    # Edit Account
    if new_account is not None:
        ACCOUNT_FONT_FILE = "fonts/Inter_24pt-Regular.ttf"
        ACCOUNT_OLD_TEXT = "254762"
        ACCOUNT_FONT_SIZE = 10
        ACCOUNT_FONT_NAME = "F3"
        ACCOUNT_COLOR = (0, 0, 0)

        text_instance = page.search_for(ACCOUNT_OLD_TEXT)[0]
        
        blocks = page.get_text("dict", clip=text_instance)

        block = blocks["blocks"][0]
        line = block["lines"][0]
        span = line["spans"][0]

        page.draw_rect(text_instance, color=(1, 1, 1), fill=(1, 1, 1))

        page.insert_text(
            (span["bbox"][0], 421),
            new_account,
            fontname=ACCOUNT_FONT_NAME,
            fontfile=ACCOUNT_FONT_FILE,
            fontsize=ACCOUNT_FONT_SIZE,
            color=ACCOUNT_COLOR,
        )

    doc.save(output_pdf)
    doc.close()
    return output_pdf
