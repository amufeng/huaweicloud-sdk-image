/**
 * 低光照增强服务token 方式请求的使用示例
 */
var enhance = require("./image_sdk/dark_enhance");
var token = require("./image_sdk/gettoken");
var utils = require("./image_sdk/utils");

// 初始化服务的区域信息，目前支持华北-北京(cn-north-4)、亚太-香港(ap-southeast-1)等区域信息
utils.initRegion("cn-north-4");

var username = "*******";        // 配置用户名
var domain_name = "*******";     // 配置用户名
var password = "*******";        // 密码

var filepath = "./data/dark-enhance-demo.bmp";
var data = utils.changeFileToBase64(filepath);

token.getToken(username, domain_name, password, function (token) {
    enhance.dark_enhance(token, data, 0.9, function (result) {
        var resultObj = JSON.parse(result);
        utils.getFileByBase64Str("./data/dark-enhance-demo-token.bmp", resultObj.result);

    })
});
