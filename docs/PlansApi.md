# viswiz_sdk.PlansApi

All URIs are relative to *https://api.viswiz.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_plan**](PlansApi.md#cancel_plan) | **DELETE** /account/cancel-plan | Cancel the active plan
[**get_plans**](PlansApi.md#get_plans) | **GET** /plans | Get all plans


# **cancel_plan**
> cancel_plan()

Cancel the active plan

Cancels the active subscription plan for the account. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = viswiz_sdk.PlansApi()

try:
    # Cancel the active plan
    api_instance.cancel_plan()
except ApiException as e:
    print("Exception when calling PlansApi->cancel_plan: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plans**
> InlineResponse200 get_plans()

Get all plans

Get a list of all the subscription plans available. 

### Example
```python
from __future__ import print_function
import time
import viswiz_sdk
from viswiz_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = viswiz_sdk.PlansApi()

try:
    # Get all plans
    api_response = api_instance.get_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

