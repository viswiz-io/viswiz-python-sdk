# viswiz_sdk.ProjectsApi

All URIs are relative to *https://api.viswiz.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a project
[**get_project_notifications**](ProjectsApi.md#get_project_notifications) | **GET** /projects/{projectID}/notifications | Get notifications settings
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get all projects
[**update_project_notifications**](ProjectsApi.md#update_project_notifications) | **PUT** /projects/{projectID}/notifications | Update notifications settings


# **create_project**
> Project create_project(body)

Create a project

Create a new project for the account. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = viswiz_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viswiz_sdk.ProjectsApi(viswiz_sdk.ApiClient(configuration))
body = viswiz_sdk.Body1() # Body1 | 

try:
    # Create a project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_notifications**
> Notifications get_project_notifications(project_id)

Get notifications settings

Get the notifications settings for a project. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = viswiz_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viswiz_sdk.ProjectsApi(viswiz_sdk.ApiClient(configuration))
project_id = 'project_id_example' # str | The requested project ID

try:
    # Get notifications settings
    api_response = api_instance.get_project_notifications(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The requested project ID | 

### Return type

[**Notifications**](Notifications.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> InlineResponse2002 get_projects()

Get all projects

Get a list of all the projects for the account. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = viswiz_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viswiz_sdk.ProjectsApi(viswiz_sdk.ApiClient(configuration))

try:
    # Get all projects
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_notifications**
> Notifications update_project_notifications(project_id, body)

Update notifications settings

Update the notifications settings for a project. All fields are optional. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = viswiz_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = viswiz_sdk.ProjectsApi(viswiz_sdk.ApiClient(configuration))
project_id = 'project_id_example' # str | The requested project ID
body = viswiz_sdk.Notifications() # Notifications | 

try:
    # Update notifications settings
    api_response = api_instance.update_project_notifications(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The requested project ID | 
 **body** | [**Notifications**](Notifications.md)|  | 

### Return type

[**Notifications**](Notifications.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

