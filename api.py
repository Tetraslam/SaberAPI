class running:
    def runthisapp():
        import flask
        from flask import request, jsonify

        app = flask.Flask(__name__)
        app.config["DEBUG"] = True

        # Create some test data for our catalog in the form of a list of dictionaries.

        lightsaberforms = [
            {'id': 1,
            'name': 'Shii-Cho',
            'link': 'http://127.0.0.1:5000/form1',
            'focus': 'Parries and strikes',
            },
            {'id': 2,
            'name': 'Makashi',
            'link': 'http://127.0.0.1:5000/form3',
            'focus': 'Duelling',
            },
            {'id': 3,
            'name': 'Soresu',
            'link': 'http://127.0.0.1:5000/form3',
            'focus': 'Defence against blaster bolts',
            },
            {'id': 4,
            'name': 'Ataru',
            'link': 'http://127.0.0.1:5000/form4',
            'focus': 'Strength, speed and agility, through agression',
            },
            {'id': 5,
            'name': 'Shien/Djem So',
            'link': 'http://127.0.0.1:5000/form5',
            'focus': 'An advancement on Form III, with more focus on counterattacks.',
            },
            {'id': 6,
            'name': 'Niman',
            'link': 'http://127.0.0.1:5000/form6',
            'focus': 'Dual-blade wielding and jack-of-all-trades fighting.',
            },
            {'id': 7,
            'name': 'Juyo/Vapaad',
            'link': 'http://127.0.0.1:5000/form7',
            'focus': 'More than just a lightsaber form, it is also a state of mind where the user feels relish in battle. This is the lightsaber form that takes the user the closest to the dark side.',
            }
            
        ]

        form1={
            'id':1,
            'name': 'Shii-Cho',
            'focus': 'Parries and strikes',
        }
        form2={
            'id':2,
            'name': 'Makashi',
            'focus': 'Duelling',
        }
        form3={
            'id': 3,
            'name': 'Soresu',
            'focus': 'Defence against blaster bolts',
        }

        form4={
            'id': 4,
            'name': 'Ataru',
            'focus': 'Strength, speed and agility, through agression',
        }

        form5={
            'id': 5,
            'name': 'Shien/Djem So',
            'focus': 'An advancement on Form III, with more focus on counterattacks.',
        }

        form6={
            'id': 6,
            'name': 'Niman',
            'focus': 'Dual-blade wielding and jack-of-all-trades fighting.',
        }

        form7={
            'id': 7,
            'name': 'Juyo/Vapaad',
            'focus': 'More than just a lightsaber form, it is also a state of mind where the user feels relish in battle. This is the lightsaber form that takes the user the closest to the dark side.',
        }

        @app.route('/', methods=['GET'])
        def home():
            return '''<h1 style = "font-family:candara,geneva,optima;">SaberAPI</h1>
        <p style = "font-family:candara,geneva,optima;">A prototype API for seekers of information regarding the 7 forms of lightsaber combat.</p>
        <br>
        <table border=1"5">
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form1">Form 1 (Shii-Cho)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form2">Form 2 (Makashi)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form3">Form 3 (Soresu)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form4">Form 4 (Ataru)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form5">Form 5 (Shien/Djem So)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form6">Form 6 (Niman)</a>
        </td>
        </tr>
        <tr>
        <td>
        <a href="http://127.0.0.1:5000/form7">Form 2 (Juyo/Vapaad)</a>
        </td>
        </tr>
        </table>
        '''


        @app.route('/allforms', methods=['GET'])
        def api_all():
            return jsonify(lightsaberforms)

        @app.route('/form1', methods=['GET'])
        def api_form1():
            return jsonify(form1)
        @app.route('/form2', methods=['GET'])
        def api_form2():
            return jsonify(form2)
        @app.route('/form3', methods=['GET'])
        def api_form3():
            return jsonify(form3)
        @app.route('/form4', methods=['GET'])
        def api_form4():
            return jsonify(form4)
        @app.route('/form5', methods=['GET'])
        def api_form5():
            return jsonify(form5)
        @app.route('/form6', methods=['GET'])
        def api_form6():
            return jsonify(form6)
        @app.route('/form7', methods=['GET'])
        def api_form7():
            return jsonify(form7)

        @app.route('/form', methods=['GET'])
        def api_id():
            if 'id' in request.args:
                id = int(request.args['id'])
            else:
                return "Error: No id field provided. Please specify an id."
            results = []
            for x in lightsaberforms:
                if x['id'] == id:
                    results.append(lightsaberforms[x])
            return jsonify(results)
        app.run()

