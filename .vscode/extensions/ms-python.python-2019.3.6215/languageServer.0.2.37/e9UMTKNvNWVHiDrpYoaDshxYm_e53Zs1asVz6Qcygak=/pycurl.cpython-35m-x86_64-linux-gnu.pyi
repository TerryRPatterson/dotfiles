import builtins as _mod_builtins
import importlib._bootstrap as _mod_importlib__bootstrap

ACCEPTTIMEOUT_MS = 212
ACCEPT_ENCODING = 10102
ADDRESS_SCOPE = 171
APPCONNECT_TIME = 3145761
APPEND = 50
AUTOREFERER = 58
BUFFERSIZE = 98
CAINFO = 10065
CAPATH = 10097
CLOSESOCKETFUNCTION = 20208
COMPILE_DATE = 'May 29 2017 14:59:29'
COMPILE_LIBCURL_VERSION_NUM = 471808
COMPILE_PY_VERSION_HEX = 50660336
CONDITION_UNMET = 2097187
CONNECTTIMEOUT = 78
CONNECTTIMEOUT_MS = 156
CONNECT_ONLY = 141
CONNECT_TIME = 3145733
CONTENT_LENGTH_DOWNLOAD = 3145743
CONTENT_LENGTH_UPLOAD = 3145744
CONTENT_TYPE = 1048594
COOKIE = 10022
COOKIEFILE = 10031
COOKIEJAR = 10082
COOKIELIST = 10135
COOKIESESSION = 96
COPYPOSTFIELDS = 10165
CRLF = 27
CRLFILE = 10169
CSELECT_ERR = 4
CSELECT_IN = 1
CSELECT_OUT = 2
CURL_HTTP_VERSION_1_0 = 1
CURL_HTTP_VERSION_1_1 = 2
CURL_HTTP_VERSION_2 = 3
CURL_HTTP_VERSION_2TLS = 4
CURL_HTTP_VERSION_2_0 = 3
CURL_HTTP_VERSION_LAST = 6
CURL_HTTP_VERSION_NONE = 0
CUSTOMREQUEST = 10036
class Curl(_mod_builtins.object):
    'Curl() -> New Curl object\n\nCreates a new :ref:`curlobject` which corresponds to a\n``CURL`` handle in libcurl. Curl objects automatically set\nCURLOPT_VERBOSE to 0, CURLOPT_NOPROGRESS to 1, provide a default\nCURLOPT_USERAGENT and setup CURLOPT_ERRORBUFFER to point to a\nprivate error buffer.\n\nImplicitly calls :py:func:`pycurl.global_init` if the latter has not yet been called.'
    __class__ = Curl
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getstate__(self):
        pass
    
    def __init__(self):
        'Curl() -> New Curl object\n\nCreates a new :ref:`curlobject` which corresponds to a\n``CURL`` handle in libcurl. Curl objects automatically set\nCURLOPT_VERBOSE to 0, CURLOPT_NOPROGRESS to 1, provide a default\nCURLOPT_USERAGENT and setup CURLOPT_ERRORBUFFER to point to a\nprivate error buffer.\n\nImplicitly calls :py:func:`pycurl.global_init` if the latter has not yet been called.'
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close() -> None\n\nClose handle and end curl session.\n\nCorresponds to `curl_easy_cleanup`_ in libcurl. This method is\nautomatically called by pycurl when a Curl object no longer has any\nreferences to it, but can also be called explicitly.\n\n.. _curl_easy_cleanup:\n    http://curl.haxx.se/libcurl/c/curl_easy_cleanup.html'
        pass
    
    def errstr(self):
        'errstr() -> string\n\nReturn the internal libcurl error buffer of this handle as a string.\n\nReturn value is a ``str`` instance on all Python versions.'
        return ''
    
    def getinfo(self, info):
        'getinfo(info) -> Result\n\nExtract and return information from a curl session.\n\nCorresponds to `curl_easy_getinfo`_ in libcurl, where *option* is\nthe same as the ``CURLINFO_*`` constants in libcurl, except that the\n``CURLINFO_`` prefix has been removed. (See below for exceptions.)\n*Result* contains an integer, float or string, depending on which\noption is given. The ``getinfo`` method should not be called unless\n``perform`` has been called and finished.\n\nIn order to distinguish between similarly-named CURLOPT and CURLINFO\nconstants, some have ``OPT_`` and ``INFO_`` prefixes. These are\n``INFO_FILETIME``, ``OPT_FILETIME``, ``INFO_COOKIELIST`` (but ``setopt`` uses\n``COOKIELIST``!), ``INFO_CERTINFO``, and ``OPT_CERTINFO``.\n\nThe value returned by ``getinfo(INFO_CERTINFO)`` is a list with one element\nper certificate in the chain, starting with the leaf; each element is a\nsequence of *(key, value)* tuples.\n\nExample usage::\n\n    import pycurl\n    c = pycurl.Curl()\n    c.setopt(pycurl.URL, "http://sf.net")\n    c.setopt(pycurl.FOLLOWLOCATION, 1)\n    c.perform()\n    print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)\n    ...\n    --> 200 "http://sourceforge.net/"\n\n\nRaises pycurl.error exception upon failure.\n\n.. _curl_easy_getinfo:\n    http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html'
        pass
    
    def pause(self, bitmask):
        'pause(bitmask) -> None\n\nPause or unpause a curl handle. Bitmask should be a value such as\nPAUSE_RECV or PAUSE_CONT.\n\nCorresponds to `curl_easy_pause`_ in libcurl. The argument should be\nderived from the ``PAUSE_RECV``, ``PAUSE_SEND``, ``PAUSE_ALL`` and\n``PAUSE_CONT`` constants.\n\nRaises pycurl.error exception upon failure.\n\n.. _curl_easy_pause: http://curl.haxx.se/libcurl/c/curl_easy_pause.html'
        pass
    
    def perform(self):
        'perform() -> None\n\nPerform a file transfer.\n\nCorresponds to `curl_easy_perform`_ in libcurl.\n\nRaises pycurl.error exception upon failure.\n\n.. _curl_easy_perform:\n    http://curl.haxx.se/libcurl/c/curl_easy_perform.html'
        pass
    
    def reset(self):
        'reset() -> None\n\nReset all options set on curl handle to default values, but preserves\nlive connections, session ID cache, DNS cache, cookies, and shares.\n\nCorresponds to `curl_easy_reset`_ in libcurl.\n\n.. _curl_easy_reset: http://curl.haxx.se/libcurl/c/curl_easy_reset.html'
        pass
    
    def setopt(self, option, value):
        'setopt(option, value) -> None\n\nSet curl session option. Corresponds to `curl_easy_setopt`_ in libcurl.\n\n*option* specifies which option to set. PycURL defines constants\ncorresponding to ``CURLOPT_*`` constants in libcurl, except that\nthe ``CURLOPT_`` prefix is removed. For example, ``CURLOPT_URL`` is\nexposed in PycURL as ``pycurl.URL``. For convenience, ``CURLOPT_*``\nconstants are also exposed on the Curl objects themselves::\n\n    import pycurl\n    c = pycurl.Curl()\n    c.setopt(pycurl.URL, "http://www.python.org/")\n    # Same as:\n    c.setopt(c.URL, "http://www.python.org/")\n\nIn order to distinguish between similarly-named CURLOPT and CURLINFO\nconstants, some have CURLOPT constants have ``OPT_`` prefixes.\nThese are ``OPT_FILETIME`` and ``OPT_CERTINFO``.\nAs an exception to the exception, ``COOKIELIST`` does not have an ``OPT_``\nprefix but the corresponding CURLINFO option is ``INFO_COOKIELIST``.\n\n*value* specifies the value to set the option to. Different options accept\nvalues of different types:\n\n- Options specified by `curl_easy_setopt`_ as accepting ``1`` or an\n  integer value accept Python integers, long integers (on Python 2.x) and\n  booleans::\n\n    c.setopt(pycurl.FOLLOWLOCATION, True)\n    c.setopt(pycurl.FOLLOWLOCATION, 1)\n    # Python 2.x only:\n    c.setopt(pycurl.FOLLOWLOCATION, 1L)\n\n- Options specified as accepting strings by ``curl_easy_setopt`` accept\n  byte strings (``str`` on Python 2, ``bytes`` on Python 3) and\n  Unicode strings with ASCII code points only.\n  For more information, please refer to :ref:`unicode`. Example::\n\n    c.setopt(pycurl.URL, "http://www.python.org/")\n    c.setopt(pycurl.URL, u"http://www.python.org/")\n    # Python 3.x only:\n    c.setopt(pycurl.URL, b"http://www.python.org/")\n\n- ``HTTP200ALIASES``, ``HTTPHEADER``, ``POSTQUOTE``, ``PREQUOTE``,\n  ``PROXYHEADER`` and\n  ``QUOTE`` accept a list or tuple of strings. The same rules apply to these\n  strings as do to string option values. Example::\n\n    c.setopt(pycurl.HTTPHEADER, ["Accept:"])\n    c.setopt(pycurl.HTTPHEADER, ("Accept:",))\n\n- ``READDATA`` accepts a file object or any Python object which has\n  a ``read`` method. On Python 2, a file object will be passed directly\n  to libcurl and may result in greater transfer efficiency, unless\n  PycURL has been compiled with ``AVOID_STDIO`` option.\n  On Python 3 and on Python 2 when the value is not a true file object,\n  ``READDATA`` is emulated in PycURL via ``READFUNCTION``.\n  The file should generally be opened in binary mode. Example::\n\n    f = open(\'file.txt\', \'rb\')\n    c.setopt(c.READDATA, f)\n\n- ``WRITEDATA`` and ``WRITEHEADER`` accept a file object or any Python\n  object which has a ``write`` method. On Python 2, a file object will\n  be passed directly to libcurl and may result in greater transfer efficiency,\n  unless PycURL has been compiled with ``AVOID_STDIO`` option.\n  On Python 3 and on Python 2 when the value is not a true file object,\n  ``WRITEDATA`` is emulated in PycURL via ``WRITEFUNCTION``.\n  The file should generally be opened in binary mode. Example::\n\n    f = open(\'/dev/null\', \'wb\')\n    c.setopt(c.WRITEDATA, f)\n\n- ``*FUNCTION`` options accept a function. Supported callbacks are documented\n  in :ref:`callbacks`. Example::\n\n    # Python 2\n    import StringIO\n    b = StringIO.StringIO()\n    c.setopt(pycurl.WRITEFUNCTION, b.write)\n\n- ``SHARE`` option accepts a :ref:`curlshareobject`.\n\nIt is possible to set integer options - and only them - that PycURL does\nnot know about by using the numeric value of the option constant directly.\nFor example, ``pycurl.VERBOSE`` has the value 42, and may be set as follows::\n\n    c.setopt(42, 1)\n\n*setopt* can reset some options to their default value, performing the job of\n:py:meth:`pycurl.Curl.unsetopt`, if ``None`` is passed\nfor the option value. The following two calls are equivalent::\n\n    c.setopt(c.URL, None)\n    c.unsetopt(c.URL)\n\nRaises TypeError when the option value is not of a type accepted by the\nrespective option, and pycurl.error exception when libcurl rejects the\noption or its value.\n\n.. _curl_easy_setopt: http://curl.haxx.se/libcurl/c/curl_easy_setopt.html'
        pass
    
    def setopt_string(self, option, value):
        'setopt_string(option, value) -> None\n\nSet curl session option to a string value.\n\nThis method allows setting string options that are not officially supported\nby PycURL, for example because they did not exist when the version of PycURL\nbeing used was released.\n:py:meth:`pycurl.Curl.setopt` should be used for setting options that\nPycURL knows about.\n\n**Warning:** No checking is performed that *option* does, in fact,\nexpect a string value. Using this method incorrectly can crash the program\nand may lead to a security vulnerability.\nFurthermore, it is on the application to ensure that the *value* object\ndoes not get garbage collected while libcurl is using it.\nlibcurl copies most string options but not all; one option whose value\nis not copied by libcurl is `CURLOPT_POSTFIELDS`_.\n\n*option* would generally need to be given as an integer literal rather than\na symbolic constant.\n\n*value* can be a binary string or a Unicode string using ASCII code points,\nsame as with string options given to PycURL elsewhere.\n\nExample setting URL via ``setopt_string``::\n\n    import pycurl\n    c = pycurl.Curl()\n    c.setopt_string(10002, "http://www.python.org/")\n\n.. _CURLOPT_POSTFIELDS: http://curl.haxx.se/libcurl/c/CURLOPT_POSTFIELDS.html'
        pass
    
    def unsetopt(self, option):
        'unsetopt(option) -> None\n\nReset curl session option to its default value.\n\nOnly some curl options may be reset via this method.\n\nlibcurl does not provide a general way to reset a single option to its default value;\n:py:meth:`pycurl.Curl.reset` resets all options to their default values,\notherwise :py:meth:`pycurl.Curl.setopt` must be called with whatever value\nis the default. For convenience, PycURL provides this unsetopt method\nto reset some of the options to their default values.\n\nRaises pycurl.error exception on failure.\n\n``c.unsetopt(option)`` is equivalent to ``c.setopt(option, None)``.'
        pass
    

