"""
    test_get_grant.py -- Given a URI of a grant, return a python
    structure representing the attributes of the grant

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-01-04
    --  Format output using json.dumps
    Version 0.3 MC 2014-09-02
    --  PEP 8, vivogrants

"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.3"

from vivogrants import get_grant
from datetime import datetime

print datetime.now(), "Start"
grants = \
    [
        "http://vivo.ufl.edu/individual/n1769500492",
        "http://vivo.ufl.edu/individual/n678985748",
        "http://vivo.ufl.edu/individual/n1725957599",
        "http://vivo.ufl.edu/individual/n859986285",
        "http://vivo.ufl.edu/individual/n899821550",
        "http://vivo.ufl.edu/individual/n2026295266",
        "http://vivo.ufl.edu/individual/n719692692",
        "http://vivo.ufl.edu/individual/n482305201",
        "http://vivo.ufl.edu/individual/n276081150",
        "http://vivo.ufl.edu/individual/n1863481639"
    ]
for grant in grants:
    print "\n", get_grant(grant, get_investigators=False)
print datetime.now(), "Finish"
