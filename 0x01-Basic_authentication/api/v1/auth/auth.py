#!/usr/bin/env python3
"""Authentication class"""
from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """Auth class"""
    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        """
        A public method to validate if a url requires an authentication

        Return: False or True
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        A public method that checks the authorization header
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method that checks for current user"""
        return request