class CurlMulti(_mod_builtins.object):
    'CurlMulti() -> New CurlMulti object\n\nCreates a new :ref:`curlmultiobject` which corresponds to\na ``CURLM`` handle in libcurl.'
    __class__ = CurlMulti
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getstate__(self):
        pass
    
    def __init__(self):
        'CurlMulti() -> New CurlMulti object\n\nCreates a new :ref:`curlmultiobject` which corresponds to\na ``CURLM`` handle in libcurl.'
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add_handle(self, Curlobject):
        'add_handle(Curl object) -> None\n\nCorresponds to `curl_multi_add_handle`_ in libcurl. This method adds an\nexisting and valid Curl object to the CurlMulti object.\n\nIMPORTANT NOTE: add_handle does not implicitly add a Python reference to the\nCurl object (and thus does not increase the reference count on the Curl\nobject).\n\n.. _curl_multi_add_handle:\n    http://curl.haxx.se/libcurl/c/curl_multi_add_handle.html'
        pass
    
    def assign(self, sockfd, object):
        'assign(sockfd, object) -> None\n\nCreates an association in the multi handle between the given socket and\na private object in the application.\nCorresponds to `curl_multi_assign`_ in libcurl.\n\n.. _curl_multi_assign: http://curl.haxx.se/libcurl/c/curl_multi_assign.html'
        pass
    
    def close(self):
        'close() -> None\n\nCorresponds to `curl_multi_cleanup`_ in libcurl. This method is\nautomatically called by pycurl when a CurlMulti object no longer has any\nreferences to it, but can also be called explicitly.\n\n.. _curl_multi_cleanup:\n    http://curl.haxx.se/libcurl/c/curl_multi_cleanup.html'
        pass
    
    def fdset(self):
        'fdset() -> tuple of lists with active file descriptors, readable, writeable, exceptions\n\nReturns a tuple of three lists that can be passed to the select.select() method.\n\nCorresponds to `curl_multi_fdset`_ in libcurl. This method extracts the\nfile descriptor information from a CurlMulti object. The returned lists can\nbe used with the ``select`` module to poll for events.\n\nExample usage::\n\n    import pycurl\n    c = pycurl.Curl()\n    c.setopt(pycurl.URL, "http://curl.haxx.se")\n    m = pycurl.CurlMulti()\n    m.add_handle(c)\n    while 1:\n        ret, num_handles = m.perform()\n        if ret != pycurl.E_CALL_MULTI_PERFORM: break\n    while num_handles:\n        apply(select.select, m.fdset() + (1,))\n        while 1:\n            ret, num_handles = m.perform()\n            if ret != pycurl.E_CALL_MULTI_PERFORM: break\n\n.. _curl_multi_fdset:\n    http://curl.haxx.se/libcurl/c/curl_multi_fdset.html'
        pass
    
    def info_read(self, max_objects=None):
        'info_read([max_objects]) -> tuple(number of queued messages, a list of successful objects, a list of failed objects)\n\nReturns a tuple (number of queued handles, [curl objects]).\n\nCorresponds to the `curl_multi_info_read`_ function in libcurl. This\nmethod extracts at most *max* messages from the multi stack and returns them\nin two lists. The first list contains the handles which completed\nsuccessfully and the second list contains a tuple *(curl object, curl error\nnumber, curl error message)* for each failed curl object. The number of\nqueued messages after this method has been called is also returned.\n\n.. _curl_multi_info_read:\n    http://curl.haxx.se/libcurl/c/curl_multi_info_read.html'
        pass
    
    def perform(self):
        'perform() -> tuple of status and the number of active Curl objects\n\nCorresponds to `curl_multi_perform`_ in libcurl.\n\n.. _curl_multi_perform:\n    http://curl.haxx.se/libcurl/c/curl_multi_perform.html'
        pass
    
    def remove_handle(self, Curlobject):
        'remove_handle(Curl object) -> None\n\nCorresponds to `curl_multi_remove_handle`_ in libcurl. This method\nremoves an existing and valid Curl object from the CurlMulti object.\n\nIMPORTANT NOTE: remove_handle does not implicitly remove a Python reference\nfrom the Curl object (and thus does not decrease the reference count on the\nCurl object).\n\n.. _curl_multi_remove_handle:\n    http://curl.haxx.se/libcurl/c/curl_multi_remove_handle.html'
        pass
    
    def select(self, timeout=None):
        'select([timeout]) -> number of ready file descriptors or -1 on timeout\n\nReturns result from doing a select() on the curl multi file descriptor\nwith the given timeout.\n\nThis is a convenience function which simplifies the combined use of\n``fdset()`` and the ``select`` module.\n\nExample usage::\n\n    import pycurl\n    c = pycurl.Curl()\n    c.setopt(pycurl.URL, "http://curl.haxx.se")\n    m = pycurl.CurlMulti()\n    m.add_handle(c)\n    while 1:\n        ret, num_handles = m.perform()\n        if ret != pycurl.E_CALL_MULTI_PERFORM: break\n    while num_handles:\n        ret = m.select(1.0)\n        if ret == -1:  continue\n        while 1:\n            ret, num_handles = m.perform()\n            if ret != pycurl.E_CALL_MULTI_PERFORM: break'
        pass
    
    def setopt(self, option, value):
        'setopt(option, value) -> None\n\nSet curl multi option. Corresponds to `curl_multi_setopt`_ in libcurl.\n\n*option* specifies which option to set. PycURL defines constants\ncorresponding to ``CURLMOPT_*`` constants in libcurl, except that\nthe ``CURLMOPT_`` prefix is replaced with ``M_`` prefix.\nFor example, ``CURLMOPT_PIPELINING`` is\nexposed in PycURL as ``pycurl.M_PIPELINING``. For convenience, ``CURLMOPT_*``\nconstants are also exposed on CurlMulti objects::\n\n    import pycurl\n    m = pycurl.CurlMulti()\n    m.setopt(pycurl.M_PIPELINING, 1)\n    # Same as:\n    m.setopt(m.M_PIPELINING, 1)\n\n*value* specifies the value to set the option to. Different options accept\nvalues of different types:\n\n- Options specified by `curl_multi_setopt`_ as accepting ``1`` or an\n  integer value accept Python integers, long integers (on Python 2.x) and\n  booleans::\n\n    m.setopt(pycurl.M_PIPELINING, True)\n    m.setopt(pycurl.M_PIPELINING, 1)\n    # Python 2.x only:\n    m.setopt(pycurl.M_PIPELINING, 1L)\n\n- ``*FUNCTION`` options accept a function. Supported callbacks are\n  ``CURLMOPT_SOCKETFUNCTION`` AND ``CURLMOPT_TIMERFUNCTION``. Please refer to\n  the PycURL test suite for examples on using the callbacks.\n\nRaises TypeError when the option value is not of a type accepted by the\nrespective option, and pycurl.error exception when libcurl rejects the\noption or its value.\n\n.. _curl_multi_setopt: http://curl.haxx.se/libcurl/c/curl_multi_setopt.html'
        pass
    
    def socket_action(self, sockfd, ev_bitmask):
        'socket_action(sockfd, ev_bitmask) -> tuple\n\nReturns result from doing a socket_action() on the curl multi file descriptor\nwith the given timeout.\nCorresponds to `curl_multi_socket_action`_ in libcurl.\n\n.. _curl_multi_socket_action: http://curl.haxx.se/libcurl/c/curl_multi_socket_action.html'
        pass
    
    def socket_all(self):
        'socket_all() -> Tuple.\n\nReturns result from doing a socket_all() on the curl multi file descriptor\nwith the given timeout.'
        pass
    
    def timeout(self):
        'timeout() -> int\n\nReturns how long to wait for action before proceeding.\nCorresponds to `curl_multi_timeout`_ in libcurl.\n\n.. _curl_multi_timeout: http://curl.haxx.se/libcurl/c/curl_multi_timeout.html'
        return 1
    

