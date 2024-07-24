import re
from datetime import datetime


def regex_main(pattern: str, log_string: str) -> str:
    """

    """
    regex = re.compile(pattern)
    output = regex.search(log_string)
    return output.group() if output else None


def regex_get_addr(log_string: str) -> str:
    """
    """
    return regex_main(
        r'[a-zA-Z0-9._]*@[a-zA-Z0-9.-]*.(ru|com|net|cz|su|gs)',
        log_string),


def regex_get_id(log_string: str) -> str:
    """

    """
    return log_string.rsplit(
        'id=', 1)[-1].strip() if 'id=' in log_string else None


def regex_get_int_id(log_string: str) -> str:
    """
    """
    return regex_main(
        r'1[a-zA-Z0-9]{5}-000[a-zA-Z0-9]{3}-[a-zA-Z0-9]{2}',
        log_string)


def regex_log_worker(log_line: str):
    """

    """
    log_created = datetime.strptime(
        regex_main(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_line),
        '%Y-%m-%d %H:%M:%S',
    )
    log_int_id = regex_get_int_id(log_line)
    log_id = regex_get_id(log_line)
    log_message = log_line.removeprefix(f'{log_created}').strip()

    if '<=' in log_line:
        return {
            "log_type": "message",
            "data": {
                "id": log_id,
                "int_id": log_int_id,
                "str": log_message,
                "created": log_created,
            }
        }
    else:
        log_address = regex_get_addr(log_line)[0]
        return {
            "log_type": "log",
            "data": {
                "int_id": log_int_id,
                "str": log_message,
                "created": log_created,
                "address": log_address,
            }
        }
