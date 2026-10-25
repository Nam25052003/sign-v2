from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode


def encode_url(url: str) -> str:
    """
    Encode query parameters trong URL, giữ nguyên scheme, host và path.

    Args:
        url: URL cần encode.

    Returns:
        URL đã encode query parameters.
    """
    parsed = urlsplit(url)

    query_params = parse_qsl(
        parsed.query,
        keep_blank_values=True,
    )

    encoded_query = urlencode(query_params)

    return urlunsplit((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        encoded_query,
        parsed.fragment,
    ))


if __name__ == "__main__":
    qs = "MOqooZ9hMXZlKOaP7OFhdDAWD7Lnud7HVKb7xJCU2p-rzJUeqXoGgzzv48e5VeXgYg5tlIpg84YVRxRaF2WQ82Ejb6kFi263m0ykCFbQeGZ1t4l2tEwuyayRcBenewn8ehWQuJ1/Qdx1JBZt1ufkcHe5GJqQeMD97GNAXJfo31JuxVvcUiEwKvnGxKwRRU9LylczMggVMwrQLI0MqaCao5vRH9gRpWW-Y9AdESky-qMXQbG5m9ZAuK2IoiD0Y2JusX9xAaKc0lsvF/5xZyx5vdcYPfh9-qoznX3p4xXzYn93kM-OLMFvoq7k6zpmJh7Bb2qmKwr5YMLDTpUkAJtxQWiBNAKqr0xPv8yw-UgPrz9glSQnbIPslNM0trcB-eWNqpNZmoEvweb5/aSHTvPVFZtMAesqZUxFyTNs-gfq9isOQOw572/="

    encoded_url = encode_url(qs)

    print(encoded_url)