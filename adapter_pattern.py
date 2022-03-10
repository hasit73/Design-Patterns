"""
Adapter Design Pattern

Adapter pattern works as a bridge between two incompatible interfaces.
This type of design pattern comes under structural pattern as
this pattern combines the capability of two independent interfaces.

Assume that there is one API that gives information about location.
and its response is in JSON format.

but you want to show xml response to the users.
Then create Adapter class that convert JSON to XML

"""


class MyAPI:

    def __init__(self, service_name):
        """ MyAPI is sample class that works as API
            But actually it isn't API
            It just returns static response.
        Args:
            service_name (str): Name of service
        """
        self.service_name = service_name
        # right now response is static
        # Not going to develop actual API.
        self.response = {
            "Service": self.service_name,
        }

    def get(self, url):
        """ Get method
        Args:
            url (str): URL
        Returns:
            dict: JSON response
        """
        self.response["method"] = "GET"
        self.response["url"] = url
        self.response["status_code"] = "200"
        return self.response

    def post(self, url):
        """ Post method
        Args:
            url (str): URL
        Returns:
            dict: JSON response
        """

        self.response["method"] = "POST"
        self.response["status_code"] = "200"
        return self.response


class JSONToXMLAdapter:
    """ Use Adapter Design pattern
        To create JSONToXMLAdapter class
    """
    def __init__(self):
        self.level = 1

    def convert_json_to_xml(self, json_response):
        """ Convert json to xml response
        Args:
            json_response (str): JSON response
        Returns:
            xml_response (str): XML response
        """
        xml_response = "\n<response>"
        for tag, value in json_response.items():
            text = f"\n<{tag}> {value} </{tag}>"
            xml_response += text
        xml_response += "\n</response>"
        return xml_response


if __name__ == "__main__":

    api = MyAPI("SMTP")
    xml_parser = JSONToXMLAdapter()

    json_response = api.get("google.com")
    print("JSON response : ", json_response)

    xml_response = xml_parser.convert_json_to_xml(json_response)
    print("XML response : ", xml_response)
