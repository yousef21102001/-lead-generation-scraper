import random
import threading
import os
from dotenv import load_dotenv
from app.utils.logger import logger

load_dotenv()


class ProxyRotator:
    """
    Manages proxy rotation and failure handling
    """

    def __init__(self):
        proxy_list = os.getenv("PROXY_LIST", "")
        self.proxies = [p.strip() for p in proxy_list.split(",") if p.strip()]
        self.failed_proxies = set()
        self.lock = threading.Lock()

        if not self.proxies:
            logger.warning("No proxies found in PROXY_LIST environment variable")

    def get_proxy(self) -> str | None:
        """
        Returns a random working proxy
        """
        with self.lock:
            available = list(set(self.proxies) - self.failed_proxies)

            if not available:
                logger.error("No available proxies left")
                return None

            proxy = random.choice(available)
            logger.debug(f"Using proxy: {proxy}")
            return proxy

    def mark_failed(self, proxy: str):
        """
        Mark proxy as failed to avoid reuse
        """
        if not proxy:
            return

        with self.lock:
            self.failed_proxies.add(proxy)
            logger.warning(f"Marked proxy as failed: {proxy}")

    def reset(self):
        """
        Reset failed proxies list
        """
        with self.lock:
            self.failed_proxies.clear()
            logger.info("Proxy failure list reset")


# Singleton instance
_proxy_rotator = ProxyRotator()


def get_proxy() -> str | None:
    """
    Public helper to get a proxy
    """
    return _proxy_rotator.get_proxy()


def mark_proxy_failed(proxy: str):
    """
    Public helper to mark proxy as failed
    """
    _proxy_rotator.mark_failed(proxy)
