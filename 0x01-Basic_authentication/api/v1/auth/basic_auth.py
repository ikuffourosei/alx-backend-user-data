#!/usr/bin/env python3
"""Basic Auth"""
from api.v1.auth.auth import Auth
from typing import Tuple
import base64 as b


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decoding the extracted string to base64"""
        if isinstance(base64_authorization_header, str):
            try:
                dec_bytes = b.b64decode(base64_authorization_header)
                base_header = base64_authorization_header
                if b.b64encode(dec_bytes).decode('utf-8') == base_header:
                    return dec_bytes.decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """Extract user's name and password"""
        if isinstance(decoded_base64_authorization_header, str):
            dec_header = decoded_base64_authorization_header.split(':')
            if len(dec_header) > 1:
                return (dec_header[0], dec_header[1])
        return (None, None)
