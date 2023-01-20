from multiprocessing.managers import BaseProxy

class AcquirerProxy(BaseProxy):
    _exposed_ = ('acquire', 'release')
    def acquire(self, blocking=True, timeout=None):
        args = (blocking,) if timeout is None else (blocking, timeout)
        return self._callmethod('acquire', args)
    def release(self):
        return self._callmethod('release')
    def __enter__(self):
        return self._callmethod('acquire')
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._callmethod('release')