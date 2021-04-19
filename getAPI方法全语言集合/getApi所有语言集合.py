import json
import requests
#python
res=requests.get(url="http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f")
print(res.text)
"""
java语言

package exampleApi;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class ExampleApi {
	
	
	public static void doPostOrGet(String pathUrl,String data) {
		OutputStreamWriter out =null;
		
		BufferedReader br =null;
		
		String result ="";
		
		try {
			
			URL url =new URL(pathUrl);
			
			//打开和2url之间的连接
            HttpURLConnection conn =(HttpURLConnection) url.openConnection();
            
            //请求方式
            conn.setRequestMethod("GET");

            //设置通用的请求属性
            
            conn.setRequestProperty("accept", "*/*");
            conn.setRequestProperty("connection", "Keep-Alive");
            conn.setRequestProperty("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36");
            conn.setRequestProperty("Content-Type", "application/json;charset=utf-8");


            //DoOutput设置是否向httpUrlConnection输出，DoInput设置是否从httpUrlConnection读入，此外发送post请求必须设置这两个

               conn.setDoOutput(true);
               conn.setDoInput(true);
            /**
             * 下面的三句代码，就是调用第三方2http接口
             */
            //获取URLConnection对象对应的输出流
          
             out =new OutputStreamWriter(conn.getOutputStream(),"UTF-8");
            //发送请求参数即数据
            
             out.write(data);
            //flush输出流的缓冲
             out.flush();
   

            /**
             * 下面的代码相当于，获取调用第三方2http接口后返回的结果
             */
            //获取URLConnection对象对应的输入流
             InputStream is =conn.getInputStream();
             
            //构造一个字符流缓存
            // 2br =new BufferedReader(new InputStreamReader(is));
             
             BufferedReader r = new BufferedReader(new InputStreamReader(is,"UTF-8"));
             
             String str="";
             while((str=r.readLine())!=null) {
            	 result +=str;
             }
             System.out.println(result);
            //关闭流
            is.close();
            //断开连接，disconnect是在底层 2tcp socket链接空闲时才切断，如果正在被其他线程使用就不切断。
            conn.disconnect();
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try {
				
				if(out!=null) {
					out.close();
				}
				
				if(br!=null) {
					br.close();
				}
				
				
			}catch(IOException e) {
				e.printStackTrace();
			}
		}
		
		
	}
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
       System.out.println("2222");
       doPostOrGet("http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f", "");
	}

}
"""



""" go语言
package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"time"
)
func Get(url string) string {

// 超时时间：5秒
client := &http.Client{Timeout: 5 * time.Second}
resp, err := client.Get(url)
if err != nil {
panic(err)
}
defer resp.Body.Close()
var buffer [512]byte
result := bytes.NewBuffer(nil)
for {
n, err := resp.Body.Read(buffer[0:])
result.Write(buffer[0:n])
if err != nil && err == io.EOF {
break
} else if err != nil {
panic(err)
}
}
fmt.Println(result)
return result.String()
}

func main(){
	//fmt.Println("222")
	res :=Get("http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f");


	fmt.Println(res);
}



"""

"""
php语言


$f=file_get_contents("http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f");

//echo $f;
echo "<pre>";
var_dump($f);

$a=json_decode($f,true);  //成功转换json数据为数组 
print_r($a["result"]); //取得下一个数组
var_dump($a,true);

"""



"""
node



var request = require('request');
var querystring = require('querystring');

var queryData = querystring.stringify({
    "ip": "103.253.249.84",  // 查询的IP地址
    "key": "cd1f68b9c8503206985cc6fd1b6b083f",  // 申请的接口请求key
});

var queryUrl = 'http://apis.juhe.cn/ip/ipNew?'+queryData;

request(queryUrl, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        var jsonObj = JSON.parse(body); // 解析接口返回的JSON内容
        if (jsonObj) {
            var errorCode = jsonObj.error_code;
            var reason = jsonObj.reason;
            if (errorCode == 0) {
                // 请求成功
                var country = jsonObj.result.Country;
                var province = jsonObj.result.Province;
                var city = jsonObj.result.City;
                var isp = jsonObj.result.Isp;
                console.log("国家："+country+"\n省份："+province+"\n城市："+country+"\n运营商："+isp);
            } else {
                // 请求失败
                console.log('请求失败：'+errorCode+' '+reason);
            }
        } else{
            console.log('解析JSON异常');
        }
    } else {
        console.log('请求异常');
    }
})
"""

