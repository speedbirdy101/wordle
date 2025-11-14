from enum import Enum, unique


@unique
class Color(Enum):
    """Options for standard colors and effects."""

    # Colors
    GREEN       = "\033[32m"
    YELLOW      = "\033[33m"
    RED         = "\033[31m"
    MAGENTA     = "\033[35m"
    BLUE        = "\033[34m"
    CYAN        = "\033[36m"
    WHITE       = "\033[37m"
    BLACK       = "\033[30m"
    GREY        = "\033[90m"

    OFF         = "\033[0m"

    def __str__(self) -> str:
        return str(self.value)
