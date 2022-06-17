# <div align="center">Request Processing Status</div>
- Nome: Request Processing Status
- API URL: https://8kad2d3fg6.execute-api.sa-east-1.amazonaws.com/default/full-stack-exam-get-processing-status
- Método: GET
- Autenticação: JWT token
- Descrição: Esta API recebe uma requisição HTTP via GET e, passando o batch id como query string, retorna o stauts do processamento do batch.

<br>

## <div align="center">Exemplos</div>

## Python

<details open>
<summary>Como usar</summary>

Você pode encontrar um exemplo de uso completo [aqui](./test_get_processing_status_api.py).

</details>

## curl

<details open>
<summary>Como chamar a API</summary>

```bash
export GET_UPLOAD_DETAILS_URL=https://8wvaarvrsc.execute-api.sa-east-1.amazonaws.com/default/fullstack_exam_get_presigned_url
export GET_UPLOAD_DETAILS_TOKEN= # add your token here
export BATCH_ID= # replace by your batch id
curl $GET_UPLOAD_DETAILS_URL?batch_id=$BATCH_ID -H "Authorization: Bearer $GET_UPLOAD_DETAILS_TOKEN"
```

</details>

<details open>
<summary>Retorno esperado</summary>

```bash
{
    "statusCode": 200,
    "progress": 100,
    "results": {
        "000000000049.jpg": [
            {
                "class": 17,
                "conf": 0.6347573399543762,
                "position": [
                    161,
                    238,
                    290,
                    410
                ]
            },
            {
                "class": 0,
                "conf": 0.6345021724700928,
                "position": [
                    119,
                    339,
                    131,
                    369
                ]
            },
            {
                "class": 17,
                "conf": 0.5651221871376038,
                "position": [
                    79,
                    261,
                    188,
                    404
                ]
            },
            {
                "class": 0,
                "conf": 0.5590903759002686,
                "position": [
                    282,
                    330,
                    294,
                    360
                ]
            }
        ],
        "000000000025.jpg": [
            {
                "class": 23,
                "conf": 0.7802602052688599,
                "position": [
                    362,
                    53,
                    588,
                    360
                ]
            },
            {
                "class": 23,
                "conf": 0.5228772759437561,
                "position": [
                    50,
                    350,
                    183,
                    417
                ]
            }
        ],
        "000000000030.jpg": [],
        "000000000042.jpg": [],
        "000000000009.jpg": [
            {
                "class": 45,
                "conf": 0.5025942325592041,
                "position": [
                    379,
                    8,
                    627,
                    245
                ]
            }
        ],
        "000000000034.jpg": [
            {
                "class": 22,
                "conf": 0.8807379603385925,
                "position": [
                    1,
                    18,
                    439,
                    389
                ]
            }
        ],
        "000000000072.jpg": [],
        "000000000064.jpg": [
            {
                "class": 74,
                "conf": 0.8976976871490479,
                "position": [
                    113,
                    40,
                    269,
                    200
                ]
            },
            {
                "class": 2,
                "conf": 0.5329798460006714,
                "position": [
                    49,
                    395,
                    195,
                    536
                ]
            }
        ],
        "000000000071.jpg": [],
        "000000000073.jpg": []
    },
    "processing_status": "completed",
    "created_at": "2022-06-16T20:05:21.662031",
    "updated_at": "2022-06-16T20:14:23.239377",
    "download_url": "https://daedalus-full-stack-exam-bucket.s3.amazonaws.com/dc4d0140-cb72-4d8a-bb19-2cb92b378b7b.zip?AWSAccessKeyId=ASIAQ3P7ZJ2NVSUDXCWN&Signature=luPb5F2xsDBbAJqVvE1k96YNiSY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXNhLWVhc3QtMSJIMEYCIQDM%2Fko0hSUm9m%2FRFMdIQW4tF3C3o5G7ci4iolluRo%2FUSQIhAJexfZimi3scnwwwtk4Ys7rEurngnUB6mmJRGnH0N%2BZRKrMCCMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMDU5MDU1MzYxNjkxIgzQJc4yqxTDFmmIoPkqhwIFKLA6GE%2BE%2B1VZCyrklgA%2FMlydudhb1KmbVVrqboz7tK5nefW7uow%2FisPGbGT9gAbuJVhAlpdfGodPjtUAYMRFkKSVFMFE%2BikUidxmliBVqeUBnknem%2FZnantSR858HgZTpMXsaINLGNzA5rY7KhstauZ4IDIGm5ZJ6j0gcDXYCeugU9poVrYb7QSyMbQDAAq8TNSnTcxhWcGxvIQxPBhEGss7E2ryaXN6HJPqRRaPm%2FnhjCXYRXoAzbT6UQhSDkNW6Kl5z%2BOYB9Z%2Fs793tOyhtIBp2s2I4VRjXdLt7DLslS4dPAiKAtjOOBh88CtfyNlVDgkg716I8nSwDwZs%2ByeigiOTZU4dOzDWvK6VBjqZAZJZAZzYMe0Ra8CLXbmg7WT%2BayyEmPHXP2DrmMahX%2B4nEcKPvQgBkwYwnecmUUMTBaAqu5H3iGxmKgYQAHM8hsRT3pIQpNJc3fuLsHKHU%2BrBjY8FJWhCxDHW9URuLtzkWnAqA13Kns3Blnz6ZbKcVGbETY4NAHpKzckOfw2MU5s2Lal2xGGLe32EFA2e4JvmKN4Upm88YnSjhw%3D%3D&Expires=1655414959"
}
```

</details>

## <div align="center">Descrição dos Resultados</div>

O resultado do request possui os seguintes campos:
- statusCode: status de resposta do request.
- progress: progresso em porcentagem do processamento.
- processing_status: status do processamento. Pode ser waiting, processing, completed ou failed.
- created_at: timestamp de quando o status do processamento foi criado.
- updated_at: timestamp da última vez em que o status do processamento foi atualizado.
- download_url: pode ser utilizada para baixar o .zip. A URL é válida por 10 minutos.
- results: um dicionário em contendo as informações para cada imagem no batch. As Keys dos dicionários são os nomes das imagens e os valores são listas contendo as detecções:
    - class: classe do objeto identificado. Você pode encontrar a relação entre classe e id [aqui](./classes.csv).
    - conf: confiança da detecção.
    - position: posição da detecção. As coordenadas são x0, y0, x1, y1. O ponto superior esquerdo da detecção é composto por (x0, y0) e, o ponto inferior direito, por (x1, y1). Você pode ver um exemplo na imagem a seguir:


![alt text](../.images/coords.png)