"""
javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js">
</script>
</head>
<body>

</body>
<script type="text/javascript">

<!--    var HttpClient = function() {-->
<!--    this.get = function(aUrl, aCallback) {-->
<!--        var anHttpRequest = new XMLHttpRequest();-->
<!--        anHttpRequest.onreadystatechange = function() {-->
<!--            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)-->
<!--                aCallback(anHttpRequest.responseText);-->
<!--        }-->

<!--        anHttpRequest.open( "GET", aUrl, true );-->
<!--        anHttpRequest.send( null );-->
<!--    }}-->

<!--    var client = new HttpClient();-->
<!--    client.get('http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f', function(response) {-->
<!--    // do something with response-->
<!--     console.log(response)-->
<!--    });-->

$(document).ready(function(){
    $.ajax({
        url: "http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f",
        type: "get",
        dataType: "jsonp", //指定服务器返回的数据类型
        success: function (data) {
            console.log(data);
        }
    });
});
</script>
</html>


"""



"""
c#

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace TestApi
{
    class Program
    {

       public static string HttpGet(string url)
        {
            //创建
            HttpWebRequest httpWebRequest = (HttpWebRequest)HttpWebRequest.Create(url);
            //设置请求方法
            httpWebRequest.Method = "GET";
            //请求超时时间
            httpWebRequest.Timeout = 20000;
            //发送请求
            HttpWebResponse httpWebResponse = (HttpWebResponse)httpWebRequest.GetResponse();
            //利用Stream流读取返回数据
            StreamReader streamReader = new StreamReader(httpWebResponse.GetResponseStream(), Encoding.UTF8);
            //获得最终数据，一般是json
            string responseContent = streamReader.ReadToEnd();
            streamReader.Close();
            httpWebResponse.Close();
            Console.WriteLine(responseContent);
            return responseContent;
        }
        static void Main(string[] args)
        {
            ///Console.WriteLine("222");
            //Console.ReadKey();
           HttpGet("http://apis.juhe.cn/ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f");
            Console.ReadKey();

        }
    }
}

"""


