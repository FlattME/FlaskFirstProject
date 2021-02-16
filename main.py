from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def s() :
    return "Миссия Колонизация Марса"


@app.route('/index')
def index() :
    return "И на Марсе будут яблони цвести!"


box = ['Человечество вырастает из детства.',
       'Человечеству мала одна планета.',
       'Мы сделаем обитаемыми безжизненные пока планеты.',
       'И начнем с Марса!',
       'Присоединяйся!']


@app.route('/promotion')
def promotion() :
    return '</br>'.join(box)


@app.route('/image_mars')
def image_mars() :
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='ima/MARS.png')}" alt="А где я??">
    <p>Вот она какая, красная планета</p>
</body>
</html>'''


@app.route('/promotion_image')
def promotion_image() :
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="static/img/MARS.png" alt="А где я??">
    <p>Вот она какая, красная планета</p>
    <div class="alert alert-secondary" role="alert">
        Человечество вырастает из детства
    </div>
    <div class="alert alert-success" role="alert">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-info" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-warning" role="alert">
        И начнем с Марса!
    </div>
    <div class="alert alert-danger" role="alert">
        Присоединяйся!
    </div>
</body>
</html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection() :
    if request.method == 'GET' :
        return f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                <title>Привет, Марс!</title>
            </head>
            <body>
                <h1>Анкета претендента</h1>
                <h2>на участие в миссии</h2> 
                <form class="login_form" method="post">
                    <input type="text" name="lastname" class="input_field" id="lastname" placeholder="Введите фамилию">
                    <input type="text" name="firstname" class="input_field" id="firstname" placeholder="Введите имя">
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                    <h6>Какое у вас образование?</h6>

                    <select name="education" id="education" class="form-control">
                        <option>Начальное</option>
                        <option>Среднее</option>
                        <option>Высшее</option>
                        <option>Другое..</option>
                    </select>

                    <h6>Какие у вас есть професии?</h6>
                    <div class="form-group form-check">

                        <input class="form-check-input" type="checkbox" name="educ1" id="1" checked>
                        <label for="educ1">Инженер-исследователь</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ2" id="2" checked>
                        <label for="educ2">пилот</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ3" id="3" checked>
                        <label for="educ3">строитель</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ4" id="4" checked>
                        <label for="educ4">экзобиолог</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ5" id="5" checked>
                        <label for="educ5">врач</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ6" id="6" checked>
                        <label for="educ6">инженер по терраформированию</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ7" id="7" checked>
                        <label for="educ7">климатоло</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ8" id="8" checked>
                        <label for="educ8">специалист по радиационной защите</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ9" id="9" checked>
                        <label for="educ9">астрогеолог</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ10" id="10" checked>
                        <label for="educ10">гляциолог</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ11" id="11" checked>
                        <label for="educ11">инженер жизнеобеспечения</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ12" id="12" checked>
                        <label for="educ12">метеоролог</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ13" id="13" checked>
                        <label for="educ13">оператор марсохода</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ14" id="14" checked>
                        <label for="educ14">киберинженер</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ15" id="15" checked>
                        <label for="educ15">штурман</label>
                        <br>
                        <input class="form-check-input" type="checkbox" name="educ16" id="16" checked>
                        <label for="educ16">пилот дронов</label>
                    </div>

                    <h6>Укажите пол</h6>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                        <label class="form-check-label" for="male">
                          Мужской
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                        <label class="form-check-label" for="female">
                          Женский
                        </label>
                    </div>

                    <h6>
                        Почему вы хотите принять участие в миссии?
                    </h6>
                    <textarea class="form-control" id="about" rows="4" name="about"></textarea>

                    <h6>
                        Приложите фотографию
                    </h6>
                    <input type="file" class="form-control-file" id="photo" name="file">

                    <input class="form-check-input" type="checkbox" name="u_sure" id="16" checked>
                    <label for="u_sure">Вы готовы отправиться на Марс?</label></br>

                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </body>
            </html>'''
    elif request.method == 'POST' :
        print(request.form['lastname'])
        print(request.form['firstname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['educ1'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['u_sure'])
        print(request.form['sex'])

        print(request.form['educ1'])
        print(request.form['educ2'])
        print(request.form['educ3'])
        print(request.form['educ4'])
        print(request.form['educ5'])
        print(request.form['educ6'])
        print(request.form['educ7'])
        print(request.form['educ8'])
        print(request.form['educ9'])
        print(request.form['educ10'])
        print(request.form['educ11'])
        print(request.form['educ12'])
        print(request.form['educ13'])
        print(request.form['educ14'])
        print(request.form['educ15'])
        print(request.form['educ16'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name) :
    return f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <h2>Эта планета близка к Земле;</h2>
                <div class="alert alert-success" role="alert">
                    На ней много необходимых ресурсов;
                </div>
                <div class="alert alert-secondary" role="alert">
                    На ней есть вода и атмосфера;
                </div>
                <div class="alert alert-warning" role="alert">
                    На ней есть небольшое магнитное поле;
                </div>

                <div class="alert alert-danger" role="alert">
                    Наконец, она просто красива!
                </div>   
            </body>
            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating) :
    return f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                <title>Привет, Марс!</title>
            </head>
            <body>
                <h1>Результаты отбора</h1>
                <h2>Пратендента на участие в миссии {nickname}:</h2>
                <div class="alert alert-success" role="alert">
                    Поздравляем! Ваш рейтинг после {level} этапа отбора!
                </div>
                <p>составляет {rating}!</p>

                <div class="alert alert-warning" role="alert">
                    Желаем удачи!
                </div>
            </body>
            </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo() :
    if request.method == 'GET' :
        return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href='{url_for('static', filename='css/style.css')}'>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                    <h1>Загрузка фотографии</h1>
                    <h2>для участия в миссии</h2>
                    <form class="login_form" method="post">
                        <div class="form">
                            <h6>
                                Приложите фотографию
                            </h6>
                            <input type="file" class="form-control-file" id="photo" name="file">

                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </div>
                    </form>
                </body>
                </html>'''
    elif request.method == 'POST' :
        text = request.form['file']

        return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href='{url_for('static', filename='css/style.css')}'>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                    <h1>Загрузка фотографии</h1>
                    <h2>для участия в миссии</h2>
                    <form class="login_form" method="post">
                        <div class="form">
                            <h6>
                                Приложите фотографию
                            </h6>
                            <input type="file" class="form-control-file" id="photo" name="file">
                            f'<img src="{url_for("static", filename=f"img/{text}")}" alt="фотографии нет">'

                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </div>
                    </form>
                </body>
                </html>'''


@app.route('/carousel')
def carousel() :
    return f'''<!doctype html>
            <html lang="en">
              <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <!-- main css file -->
                <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

                <title>Пейзажи Марса</title>
              </head>
              <body>
                <h1>Пейзажи Марса</h1>


                <div class="slider">
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        </ol>
                        <div class="carousel-inner">
                          <div class="carousel-item active">
                            <img class="d-block w-100" src="{url_for("static", filename="img/mars_1.jpg")}" alt="First slide">
                          </div>
                          <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for("static", filename="img/mars_2.jpg")}" alt="Second slide">
                          </div>
                          <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for("static", filename="img/mars_3.jpg")}" alt="Third slide">
                          </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                          <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                          <span class="carousel-control-next-icon" aria-hidden="true"></span>
                          <span class="sr-only">Next</span>
                        </a>
                      </div>
                </div>

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
              </body>'''


if __name__ == '__main__' :
    app.run(port=8080, host='127.0.0.1')