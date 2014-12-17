from starflyer import Application, URL
from sfext.mongo import mongodb

import meetings
import meeting
import document
import documents

class API(Application):
    """a for now simple eschweiler output application"""

    defaults = {
        'mongodb_name'  : 'eschweiler',
    }

    routes = [
        URL("/<city>/meetings", "meetings", meetings.Meetings),  # list of the last x meetings by date
        URL("/<city>/meetings/<mid>", "meeting", meeting.Meeting),  # one meetings with all the details
        URL("/<city>/documents", "documents", documents.Documents),  # list of the last x documents by date
        URL("/<city>/documents/<did>", "document", document.Document),  # one document with all the details
    ]

    modules = [
        mongodb(mongodb_name = "eschweiler"),
    ]


def app(config, **local_config):
    """return the application"""
    app = API(__name__, local_config)
    if app.config.debug:
        from werkzeug import DebuggedApplication
        return DebuggedApplication(app)
    return app

