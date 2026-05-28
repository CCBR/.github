import logging


logger = logging.getLogger(__name__)


def get_api_error_message(response):
    message = ""
    payload = None

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if isinstance(payload, dict):
        message = payload.get("message", "")

    return message


def is_critical_api_error(response):
    message = get_api_error_message(response).lower()
    has_auth_status = response.status_code in {401, 403}
    has_auth_message = any(
        token in message
        for token in (
            "bad credentials",
            "requires authentication",
            "resource not accessible",
            "must have admin rights",
            "forbidden",
            "rate limit",
            "secondary rate limit",
        )
    )

    return has_auth_status or has_auth_message


def raise_api_error(response, endpoint):
    error_message = get_api_error_message(response)
    message_suffix = ""
    if error_message:
        message_suffix = f" GitHub API message: {error_message}."

    raise RuntimeError(
        f"Failed to retrieve {endpoint} from GitHub API "
        f"(status {response.status_code}). "
        "Critical README data is unavailable. "
        "Check whether GITHUB_TOKEN is expired or missing required permissions."
        f"{message_suffix}"
    )


def log_noncritical_api_error(response, endpoint, fallback_description, log=None):
    active_logger = log or logger
    error_message = get_api_error_message(response) or "<no message>"
    active_logger.warning(
        "Skipping %s due to GitHub API response %s (%s). Using %s.",
        endpoint,
        response.status_code,
        error_message,
        fallback_description,
    )
