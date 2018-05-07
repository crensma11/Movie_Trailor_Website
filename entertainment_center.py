"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes

"""Creates six Movie objects, initialising these objects with title, storyline,
poster image link, video trailer link, release date and rating."""

zootopia = media.Movie(
    "Zootopia", "From the largest elephant to the smallest"
    "shrew, the city of Zootopia is a mammal metropolis where various animals"
    "live and thrive. When Judy Hopps (Ginnifer Goodwin) becomes the first"
    "rabbit to join the police force, she quickly learns how tough it is to"
    "enforce the law. Determined to prove herself, Judy jumps at the"
    "opportunity to solve a mysterious case. Unfortunately, that means working"
    "with Nick Wilde (Jason Bateman), a wily fox who makes her job even"
    "harder.",
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM", "March 4, 2016", "PG")

avatar = media.Movie(
    "Avatar", "On the lush alien world of Pandora live the"
    "Na'vi, beings who appear primitive but are highly evolved. Because the"
    "planet's environment is poisonous, human/Na'vi hybrids, called Avatars,"
    "must link to human minds to allow for free movement on Pandora. Jake"
    "Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again"
    "through one such Avatar and falls in love with a Na'vi woman"
    "(Zoe Saldana). As a bond with her grows, he is drawn into a battle for"
    "the survival of her world.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io", "December 18, 2009", "PG-13")

lone_survivor = media.Movie(
    "Lone Survivor", "In 2005 Afghanistan, Navy SEALs"
    "Marcus Luttrell (Mark Wahlberg), Michael Murphy (Taylor Kitsch), Danny"
    "Dietz (Emile Hirsch) and Matthew 'Axe' Axelson (Ben Foster) deploy on a"
    "mission of surveillance and to take out Taliban leader Ahmad Shah. Though"
    "spotted by goatherds, Luttrell and his team decide not to kill them. But"
    "one of the Afghans alerts a group of Taliban fighters to the invaders,"
    "and a terrible battle ensues, in which the SEALs find themselves"
    "hopelessly outnumbered and outgunned.",
    "https://upload.wikimedia.org/wikipedia/en/b/bd/Lone_Survivor_poster.jpg",
    "https://www.youtube.com/watch?v=yoLFk4JK_RM", "December 25, 2013", "R")

limitless = media.Movie(
    "Limitless", "Facing unemployment and his girlfriend's"
    "rejection, writer Eddie Morra (Bradley Cooper) is sure that he has no"
    "future. That all changes when an old friend gives him a drug that"
    "produces enhanced mental acuity. Stoked on the untested chemical, Eddie"
    "rises to the top of the financial world and attracts the attention of a"
    "tycoon (Robert De Niro) who intends to use him to make a fortune. But"
    "terrible side-effects and a dwindling supply threaten to collapse Eddie's"
    "house of cards.",
    "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
    "https://www.youtube.com/watch?v=jOLqNOfzus4", "March 18, 2011", "PG-13")

transformers = media.Movie(
    "Transformers", "The fate of humanity is at stake"
    "when two races of robots, the good Autobots and the villainous"
    "Decepticons, bring their war to Earth. The robots have the ability to"
    "change into different mechanical objects as they seek the key to ultimate"
    "power. Only a human youth, Sam Witwicky (Shia LaBeouf) can save the world"
    "from total destruction.",
    "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
    "https://www.youtube.com/watch?v=dxQxgAfNzyE", "July 3, 2007", "PG-13")

inception = media.Movie(
    "Inception", "Dom Cobb (Leonardo DiCaprio) is a thief"
    "with the rare ability to enter people's dreams and steal their secrets"
    "from their subconscious. His skill has made him a hot commodity in the"
    "world of corporate espionage but has also cost him everything he loves."
    "Cobb gets a chance at redemption when he is offered a seemingly"
    "impossible task: Plant an idea in someone's mind. If he succeeds, it will"
    "be the perfect crime, but a dangerous enemy anticipates Cobb's every"
    "move.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=8hP9D6kZseM", "July 16, 2010", "PG-13")

"""Store the Movie objects in a list."""
movies = [zootopia, avatar, lone_survivor, limitless, transformers, inception]

"""Open the movie website in the user's browser, featuring the movies above."""
fresh_tomatoes.open_movies_page(movies)
