''' 1 susidiegiame Flask
        pip3 install Flask
        pip install Flask
''' 


from flask import Flask, request
app = Flask(__name__)


skaicius = 0 

def sudetis(pirmas,antras):
        return pirmas + antras

def atimtis(pirmas,antras):
        return pirmas - antras

def daugyba(pirmas,antras):
        return pirmas * antras

def dalyba(pirmas,antras):
        return pirmas / antras






@app.route("/") 
def hello_world():

    return f"""
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                        
                    <label for="[[__ID__]]">skaicius 2</label><br>   
                        <input type="text" id="[[__ID__]]" name="[[__ID__]]" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
                </form> 
            """




@app.route("/labas")  
def sakyk_labas():
    global skaicius ## Naudoju globalu kintamaji
    skaicius = skaicius +1 ## kaskart atidare pridedam 1
    return f"Labas {skaicius}"


    '''
        /skaicius?test=100
        /skaicius?test=0  &  test2=0
    '''




@app.route("/skaicius") 
def skaiciuoti():

    pirmas = request.args.get("arg1") 
    antras = request.args.get("arg2") 

    sudetis = sudetis(pirmas, antras)
    atimtis = atimtis(pirmas, antras)
    daugyba = daugyba(pirmas, antras)
    dalyba = dalyba(pirmas, antras)

    return f"""
    <p>Sudetis: {sudetis}</p>
    <p>Atimtis: {atimtis}</p>
    <p>Daugyba: {daugyba}</p>
    <p>Dalyba: {dalyba}</p>
    """




if __name__ == "__main__":
    app.run()
