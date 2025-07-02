import pytz
from datetime import datetime

def get_date_string() -> str:
    MONTHS = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }

    current_date = datetime.now(pytz.timezone('America/Sao_Paulo'))

    date_str = f"{current_date.day} de {MONTHS[current_date.month]} de {current_date.year}, às {current_date.hour}:{str(current_date.minute).zfill(2)}:{str(current_date.second).zfill(2)}."
    return date_str
