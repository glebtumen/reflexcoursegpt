"""Supabase client singleton implementation.

This file provides a singleton instance of the Supabase client to ensure that session state is maintained
across various authentication operations (such as setting the session and updating the user).
"""

import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Retrieve the Supabase URL and anon key from environment variables.
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise Exception("SUPABASE_URL and SUPABASE_ANON_KEY must be set in the environment variables.")

# Global variable to hold the singleton instance of the Supabase client.
_SUPABASE_INSTANCE: Client = None

def supabase_client() -> Client:
    """
    Returns a singleton instance of the Supabase client.
    If the client has not been created yet, it initializes it using the SUPABASE_URL and SUPABASE_ANON_KEY.
    """
    global _SUPABASE_INSTANCE
    if _SUPABASE_INSTANCE is None:
        _SUPABASE_INSTANCE = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return _SUPABASE_INSTANCE
