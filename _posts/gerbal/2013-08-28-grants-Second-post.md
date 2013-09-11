---
layout: post
author: gmclendon
categories: gmclendon
title: Grant shows some syntax highlighting
---

Here's some python from [this project](https://github.com/twilio/twilio-python) just to show off syntax highlighting.

```python
class ApplicationsTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.resource = Applications("http://api.twilio.com", ("user", "pass"))

    def test_create_appliation_sms_url_method(self):
        self.resource.create_instance = Mock()
        self.resource.create(sms_method="hey")
        self.resource.create_instance.assert_called_with({"sms_method": "hey"})

    def test_create_appliation_sms_url(self):
        self.resource.create_instance = Mock()
        self.resource.create(sms_url="hey")
        self.resource.create_instance.assert_called_with({"sms_url": "hey"})

    def test_update_appliation_sms_url_method(self):
        self.resource.update_instance = Mock()
        self.resource.update("123", sms_method="hey")
        self.resource.update_instance.assert_called_with(
            "123", {"sms_method": "hey"})
```

ain't it pretty.
