"""
Top-level State for the App.

Authentication data is stored in the base State class so that all substates can
access it for verifying access to event handlers and computed vars.
"""

import os
import jwt
import time
import reflex as rx
from dotenv import load_dotenv

# load env
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

from .auth.supabase__client import supabase_client

import logging

logging.basicConfig(level=logging.INFO)


class State(rx.State):

    auth_token: str = rx.Cookie(name="auth_token", secure=True)
    is_paid: bool = False

    def do_logout(self):
        """Sign out, remove auth cookie and redirect to the login page."""
        self.auth_token = ""
        yield rx.remove_cookie("auth_token")
        yield rx.redirect("/login")

    @rx.var(cache=True)
    def decodeJWT(self) -> dict:
        """
        Decode the JWT token.

        This method decodes the JWT token using the provided secret and algorithm,
        verifies its authenticity, and checks if it's within the valid time range.

        Returns:
            dict: A dictionary containing the decoded JWT token if it's valid,
                  otherwise returns an empty dictionary.

        Raises:
            Exception: Any exception encountered during the decoding process.
        """
        try:
            decoded_token = jwt.decode(
                self.auth_token,
                JWT_SECRET,
                do_verify=True,
                algorithms=[JWT_ALGORITHM],
                audience="authenticated",
                leeway=1,
            )
            return (
                decoded_token
                if decoded_token["exp"] >= time.time()
                and decoded_token["iat"] <= time.time()
                else None
            )
        except Exception as e:
            return {}

    @rx.var
    def token_is_valid(self) -> bool:
        """
        Check if the JWT token is valid.

        This method checks if the JWT token is valid by attempting to decode it.
        If decoding is successful, it returns True, indicating that the token is valid.
        If decoding fails for any reason, it returns False.

        Returns:
            bool: True if the JWT token is valid, False otherwise.
        """
        try:
            return bool(self.decodeJWT)
        except Exception:
            return False

    @rx.var
    def user_email(self) -> str:
        token = self.decodeJWT
        if token and isinstance(token, dict):
            return token.get("email", "No email")
        return "No email"

    @rx.var
    def user_id(self) -> str:
        token = self.decodeJWT
        if token and isinstance(token, dict):
            return token.get("sub", "")
        return ""

    @rx.var
    def is_user_paid(self) -> bool:
        token = self.decodeJWT
        if token and isinstance(token, dict):
            user_id = token.get("sub", "")
            response = (
                supabase_client()
                .table("user_profile")
                .select("is_paid")
                .eq("id", user_id)
                .execute()
            )
            if response.data[0].get("is_paid", False):
                self.is_paid = True
                return True
        return False