class CurlShare(_mod_builtins.object):
    'CurlShare() -> New CurlShare object\n\nCreates a new :ref:`curlshareobject` which corresponds to a\n``CURLSH`` handle in libcurl. CurlShare objects is what you pass as an\nargument to the SHARE option on :ref:`Curl objects <curlobject>`.'
    __class__ = CurlShare
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getstate__(self):
        pass
    
    def __init__(self):
        'CurlShare() -> New CurlShare object\n\nCreates a new :ref:`curlshareobject` which corresponds to a\n``CURLSH`` handle in libcurl. CurlShare objects is what you pass as an\nargument to the SHARE option on :ref:`Curl objects <curlobject>`.'
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close() -> None\n\nClose shared handle.\n\nCorresponds to `curl_share_cleanup`_ in libcurl. This method is\nautomatically called by pycurl when a CurlShare object no longer has\nany references to it, but can also be called explicitly.\n\n.. _curl_share_cleanup:\n    http://curl.haxx.se/libcurl/c/curl_share_cleanup.html'
        pass
    
    def setopt(self, option, value):
        "setopt(option, value) -> None\n\nSet curl share option.\n\nCorresponds to `curl_share_setopt`_ in libcurl, where *option* is\nspecified with the ``CURLSHOPT_*`` constants in libcurl, except that the\n``CURLSHOPT_`` prefix has been changed to ``SH_``. Currently, *value* must be\neither ``LOCK_DATA_COOKIE`` or ``LOCK_DATA_DNS``.\n\nExample usage::\n\n    import pycurl\n    curl = pycurl.Curl()\n    s = pycurl.CurlShare()\n    s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_COOKIE)\n    s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_DNS)\n    curl.setopt(pycurl.URL, 'http://curl.haxx.se')\n    curl.setopt(pycurl.SHARE, s)\n    curl.perform()\n    curl.close()\n\nRaises pycurl.error exception upon failure.\n\n.. _curl_share_setopt:\n    http://curl.haxx.se/libcurl/c/curl_share_setopt.html"
        pass
    

