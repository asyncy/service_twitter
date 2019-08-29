import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app() -> Flask:
    print(""" Provides an instance of our Flask app """)
    from app import app
    
    return app
    
