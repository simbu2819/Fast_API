# importing required packages

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

api_nani=FastAPI()

response = {}
origins = ["*"]

api_nani.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel

class Features(BaseModel):
    firstname :Optional[str]
    secondname:Optional[str]
    age: int
    gender: Optional[str]


@api_nani.post("/nani_link")
async def event_members_count(data:Features):
    firstname = data.firstname
    secondname = data.secondname
    age = data.age
    gender = data.gender

    response='Entered Successfully'
    return response


@api_nani.post("/simbu_link")
async def event_members(data:Features):
    firstname = data.firstname
    secondname = data.secondname
    age = data.age
    gender = data.gender

    response['title']="You are Entered Details is Mentioned Below"
    response['firstname']=firstname
    response['secondname'] = secondname
    response['age'] = age
    response['gender'] = gender
    return response

if __name__ == "__main__":
    uvicorn.run("main:api_nani", host="localhost", port=5001,reload=True)

