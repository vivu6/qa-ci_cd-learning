from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver():
    """Returns a compatible ChromeDriver executable path."""
    return ChromeDriverManager().install()
