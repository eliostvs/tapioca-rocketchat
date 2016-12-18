from __future__ import unicode_literals

import pytest
import requests_mock

from tapioca_rocketchat import RocketChat

AUTH_RESOURCE = 'http://localhost.com/api/v1/login'
AUTH_RESPONSE = {'status': 'success', 'data': {'authToken': 'authToken', 'userId': 'userId'}}
AUTH_HEADERS = {'X-Auth-Token': 'authToken', 'X-User-Id': 'userId'}


@pytest.fixture
def client():
    return RocketChat(host='http://localhost.com', username='user', password='password')


@pytest.fixture
def client_token():
    return RocketChat(host='http://localhost.com', token='authToken', user_id='userId')


def test_should_hit_the_info_resource(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/info', request_headers=AUTH_HEADERS)

        response = client.info().get()

        assert response._response.status_code == 200


def test_should_login(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        response = client.login().post(data={'user': 'user', 'password': 'password'})

        assert response._response.status_code == 200


def test_should_logout(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/logout')

        response = client.logout().get()

        assert response._response.status_code == 200


def test_should_get_logged_user_info(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/me')

        response = client.me().get()

        assert response._response.status_code == 200


def test_should_get_setting(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/settings/Livechat_enabled')

        response = client.settings(id='Livechat_enabled').get()

        assert response._response.status_code == 200


def test_should_set_setting(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/settings/Livechat_enabled')

        response = client.settings(id='Livechat_enabled').post(data={'value': True})

        assert response._response.status_code == 200


def test_should_send_a_message(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/chat.postMessage', status_code=201)

        response = client.send_message().post(data={'channel': '#general', 'text': 'Sample message'})

        assert response._response.status_code == 201


def test_should_delete_a_message(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/chat.deleteMessage')

        response = client.delete_message().post(data={'roomId': '#general', 'msgId': 'Sample message'})

        assert response._response.status_code == 200


def test_should_create_an_user(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/users.create')

        response = client.user_create().post(data={'name': 'name', 'email': 'user@email.com', 'password': 'password'})

        assert response._response.status_code == 200


def test_should_delete_an_user(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/users.delete')

        response = client.user_delete().post(data={'userId': 'id'})

        assert response._response.status_code == 200


def test_should_get_user_presence(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/users.getPresence?userId=id')

        response = client.user_presence().get(params={'userId': 'id'})

        assert response._response.status_code == 200


def test_should_get_user_info(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/users.info?userId=id')

        response = client.user_info().get(params={'userId': 'id'})

        assert response._response.status_code == 200


def test_should_get_user_list(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/users.list')

        response = client.user_list().get()

        assert response._response.status_code == 200


def test_should_set_user_avatar(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/users.setAvatar')

        response = client.user_avatar().post(data={'avatarUrl': 'http://domain.tld/to/my/own/avatar.jpg'})

        assert response._response.status_code == 200


def test_should_update_user_data(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/users.update')

        response = client.user_update().post(data={'userId': 'id', 'data': {'name': 'new name'}})

        assert response._response.status_code == 200


def test_should_add_all_users_to_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.addAll')

        response = client.channel_add().post(data={'roomId': 'id'})

        assert response._response.status_code == 200


def test_should_archives_a_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.archive')

        response = client.channel_archive().post(data={'roomId': 'id'})

        assert response._response.status_code == 200


def test_should_remove_messages_from_the_provided_time_range(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.cleanHistory')

        data = {'roomId': 'channelId', 'latest': '2016-12-09T13:42:25.304Z', 'oldest': '2016-08-30T13:42:25.304Z'}
        response = client.channel_clear().post(data=data)

        assert response._response.status_code == 200


def test_should_remove_channel_from_user_list_of_channels(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.close')

        response = client.channel_close().post(data={'roomId': 'channelId'})

        assert response._response.status_code == 200


def test_should_retrieve_messages_from_a_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/channels.history?roomId=roomId')

        response = client.channel_history().get(params={'roomId': 'roomId'})

        assert response._response.status_code == 200


def test_should_add_a_user_to_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.invite')

        response = client.channel_invite().post(data={'roomId': 'roomId', 'userId': 'userId'})

        assert response._response.status_code == 200


def test_should_remove_a_user_from_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.kick')

        response = client.channel_kick().post(data={'roomId': 'roomId', 'userId': 'userId'})

        assert response._response.status_code == 200


def test_should_logged_user_leave_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.leave')

        response = client.channel_leave().post(data={'roomId': 'roomId'})

        assert response._response.status_code == 200


def test_should_list_all_channels(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/channels.list')

        response = client.channel_list().get()

        assert response._response.status_code == 200


def test_should_list_all_channels_that_the_logged_user_has_joined(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.get('http://localhost.com/api/v1/channels.list.joined')

        response = client.channel_joined().get()

        assert response._response.status_code == 200


def test_should_add_channel_back_to_the_user_list_of_channels(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.open')

        response = client.channel_open().post(data={'roomId': 'roomId'})

        assert response._response.status_code == 200


def test_should_change_the_name_of_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.rename')

        response = client.channel_rename().post(data={'roomId': 'roomId', 'name': 'new name'})

        assert response._response.status_code == 200


def test_should_set_the_description_of_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.setDescription')

        response = client.channel_description().post(data={'roomId': 'roomId', 'description': 'description'})

        assert response._response.status_code == 200


def test_should_set_purpose_of_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.setPurpose')

        response = client.channel_purpose().post(data={'roomId': 'roomId', 'purpose': 'purpose'})

        assert response._response.status_code == 200


def test_should_set_topic_for_the_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.setTopic')

        response = client.channel_topic().post(data={'roomId': 'roomId', 'topic': 'topic'})

        assert response._response.status_code == 200


def test_should_unarchive_a_channel(client):
    with requests_mock.Mocker() as m:
        m.post(AUTH_RESOURCE, json=AUTH_RESPONSE)

        m.post('http://localhost.com/api/v1/channels.unarchive')

        response = client.channel_unarchive().post(data={'roomId': 'roomId'})

        assert response._response.status_code == 200
