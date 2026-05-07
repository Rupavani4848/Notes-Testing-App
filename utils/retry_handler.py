import time
from utils.logger import logger


def retry(max_attempts=3, delay=2):

    def decorator(function):

        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):

                try:

                    logger.info(
                        f"Executing {function.__name__} - Attempt {attempt}"
                    )

                    return function(*args, **kwargs)

                except Exception as error:

                    logger.warning(
                        f"Attempt {attempt} failed for "
                        f"{function.__name__}"
                    )

                    logger.error(str(error))

                    if attempt == max_attempts:
                        raise error

                    time.sleep(delay)

        return wrapper

    return decorator