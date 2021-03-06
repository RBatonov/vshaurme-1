from flask import url_for
from flask_babel import lazy_gettext as _l

from vshaurme.extensions import db
from vshaurme.models import Notification


def push_follow_notification(follower, receiver):
    message = _l('User <a href=\"%s\">%s</a> followed you.') % \
              (url_for('user.index', username=follower.username), follower.username)
    notification = Notification(message=message, receiver=receiver)
    add_notification(notification)


def push_comment_notification(photo_id, receiver, page=1):
    message = _l('<a href=\"%s#comments\">This photo</a> has new comment/reply.') % \
              (url_for('main.show_photo', photo_id=photo_id, page=page))
    notification = Notification(message=message, receiver=receiver)
    add_notification(notification)


def push_collect_notification(collector, photo_id, receiver):
    message = _l('User <a href=\"%s\">%s</a> collected your <a href=\"%s\">photo</a>') % \
              (url_for('user.index', username=collector.username),
               collector.username,
               url_for('main.show_photo', photo_id=photo_id))
    notification = Notification(message=message, receiver=receiver)
    add_notification(notification)


def add_notification(notification):
    if notification:
        db.session.add(notification)
        db.session.commit()
        db.session.close()
