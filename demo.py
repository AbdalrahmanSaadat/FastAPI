from fastapi import FastAPI, Path


students = {
    1 : {
        "name" : "abdo",
        "age" : 26,
        "class" : "pharma"
    },
    2 : {
        "name" : "amal",
        "age" : 25,
        "class" : "ceutical"
    },
    3 : {
        "name" : "ahmed",
        "age" : 23,
        "class" : "analytical"
    }
}


app = FastAPI()


@app.get("/")
def index():
    return "welcome to our university"


@app.get("/get-by-id/{student_id}")
def student_id(student_id : int = Path(description="write your id", gt= 0 , le=3) ):
    return students[student_id]


@app.get("/get-by-name/")
def student_id(name : str):
    for id in students:
        if students[id]["name"] == name:
            return students[id]
        
    return "not found"
    

