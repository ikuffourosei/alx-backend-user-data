#!/usr/bin/env python3
"""Basic Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A Basic Auth class that inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """A public method to extract base64 header"""
        if isinstance(authorization_header, str):
            val = authorization_header.split()
            if len(val) > 1 and val[0] == 'Basic':
                return val[1]
        return None
