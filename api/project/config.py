import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ARKIME_FIELDS_INDEX = f"{os.getenv('ARKIME_FIELDS_INDEX', 'arkime_fields')}"
    ARKIME_INDEX_PATTERN = f"{os.getenv('ARKIME_INDEX_PATTERN', 'arkime_sessions3-*')}"
    ARKIME_INDEX_TIME_FIELD = f"{os.getenv('ARKIME_INDEX_TIME_FIELD', 'firstPacket')}"
    BUILD_DATE = f"{os.getenv('BUILD_DATE', 'unknown')}"
    DASHBOARDS_URL = f"{os.getenv('DASHBOARDS_URL', 'http://dashboards:5601/dashboards')}"
    MALCAP_API_PREFIX = f"{os.getenv('MALCAP_API_PREFIX', 'mapi')}"
    MALCAP_API_DEBUG = f"{os.getenv('MALCAP_API_DEBUG', 'false')}"
    MALCAP_TEMPLATE = f"{os.getenv('MALCAP_TEMPLATE', 'malcap_template')}"
    MALCAP_VERSION = f"{os.getenv('MALCAP_VERSION', 'unknown')}"
    OPENSEARCH_URL = f"{os.getenv('OPENSEARCH_URL', 'http://opensearch:9200')}"
    OPENSEARCH_LOCAL = f"{os.getenv('OPENSEARCH_LOCAL', 'true')}"
    OPENSEARCH_SSL_CERTIFICATE_VERIFICATION = f"{os.getenv('OPENSEARCH_SSL_CERTIFICATE_VERIFICATION', 'false')}"
    OPENSEARCH_CREDS_CONFIG_FILE = (
        f"{os.getenv('OPENSEARCH_CREDS_CONFIG_FILE', '/var/local/curlrc/.opensearch.primary.curlrc')}"
    )
    RESULT_SET_LIMIT = int(f"{os.getenv('RESULT_SET_LIMIT', '500')}")
    VCS_REVISION = f"{os.getenv('VCS_REVISION', 'unknown')}"
