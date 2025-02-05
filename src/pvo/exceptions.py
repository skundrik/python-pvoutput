"""Exceptions for the PVOutput API client."""


class PVOutputError(Exception):
    """Generic PVOutput exception."""


class PVOutputAuthenticationError(PVOutputError):
    """PVOutput authentication exception."""


class PVOutputConnectionError(PVOutputError):
    """PVOutput connection exception."""


class InvalidSystemIDError(PVOutputError):
    """Invalid system ID exception."""
