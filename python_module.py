from enum import Enum


def _join_urls(*url_parts) -> str:
    if not url_parts or not all(isinstance(url_part, str) for url_part in url_parts):
        raise TypeError(f"Didn't get URLs parts to join, or the URLs parts are not strings, URLs parts: {url_parts}")
    return "/".join(part.strip('/') for part in url_parts if part)

class SystemURLs(Enum):
    _base_url = "https://my-url.com/prod"
    _start_url = _join_urls(_base_url, "/start")

