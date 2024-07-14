#!/usr/bin/env python3
"""Authentication class"""
from flask import request
from typing import (
    List,
    TypeVar
)
from os import getenv


class Auth:
    """Auth class"""
    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        """
        A public method to validate if a url requires an authentication

        Return: False if it does not require
        or True if it does require authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        allowed = []
        for _ in excluded_paths:
            if _.endswith('/'):
                _ = _.rstrip('/')
            allowed.append(_)
        if path and path.endswith('/'):
            path = path.rstrip('/')
        if path in allowed:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        A public method that checks the authorization header
        """
        if request is not None:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method that checks for current user"""
        if request is not None:
            user = getattr(request, 'user', None)
            if user and not user.is_anonymous:
                return request.user
        return None

    def session_cookie(self, request=None) -> str:
        """Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
