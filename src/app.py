
def lambda_handler(event, context):
    request = event["Records"][0]["cf"]["request"]
    old_uri: str = request["uri"]
    if old_uri.endswith("/"):
        new_uri = old_uri + "index.html"
    else:
        new_uri = old_uri
    request["uri"] = new_uri
    return request

