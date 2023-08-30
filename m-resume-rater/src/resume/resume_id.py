class ResumeId:
    KIND_URL = 0

    def __init__(self, kind: int, url: str) -> None:
        pass

    @staticmethod
    def check_kind(kind: int) -> bool:
        print(ResumeId.KIND_URL)
        return False

    @staticmethod
    def check_url(url: str) -> bool:
        pass

# todo del
# >>> import validators
# >>> validators.url("http://google.com")
# True
# >>> validators.url("http://google")
# ValidationFailure(func=url, args={'value': 'http://google', 'require_tld': True})
# >>> if not validators.url("http://google"):
# ...     print "not valid"
# ...
# not valid
# >>>
# Install it from PyPI with pip (pip install validators).
