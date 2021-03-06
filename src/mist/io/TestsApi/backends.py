import json
from MyRequestsClass import MyRequests

def list_backends(uri, cookie=None):
    req = MyRequests(uri=uri + '/backends', cookie=cookie)
    response = req.get()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    try:
        params = response.json()
        return params
    except Exception as e:
        assert False, u'Exception: %s' %e


def supported_providers(uri, cookie=None):
    req = MyRequests(uri=uri+'/providers', cookie=cookie)
    response = req.get()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    try:
        params = response.json()
    except Exception as e:
        assert False, u'Exception: %s' %e

    SUPPORTED_PROVIDERS = params['supported_providers']
    print '\nSupported providers:'
    return SUPPORTED_PROVIDERS


def add_backend(uri, title, provider, apikey, apisecret, apiurl=None, tenant_name=None, cookie=None):
    payload = {
        'title': title,
        'provider': provider,
        'apikey': apikey,
        'apisecret': apisecret,
        'apiurl': apiurl,
        'tenant_name': tenant_name
    }

    req = MyRequests(uri=uri+'/backends', data=json.dumps(payload), cookie=cookie)
    response = req.post()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    try:
        params = response.json()
        return params
    except Exception as e:
        assert False, u'Exception: %s' % e


def delete_backend(uri, backend_id, cookie=None):
    req = MyRequests(uri=uri+'/backends/'+backend_id, cookie=cookie)
    response = req.delete()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    print "Deleted Backend with id: %s" % backend_id


def list_images(uri, backend_id, search_term=None, cookie=None):
    payload = {
        'search_term': search_term
    }
    if not search_term:
        req = MyRequests(uri=uri+"/backends/"+backend_id+"/images", cookie=cookie)
        response = req.post()
    else:
        req = MyRequests(uri=uri+"/backends/"+backend_id+"/images", data=json.dumps(payload), cookie=cookie)
        response = req.get()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    try:
        params = response.json()
        return params
    except Exception as e:
        assert False, u'Exception: %s' % e


def list_sizes(uri, backend_id, cookie=None):
    req = MyRequests(uri=uri+"/backends/"+backend_id+"/sizes", cookie=cookie)
    response = req.get()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)

    try:
        params = response.json()
        return params
    except Exception as e:
        assert False, u'Exception: %s' % e


def list_locations(uri, backend_id, cookie=None):
    req = MyRequests(uri=uri+"/backends/"+backend_id+"/locations", cookie=cookie)
    response = req.get()
    assert response.ok, u'\nGot %d Response Status: %s \n%s' % (response.status_code, response.reason, response.text)
    try:
        params = response.json()
        return params
    except Exception as e:
        assert False, u'Exception: %s' % e
