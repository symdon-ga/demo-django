"""
THIS FILE COPIED https://github.com/django/django/blob/master/django/views/static.py AND MODIFIED.

See `********** MODIFIED **************`
"""
from __future__ import unicode_literals

import mimetypes
import os
import posixpath
import stat

from django.http import (
    FileResponse, Http404, HttpResponseNotModified,
    HttpResponseRedirect,
)
from django.utils.six.moves.urllib.parse import unquote
from django.utils.http import http_date
from django.utils.translation import ugettext as _
from django.views.static import (
    directory_index,
    was_modified_since,
    )


def serve(request, path, document_root=None, show_indexes=False,
              directory_index_allows=[]):
    path = posixpath.normpath(unquote(path))
    path = path.lstrip('/')
    newpath = ''
    for part in path.split('/'):
        if not part:
            # Strip empty path components.
            continue
        drive, part = os.path.splitdrive(part)
        head, part = os.path.split(part)
        if part in (os.curdir, os.pardir):
            # Strip '.' and '..' in path.
            continue
        newpath = os.path.join(newpath, part).replace('\\', '/')
    if newpath and path != newpath:
        return HttpResponseRedirect(newpath)
    fullpath = os.path.join(document_root, newpath)

    # ********** MODIFIED **************
    if directory_index_allows:
        if os.path.isdir(fullpath):
            for index_filename in directory_index_allows:
                index_filepath = os.path.join(fullpath, index_filename)
                if os.path.isfile(index_filepath):
                    fullpath = index_filepath
                    break
    # **********************************

    if os.path.isdir(fullpath):
        if show_indexes:
            return directory_index(newpath, fullpath)
        raise Http404(_("Directory indexes are not allowed here."))
    if not os.path.exists(fullpath):
        raise Http404(_('"%(path)s" does not exist') % {'path': fullpath})
    # Respect the If-Modified-Since header.
    statobj = os.stat(fullpath)
    if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                              statobj.st_mtime, statobj.st_size):
        return HttpResponseNotModified()
    content_type, encoding = mimetypes.guess_type(fullpath)
    content_type = content_type or 'application/octet-stream'
    response = FileResponse(open(fullpath, 'rb'), content_type=content_type)
    response["Last-Modified"] = http_date(statobj.st_mtime)
    if stat.S_ISREG(statobj.st_mode):
        response["Content-Length"] = statobj.st_size
    if encoding:
        response["Content-Encoding"] = encoding
    return response
