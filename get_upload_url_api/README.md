# <div align="center">Request bucket URL</div>
- Nome: Request bucket URL
- Método: GET
- Autenticação: JWT token
- Descrição: Esta API recebe uma requisição HTTP via GET e retorna uma URL com dados de acesso a um bucket privado para fazer upload de um arquivo comprimido com imagens. Além disso, também é retornado o ID da requisição, que deverá ser usado posteriormente para consulta de status de processamento. A URL será válida para upload por 10 minutos.

<br>

## <div align="center">Exemplos</div>

## Python

<details open>
<summary>Como usar</summary>

Você pode encontrar um exemplo de uso completo [aqui](./test_get_url_api.py).

</details>

## curl

<details open>
<summary>Como chamar a API</summary>

```bash
export GET_UPLOAD_DETAILS_URL=https://8wvaarvrsc.execute-api.sa-east-1.amazonaws.com/default/fullstack_exam_get_presigned_url
export GET_UPLOAD_DETAILS_TOKEN= # add your token here
curl $GET_UPLOAD_DETAILS_URL -H "Authorization: Bearer $GET_UPLOAD_DETAILS_TOKEN"
```

</details>

<details open>
<summary>Retorno esperado</summary>

```bash
{
    "statusCode": 200,
    "batch_id": "f3d5c078-3860-4759-a872-9ef79e0e0427",
    "upload_details": {
        "url": "https://daedalus-full-stack-exam-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "f3d5c078-3860-4759-a872-9ef79e0e0427.zip",
            "AWSAccessKeyId": "ASIAQ3P7ZJ2NQAC7HW7Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjELz//////////wEaCXNhLWVhc3QtMSJHMEUCIQCP2wTiMGeJZpFUVBZ02UqhcNO1zXxm1ufole2Q+Y5vHwIgQpScZZGn/ECPHBNdqTvg+hM0AUpOCWmKteZcQpiaZdAqrgIIxf//////////ARABGgwwNTkwNTUzNjE2OTEiDBANJysy/GWRWoRgeiqCAu4qi3IH85tZJUuRwCm3Yi79AwHkNVRN+bHZeO9gP9NcjpauNCKNjCZEkutes14o6qRM2Ea1JLNTR6YR7zEbYdEL+w4d0NcojV79fHICrRgnPIQ5b95kVv0W3QiZPh3THdIRRDwON/hw4BSOjlJpm0D2ClA0nFo+IpM/1rkWyc2AmtwdB6WSJdKhoa37/XWTkVy5M5ZMudjxeJk64C95izN35/FscZm5PPCvRgfKKXFavQ1riNlzaEuCn5IvXqfFfuA6X79TkwgdioxUpwMjrTawEK/Rg3s78edmUA8URLiSmFKpLl0vFZn+CBJlwkbDU4X/FqanmJBrodZssnU9iJiPMjDSkq6VBjqaAeZminH3l3ZKDLXrRATtwIUudQkApfipxpbEF57INnCZAMrPhSrkwsV/mhVp4QNlgConkMvgw1uxZPEBQB+NPXmTlKxuG/QP0jP5qNKmpCyEhiq6do314dna7V41lcBbciLYAhuXdF8GNvAfkULqVvYzKhr5r7HPvl1xuxPg6CkRymAH7UhEZ+B1SF6RLj08IAyEETvBmCkHkUU=",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjItMDYtMTZUMTk6NTk6MzhaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiZGFlZGFsdXMtZnVsbC1zdGFjay1leGFtLWJ1Y2tldCJ9LCB7ImtleSI6ICJmM2Q1YzA3OC0zODYwLTQ3NTktYTg3Mi05ZWY3OWUwZTA0MjcuemlwIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVMei8vLy8vLy8vLy93RWFDWE5oTFdWaGMzUXRNU0pITUVVQ0lRQ1Ayd1RpTUdlSlpwRlVWQlowMlVxaGNOTzF6WHhtMXVmb2xlMlErWTV2SHdJZ1FwU2NaWkduL0VDUEhCTmRxVHZnK2hNMEFVcE9DV21LdGVaY1FwaWFaZEFxcmdJSXhmLy8vLy8vLy8vL0FSQUJHZ3d3TlRrd05UVXpOakUyT1RFaURCQU5KeXN5L0dXUldvUmdlaXFDQXU0cWkzSUg4NXRaSlV1UndDbTNZaTc5QXdIa05WUk4rYkhaZU85Z1A5TmNqcGF1TkNLTmpDWkVrdXRlczE0bzZxUk0yRWExSkxOVFI2WVI3ekViWWRFTCt3NGQwTmNvalY3OWZISUNyUmduUElRNWI5NWtWdjBXM1FpWlBoM1RIZElSUkR3T04vaHc0QlNPamxKcG0wRDJDbEEwbkZvK0lwTS8xcmtXeWMyQW10d2RCNldTSmRLaG9hMzcvWFdUa1Z5NU01Wk11ZGp4ZUprNjRDOTVpek4zNS9Gc2NabTVQUEN2UmdmS0tYRmF2UTFyaU5semFFdUNuNUl2WHFmRmZ1QTZYNzlUa3dnZGlveFVwd01qclRhd0VLL1JnM3M3OGVkbVVBOFVSTGlTbUZLcExsMHZGWm4rQ0JKbHdrYkRVNFgvRnFhbm1KQnJvZFpzc25VOWlKaVBNakRTa3E2VkJqcWFBZVptaW5IM2wzWktETFhyUkFUdHdJVXVkUWtBcGZpcHhwYkVGNTdJTm5DWkFNclBoU3Jrd3NWL21oVnA0UU5sZ0NvbmtNdmd3MXV4WlBFQlFCK05QWG1UbEt4dUcvUVAwalA1cU5LbXBDeUVoaXE2ZG8zMTRkbmE3VjQxbGNCYmNpTFlBaHVYZEY4R052QWZrVUxxVnZZektocjVyN0hQdmwxeHV4UGc2Q2tSeW1BSDdVaEVaK0IxU0Y2UkxqMDhJQXlFRVR2Qm1Da0hrVVU9In1dfQ==",
            "signature": "YrIRpfNY8abJ0RgtdZfVaWcCjvE="
        }
    }
}
```

