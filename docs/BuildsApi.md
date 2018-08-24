# viswiz_sdk.BuildsApi

All URIs are relative to *https://api.viswiz.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_build**](BuildsApi.md#create_build) | **POST** /projects/{projectID}/builds | Create a build
[**finish_build**](BuildsApi.md#finish_build) | **POST** /builds/{buildID}/finish | Finish a build
[**get_build_results**](BuildsApi.md#get_build_results) | **GET** /builds/{buildID}/results | Get results for a build
[**get_builds**](BuildsApi.md#get_builds) | **GET** /projects/{projectID}/builds | Get builds for a project


# **create_build**
> Build create_build(project_id, body)

Create a build

Create a new build for a project. 

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
api_instance = viswiz_sdk.BuildsApi(viswiz_sdk.ApiClient(configuration))
project_id = 'project_id_example' # str | The requested project ID
body = viswiz_sdk.Body2() # Body2 | 

try:
    # Create a build
    api_response = api_instance.create_build(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->create_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The requested project ID | 
 **body** | [**Body2**](Body2.md)|  | 

### Return type

[**Build**](Build.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_build**
> finish_build(build_id)

Finish a build

Finish a build when all images have been created. This triggers the actual build comparison to execute. 

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
api_instance = viswiz_sdk.BuildsApi(viswiz_sdk.ApiClient(configuration))
build_id = 'build_id_example' # str | The requested build ID

try:
    # Finish a build
    api_instance.finish_build(build_id)
except ApiException as e:
    print("Exception when calling BuildsApi->finish_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| The requested build ID | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_results**
> BuildResults get_build_results(build_id)

Get results for a build

Get the results for a build which has been compared to another build. 

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
api_instance = viswiz_sdk.BuildsApi(viswiz_sdk.ApiClient(configuration))
build_id = 'build_id_example' # str | The requested build ID

try:
    # Get results for a build
    api_response = api_instance.get_build_results(build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| The requested build ID | 

### Return type

[**BuildResults**](BuildResults.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> Builds get_builds(project_id)

Get builds for a project

Get a list of all the builds for a project. 

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
api_instance = viswiz_sdk.BuildsApi(viswiz_sdk.ApiClient(configuration))
project_id = 'project_id_example' # str | The requested project ID

try:
    # Get builds for a project
    api_response = api_instance.get_builds(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The requested project ID | 

### Return type

[**Builds**](Builds.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

