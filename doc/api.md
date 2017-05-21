GET http://115.28.89.174:8000/api/server_info/
{
  "message": "succeed",
  "code": 0,
  "data": [
    {
      "uuid": "12b2ff72-9b78-4378-8e6b-9760b17d09eb",
      "manufactory": "DELL",
      "model": "R730",
      "cpu": 16,
      "mem": 512,
      "disk_type": 0,
      "disk_capacity": 1024,
      "nic": "千兆",
      "idc": "北京兆维",
      "apply_date": "2017-05-01",
      "expire_date": "2017-06-01"
    },
    {
      "uuid": "b876d8f9-85fd-42e7-8fbf-00ba789116b7",
      "manufactory": "HP",
      "model": "DL580",
      "cpu": 32,
      "mem": 262144,
      "disk_type": 1,
      "disk_capacity": 1024,
      "nic": "万兆",
      "idc": "北京土城",
      "apply_date": "2017-05-01",
      "expire_date": "2017-06-01"
    }
  ]
}


GET http://115.28.89.174:8000/api/server_info/12b2ff72-9b78-4378-8e6b-9760b17d09eb
{
  "message": "succeed",
  "code": 0,
  "data": {
    "uuid": "12b2ff72-9b78-4378-8e6b-9760b17d09eb",
    "manufactory": "DELL",
    "model": "R730",
    "cpu": 16,
    "mem": 512,
    "disk_type": 0,
    "disk_capacity": 1024,
    "nic": "千兆",
    "idc": "北京兆维",
    "apply_date": "2017-05-01",
    "expire_date": "2017-06-01"
  }
}


PUT http://115.28.89.174:8000/api/server_info/394631c1-4e87-4bfc-a87d-6745516d76c7
{
    "uuid": "394631c1-4e87-4bfc-a87d-6745516d76c7",
    "manufactory": "IBM",
    "model": "HS22",
    "cpu": 16,
    "mem": 512,
    "disk_type": 0,
    "disk_capacity": 1024,
    "nic": "千兆",
    "idc": "北京兆维",
    "apply_date": "2017-05-01",
    "expire_date": "2017-06-01"
}
{
  "message": "succeed",
  "code": 0
}

POST http://115.28.89.174:8000/api/server_info/394631c1-4e87-4bfc-a87d-6745516d76c7
{
    "manufactory": "Cisco"
}
{
  "message": "succeed",
  "code": 0
}

DELETE http://115.28.89.174:8000/api/server_info/394631c1-4e87-4bfc-a87d-6745516d76c7
{
  "message": "succeed",
  "code": 0
}

GET http://115.28.89.174:8000/api/server_status/
{
  "message": "succeed",
  "code": 0,
  "data": [
    {
      "server_info": "12b2ff72-9b78-4378-8e6b-9760b17d09eb",
      "project": "CMDB",
      "owner": "胡湘林",
      "allocation_status": 1,
      "health_status": 1
    },
    {
      "server_info": "b876d8f9-85fd-42e7-8fbf-00ba789116b7",
      "project": "服务树",
      "owner": "赵培武",
      "allocation_status": 0,
      "health_status": 0
    }
  ]
}

GET http://115.28.89.174:8000/api/server_status/12b2ff72-9b78-4378-8e6b-9760b17d09eb
{
  "message": "succeed",
  "code": 0,
  "data": {
    "server_info": "12b2ff72-9b78-4378-8e6b-9760b17d09eb",
    "project": "CMDB",
    "owner": "胡湘林",
    "allocation_status": 1,
    "health_status": 1
  }
}

PUT http://115.28.89.174:8000/api/server_status/b876d8f9-85fd-42e7-8fbf-00ba78911aaa
{
    "project": "CMDB"
}
{
  "message": "succeed",
  "code": 0
}