</details>

<details open>
<summary>Upload do arquivo</summary>

```bash
export ZIP_PATH=images.zip
curl -v --request POST -H "Content-Type: multipart/form-data" \
     -F key=dc4d0140-cb72-4d8a-bb19-2cb92b378b7b.zip \
     -F AWSAccessKeyId=ASIAQ3P7ZJ2N5D2EYNPU \
     -F x-amz-security-token=IQoJb3JpZ2luX2VjELz//////////wEaCXNhLWVhc3QtMSJIMEYCIQDvA7KLKikS0wnCY//2lSXbqEnkq1LA9y3bpjDHuHrijAIhAPpY5UNAXtEGFdIegyUINTuJ5i6T3b09aoE4leD+7N5DKq4CCMX//////////wEQARoMMDU5MDU1MzYxNjkxIgy2EpE9waR71Wsxq8gqggJWS3nkNyA+Ul+N4h9mCtt3NLMYZPsAsUnssBH9QU1djYYMBhKTGt0gANtt5XuideEp3bi/WshE1wLGxO61jgM7Fc1Rb4qydRs1at9+b4xF0cjZxPhQiBfda1BSR5KlALzEywbho1hKj3DGzDOHAUx18wwRHaRGKVxVzeayYlQ7+E2P0Wk3+HflvNdnLXzZA2XZD+3DS7/HP6WF5f+y4+PKAOik7pDtRg5H5iQzcGS2wU2gi6Yq76YyqQyZ4roeKyIjJK6nsND5hMUVImBo2KHBXsyOJ5DBEtS17ASNKEHrLsmHbimUK0qOormQ9h+LGjjOFZyZ0hRk95Lr8I5ZcGL2NCswgZqulQY6mQHkYQ3wNmEga+Qh1OTLcIy32zCLf8s9zSsw6hiFI0lon31ObZqCwV+uT5uxrSHFcYSgALDi5/2oeRKywLItmA2MJNIbHSQaj/WekArgoGoTXcoYc4O6rJN6zFqlTeZsH2AldYTpBsU64tJ6X6as0GZVrNhnZXsyYJtdy69A1uWfHZWUCdDfnb+kNJj1D11UTektFB4bvB2L32s= \
     -F policy=eyJleHBpcmF0aW9uIjogIjIwMjItMDYtMTZUMjA6MTU6MjFaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiZGFlZGFsdXMtZnVsbC1zdGFjay1leGFtLWJ1Y2tldCJ9LCB7ImtleSI6ICJkYzRkMDE0MC1jYjcyLTRkOGEtYmIxOS0yY2I5MmIzNzhiN2IuemlwIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVMei8vLy8vLy8vLy93RWFDWE5oTFdWaGMzUXRNU0pJTUVZQ0lRRHZBN0tMS2lrUzB3bkNZLy8ybFNYYnFFbmtxMUxBOXkzYnBqREh1SHJpakFJaEFQcFk1VU5BWHRFR0ZkSWVneVVJTlR1SjVpNlQzYjA5YW9FNGxlRCs3TjVES3E0Q0NNWC8vLy8vLy8vLy93RVFBUm9NTURVNU1EVTFNell4TmpreElneTJFcEU5d2FSNzFXc3hxOGdxZ2dKV1MzbmtOeUErVWwrTjRoOW1DdHQzTkxNWVpQc0FzVW5zc0JIOVFVMWRqWVlNQmhLVEd0MGdBTnR0NVh1aWRlRXAzYmkvV3NoRTF3TEd4TzYxamdNN0ZjMVJiNHF5ZFJzMWF0OStiNHhGMGNqWnhQaFFpQmZkYTFCU1I1S2xBTHpFeXdiaG8xaEtqM0RHekRPSEFVeDE4d3dSSGFSR0tWeFZ6ZWF5WWxRNytFMlAwV2szK0hmbHZOZG5MWHpaQTJYWkQrM0RTNy9IUDZXRjVmK3k0K1BLQU9pazdwRHRSZzVINWlRemNHUzJ3VTJnaTZZcTc2WXlxUXlaNHJvZUt5SWpKSzZuc05ENWhNVVZJbUJvMktIQlhzeU9KNURCRXRTMTdBU05LRUhyTHNtSGJpbVVLMHFPb3JtUTloK0xHampPRlp5WjBoUms5NUxyOEk1WmNHTDJOQ3N3Z1pxdWxRWTZtUUhrWVEzd05tRWdhK1FoMU9UTGNJeTMyekNMZjhzOXpTc3c2aGlGSTBsb24zMU9iWnFDd1YrdVQ1dXhyU0hGY1lTZ0FMRGk1LzJvZVJLeXdMSXRtQTJNSk5JYkhTUWFqL1dla0FyZ29Hb1RYY29ZYzRPNnJKTjZ6RnFsVGVac0gyQWxkWVRwQnNVNjR0SjZYNmFzMEdaVnJOaG5aWHN5WUp0ZHk2OUExdVdmSFpXVUNkRGZuYitrTkpqMUQxMVVUZWt0RkI0YnZCMkwzMnM9In1dfQ== \
     -F signature=ngcx37c79ZKfEEN0smBZnrYI1lM= \
     -F file=@$ZIP_PATH https://daedalus-full-stack-exam-bucket.s3.amazonaws.com/
```

