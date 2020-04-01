from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planishere

app = Flask(__name__)

@app.route('/')
def index():
    session['room_name'] = planishere.START
    session['guess_count'] = 0
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == 'GET':
        if room_name:
            room = planishere.load_room(room_name)
            return render_template('show_room.html', room=room)
        else:
            return render_template('you_died.html')

    else:
        action = request.form.get('action')



        if room_name and action:
            print(room_name)
            room = planishere.load_room(room_name)
            next_room = room.go(action)

            if (not next_room) and room_name == 'laser_weapon_armory':

                if session.get('guess_count') < 10:
                    session['guess_count'] += 1
                    print(session.get('guess_count'))
                else:
                    session['guess_count'] = 0
                    next_room = room.go('*')


            if not next_room:
                session['room_name'] = planishere.name_room(room)
            else:
                session['room_name'] = planishere.name_room(next_room)

        return redirect(url_for('game'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