CurlSockAddr = _mod_importlib__bootstrap.CurlSockAddr
DEBUGFUNCTION = 20094
DEFAULT_PROTOCOL = 10238
DIRLISTONLY = 48
DNS_CACHE_TIMEOUT = 92
DNS_SERVERS = 10211
DNS_USE_GLOBAL_CACHE = 91
EFFECTIVE_URL = 1048577
EGDSOCKET = 10077
ENCODING = 10102
EXPECT_100_TIMEOUT_MS = 227
E_ABORTED_BY_CALLBACK = 42
E_AGAIN = 81
E_ALREADY_COMPLETE = 99999
E_BAD_CALLING_ORDER = 44
E_BAD_CONTENT_ENCODING = 61
E_BAD_DOWNLOAD_RESUME = 36
E_BAD_FUNCTION_ARGUMENT = 43
E_BAD_PASSWORD_ENTERED = 46
E_CALL_MULTI_PERFORM = -1
E_CHUNK_FAILED = 88
E_CONV_FAILED = 75
E_CONV_REQD = 76
E_COULDNT_CONNECT = 7
E_COULDNT_RESOLVE_HOST = 6
E_COULDNT_RESOLVE_PROXY = 5
E_FAILED_INIT = 2
E_FILESIZE_EXCEEDED = 63
E_FILE_COULDNT_READ_FILE = 37
E_FTP_ACCEPT_FAILED = 10
E_FTP_ACCEPT_TIMEOUT = 12
E_FTP_ACCESS_DENIED = 9
E_FTP_BAD_DOWNLOAD_RESUME = 36
E_FTP_BAD_FILE_LIST = 87
E_FTP_CANT_GET_HOST = 15
E_FTP_CANT_RECONNECT = 16
E_FTP_COULDNT_GET_SIZE = 32
E_FTP_COULDNT_RETR_FILE = 19
E_FTP_COULDNT_SET_ASCII = 29
E_FTP_COULDNT_SET_BINARY = 17
E_FTP_COULDNT_SET_TYPE = 17
E_FTP_COULDNT_STOR_FILE = 25
E_FTP_COULDNT_USE_REST = 31
E_FTP_PARTIAL_FILE = 18
E_FTP_PORT_FAILED = 30
E_FTP_PRET_FAILED = 84
E_FTP_QUOTE_ERROR = 21
E_FTP_SSL_FAILED = 64
E_FTP_USER_PASSWORD_INCORRECT = 10
E_FTP_WEIRD_227_FORMAT = 14
E_FTP_WEIRD_PASS_REPLY = 11
E_FTP_WEIRD_PASV_REPLY = 13
E_FTP_WEIRD_SERVER_REPLY = 8
E_FTP_WEIRD_USER_REPLY = 12
E_FTP_WRITE_ERROR = 20
E_FUNCTION_NOT_FOUND = 41
E_GOT_NOTHING = 52
E_HTTP2 = 16
E_HTTP_NOT_FOUND = 22
E_HTTP_PORT_FAILED = 45
E_HTTP_POST_ERROR = 34
E_HTTP_RANGE_ERROR = 33
E_HTTP_RETURNED_ERROR = 22
E_INTERFACE_FAILED = 45
E_LDAP_CANNOT_BIND = 38
E_LDAP_INVALID_URL = 62
E_LDAP_SEARCH_FAILED = 39
E_LIBRARY_NOT_FOUND = 40
E_LOGIN_DENIED = 67
E_MALFORMAT_USER = 24
E_MULTI_ADDED_ALREADY = 7
E_MULTI_BAD_EASY_HANDLE = 2
E_MULTI_BAD_HANDLE = 1
E_MULTI_BAD_SOCKET = 5
E_MULTI_CALL_MULTI_PERFORM = -1
E_MULTI_CALL_MULTI_SOCKET = -1
E_MULTI_INTERNAL_ERROR = 4
E_MULTI_OK = 0
E_MULTI_OUT_OF_MEMORY = 3
E_MULTI_UNKNOWN_OPTION = 6
E_NOT_BUILT_IN = 4
E_NO_CONNECTION_AVAILABLE = 89
E_OK = 0
E_OPERATION_TIMEDOUT = 28
E_OPERATION_TIMEOUTED = 28
E_OUT_OF_MEMORY = 27
E_PARTIAL_FILE = 18
E_PEER_FAILED_VERIFICATION = 51
E_QUOTE_ERROR = 21
E_RANGE_ERROR = 33
E_READ_ERROR = 26
E_RECV_ERROR = 56
E_REMOTE_ACCESS_DENIED = 9
E_REMOTE_DISK_FULL = 70
E_REMOTE_FILE_EXISTS = 73
E_REMOTE_FILE_NOT_FOUND = 78
E_RTSP_CSEQ_ERROR = 85
E_RTSP_SESSION_ERROR = 86
E_SEND_ERROR = 55
E_SEND_FAIL_REWIND = 65
E_SHARE_IN_USE = 57
E_SSH = 79
E_SSL_CACERT = 60
E_SSL_CACERT_BADFILE = 77
E_SSL_CERTPROBLEM = 58
E_SSL_CIPHER = 59
E_SSL_CONNECT_ERROR = 35
E_SSL_CRL_BADFILE = 82
E_SSL_ENGINE_INITFAILED = 66
E_SSL_ENGINE_NOTFOUND = 53
E_SSL_ENGINE_SETFAILED = 54
E_SSL_INVALIDCERTSTATUS = 91
E_SSL_ISSUER_ERROR = 83
E_SSL_PEER_CERTIFICATE = 51
E_SSL_PINNEDPUBKEYNOTMATCH = 90
E_SSL_SHUTDOWN_FAILED = 80
E_TELNET_OPTION_SYNTAX = 49
E_TFTP_DISKFULL = 70
E_TFTP_EXISTS = 73
E_TFTP_ILLEGAL = 71
E_TFTP_NOSUCHUSER = 74
E_TFTP_NOTFOUND = 68
E_TFTP_PERM = 69
E_TFTP_UNKNOWNID = 72
E_TOO_MANY_REDIRECTS = 47
E_UNKNOWN_OPTION = 48
E_UNKNOWN_TELNET_OPTION = 48
E_UNSUPPORTED_PROTOCOL = 1
E_UPLOAD_FAILED = 25
E_URL_MALFORMAT = 3
E_URL_MALFORMAT_USER = 4
E_USE_SSL_FAILED = 64
E_WRITE_ERROR = 23
FAILONERROR = 45
FILE = 10001
FOLLOWLOCATION = 52
FORBID_REUSE = 75
FORM_BUFFER = 11
FORM_BUFFERPTR = 12
FORM_CONTENTS = 4
FORM_CONTENTTYPE = 14
FORM_FILE = 10
FORM_FILENAME = 16
FRESH_CONNECT = 74
FTPAPPEND = 50
FTPAUTH_DEFAULT = 0
FTPAUTH_SSL = 1
FTPAUTH_TLS = 2
FTPLISTONLY = 48
FTPMETHOD_DEFAULT = 0
FTPMETHOD_MULTICWD = 1
FTPMETHOD_NOCWD = 2
FTPMETHOD_SINGLECWD = 3
FTPPORT = 10017
FTPSSLAUTH = 129
FTPSSL_ALL = 3
FTPSSL_CONTROL = 2
FTPSSL_NONE = 0
FTPSSL_TRY = 1
FTP_ACCOUNT = 10134
FTP_ALTERNATIVE_TO_USER = 10147
FTP_CREATE_MISSING_DIRS = 110
FTP_ENTRY_PATH = 1048606
FTP_FILEMETHOD = 138
FTP_RESPONSE_TIMEOUT = 112
FTP_SKIP_PASV_IP = 137
FTP_SSL = 119
FTP_SSL_CCC = 154
FTP_USE_EPRT = 106
FTP_USE_EPSV = 85
FTP_USE_PRET = 188
GLOBAL_ACK_EINTR = 4
GLOBAL_ALL = 3
GLOBAL_DEFAULT = 3
GLOBAL_NOTHING = 0
GLOBAL_SSL = 1
GLOBAL_WIN32 = 2
GSSAPI_DELEGATION = 210
GSSAPI_DELEGATION_FLAG = 2
GSSAPI_DELEGATION_NONE = 0
GSSAPI_DELEGATION_POLICY_FLAG = 1
HEADER = 42
HEADERFUNCTION = 20079
HEADEROPT = 229
HEADER_SEPARATE = 1
HEADER_SIZE = 2097163
HEADER_UNIFIED = 0
HTTP200ALIASES = 10104
HTTPAUTH = 107
HTTPAUTH_ANY = -17
HTTPAUTH_ANYSAFE = -18
HTTPAUTH_AVAIL = 2097175
HTTPAUTH_BASIC = 1
HTTPAUTH_DIGEST = 2
HTTPAUTH_DIGEST_IE = 16
HTTPAUTH_GSSNEGOTIATE = 4
HTTPAUTH_NEGOTIATE = 4
HTTPAUTH_NONE = 0
HTTPAUTH_NTLM = 8
HTTPAUTH_NTLM_WB = 32
HTTPAUTH_ONLY = 2147483648
HTTPGET = 80
HTTPHEADER = 10023
HTTPPOST = 10024
HTTPPROXYTUNNEL = 61
HTTP_CODE = 2097154
HTTP_CONNECTCODE = 2097174
HTTP_CONTENT_DECODING = 158
HTTP_TRANSFER_DECODING = 157
HTTP_VERSION = 84
IGNORE_CONTENT_LENGTH = 136
INFILE = 10009
INFILESIZE = 30115
INFILESIZE_LARGE = 30115
INFOTYPE_DATA_IN = 3
INFOTYPE_DATA_OUT = 4
INFOTYPE_HEADER_IN = 1
INFOTYPE_HEADER_OUT = 2
INFOTYPE_SSL_DATA_IN = 5
INFOTYPE_SSL_DATA_OUT = 6
INFOTYPE_TEXT = 0
INFO_CERTINFO = 4194338
INFO_COOKIELIST = 4194332
INFO_FILETIME = 2097166
INFO_RTSP_CLIENT_CSEQ = 2097189
INFO_RTSP_CSEQ_RECV = 2097191
INFO_RTSP_SERVER_CSEQ = 2097190
INFO_RTSP_SESSION_ID = 1048612
INTERFACE = 10062
IOCMD_NOP = 0
IOCMD_RESTARTREAD = 1
IOCTLFUNCTION = 20130
IOE_FAILRESTART = 2
IOE_OK = 0
IOE_UNKNOWNCMD = 1
IPRESOLVE = 113
IPRESOLVE_V4 = 1
IPRESOLVE_V6 = 2
IPRESOLVE_WHATEVER = 0
ISSUERCERT = 10170
KEYPASSWD = 10026
KHMATCH_MISMATCH = 1
KHMATCH_MISSING = 2
KHMATCH_OK = 0
KHSTAT_DEFER = 3
KHSTAT_FINE = 1
KHSTAT_FINE_ADD_TO_FILE = 0
KHSTAT_REJECT = 2
KHTYPE_DSS = 3
KHTYPE_RSA = 2
KHTYPE_RSA1 = 1
KHTYPE_UNKNOWN = 0
KRB4LEVEL = 10063
KRBLEVEL = 10063
KhKey = _mod_importlib__bootstrap.KhKey
LASTSOCKET = 2097181
LOCALPORT = 139
LOCALPORTRANGE = 140
LOCAL_IP = 1048617
LOCAL_PORT = 2097194
LOCK_DATA_COOKIE = 2
LOCK_DATA_DNS = 3
LOCK_DATA_SSL_SESSION = 4
LOGIN_OPTIONS = 10224
LOW_SPEED_LIMIT = 19
LOW_SPEED_TIME = 20
MAIL_AUTH = 10217
MAIL_FROM = 10186
MAIL_RCPT = 10187
MAXCONNECTS = 71
MAXFILESIZE = 30117
MAXFILESIZE_LARGE = 30117
MAXREDIRS = 68
MAX_RECV_SPEED_LARGE = 30146
MAX_SEND_SPEED_LARGE = 30145
M_CHUNK_LENGTH_PENALTY_SIZE = 30010
M_CONTENT_LENGTH_PENALTY_SIZE = 30009
M_MAXCONNECTS = 6
M_MAX_HOST_CONNECTIONS = 7
M_MAX_PIPELINE_LENGTH = 8
M_MAX_TOTAL_CONNECTIONS = 13
M_PIPELINING = 3
M_PIPELINING_SERVER_BL = 10012
M_PIPELINING_SITE_BL = 10011
M_SOCKETFUNCTION = 20001
M_TIMERFUNCTION = 20004
NAMELOOKUP_TIME = 3145732
NETRC = 51
NETRC_FILE = 10118
NETRC_IGNORED = 0
NETRC_OPTIONAL = 1
NETRC_REQUIRED = 2
NEW_DIRECTORY_PERMS = 160
NEW_FILE_PERMS = 159
NOBODY = 44
NOPROGRESS = 43
NOPROXY = 10177
NOSIGNAL = 99
NUM_CONNECTS = 2097178
OPENSOCKETFUNCTION = 20163
OPT_CERTINFO = 172
OPT_FILETIME = 69
OS_ERRNO = 2097177
PASSWORD = 10174
PATH_AS_IS = 234
PAUSE_ALL = 5
PAUSE_CONT = 0
PAUSE_RECV = 1
PAUSE_SEND = 4
PINNEDPUBLICKEY = 10230
PIPEWAIT = 237
PIPE_HTTP1 = 1
PIPE_MULTIPLEX = 2
PIPE_NOTHING = 0
POLL_IN = 1
POLL_INOUT = 3
POLL_NONE = 0
POLL_OUT = 2
POLL_REMOVE = 4
PORT = 3
POST = 47
POST301 = 161
POSTFIELDS = 10015
POSTFIELDSIZE = 30120
POSTFIELDSIZE_LARGE = 30120
POSTQUOTE = 10039
POSTREDIR = 161
PREQUOTE = 10093
PRETRANSFER_TIME = 3145734
PRIMARY_IP = 1048608
PRIMARY_PORT = 2097192
PROGRESSFUNCTION = 20056
PROTOCOLS = 181
PROTO_ALL = -1
PROTO_DICT = 512
PROTO_FILE = 1024
PROTO_FTP = 4
PROTO_FTPS = 8
PROTO_GOPHER = 33554432
PROTO_HTTP = 1
PROTO_HTTPS = 2
PROTO_IMAP = 4096
PROTO_IMAPS = 8192
PROTO_LDAP = 128
PROTO_LDAPS = 256
PROTO_POP3 = 16384
PROTO_POP3S = 32768
PROTO_RTMP = 524288
PROTO_RTMPE = 2097152
PROTO_RTMPS = 8388608
PROTO_RTMPT = 1048576
PROTO_RTMPTE = 4194304
PROTO_RTMPTS = 16777216
PROTO_RTSP = 262144
PROTO_SCP = 16
PROTO_SFTP = 32
PROTO_SMB = 67108864
PROTO_SMBS = 134217728
PROTO_SMTP = 65536
PROTO_SMTPS = 131072
PROTO_TELNET = 64
PROTO_TFTP = 2048
PROXY = 10004
PROXYAUTH = 111
PROXYAUTH_AVAIL = 2097176
PROXYHEADER = 10228
PROXYPASSWORD = 10176
PROXYPORT = 59
PROXYTYPE = 101
PROXYTYPE_HTTP = 0
PROXYTYPE_HTTP_1_0 = 1
PROXYTYPE_SOCKS4 = 4
PROXYTYPE_SOCKS4A = 6
PROXYTYPE_SOCKS5 = 5
PROXYTYPE_SOCKS5_HOSTNAME = 7
PROXYUSERNAME = 10175
PROXYUSERPWD = 10006
PROXY_SERVICE_NAME = 10235
PROXY_TRANSFER_MODE = 166
PUT = 54
QUOTE = 10028
RANDOM_FILE = 10076
RANGE = 10007
READDATA = 10009
READFUNCTION = 20012
READFUNC_ABORT = 268435456
READFUNC_PAUSE = 268435457
REDIRECT_COUNT = 2097172
REDIRECT_TIME = 3145747
REDIRECT_URL = 1048607
REDIR_POST_301 = 1
REDIR_POST_302 = 2
REDIR_POST_303 = 4
REDIR_POST_ALL = 7
REDIR_PROTOCOLS = 182
REFERER = 10016
REQUEST_SIZE = 2097164
RESOLVE = 10203
RESPONSE_CODE = 2097154
RESUME_FROM = 30116
RESUME_FROM_LARGE = 30116
SASL_IR = 218
SEEKFUNCTION = 20167
SEEKFUNC_CANTSEEK = 2
SEEKFUNC_FAIL = 1
SEEKFUNC_OK = 0
SERVICE_NAME = 10236
SHARE = 10100
SH_SHARE = 1
SH_UNSHARE = 2
SIZE_DOWNLOAD = 3145736
SIZE_UPLOAD = 3145735
SOCKET_TIMEOUT = -1
SOCKOPTFUNCTION = 20148
SOCKOPT_ALREADY_CONNECTED = 2
SOCKOPT_ERROR = 1
SOCKOPT_OK = 0
SOCKS5_GSSAPI_NEC = 180
SOCKS5_GSSAPI_SERVICE = 10179
SOCKTYPE_ACCEPT = 1
SOCKTYPE_IPCXN = 0
SPEED_DOWNLOAD = 3145737
SPEED_UPLOAD = 3145738
SSH_AUTH_ANY = -1
SSH_AUTH_DEFAULT = -1
SSH_AUTH_HOST = 4
SSH_AUTH_KEYBOARD = 8
SSH_AUTH_NONE = 0
SSH_AUTH_PASSWORD = 2
SSH_AUTH_PUBLICKEY = 1
SSH_AUTH_TYPES = 151
SSH_HOST_PUBLIC_KEY_MD5 = 10162
SSH_KEYFUNCTION = 20184
SSH_KNOWNHOSTS = 10183
SSH_PRIVATE_KEYFILE = 10153
SSH_PUBLIC_KEYFILE = 10152
SSLCERT = 10025
SSLCERTPASSWD = 10026
SSLCERTTYPE = 10086
SSLENGINE = 10089
SSLENGINE_DEFAULT = 90
SSLKEY = 10087
SSLKEYPASSWD = 10026
SSLKEYTYPE = 10088
SSLOPT_ALLOW_BEAST = 1
SSLOPT_NO_REVOKE = 2
SSLVERSION = 32
SSLVERSION_DEFAULT = 0
SSLVERSION_SSLv2 = 2
SSLVERSION_SSLv3 = 3
SSLVERSION_TLSv1 = 1
SSLVERSION_TLSv1_0 = 4
SSLVERSION_TLSv1_1 = 5
SSLVERSION_TLSv1_2 = 6
SSL_CIPHER_LIST = 10083
SSL_ENABLE_ALPN = 226
SSL_ENABLE_NPN = 225
SSL_ENGINES = 4194331
SSL_FALSESTART = 233
SSL_OPTIONS = 216
SSL_SESSIONID_CACHE = 150
SSL_VERIFYHOST = 81
SSL_VERIFYPEER = 64
SSL_VERIFYRESULT = 2097165
SSL_VERIFYSTATUS = 232
STARTTRANSFER_TIME = 3145745
STDERR = 10037
TCP_KEEPALIVE = 213
TCP_KEEPIDLE = 214
TCP_KEEPINTVL = 215
TCP_NODELAY = 121
TELNETOPTIONS = 10070
TFTP_BLKSIZE = 178
TIMECONDITION = 33
TIMECONDITION_IFMODSINCE = 1
TIMECONDITION_IFUNMODSINCE = 2
TIMECONDITION_LASTMOD = 3
TIMECONDITION_NONE = 0
TIMEOUT = 13
TIMEOUT_MS = 155
TIMEVALUE = 34
TLSAUTH_PASSWORD = 10205
TLSAUTH_TYPE = 10206
TLSAUTH_USERNAME = 10204
TOTAL_TIME = 3145731
TRANSFERTEXT = 53
TRANSFER_ENCODING = 207
UNIX_SOCKET_PATH = 10231
UNRESTRICTED_AUTH = 105
UPLOAD = 46
URL = 10002
USERAGENT = 10018
USERNAME = 10173
USERPWD = 10005
USESSL_ALL = 3
USESSL_CONTROL = 2
USESSL_NONE = 0
USESSL_TRY = 1
USE_SSL = 119
VERBOSE = 41
VERSION_ASYNCHDNS = 128
VERSION_CONV = 4096
VERSION_CURLDEBUG = 8192
VERSION_DEBUG = 64
VERSION_GSSAPI = 131072
VERSION_GSSNEGOTIATE = 32
VERSION_HTTP2 = 65536
VERSION_IDN = 1024
VERSION_IPV6 = 1
VERSION_KERBEROS4 = 2
VERSION_KERBEROS5 = 262144
VERSION_LARGEFILE = 512
VERSION_LIBZ = 8
VERSION_NTLM = 16
VERSION_NTLM_WB = 32768
VERSION_PSL = 1048576
VERSION_SPNEGO = 256
VERSION_SSL = 4
VERSION_SSPI = 2048
VERSION_TLSAUTH_SRP = 16384
VERSION_UNIX_SOCKETS = 524288
WILDCARDMATCH = 197
WRITEDATA = 10001
WRITEFUNCTION = 20011
WRITEFUNC_PAUSE = 268435457
WRITEHEADER = 10029
XFERINFOFUNCTION = 20219
XOAUTH2_BEARER = 10220
__doc__ = 'This module implements an interface to the cURL library.\n\nTypes:\n\nCurl() -> New object.  Create a new curl object.\nCurlMulti() -> New object.  Create a new curl multi object.\nCurlShare() -> New object.  Create a new curl share object.\n\nFunctions:\n\nglobal_init(option) -> None.  Initialize curl environment.\nglobal_cleanup() -> None.  Cleanup curl environment.\nversion_info() -> tuple.  Return version information.'
__file__ = '/usr/lib64/python3.5/site-packages/pycurl.cpython-35m-x86_64-linux-gnu.so'
__name__ = 'pycurl'
__package__ = ''
class error(_mod_builtins.Exception):
    __class__ = error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    __module__ = 'pycurl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def global_cleanup():
    'global_cleanup() -> None\n\nCleanup curl environment.\n\nCorresponds to `curl_global_cleanup`_ in libcurl.\n\n.. _curl_global_cleanup: http://curl.haxx.se/libcurl/c/curl_global_cleanup.html'
    pass