</details>

<details open>
<summary>Retorno esperado</summary>

```bash
*   Trying 52.95.165.113:443...
* Connected to daedalus-full-stack-exam-bucket.s3.amazonaws.com (52.95.165.113) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*  CAfile: /home/user/anaconda3/ssl/cacert.pem
*  CApath: none
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: CN=*.s3.amazonaws.com
*  start date: Dec 15 00:00:00 2021 GMT
*  expire date: Dec  3 23:59:59 2022 GMT
*  subjectAltName: host "daedalus-full-stack-exam-bucket.s3.amazonaws.com" matched cert's "*.s3.amazonaws.com"
*  issuer: C=US; O=Amazon; OU=Server CA 1B; CN=Amazon
*  SSL certificate verify ok.
> POST / HTTP/1.1
> Host: daedalus-full-stack-exam-bucket.s3.amazonaws.com
> User-Agent: curl/7.78.0
> Accept: */*
> Content-Length: 2940537
> Content-Type: multipart/form-data; boundary=------------------------73f2fe7008c11ab9
> Expect: 100-continue
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 100 Continue
* We are completely uploaded and fine
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< x-amz-id-2: 2gsTwncTgwSkNh1QTJzpzaS+JPgeFGr7Jva94NOcg+DXFCVA7BVF0LvFQ3oSXt6iTv4yyolxQfs=
< x-amz-request-id: Y59VXQHTEZ07YHWJ
< Date: Thu, 16 Jun 2022 20:23:00 GMT
< ETag: "873bad0ccbfabcccf8ef029cdaac6f44"
< Location: https://daedalus-full-stack-exam-bucket.s3.amazonaws.com/b40a447e-aac5-4624-8833-65648838e1d0.zip
< Server: AmazonS3
< 
* Connection #0 to host daedalus-full-stack-exam-bucket.s3.amazonaws.com left intact
```

</details>