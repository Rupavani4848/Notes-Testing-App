from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)


class ExceptionHandler:

    flaky_exceptions = (
        TimeoutException,
        StaleElementReferenceException
    )

    @staticmethod
    def is_flaky(exception):

        return isinstance(
            exception,
            ExceptionHandler.flaky_exceptions
        )