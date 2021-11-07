import acetaria_game
# from flask_server.server import app
import dill

if __name__ == "__main__":
    # game = acetaria_game.Game()
    # game.test()
    # app.run(host="0.0.0.0", port=5000)

    # with open(f'gamedata\\game-{game.id}.pickle', 'wb') as datafile:
    #     dill.dump(game, datafile)

    with open('gamedata\\game-965519d8-1265-4c55-8abc-a76edae3c512.pickle', 'rb') as datafile:
        game = dill.load(datafile)

    print(game.__dict__)
    game.market.show()
    game.deck.print_cards()

