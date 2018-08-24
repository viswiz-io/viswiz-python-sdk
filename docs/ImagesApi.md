# viswiz_sdk.ImagesApi

All URIs are relative to *https://api.viswiz.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](ImagesApi.md#create_image) | **POST** /builds/{buildID}/images | Create an image
[**get_images**](ImagesApi.md#get_images) | **GET** /builds/{buildID}/images | Get images for a build


# **create_image**
> Image create_image(build_id, name, image)

Create an image

Upload a new image for a build. This endpoint accepts only one PNG image per request.  This request requires a `Content-Type: multipart/form-data` HTTP header. 

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
api_instance = viswiz_sdk.ImagesApi(viswiz_sdk.ApiClient(configuration))
build_id = 'build_id_example' # str | The requested build ID
name = 'name_example' # str | The name of the image
image = '/path/to/file.txt' # file | The contents of the image

try:
    # Create an image
    api_response = api_instance.create_image(build_id, name, image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| The requested build ID | 
 **name** | **str**| The name of the image | 
 **image** | **file**| The contents of the image | 

### Return type

[**Image**](Image.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> Images get_images(build_id)

Get images for a build

Get a list of all images for a build. 

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
api_instance = viswiz_sdk.ImagesApi(viswiz_sdk.ApiClient(configuration))
build_id = 'build_id_example' # str | The requested build ID

try:
    # Get images for a build
    api_response = api_instance.get_images(build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| The requested build ID | 

### Return type

[**Images**](Images.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