"""
 C++
 
 #include <string>
#include <windows.h>
#include <winhttp.h>
#include<iostream>
#pragma comment(lib, "winhttp.lib")

using namespace std;

int main()
{

	HINTERNET hSession = NULL;
	HINTERNET hConnect = NULL;
	HINTERNET hRequest = NULL;

	//1. 初始化一个WinHTTP-session句柄，参数1为此句柄的名称
	hSession = WinHttpOpen(L"WinHTTP Example/1.0",
		WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
		WINHTTP_NO_PROXY_NAME,
		WINHTTP_NO_PROXY_BYPASS, 0);

	if (hSession == NULL) {
		cout << "Error:Open session failed: " << GetLastError() << endl;
		exit(0);
	}

	//2. 通过上述句柄连接到服务器，需要指定服务器IP和端口号 INTERNET_DEFAULT_HTTP_PORT:80。若连接成功，返回的hConnect句柄不为NULL
	hConnect = WinHttpConnect(hSession, L"apis.juhe.cn", INTERNET_DEFAULT_HTTP_PORT, 0);
	if (hConnect == NULL) {
		cout << "Error:Connect failed: " << GetLastError() << endl;
		exit(0);
	}

	//3. 通过hConnect句柄创建一个hRequest句柄，用于发送数据与读取从服务器返回的数据。
	hRequest = WinHttpOpenRequest(hConnect, L"GET", L"ip/ipNew?ip=112.112.11.11&key=cd1f68b9c8503206985cc6fd1b6b083f", NULL, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, 0);
	//其中参数2表示请求方式，此处为Get；参数3:给定Get的具体地址，如这里的具体地址为https://www.citext.cn/GetTime.php
	if (hRequest == NULL) {
		cout << "Error:OpenRequest failed: " << GetLastError() << endl;
		exit(0);
	}

	BOOL bResults;
	bResults = WinHttpSendRequest(hRequest,
		WINHTTP_NO_ADDITIONAL_HEADERS,
		0, WINHTTP_NO_REQUEST_DATA, 0,
		0, 0);

	if (!bResults){
		cout << "Error:SendRequest failed: " << GetLastError() << endl;
		exit(0);
	}
	else{
		//（3） 发送请求成功则准备接受服务器的response。注意：在使用 WinHttpQueryDataAvailable和WinHttpReadData前必须使用WinHttpReceiveResponse才能access服务器返回的数据
		bResults = WinHttpReceiveResponse(hRequest, NULL);
	}


	LPVOID lpHeaderBuffer = NULL;
	DWORD dwSize = 0;
	//4-3. 获取服务器返回数据
	LPSTR pszOutBuffer = NULL;
	DWORD dwDownloaded = 0;         //实际收取的字符数
	wchar_t *pwText = NULL;
	if (bResults)
	{
		do
		{
			//(1) 获取返回数据的大小（以字节为单位）
			dwSize = 0;
			if (!WinHttpQueryDataAvailable(hRequest, &dwSize)){
				cout << "Error：WinHttpQueryDataAvailable failed：" << GetLastError() << endl;
				break;
			}
			if (!dwSize)    break;  //数据大小为0                

			//(2) 根据返回数据的长度为buffer申请内存空间
			pszOutBuffer = new char[dwSize + 1];
			if (!pszOutBuffer){
				cout << "Out of memory." << endl;
				break;
			}
			ZeroMemory(pszOutBuffer, dwSize + 1);       //将buffer置0

			//(3) 通过WinHttpReadData读取服务器的返回数据
			if (!WinHttpReadData(hRequest, pszOutBuffer, dwSize, &dwDownloaded)){
				cout << "Error：WinHttpQueryDataAvailable failed：" << GetLastError() << endl;
			}
			if (!dwDownloaded)
				break;

			
		} while (dwSize > 0);
		//4-4. 将返回数据转换成UTF8
		DWORD dwNum = MultiByteToWideChar(CP_ACP, 0, pszOutBuffer, -1, NULL, 0);    //返回原始ASCII码的字符数目       
		pwText = new wchar_t[dwNum];                                                //根据ASCII码的字符数分配UTF8的空间
		MultiByteToWideChar(CP_UTF8, 0, pszOutBuffer, -1, pwText, dwNum);           //将ASCII码转换成UTF8
		printf("\ncitext.cn返回时间: %S\n\n", pwText);


	}


	//5. 依次关闭request，connect，session句柄
	if (hRequest) WinHttpCloseHandle(hRequest);
	if (hConnect) WinHttpCloseHandle(hConnect);
	if (hSession) WinHttpCloseHandle(hSession);



	
	return 0;
} //成功 字符不够 要完整的自己去调字符
"""


"""
C
liunx版本 windows版本很多 实用性很少 继续研究以后上传
首先，安装编译环境apt-get install gcc libssl-dev

https版本客户端编译命令为gcc -o client client.c

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>

#define host   "www.baidu.com"
#define port    80

char sendbuff[1024*50];
char recvbuff[1024*50];

int main () {
    int fd = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
    struct sockaddr_in sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(port);
    /* 如果host是IP，直接使用下面方式
    sin.sin_addr.s_addr = inet_addr(host);
    */
    struct hostent *ip = gethostbyname(host); // 域名dns解析
    if(ip == NULL) {
        printf("gethostbyname error");
        return 0;
    }
    sin.sin_addr = *(struct in_addr*)ip->h_addr_list[0];
    if(connect(fd,(struct sockaddr*)&sin, sizeof(sin)) < 0) {
        printf("connect error");
        return 0;
    }
    strcpy(sendbuff,"GET /index.html HTTP/1.1\r\n"
                    "Host: "host"\r\n"
                    "User-Agent: www.worldflying.cn client\r\n"
                    "Accept: */*\r\n"
                    "Cache-Control: no-cache\r\n"
                    "Accept-Encoding: gzip, deflate, br\r\n"
                    "Connection: keep-alive\r\n\r\n");
    write(fd, sendbuff, strlen(sendbuff));
    while (1) {
        memset(recvbuff, 0, sizeof(recvbuff));
        if (read(fd,recvbuff,sizeof(recvbuff)-1) <= 0) {
            break;
        }
        printf("%s\n", recvbuff);
    }
    close(fd);
}
"""