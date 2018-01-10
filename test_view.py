from flask import render_template

@app.route('/test/')
def item(item_set):
    return render_template('questionare', item_set = item_set);