def global_init(option):
    'global_init(option) -> None\n\nInitialize curl environment.\n\n*option* is one of the constants pycurl.GLOBAL_SSL, pycurl.GLOBAL_WIN32,\npycurl.GLOBAL_ALL, pycurl.GLOBAL_NOTHING, pycurl.GLOBAL_DEFAULT.\n\nCorresponds to `curl_global_init`_ in libcurl.\n\n.. _curl_global_init: http://curl.haxx.se/libcurl/c/curl_global_init.html'
    pass

version = 'PycURL/7.43.0 libcurl/7.51.0 NSS/3.31 zlib/1.2.8 libidn2/2.0.4 libpsl/0.17.0 (+libidn2/0.11) libssh2/1.8.0 nghttp2/1.13.0'
def version_info():
    "version_info() -> tuple\n\nReturns a 12-tuple with the version info.\n\nCorresponds to `curl_version_info`_ in libcurl. Returns a tuple of\ninformation which is similar to the ``curl_version_info_data`` struct\nreturned by ``curl_version_info()`` in libcurl.\n\nExample usage::\n\n    >>> import pycurl\n    >>> pycurl.version_info()\n    (3, '7.33.0', 467200, 'amd64-portbld-freebsd9.1', 33436, 'OpenSSL/0.9.8x',\n    0, '1.2.7', ('dict', 'file', 'ftp', 'ftps', 'gopher', 'http', 'https',\n    'imap', 'imaps', 'pop3', 'pop3s', 'rtsp', 'smtp', 'smtps', 'telnet',\n    'tftp'), None, 0, None)\n\n.. _curl_version_info: http://curl.haxx.se/libcurl/c/curl_version_info.html"
    pass

