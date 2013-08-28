---
layout: post
author: gmclendon
categories: gmclendon
title: Grant shows some syntax highlighting
---

Here's some python from [this project](https://github.com/twilio/twilio-python) just to show off syntax highlighting.

```python
import six
if six.PY3:
    import unittest  # noqa
else:  # noqa
    import unittest2 as unittest  # noqa

from mock import Mock
from twilio.rest.resources import Applications


class ApplicationsTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.resource = Applications("http://api.twilio.com", ("user", "pass"))

    def test_create_appliation_sms_url_method(self):
        self.resource.create_instance = Mock()
        self.resource.create(sms_method="hey")
        self.resource.create_instance.assert_called_with({"sms_method": "hey"})
```

ain't it pretty.
