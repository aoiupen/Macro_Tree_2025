"""Application specific exception hierarchy.

This module originally exposed a :class:`TreeException` type which was used
throughout the codebase and in the accompanying unit tests.  During a refactor
it was accidentally renamed to ``MTTreeError``.  The tests – and potentially
downstream code – still import ``TreeException`` which resulted in an
``ImportError`` during test collection.

To restore compatibility we re‑introduce ``TreeException`` as the canonical
base class and provide ``MTTreeError`` as a backwards compatible alias.  All
other exceptions now inherit from ``TreeException`` so that both names refer to
the same underlying type.
"""


class TreeException(Exception):
    """Base exception for all tree related errors."""


# Backwards compatibility ---------------------------------------------------
#
# ``MTTreeError`` was the previous name for ``TreeException``.  Some modules
# may still import it, so we keep it as an alias to avoid breaking those
# imports.
MTTreeError = TreeException


class MTItemNotFoundError(TreeException):
    """Raised when a tree item cannot be located."""


class MTItemAlreadyExistsError(TreeException):
    """Raised when trying to add a tree item that already exists."""


class InvalidMTItemDomainDTOError(TreeException):
    """Raised when provided tree item data is invalid."""


# Additional custom exceptions can be defined below as needed.