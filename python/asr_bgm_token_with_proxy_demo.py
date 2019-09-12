# -*- coding:utf-8 -*-
from image_sdk.gettoken import get_token
from image_sdk.asr_bgm import asr_bgm
from image_sdk.utils import init_global_env

import os

if __name__ == '__main__':
    # setup http proxy environment
    os.environ['http_proxy'] = 'http://username:password@proxyExample.huawei.com:8080'
    os.environ['https_proxy'] = 'http://username:password@proxyExample.huawei.com:8080'

    # Services currently support North China-Beijing(cn-north-4), Asia Pacific-Hong Kong(ap-southeast-1)
    init_global_env('cn-north-4')

    #
    # access asr, asr_bgm,post data by token
    #
    user_name = '*******'
    password = '*******'
    account_name = '*******'  # the same as user_name in commonly use

    # The OBS link should match the region, and the OBS resources of different regions are not shared
    demo_data_url = 'https://obs-test-llg.obs.cn-north-1.myhuaweicloud.com/bgm_recognition'
    token = get_token(user_name, password, account_name)

    # call interface use the url
    result = asr_bgm(token, demo_data_url)
    print(result)
