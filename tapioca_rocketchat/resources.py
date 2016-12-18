from __future__ import unicode_literals

RESOURCE_MAPPING = {
    'info': {
        'resource': '/info',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/info',
        'methods': ['GET']
    },

    'login': {
        'resource': '/login',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/authentication/login',
        'methods': ['POST']
    },

    'logout': {
        'resource': '/logout',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/authentication/logout',
        'methods': ['GET']
    },

    'me': {
        'resource': '/me',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/authentication/me',
        'methods': ['GET']
    },

    'settings': {
        'resource': '/settings/{id}',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/settings',
        'methods': ['GET', 'POST']
    },

    'send_message': {
        'resource': '/chat.postMessage',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/chat/postmessage',
        'methods': ['POST']
    },

    'delete_message': {
        'resource': '/chat.deleteMessage',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/chat/delete',
        'methods': ['POST']
    },

    'user_create': {
        'resource': '/users.create',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/create',
        'methods': ['POST']
    },

    'user_delete': {
        'resource': '/users.delete',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/delete',
        'methods': ['POST']
    },

    'user_presence': {
        'resource': '/users.getPresence',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/getpresence',
        'methods': ['GET']
    },

    'user_info': {
        'resource': '/users.info',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/info',
        'methods': ['GET']
    },

    'user_list': {
        'resource': '/users.list',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/list',
        'methods': ['GET']
    },

    'user_avatar': {
        'resource': '/users.setAvatar',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/setavatar',
        'methods': ['POST']
    },

    'user_update': {
        'resource': '/users.update',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/users/update',
        'methods': ['POST']
    },

    'channel_add': {
        'resource': '/channels.addAll',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/addall',
        'methods': ['POST']
    },

    'channel_archive': {
        'resource': '/channels.archive',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/archive',
        'methods': ['POST']
    },

    'channel_clear': {
        'resource': '/channels.cleanHistory',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/cleanhistory',
        'methods': ['POST']
    },

    'channel_close': {
        'resource': '/channels.close',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/close',
        'methods': ['POST']
    },

    'channel_history': {
        'resource': '/channels.history',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/history',
        'methods': ['GET']
    },

    'channel_invite': {
        'resource': '/channels.invite',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/invite',
        'methods': ['POST']
    },

    'channel_kick': {
        'resource': '/channels.kick',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/kick',
        'methods': ['POST']
    },

    'channel_leave': {
        'resource': '/channels.leave',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/leave',
        'methods': ['POST']
    },

    'channel_list': {
        'resource': '/channels.list',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/list',
        'methods': ['GET']
    },

    'channel_joined': {
        'resource': '/channels.list.joined',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/list-joined',
        'methods': ['GET']
    },

    'channel_open': {
        'resource': '/channels.open',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/open',
        'methods': ['POST']
    },

    'channel_rename': {
        'resource': '/channels.rename',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/rename',
        'methods': ['POST']
    },

    'channel_description': {
        'resource': '/channels.setDescription',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/setdescription',
        'methods': ['POST']
    },

    'channel_purpose': {
        'resource': '/channels.setPurpose',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/setpurpose',
        'methods': ['POST']
    },

    'channel_topic': {
        'resource': '/channels.setTopic',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/settopic',
        'methods': ['POST']
    },

    'channel_unarchive': {
        'resource': '/channels.unarchive',
        'docs': 'https://rocket.chat/docs/developer-guides/rest-api/channels/unarchive',
        'methods': ['POST']
    },
}
