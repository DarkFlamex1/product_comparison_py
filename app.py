from flask import Flask, render_template, request
import pandas as pd

from scraper import Scraper

app = Flask(__name__)

ButtonPressed = 0
@app.route('/', methods=["GET", "POST"])
def button():
    # On button press, run show_tables scraper function
    if request.method == "POST":
        return show_tables()
    return render_template("view.html", ButtonPressed = ButtonPressed)

@app.route('/tables')
def show_tables():
    '''
    Run the scraper on multiple offerings, the goal is to run the scraper on all offerings
    :return:
    '''
    internalScraper = Scraper()
    test1 = internalScraper.scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-grigio")
    test2 = internalScraper.scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-red")
    test3 = internalScraper.scrape_bev_flavor("https://drinkbev.com/products/rose-wine")
    test4 = internalScraper.scrape_bev_flavor("https://drinkbev.com/products/bev-blanc")

    # Concate all the babe and bev offerings into singular data frames
    babepd = pd.concat([test1.get_dict_as_df(), test2.get_dict_as_df()], axis=1)
    bevpd = pd.concat([test3.get_dict_as_df(), test4.get_dict_as_df()], axis=1)

    # Render the offerings when the button is pressed
    return render_template('view.html', tables=[babepd.to_html(classes='babe'),
                                                bevpd.to_html(classes='bev')],
                           titles = ['na', 'Babe', 'Bev'])
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)