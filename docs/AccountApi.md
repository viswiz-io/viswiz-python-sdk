# viswiz_sdk.AccountApi

All URIs are relative to *https://api.viswiz.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](AccountApi.md#create_webhook) | **POST** /webhooks | Create a new webhook
[**get_account**](AccountApi.md#get_account) | **GET** /account | Get account info
[**get_webhooks**](AccountApi.md#get_webhooks) | **GET** /webhooks | Get all webhooks


# **create_webhook**
> WebHook create_webhook(body)

Create a new webhook

When a build comparison is finished a POST HTTP request will be triggered towards all webhooks configured for the account.  The following query parameters are sent with each request:  - `branch` - `buildID` - `comparisonBranch` - `comparisonBuildID` - `diffImagesCount` - `diffPercentage` - `imagesCount` - `projectID` 

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
api_instance = viswiz_sdk.AccountApi(viswiz_sdk.ApiClient(configuration))
body = viswiz_sdk.Body() # Body | 

try:
    # Create a new webhook
    api_response = api_instance.create_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account()

Get account info

Get the current account information 

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
api_instance = viswiz_sdk.AccountApi(viswiz_sdk.ApiClient(configuration))

try:
    # Get account info
    api_response = api_instance.get_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> InlineResponse2001 get_webhooks()

Get all webhooks

Get the list of webhooks configured for the account. 

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
api_instance = viswiz_sdk.AccountApi(viswiz_sdk.ApiClient(configuration))

try:
    # Get all webhooks
    api_response = api_instance.get_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

