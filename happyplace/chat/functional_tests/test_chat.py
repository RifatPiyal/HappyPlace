from selenium import webdriver
from chat.models import Message
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class TestChat(StaticLiveServerTestCase)