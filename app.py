from flask import Flask, render_template, redirect, request
import recommender as rc

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        Title = request.form['Title']
        print(Title)
        # task, Title, allData = rc.supreme(Title)

        task,Title,allData = [1, "Avatar", [{'title': 'Star Wars: The Force Awakens', 'url': 'http://image.tmdb.org/t/p/w500/9rd002JS49RwDW944fF1wjU8iTV.jpg', 'popularity': 64.01, 'release_date': '2015-12-15', 'overview': 'Thirty years after defeating the Galactic Empire, Han Solo and his allies face a new threat from the evil Kylo Ren and his army of Stormtroopers.', 'genres': ['Action', 'Adventure', 'Fantasy', 'Science Fiction'], 'vote_average': 7.4}, {'title': 'X-Men: Days of Future Past', 'url': 'http://image.tmdb.org/t/p/w500/bvN8iUpHyBIvniUk4e52SUZMA7Z.jpg', 'popularity': 29.501, 'release_date': '2014-05-15', 'overview': 'The ultimate X-Men ensemble fights a war for the survival of the species across two time periods as they join forces with their younger selves in an epic battle that must change the past – to save our future.', 'genres': ['Action', 'Adventure', 'Fantasy', 'Science Fiction'], 'vote_average': 7.5}, {'title': 'Star Trek Into Darkness', 'url': 'http://image.tmdb.org/t/p/w500/7XrRkhMa9lQ71RszzSyVrJVvhyS.jpg', 'popularity': 26.781, 'release_date': '2013-05-05', 'overview': 'When the crew of the Enterprise is called back home, they find an unstoppable force of terror from within their own organization has detonated the fleet and everything it stands for, leaving our world in a state of crisis.  With a personal score to settle, Captain Kirk leads a manhunt to a war-zone world to capture a one man weapon of mass destruction. As our heroes are propelled into an epic chess game of life and death, love will be challenged, friendships will be torn apart, and sacrifices must be made for the only family Kirk has left: his crew.', 'genres': ['Action', 'Adventure', 'Science Fiction'], 'vote_average': 7.3}, {'title': 'Terminator 2: Judgment Day', 'url': 'http://image.tmdb.org/t/p/w500/5M0j0B18abtBI5gi2RhfjjurTqb.jpg', 'popularity': 30.1, 'release_date': '1991-07-03', 'overview': 'Nearly 10 years have passed since Sarah Connor was targeted for termination by a cyborg from the future. Now her son, John, the future leader of the resistance, is the target for a newer, more deadly terminator. Once again, the resistance has managed to send a protector back to attempt to save John and his mother Sarah.', 'genres': ['Action', 'Science Fiction', 'Thriller'], 'vote_average': 8}, {'title': 'The Terminator', 'url': 'http://image.tmdb.org/t/p/w500/qvktm0BHcnmDpul4Hz01GIazWPr.jpg', 'popularity': 23.848, 'release_date': '1984-10-26', 'overview': 'In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the "Terminator" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?', 'genres': ['Action', 'Science Fiction', 'Thriller'], 'vote_average': 7.5}, {'title': 'Aliens', 'url': 'http://image.tmdb.org/t/p/w500/xwdPTZyyBa4U3V2N0EmozTCeEAY.jpg', 'popularity': 26.047, 'release_date': '1986-07-18', 'overview': "When Ripley's lifepod is found by a salvage crew over 50 years later, she finds that terra-formers are on the very planet they found the alien species. When the company sends a family of colonists out to investigate her story—all contact is lost with the planet and colonists. They enlist Ripley and the colonial marines to return and search for answers.", 'genres': ['Action', 'Science Fiction', 'Thriller'], 'vote_average': 7.9}, {'title': 'Predator', 'url': 'http://image.tmdb.org/t/p/w500/yXA4teFVPqfRdCG9hwBYUs8qUYh.jpg', 'popularity': 21.637, 'release_date': '1987-06-12', 'overview': 'Dutch and his group of commandos are hired by the CIA to rescue downed airmen from guerillas in a Central American jungle. The mission goes well but as they return they find that something is hunting them. Nearly invisible, it blends in with the forest, taking trophies from the bodies of its victims as it goes along. Occasionally seeing through its eyes, the audience sees it is an intelligent alien hunter, hunting them for sport, killing them off one at a time.', 'genres': ['Action', 'Adventure', 'Science Fiction', 'Thriller'], 'vote_average': 7.4}, {'title': 'The Abyss', 'url': 'http://image.tmdb.org/t/p/w500/jel2BuDv7Bq4fuv2pUrTfiBm69o.jpg', 'popularity': 15.545, 'release_date': '1989-08-09', 'overview': "A civilian oil rig crew is recruited to conduct a search and rescue effort when a nuclear submarine mysteriously sinks. One diver soon finds himself on a spectacular odyssey 25,000 feet below the ocean's surface where he confronts a mysterious force that has the power to change the world or destroy it.", 'genres': ['Adventure', 'Action', 'Thriller', 'Science Fiction'], 'vote_average': 7.3}, {'title': 'Man of Steel', 'url': 'http://image.tmdb.org/t/p/w500/7rIPjn5TUK04O25ZkMyHrGNPgLx.jpg', 'popularity': 24.048, 'release_date': '2013-06-12', 'overview': 'A young boy learns that he has extraordinary powers and is not of this earth. As a young man, he journeys to discover where he came from and what he was sent here to do. But the hero in him must emerge if he is to save the world from annihilation and become the symbol of hope for all mankind.', 'genres': ['Action', 'Adventure', 'Fantasy', 'Science Fiction'], 'vote_average': 6.5}, {'title': 'Jupiter Ascending', 'url': 'http://image.tmdb.org/t/p/w500/mb4zAOosaO9tHyH1n7g0634moK0.jpg', 'popularity': 25.783, 'release_date': '2015-02-04', 'overview': 'In a universe where human genetic material is the most precious commodity, an impoverished young Earth woman becomes the key to strategic maneuvers and internal strife within a powerful dynasty…', 'genres': ['Action', 'Adventure', 'Fantasy', 'Science Fiction'], 'vote_average': 5.4}]]


        print(allData)
    return render_template('recommend.html', task=task, Title=Title, allData=allData)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('home.html')


if __name__ == '__main__':
    # app.debug = True
    app.run()
