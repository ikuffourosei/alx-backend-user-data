#!/usr/bin/env python3
""" Main 6
"""
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

b = BasicAuth()
r = b.require_auth('/api/v1/hahaha/', [])
if r is True:
    print("\nSite not recognized! Requires immediate authorizaton\n")
else:
    print("\nSite is recognized. No authorization required\n")