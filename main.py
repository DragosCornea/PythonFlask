from website import create_app # din folderul website importam functia create_app ( care se afla in __init_.py)

app = create_app()

if __name__ == '__main__': # tot timpul va porni aplicatia din main
    app.run(debug=True) # run flask, applications