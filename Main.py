#import
import telebot
import random
import os
from telebot import types



# Main menu markup 
markup = types.ReplyKeyboardMarkup(resize_keyboard =True)

item1 = "TV Series"

item2 = "Films"

item3 = "Book"

item4 = "Test"

markup.add(item1, item2, item3, item4)

# Series markup 
markupSeries = types.ReplyKeyboardMarkup(resize_keyboard = True)

Series1 ="Friends"

Series2 = "Game of Thrones"

Series3 = "Boardwalk Empire"

Series4 = "Breaking Bad"

Series5 = "Planet Earth"

Series6 = "Chernobyl"

Series7 = "House, M.D."

Series8 = "Sherlock "

Series9 = "Peaky Blinders"

Series10 = "True Detective"

Series11 = "Firefly"

Series12 = "The Big Bang Theory"

Series13 = "Band of Brothers"

Series14 = "Sex Education"

Series15 = "The Sopranos"

SeriesBack = "Main menu"

markupSeries.add(Series1, Series2, Series3, Series4, Series5, Series6, Series7, Series8, Series9, Series10, Series11, Series12, Series13, Series14, Series15, SeriesBack)




#top 15 series 
Top15serieslist = '''
 1-Friends (1994-2004)

 2-Game of Thrones (2011 – 2019)
 
 3-Boardwalk Empire (2010 – 2014)
 
 4-Breaking Bad (2008 – 2013)
 
 5-Planet Earth (2006)
 
 6-Chernobyl (2019)
 
 7-House, M.D. (2004 – 2012)
 
 8-Sherlock (2010 – ...)
 
 9-Peaky Blinders (2013 – …)
 
 10-True Detective (2014 – ...)
 
 11-Firefly (2002 – 2003)
 
 12-The Big Bang Theory (2007 – 2019)
 
 13-Band of Brothers (2001)
 
 14-Sex Education (2019-...)
 
 15-The Sopranos(1999 – 2007)'''






# Series info + poster 



#top 15 films
Top15Films = '''
1 - The Lord of the Rings: The Return of the King

2 - Terminator

3 - The Shawshank Redemption

4 - Forrest Gump

5 - Schindler`s List

6 - Titanic

7 - The Green Mile

8 - Avatar

9 - Иван Васильевич меняет профессию

10 - Back to the Future

11 - The Matrix

12 - The Godfather

13 - The Dark Knight

14 - Gladiator

15 - Braveheart
'''
# top 15 films markup 
Films1 ="The Lord of the Rings: The Return of the King"

Films2 = "Terminator"

Films3 = "The Shawshank Redemption"

Films4 = "Forrest Gump"

Films5 = "Schindler`s List"

Films6 = "Titanic"

Films7 = "The Green Mile"

Films8 = "Avatar"

Films9 = "Иван Васильевич меняет профессию"

Films10 = "Back to the Future"

Films11 = "The Matrix"

Films12 = "The Godfather"

Films13 = "The Dark Knight"

Films14 = "Gladiator"

Films15 = "Braveheart"

markupFilms = types.ReplyKeyboardMarkup(resize_keyboard = True)


markupFilms.add(Films1, Films2, Films3, Films4, Films5, Films6, Films7, Films8, Films9, Films10, Films11, Films12, Films13, Films14, Films15, SeriesBack)


Top15Book = '''
1 - Big Sky
2 - Sweet Sorrow
3 - Machines Like Me
4 - Normal People
5 - The Silent Patient
6 - Those People
7 - The Sleepwalker
8 - No Way Out
9 - The Garden of Lost and Found
10 - After the End
11 - The Flatshare
12 - Queenie
13 - The Doll Factory
14 - City of Girls
15 - Circe
'''
Book1 = 'Big Sky'
Book2 = 'Sweet Sorrow'
Book3 = 'Machines Like Me'
Book4 = 'Normal People'
Book5 = 'The Silent Patient'
Book6 = ' Those People'
Book7 = 'The Sleepwalker'
Book8 = 'No Way Out'
Book9 = 'The Garden of Lost and Found'
Book10 = 'After the End'
Book11 = 'The Flatshare'
Book12 = 'Queenie'
Book13 = 'The Doll Factory'
Book14 = 'City of Girls'
Book15 = "Circe"
BooBack = "Main menu"
markupBook = types.ReplyKeyboardMarkup(resize_keyboard = True)
markupBook.add(Book1, Book2, Book3, Book4, Book5, Book6, Book7, Book8, Book9, Book10, Book11, Book12, Book13, Book14, Book15, BooBack)

#top 15 films + poster  



#Test markup 
markupTest = types.ReplyKeyboardMarkup(resize_keyboard =True)
agree = "I agree"
disagree = "I disagree"
markupTest.add(agree, disagree, SeriesBack)

markupHobbi = types.ReplyKeyboardMarkup(resize_keyboard =True)

''' hobbi markup '''
sport = "I like sports"

art = "I like art"

cooking = "I like cooking"

motorist = "I am motorist"

gamesIT = "I like video games and IT"

music = "I like music"

markupHobbi.add(sport, art, cooking, motorist, gamesIT, music, SeriesBack)

# ????  
Sport = False

Art = False

Cooking = False

Motorist = False

It = False

Music = False






''' test question + list '''
Testquestion1 = '1. You suffer from insomnia.'

Testquestion2 = '2. You often have a headache.'

Testquestion3 = '3. You feel moody by the end of the day.'

Testquestion4 = '4. You regularly cry.'

Testquestion5 = '5. At the end of the work/school day , do you sometimes feel like it is all useless?'

Testquestion6 = '6. You frequently cannot make up your mind.'

Testquestion7 = '7. You feel anxious even in front of your close friends.'

Testquestion8 = '8. You turn pale in awkward situations.'

Testquestion9 = '9. Do you ever eat without feeling hungry?'

Testquestion10 = '10. It is very difficult for you to get out of bed in the morning.'

Testquestion11 = '11. There are more gloomy and irritable people around these days.'

Testquestion12 = '12. You want silence.'

Testquestion13 = '13. You often get chills.'

Testquestion14 = '14. You feel like you’ve become overly sentimental.'

Testquestion15 = '15. Bright sunlight hurts your eyes.'


TestquestionList = [Testquestion1, Testquestion2, Testquestion3, Testquestion4, Testquestion5, Testquestion6, Testquestion7, Testquestion8, Testquestion9, Testquestion10, Testquestion11, Testquestion12, Testquestion13, Testquestion14, Testquestion15, "Here are some personalized recommendations for you", "good"]

# counters  
# points for test logic 
points = 0
# i for the cycle  
i = 1
# firstq check that the message is output 1 time  
firstq = 0
# a check that the message is output 1 time  
a = 0





#bot token
token  = "*token*"
bot = telebot.TeleBot(token)



# message handling 
@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Here we go!", reply_markup=markup) 


@bot.message_handler(func=lambda message: True)
def text(message):

	global i
	global a
	global Sport
	global It 
	global Art
	global Music
	global Motorist
	global points 
	global Cooking

# test logik
	if message.text.lower() == "test":
		bot.send_message(message.chat.id, "We have 16 questions for you", reply_markup=markupTest)
		bot.send_message(message.chat.id, TestquestionList[i-1])
	
		
	if message.text.lower() == ("i agree") :
		bot.send_message(message.chat.id, TestquestionList[i]) 
		i = i+1
		points = points + 1

	
	if(message.text.lower() == ("i disagree")):
		bot.send_message(message.chat.id, TestquestionList[i])
		i = i +1 
		points = points + 0
		

	if i == 16 and 1>a:
# markup activation 
		bot.send_message(message.chat.id, ".", reply_markup = markupHobbi)
		print(points)
		a = 6 
# Hobbi and output films + poster 
#it checks the hobby and the number of points in their values and decides what to give to the user
	if message.text.lower() == 'i like sports':
		
		Sport = True

		if points <= 3:
			SportFilm1 = open('sport/1.jpg', 'rb')
			SportFilm1t = "The film is based on the true story of Richmond High School basketball coach Ken Carter (played by Samuel L. Jackson), who made headlines in 1999 for suspending his undefeated high school basketball team due to poor academic results. The story was conceived from a screenplay co-written by John Gatins and Mark Schwahn, who created the TV series One Tree Hill. "

			bot.send_message(message.chat.id, SportFilm1t)
			bot.send_photo(message.chat.id, SportFilm1)

		if points >=4 and points <=6:
			SportFilm2 = open('sport/2.jpg', 'rb')
			SportFilm2t = 'Sunderland Til I Die is a sports documentary series, released on Netflix on 14 December 2018. The series is produced by Fulwell 73, and documents the events around English football club Sunderland A.F.C. during their 2017–18 season which saw them relegated from the EFL Championship.'

			bot.send_message(message.chat.id, SportFilm2t)
			bot.send_photo(message.chat.id, SportFilm2)

		if points >=7 and points <=9:
			SportFilm3 = open('sport/3.jpg', 'rb')
			SportFilm3t = 'The Game Changers is a 2018 documentary film about the benefits of plant-based eating for athletes. It covers multiple success stories of plant-based athletes, references scientific studies, and touches on other arguments for plant-based diets that extend to non-athletes.'

			bot.send_message(message.chat.id, SportFilm3t)
			bot.send_photo(message.chat.id, SportFilm3)

		if points >=10 and points <= 12:
			SportFilm4 = open('sport/4.jpg', 'rb')
			SportFilm4t = 'Legend No. 17 (Russian: Легенда №17) is a 2013 Russian biographical sports film directed by Nikolai Lebedev and produced by Trite Studio. The film is based on real events and tells of the rise to fame of the Soviet hockey player Valeri Kharlamov and about the first match of the Summit Series USSR — Canada 1972.'

			bot.send_message(message.chat.id, SportFilm4t)
			bot.send_photo(message.chat.id, SportFilm4)

		if points >=13:
			SportFilm5 = open('sport/5.jpg', 'rb')
			SportFilm5t = 'Synopsis. Philadelphia Pennsylvania, home to the number one underdog fighter, Rocky Balboa (Sylvester Stalone). The date is November 25, 1975, Rocky is fighting Spider Rico in a prize fight at a local church arena. ... Rocky, after recovering from the hit, goes after Spider and finishes him off'

			bot.send_message(message.chat.id, SportFilm5t)
			bot.send_photo(message.chat.id, SportFilm5)


	if message.text.lower() == 'ульяна':
		EasterEgg = open('music/EasterEgg.jpg', 'rb')
		bot.send_message(message.chat.id, "😈РОЦК😈")
		bot.send_photo(message.chat.id, EasterEgg)


	if message.text.lower() == 'i like art':
		if points <= 3:
			ArtFilm1 = open('atr/1.jpg', 'rb')
			ArtFilm1t = 'Abstract: The Art of Design is a Netflix original documentary series highlighting artists in the field of design. It was released on Netflix on February 10, 2017. The series was created by former Wired editor-in-chief Scott Dadich.'

			bot.send_message(message.chat.id,ArtFilm1t)
			bot.send_photo(message.chat.id, ArtFilm1)

		if points >=4 and points <=6:
			ArtFilm2 = open('atr/2.jpg', 'rb')
			ArtFilm2t = "Little Ashes is a 2008 Spanish-British drama film set against the backdrop of Spain during the 1920s and 1930s, as three of the era's most creative young talents meet at university and set off on a course to change their world. Luis Buñuel watches helplessly as the friendship between surrealist painter Salvador Dalí and the poet Federico García Lorca develops into a love affair."

			bot.send_message(message.chat.id, ArtFilm2t)
			bot.send_photo(message.chat.id, ArtFilm2)

		if points >=7 and points <=9:
			ArtFilm3 = open('atr/3.jpg', 'rb')
			ArtFilm3t = 'Pollock is a 2000 American biographical film which tells the life story of American painter Jackson Pollock. It stars Ed Harris, Marcia Gay Harden, Jennifer Connelly, Robert Knott, Bud Cort, Molly Regan and Sada Thompson, and was directed by Harris.'

			bot.send_message(message.chat.id, ArtFilm3t)
			bot.send_photo(message.chat.id, ArtFilm3)

		if points >=10 and points <= 12:
			ArtFilm4 = open('atr/4.png', 'rb')
			ArtFilm4t = "Girl with a Pearl Earring is a 1999 historical novel written by Tracy Chevalier. Set in 17th-century Delft, Holland, the novel was inspired by local painter Johannes Vermeer's Girl with a Pearl Earring. Chevalier presents a fictional account of Vermeer, the model and the painting. "

			bot.send_message(message.chat.id, ArtFilm4t)
			bot.send_photo(message.chat.id, ArtFilm4)

		if points >=13:
			ArtFilm5 = open('atr/5.jpg', 'rb')
			ArtFilm5t = "The film is set in the south of France during World War I and stars Michel Bouquet, Christa Theret, Thomas Doret and Vincent Rottiers.[6] Renoir achieved critical and commercial success both in France and abroad, most notably in the United States where it is on the Critic's Pick list of The New York Times."

			bot.send_message(message.chat.id, ArtFilm5t)
			bot.send_photo(message.chat.id, ArtFilm5)


	if message.text.lower() == 'i like cooking':
		
		Cooking = True

		if points <=3:
			CookingFilm1 = open('cooking/1.jpg', 'rb')
			CookingFilm1t = "A rat named Remy dreams of becoming a great French chef despite his family's wishes and the obvious problem of being a rat in a decidedly rodent-phobic profession. When fate places Remy in the sewers of Paris, he finds himself ideally situated beneath a restaurant made famous by his culinary hero, Auguste Gusteau"

			CookingFilm1 = open('cooking/1.jpg', 'rb')
			CookingFilm1t = "A rat named Remy dreams of becoming a great French chef despite his family's wishes and the obvious problem of being a rat in a decidedly rodent-phobic profession. When fate places Remy in the sewers of Paris, he finds himself ideally situated beneath a restaurant made famous by his culinary hero, Auguste Gusteau"

			bot.send_message(message.chat.id,CookingFilm1t)
			bot.send_photo(message.chat.id, CookingFilm1)

		if points >=4 and points <=6:
			CookingFilm2 = open('cooking/2.jpg', 'rb')
			CookingFilm2t = "Julie & Julia is a 2009 American comedy-drama film written and directed by Nora Ephron starring Meryl Streep, Amy Adams, Stanley Tucci, and Chris Messina. The film contrasts the life of chef Julia Child in the early years of her culinary career with the life of young New Yorker Julie Powell, who aspires to cook all 524 recipes in Child's cookbook in 365 days, a challenge she described on her popular blog that made her a published author"

			CookingFilm2 = open('cooking/2.jpg', 'rb')
			CookingFilm2t = "Julie & Julia is a 2009 American comedy-drama film written and directed by Nora Ephron starring Meryl Streep, Amy Adams, Stanley Tucci, and Chris Messina. The film contrasts the life of chef Julia Child in the early years of her culinary career with the life of young New Yorker Julie Powell, who aspires to cook all 524 recipes in Child's cookbook in 365 days, a challenge she described on her popular blog that made her a published author"

			bot.send_message(message.chat.id, CookingFilm2t)
			bot.send_photo(message.chat.id, CookingFilm2)

		if points >=7 and points <=9:
			CookingFilm3 = open('cooking/3.jpg', 'rb')
			CookingFilm3t = "Le Chef (2012) A veteran chef faces off against his restaurant group's new CEO, who wants to the establishment to lose a star from its rating in order to bring in a younger chef who specializes in molecular gastronomy"

			bot.send_message(message.chat.id, CookingFilm3t)
			bot.send_photo(message.chat.id, CookingFilm3)

		if points >=10 and points <= 12:
			CookingFilm4 = open('cooking/4.jpg', 'rb')
			CookingFilm4t = "Produced by David Kirkpatrick and Jonathan Filley for the Samuel Goldwyn Company, the film was met with largely positive reviews and grossed $14 million worldwide. It was nominated for the Grand Jury Prize at the Sundance Film Festival and the Grand Special Prize at the Deauville Film Festival."

			bot.send_message(message.chat.id, CookingFilm4t)
			bot.send_photo(message.chat.id, CookingFilm4)

		if points >=13:
			CookingFilm5 = open('cooking/5.jpeg', 'rb')
			CookingFilm5t = "The film tells the story of Pascal Ichak, a French opera singer and chef living in Georgia, who opens a restaurant. It also shows the life in Georgia in the beginning of the 20th century, including its short period of independence (see Democratic Republic of Georgia). After the Bolshevik coup attempt of Georgia (1920), the chef refuses to emigrate and endures the brutalities of the new regime."

			bot.send_message(message.chat.id, CookingFilm5t)
			bot.send_photo(message.chat.id, CookingFilm5)


	if message.text.lower() == 'i am motorist':
		
		Cooking = True

		if points <=3:
			MotoristFilm1 = open('motorist/1.jpg', 'rb')
			MotoristFilm1t ="Need for Speed is a 2014 sports action thriller film directed and co-edited by Scott Waugh and written by George and John Gatins. It is the film adaptation of the racing video game franchise of the same name by Electronic Arts. The film stars Aaron Paul, Dominic Cooper, Imogen Poots, Scott Mescudi, Ramón Rodríguez, Rami Malek, and Michael Keaton. It tells the story of street racer Tobey Marshall, who sets off to race cross-country as a way of avenging his friend's death at the hands of a rival racer, Dino Brewster"

			bot.send_message(message.chat.id, MotoristFilm1t)
			bot.send_photo(message.chat.id, MotoristFilm1)

		if points >=4 and points <=6:
			MotoristFilm2 = open('motorist/2.jpg', 'rb')
			MotoristFilm2t = "Taxi is a 2004 action comedy film directed by Tim Story and starring Queen Latifah, Jimmy Fallon, Gisele Bündchen, Jennifer Esposito, and Ann-Margret. It is a remake of the 1998 French film of the same name. An incompetent New York police officer is banned from driving and comes to rely on a talented taxi driver to help him solve a series of bank robberies. The film was panned by critics."

			bot.send_message(message.chat.id, MotoristFilm2t)
			bot.send_photo(message.chat.id, MotoristFilm2)

		if points >=7 and points <=9:
			MotoristFilm3 = open('motorist/3.jpg', 'rb')
			MotoristFilm3t = "Gone in 60 Seconds (also known as Gone in Sixty Seconds) is a 2000 American action heist film starring Nicolas Cage, Angelina Jolie, Giovanni Ribisi, Christopher Eccleston, Robert Duvall, Vinnie Jones, and Will Patton. The film was directed by Dominic Sena, written by Scott Rosenberg, and produced by Jerry Bruckheimer. The film is a loose remake of the 1974 H.B. Halicki film of the same name."

			bot.send_message(message.chat.id, MotoristFilm3t)
			bot.send_photo(message.chat.id, MotoristFilm3)

		if points >=10 and points <= 12:
			MotoristFilm4 = open('motorist/4.jpg', 'rb')
			MotoristFilm4t = "Max leads a good life with Alice and their son Théo; that is until Alice is threatened with death while waiting for a heart transplant. Max promises Théo that he will save Alice, but to keep his word he must find a heart, and fast. Since time is running out and he must find a solution, Max decides to reconnect with his troubled past. His decision will change his life in ways he could never have imagined"

			bot.send_message(message.chat.id, MotoristFilm4t)
			bot.send_photo(message.chat.id, MotoristFilm4)

		if points >=13:
			MotoristFilm5 = open('motorist/5.jpg', 'rb')
			MotoristFilm5t = "A young boy travels across Australia with his father, who's wanted by the law for committing a violent crime."

			bot.send_message(message.chat.id, MotoristFilm5t)
			bot.send_photo(message.chat.id, MotoristFilm5)


# it films + poster  
	if message.text.lower() == 'i like video games and it':
		
		Cooking = True

		if points <=3:
			Itfilms1 = open('it/1.jpg', 'rb')
			Itfilms1t = "A dramatic thriller based on real events that reveals the quest to expose the deceptions and corruptions of power that turned an Internet upstart into the 21st century's most fiercely debated organization. "

			bot.send_message(message.chat.id,Itfilms1t)
			bot.send_photo(message.chat.id,Itfilms1)

		if points >=4 and points <=6:
			Itfilms2 = open('it/2.jpg', 'rb')
			Itfilms2t = "Augmentation developer Hanka Robotics establishes a secret project to develop an artificial body, or shell, that can integrate a human brain rather than an AI. The sole survivor of a terrorist attack which killed her parents, Mira Killian is chosen as the test subject after her body is damaged beyond repair "

			bot.send_message(message.chat.id,Itfilms2t)
			bot.send_photo(message.chat.id,Itfilms2)

		if points >=7 and points <=9:
			Itfilms3 = open('it/3.jpg', 'rb')
			Itfilms3t = "Blackhat is a 2015 American action thriller film produced and directed by Michael Mann and starring Chris Hemsworth, Tang Wei, Viola Davis, Holt McCallany, and Wang Leehom. The film premiered at the TCL Chinese Theatre in Los Angeles on January 8, 2015, and was released in theaters on January 16.[4] Blackhat was a box office bomb, earning only $19.7 million at the box office against a budget of $70 million. While the film received generally mixed reviews, with criticisms focused on casting and pace, the film appeared on some critics' year-end lists. "

			bot.send_message(message.chat.id,Itfilms3t)
			bot.send_photo(message.chat.id,Itfilms3)

		if points >=10 and points <= 12:
			Itfilms4 = open('it/4.jpg', 'rb')
			Itfilms4t = "The NSA's illegal surveillance techniques are leaked to the public by one of the agency's employees, Edward Snowden, in the form of thousands of classified documents distributed to the press. "

			bot.send_message(message.chat.id,Itfilms4t)
			bot.send_photo(message.chat.id,Itfilms4)

		if points >=13:
			Itfilms5 = open('it/5.jpg', 'rb')
			Itfilms5t = "Durov's Code. The real story of Vkontakte and its Creator  is a novel by Nikolai Kononov about the creators of the largest social network in Europe, Vkontakte. It is an experiment with the genre of biography and biographical investigation at the intersection of journalism and essays, based on facts and interviews "

			bot.send_message(message.chat.id,Itfilms5t)
			bot.send_photo(message.chat.id,Itfilms5)


# music films + poster  

	if message.text.lower() == 'i like music':
		
		
		if points <=3:
			MusicFilms1 = open("music/1.jpg", 'rb')

			MusicFilms1t = "The story of the life and career of the legendary rhythm and blues musician Ray Charles, from his humble beginnings in the South, where he went blind at age seven, to his meteoric rise to stardom during the 1950s and 1960s."

			bot.send_message(message.chat.id, MusicFilms1t)

			bot.send_photo(message.chat.id, MusicFilms1)

		if points >=4 and points <=6:
			MusicFilms2 = open("music/2.jpg", 'rb')
			MusicFilms2t = "Walk the Line is a 2005 American biographical musical romantic drama film directed by James Mangold. The screenplay, written by Mangold and Gill Dennis, is based on two autobiographies authored by singer-songwriter Johnny Cash, 1975's Man in Black: His Own Story in His Own Words and 1997's Cash: The Autobiography. The film follows Cash's early life, his romance with June Carter, and his ascent in the country music scene. It stars Joaquin Phoenix as Cash, Reese Witherspoon as Carter, Ginnifer Goodwin as Cash's first wife Vivian Liberto, and Robert Patrick as Cash's father."

			bot.send_message(message.chat.id, MusicFilms2t)
			bot.send_photo(message.chat.id, MusicFilms2)

		if points >=7 and points <=9:
			MusicFilms3 = open("music/3.jpg", 'rb')
			MusicFilms3t = "Turo (25) is trying to overcome his fears by leading the most unknown heavy metal band in Finland, Impaled Rektum, to the hottest metal festival of Norway. The journey includes heavy metal, grave robbing, Viking heaven and an armed conflict between Finland and Norway."

			bot.send_message(message.chat.id, MusicFilms3t)
			bot.send_photo(message.chat.id, MusicFilms3)

		if points >=10 and points <= 12:
			MusicFilms4 = open("music/4.png", 'rb')
			MusicFilms4t = "Bohemian Rhapsody is a 2018 musical biographical drama film about Freddie Mercury, the lead singer of the British rock band Queen. It was directed by Bryan Singer from a screenplay by Anthony McCarten, and produced by Graham King and Queen manager Jim Beach. It stars Rami Malek as Mercury, with Lucy Boynton, Gwilym Lee, Ben Hardy, Joe Mazzello, Aidan Gillen, Tom Hollander, Allen Leech, and Mike Myers in supporting roles. Queen members Brian May and Roger Taylor served as consultants. A British-American venture, the film was produced by 20th Century Fox, Regency Enterprises, GK Films, and Queen Films, with Fox serving as distributor. The film follows the singer's life from the formation of the band up to their 1985 Live Aid performance at the original Wembley Stadium."

			bot.send_message(message.chat.id, MusicFilms4t)
			bot.send_photo(message.chat.id, MusicFilms4)

		if points >=13:
			MusicFilms5 = open("music/5.jpg", 'rb')
			MusicFilms5t = "A boat approaches the Pirate Radio ship and drops off Young Carl (Tom Sturridge), a young man who has been expelled from school for smoking marijuana. He has been sent to spend time with his godfather Quentin (Bill Nighy), who owns the ship, allegedly to straighten him out."

			bot.send_message(message.chat.id, MusicFilms5t)
			bot.send_photo(message.chat.id, MusicFilms5)

# top 15 logik 

	if message.text.lower() == 'tv series':

# markup activation 

		bot.send_message(message.chat.id, Top15serieslist, reply_markup = markupSeries )
	if message.text.lower() == 'friends':

		Series1text  = "The main characters are six friends-Rachel, Monica, Phoebe, Joey, Chandler and Ross. Three girls and three guys who are friends, live next door, kill time together and resist the harsh reality, share their secrets and sometimes fall very much in love."
		Series1photo = open('seriesphoto/1.jpg', 'rb')

		bot.send_photo(message.chat.id, Series1photo)
		bot.send_message(message.chat.id, Series1text)

	if message.text.lower() == 'game of thrones':
		Series2text = "Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss for HBO. It is an adaptation of A Song of Ice and Fire, George R. R. Martin's series of fantasy novels, the first of which is A Game of Thrones. The show was both produced and filmed in Belfast and elsewhere in the United Kingdom. Filming locations also included Canada, Croatia, Iceland, Malta, Morocco, and Spain.[4] The series premiered on HBO in the United States on April 17, 2011, and concluded on May 19, 2019, with 73 episodes broadcast over eight seasons."
		Series2photo =  open('seriesphoto/2.jpg', 'rb')

		bot.send_photo(message.chat.id, Series2photo)
		bot.send_message(message.chat.id, Series2text)

	if message.text.lower() == 'boardwalk empire':
		Series3text = "Set in the Prohibition era of the 1920s Boardwalk Empire is the story of Enoch Nucky Thompson, the treasurer of Atlantic County, Atlantic City, New Jersey. Due to his relationships with mobsters as well as political contacts, the Federal Government start to take an interest in him. His lavish lifestyle seems at odds with his position, and as well as his connections, there is prolific bootlegging in the area."
		Series3photo = open('seriesphoto/3.jpg', 'rb')

		bot.send_photo(message.chat.id, Series3photo)
		bot.send_message(message.chat.id, Series3text)

	if message.text.lower() == 'breaking bad':
		Series4text = "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future."
		Series4photo = open('seriesphoto/4.jpg', 'rb')

		bot.send_photo(message.chat.id, Series4photo)
		bot.send_message(message.chat.id, Series4text
			)
	if message.text.lower() == 'planet earth':
		Series5photo = open('seriesphoto/5.jpg', 'rb')
		Series5text = "Millions of years ago incredible forces ripped apart the Earth’s crust creating seven extraordinary continents. One Planet: Seven Worlds, presented by Sir David Attenborough, will reveal how each distinct continent has shaped the unique animal life found there. This series will feature remarkable, new animal behaviour from all the continents including the baking plains of Africa and the frozen waters off Antarctica. In Asia, the biggest of all continents, we will showcase life at the extremes, whilst in Europe we will reveal surprising wildlife dramas hidden right alongside us."

		bot.send_photo(message.chat.id, Series5photo)
		bot.send_message(message.chat.id, Series5text)

	if message.text.lower() == 'chernobyl':
		Series6photo = open('seriesphoto/6.jpg', 'rb')
		Series6text = "In April 1986, an explosion at the Chernobyl nuclear power plant in the Union of Soviet Socialist Republics becomes one of the world's worst man-made catastrophes."

		bot.send_photo(message.chat.id, Series6photo)
		bot.send_message(message.chat.id, Series6text)

	if message.text.lower() == 'house, m.d.':
		Series7photo = open('seriesphoto/7.jpg', 'rb')
		Series7text ="House often clashes with his fellow physicians, including his own diagnostic team, because many of his hypotheses about patients' illnesses are based on subtle or controversial insights. His flouting of hospital rules and procedures frequently leads him into conflict with his boss, hospital administrator and Dean of Medicine Dr. Lisa Cuddy(Lisa Edelstein). House's only true friend is Dr. James Wilson(Robert Sean Leonard), head of the Department of Oncology."

		bot.send_photo(message.chat.id, Series7photo)
		bot.send_message(message.chat.id, Series7text)

	if message.text.lower() == 'sherlock':
		Series8photo = open('seriesphoto/8.jpg', 'rb')
		Series8text ="A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London."

		bot.send_photo(message.chat.id, Series8photo)
		bot.send_message(message.chat.id, Series8text)

	if message.text.lower() == 'peaky blinders':
		Series9photo = open('seriesphoto/9.jpg', 'rb')
		Series9text = "Peaky Blinders is a British period crime drama television series created by Steven Knight. Set in Birmingham, England, the series follows the exploits of the Shelby crime family in the direct aftermath of the First World War. The fictional family is loosely based on a real 19th century urban youth gang of the same name, who were active in the city from the 1890s to the early twentieth century."

		bot.send_photo(message.chat.id, Series9photo)
		bot.send_message(message.chat.id, Series9text)

	if message.text.lower() == 'true detective':

		Series10photo = open('seriesphoto/10.jpg', 'rb')
		Series10text = "True Detective-это американский антологический криминальный сериал, созданный и написанный Ником Пиццолатто . Премьера сериала, транслируемого премиальной кабельной сетью HBO в США, состоялась 12 января 2014 года. Каждый сезон сериала структурирован как самостоятельное повествование, использующее новые актерские ансамбли и следующие различным наборам персонажей и настроек."

		bot.send_photo(message.chat.id, Series10photo)
		bot.send_message(message.chat.id, Series10text)

	if message.text.lower() == 'firefly':
		Series11photo = open('seriesphoto/11.jpg', 'rb')
		Series11text = "Captain Malcolm Reynolds — a battle-hardened veteran of the galactic civil war who fought on the wrong (losing) side, makes a living from petty crime and transports cargo on his ship, the serenity. He leads a small motley team that looks like a very ordinary family-its members are always quarreling, do not observe discipline, but will never betray their captain and follow him to the ends of the world."

		bot.send_photo(message.chat.id, Series11photo)
		bot.send_message(message.chat.id, Series11text)

	if message.text.lower() == 'the big bang theory':
		Series12photo = open('seriesphoto/12.jpg', 'rb')
		Series12text = "The Big Bang Theory is a comedy about brilliant physicists, Leonard and Sheldon, who are the kind of beautiful minds that understand how the universe works. But none of that genius helps them interact with people, especially women. All this begins to change when a free-spirited beauty named Penny moves in next door."

		bot.send_photo(message.chat.id, Series12photo)
		bot.send_message(message.chat.id, Series12text)

	if message.text.lower() == 'band of brothers':
		Series13photo = open('seriesphoto/13.jpg', 'rb')
		Series13text = "Band of Brothers is a WWII miniseries based off of the book of the same name by Stephen Ambrose, that follows the men of Easy Company, 2nd Battalion, 506th Parachute Infantry Regiment, 101st Airborne Division.Taking place from 1942-1945, and following from the Airborne Infantry's training at camp Toccoa, Georgia, USA, to variuos places in Europe, notably Normandy France, Holland, Belgium and Germany - it is set during the European theater of World War II. Band of Brothers was created by Tom Hanks, Gary Goetzman, and Steven Spielberg, and is owned by Dreamworks and Playtone."

		bot.send_photo(message.chat.id, Series13photo)
		bot.send_message(message.chat.id, Series13text)

	if message.text.lower() == 'sex education':
		Series14photo = open('seriesphoto/14.jpeg', 'rb')
		Series14text = "Sex Education is a British comedy-drama web television series created by Laurie Nunn. Starring Asa Butterfield as a socially awkward teenager and Gillian Anderson as his character's mother and a sex therapist, the series premiered on 11 January 2019 on Netflix. Ncuti Gatwa, Emma Mackey, Connor Swindells, and Kedar Williams-Stirling co-star. It became a critical and commercial success for Netflix, with over 40 million viewers streaming the first series after its debut. The second series was released on 17 January 2020, and the show has been renewed for a third series."

		bot.send_photo(message.chat.id, Series14photo)
		bot.send_message(message.chat.id, Series14text)

	if message.text.lower() == 'the sopranos':
		Series15photo = open('seriesphoto/15.jpg', 'rb')
		Series15text = "New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state, leading him to seek professional psychiatric counseling."

		bot.send_photo(message.chat.id, Series15photo)
		bot.send_message(message.chat.id, Series15text)


# markup activation 
	if message.text.lower() == "main menu":

# back to main menu
		bot.send_message(message.chat.id, "Here we go again!", reply_markup = markup)
	if message.text.lower() == "films":
# markup activation 
		bot.send_message(message.chat.id, Top15Films, reply_markup = markupFilms)

	if message.text.lower() == 'the lord of the rings: the return of the king':
		Films1text  = "The Lord of the Rings: The Return of the King (2003) is the third and final film in the trilogy, directed by Peter Jackson and based on J.R.R. Tolkien's The Lord of the Rings."
		Films1photo = open('films/1.jpg', 'rb')

		bot.send_photo(message.chat.id, Films1photo)
		bot.send_message(message.chat.id, Films1text)

	if message.text.lower() == 'terminator':
		Films2text = "The Terminator is a 1984 American science fiction film directed by James Cameron. It stars Arnold Schwarzenegger as the Terminator, a cyborg assassin sent back in time from 2029 to 1984 to kill Sarah Connor (Linda Hamilton), whose son will one day become a savior against machines in a post-apocalyptic future."
		Films2photo =  open('films/2.jpg', 'rb')

		bot.send_photo(message.chat.id, Films2photo)
		bot.send_message(message.chat.id, Films2text)
	
	if message.text.lower() == 'the shawshank redemption':
		Films3text = "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the 1982 Stephen King novella Rita Hayworth and Shawshank Redemption. It tells the story of banker Andy Dufresne (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murders of his wife and her lover, despite his claims of innocence."
		Films3photo = open('films/3.jpg', 'rb')

		bot.send_photo(message.chat.id, Films3photo)
		bot.send_message(message.chat.id, Films3text)

	if message.text.lower() == 'forrest gump':
		Films4text = " The story depicts several decades in the life of Forrest Gump (Hanks), a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining historical events in the 20th century United States. "
		Films4photo = open('films/4.jpg', 'rb')

		bot.send_photo(message.chat.id, Films4photo)
		bot.send_message(message.chat.id, Films4text)

	if message.text.lower() == 'schindler`s list':
		Films5photo = open('films/5.jpg', 'rb')
		Films5text = "The film follows Oskar Schindler, a Sudeten German businessman who together with his wife Emilie Schindler saved more than a thousand mostly Polish-Jewish refugees from the Holocaust by employing them in his factories during World War II. It stars Liam Neeson as Schindler, Ralph Fiennes as SS officer Amon Göth, and Ben Kingsley as Schindler's Jewish accountant Itzhak Stern."

		bot.send_photo(message.chat.id, Films5photo)
		bot.send_message(message.chat.id, Films5text)

	if message.text.lower() == 'titanic':
		Films6photo = open('films/6.jpg', 'rb')
		Films6text = "A love story doomed by the depths of the Atlantic Ocean. Rose Calvert, now 101 reminiscences her experience of the Titanic, to American oceanic explorers, and her emotional connection with another passenger, Jack. Jack was an American starving artist who won a trip home on the Ship of Dreams to a lucky hand in poker."

		bot.send_photo(message.chat.id, Films6photo)
		bot.send_message(message.chat.id, Films6text)

	if message.text.lower() == 'the green mile':
		Films7photo = open('films/7.jpg', 'rb')
		Films7text ="The Green Mile is a 1999 American prison fantasycrime drama film written and directed by Frank Darabont and based on Stephen King’s 1996 novel of the same name. It stars Tom Hanks as a death rowcorrections officer during the U.S. Great Depression who witnesses supernatural events that occur after an enigmatic inmate (Michael Clarke Duncan)"

		bot.send_photo(message.chat.id, Films7photo)
		bot.send_message(message.chat.id, Films7text)

	if message.text.lower() == 'avatar':
		Films8photo = open('films/8.jpg', 'rb')
		Films8text ="The film is set in the mid-22nd century when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium, a room-temperature superconductor The expansion of the mining colony threatens the continued existence of a local tribe of Na'vi – a humanoid species indigenous to Pandora. The film's title refers to a genetically engineered Na'vi body operated from the brain of a remotely located human that is used to interact with the natives of Pandora"

		bot.send_photo(message.chat.id, Films8photo)
		bot.send_message(message.chat.id, Films8text)

# best film ever 
	if message.text.lower() == 'иван васильевич меняет профессию':
		Films9photo = open('films/9.jpg', 'rb')
		Films9text = "Иван Васи́льевич меняет профеессию — фантастическаякомедия Фильм рассказывает об инженере-изобретателе Шурике, создавшем машину времени, которая открывает двери в XVI век — во времена Ивана Грозного, в результате чего царь оказывается в советской Москве, а его тёзка — управдом Иван Бунша вместе с вором-рецидивистом Жоржем Милославским — в палатах царя. Лидер советского кинопроката 1973 года — свыше 60 миллионов зрителей"

# best film ever 
		bot.send_photo(message.chat.id, Films9photo)
# best film ever 
		bot.send_message(message.chat.id, Films9text)
	
	if message.text.lower() == 'back to the future':
		Films10photo = open('films/10.jpg', 'rb')
		Films10text = "Marty McFly, a 17 year old high school student gets lost in 1955 by an accident, 30 years back in time. With the help of his friend Dr. Emmet Brown, he is desperately trying to find his way back to the future in the year 1985. It becomes a battle against the clock."

		bot.send_photo(message.chat.id, Films10photo)
		bot.send_message(message.chat.id, Films10text)

	if message.text.lower() == 'the matrix':
		Films11photo = open('films/11.jpg', 'rb')
		Films11text = "Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix"

		bot.send_photo(message.chat.id, Films11photo)
		bot.send_message(message.chat.id, Films11text)

	if message.text.lower() == 'the godfather':
		Films12photo = open('films/12.jpg', 'rb')
		Films12text = "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. The Godfather Don Vito Corleone is the head of the Corleone mafia family in New York. He is at the event of his daughter's wedding. ... But tragic circumstances make him face the legacy of his family."


		bot.send_photo(message.chat.id, Films12photo)
		bot.send_message(message.chat.id, Films12text)

	if message.text.lower() == 'the dark knight':
		Films13photo = open('films/13.jpg', 'rb')
		Films13text = " A gang of criminals rob a Gotham City mob bank, murdering each other for a higher share of the money until only the Joker remains, who escapes with the money. Batman, District Attorney Harvey Dent and Lieutenant James Gordon form an alliance to rid Gotham City of organized crime"

		bot.send_photo(message.chat.id, Films13photo)
		bot.send_message(message.chat.id, Films13text)

	if message.text.lower() == 'gladiator':
		Films14photo = open('films/14.jpg', 'rb')
		Films14text = "The film's plot was influenced by two 1960s Hollywood films of the sword-and-sandal genre, The Fall of the Roman Empire and Spartacus, and shares several plot points with The Fall of the Roman Empire, which tells the story of Livius, who, like Maximus in Gladiator, is Marcus Aurelius's intended successor."

		bot.send_photo(message.chat.id, Films14photo)
		bot.send_message(message.chat.id, Films14text)

	if message.text.lower() == 'braveheart':

		Films15photo = open('films/15.jpg', 'rb')
		Films15text = "Braveheart is a 1995 American epic historical fiction war film directed and co-produced by Mel Gibson, who portrays William Wallace, a late-13th-century Scottish warrior. The film depicts the life of Wallace leading the Scots in the First War of Scottish Independence against King Edward I of England. The film also stars Sophie Marceau, Patrick McGoohan and Catherine McCormack. The story is inspired by Blind Harry's epic poem The Actes and Deidis of the Illustre and Vallyeant Campioun Schir William Wallace and was adapted for the screen by Randall Wallace."

		bot.send_photo(message.chat.id, Films15photo)
		bot.send_message(message.chat.id, Films15text)
	if message.text.lower() == 'book':
		bot.send_message(message.chat.id, Top15Book, reply_markup =markupBook)

	if message.text.lower() == 'big sky':
		Book1Photo = open('book/1.jpg', 'rb')
		Book1t = 'Jackson Brodie’s back. Fans have been counting the days to read the fifth instalment in Kate Atkinson’s literary crime series about the tough ex-soldier turned private investigator, and Big Sky is well worth the wait. This time round Brodie has moved to a quiet seaside village in the northeast, occasionally joined by his tricky teenage son and his ex-partner’s ageing labrador. But once again he gets drawn into a sinister investigation and old secrets come to the fore. Superbly written and utterly readable, this novel is a delight from start to finish.'
		bot.send_photo(message.chat.id, Book1Photo)
		bot.send_message(message.chat.id, Book1t)

	if message.text.lower() == 'sweet sorrow':
		Book2Photo = open('book/2.jpg', 'rb')
		Book2t = 'Sweet Sorrow is another of this summer’s most eagerly awaited novels. David Nicholls, who recently won a Bafta for his TV adaptation of the Patrick Melrose novels, made his name with One Day and excels at writing tender, funny books about love and friendship. This coming-of-age novel tells the story of 16-year-old Charlie Lewis and his love affair with a girl he meets when he reluctantly gets involved in a production of Romeo and Juliet. It’s poignant and insightful but the most affecting scenes focus on Charlie’s relationship with his dad, whose life has imploded in a disastrous way.'
		bot.send_photo(message.chat.id, Book2Photo)
		bot.send_message(message.chat.id, Book2t)

	if message.text.lower() == 'machines like me':
		Book3Photo = open('book/3.jpg', 'rb')
		Book3t = 'From the case of a young boy who refuses medical treatment on religious grounds (The Children Act) to the angst of a young couple honeymooning on the Dorset coast (On Chesil Beach), Ian McEwan’s choice of subjects is never predictable. Machines Like Me, his 15th novel, is set in an alternative 1980s London.'
		bot.send_photo(message.chat.id, Book3Photo)
		bot.send_message(message.chat.id, Book3t)

	if message.text.lower() == 'normal people':
		Book4Photo = open('book/4.jpg', 'rb')
		Book4t = 'Sally Rooney’s Normal People has won a host of awards, including both the top prize and fiction book of the year at this year’s British Book Awards, the Costa novel award and Waterstones Book of the Year. The 28-year-old Irish novelist has been described as “a millennial writer with millennial concerns” but readers of all ages will enjoy her story of two college friends who try to stay apart but find they can’t. We can’t wait to see what she does next.'
		bot.send_photo(message.chat.id, Book4Photo)
		bot.send_message(message.chat.id, Book4t)

	if message.text.lower() == 'the silent patient':
		Book5Photo = open('book/5.jpg', 'rb')
		Book5t = 'Alex Michaelides was inspired to write his debut novel while he was doing a postgraduate course in psychotherapy and working part-time at a secure psychiatric unit. It’s the tale of Alicia Berenson, a painter who lives with her fashion photographer husband Gabriel on the edge of Hampstead Heath. But when Gabriel returns late one night from a fashion shoot Alicia shoots him dead. Psychotherapist Theo Faber is fascinated by the fact that Alicia has never spoken since the shooting and five years on is determined to discover exactly what happened. A smart, sophisticated psychological thriller.'
		bot.send_photo(message.chat.id, Book5Photo)
		bot.send_message(message.chat.id, Book5t)

	if message.text.lower() == 'those people':
		Book6Photo = open('book/6.jpg', 'rb')
		Book6t = 'Louise Candlish won the crime and thriller book of the year for Our House and her latest novel is equally gripping. Lowland Way in south London is a suburban paradise, with friendly neighbours, convivial chat and children playing in the street. Everything seems perfect till Darren and Jodie move in and cause havoc and upset with their loud music, multiple cars and disruptive building work. A clever, pacey novel that will keep you guessing right until the end.'
		bot.send_photo(message.chat.id, Book6Photo)
		bot.send_message(message.chat.id, Book6t)

	if message.text.lower() == 'the sleepwalker':
		Book7Photo = open('book/7.jpg', 'rb')
		Book7t = 'Former bookseller Joseph Knox is an exciting new name in crime fiction. The Sleepwalker is the third of his series about Aidan Watts, a flawed Manchester detective with a complex family background. As the novel opens, Waits is on duty in an abandoned hospital ward, sitting with a dying murderer and hoping he’ll reveal the location of his final victim before he dies. Dark, gritty and compelling, this will have you turning the pages until the early hours of the morning.'
		bot.send_photo(message.chat.id, Book7Photo)
		bot.send_message(message.chat.id, Book7t)

	if message.text.lower() == 'no way out':
		Book8Photo = open('book/8.jpg', 'rb')
		Book8t = 'From Brideshead Revisited to the Inspector Morse books, Oxford is the setting for some remarkable novels. Cara Hunter is the latest novelist to set her books in the city – to striking effect. No Way Out is her third novel about detective inspector Adam Fawley and it’s a cracking read. It’s the Christmas holidays and two children have just been pulled from the wreckage of their home in upmarket north Oxford. The toddler is dead and his elder brother is fighting for his life – but why were they left alone? Switch off your phone and settle down on the sofa. You won’t be able to put this book down until you’ve found out what happened – and who’s responsible.'
		bot.send_photo(message.chat.id, Book8Photo)
		bot.send_message(message.chat.id, Book8t)

	if message.text.lower() == 'the garden of lost and found':
		Book9Photo = open('book/9.jpg', 'rb')
		Book9t = 'In 1919 Liddy Horner discovers her celebrated artist husband, Ned, burning his best-known painting. Known as The Garden of Lost and Found, the picture depicts his two children on an idyllic day, playing in the garden of Nightingale House, the family’s Cotswolds home. Almost a century later, the couple’s granddaughter Juliet is sent the key to Nightingale House out of the blue and starts to unravel the tragic secrets of the past. Harriet Evans’s 11th novel is a spellbinding story, brimming with flowers and paintings, loss and courage.'
		bot.send_photo(message.chat.id, Book9Photo)
		bot.send_message(message.chat.id, Book9t)

	if message.text.lower() == 'after the end':
		Book10Photo = open('book/10.jpg', 'rb')
		Book10t = 'Ex-police officer Clare Mackintosh has won legions of fans for her clever crime novels, I Let You Go, I See You and Let Me Lie. Her new book, After the End, is a radical departure, but just as powerful. Max and Pip are devoted to each other but when their young son Dylan is diagnosed with a brain tumour they face an impossible choice – and they can’t agree. This moving and thought-provoking theme is one that’s close to Mackintosh’s heart. As she explains in a note at the end of the book, in 2006 she and her husband had to decide whether to keep their critically ill son alive or remove his life support.'
		bot.send_photo(message.chat.id, Book10Photo)
		bot.send_message(message.chat.id, Book10t)

	if message.text.lower() == 'the flatshare':
		Book11Photo = open('book/11.jpg', 'rb')
		Book11t = 'Beth O’Leary’s first novel is feel-good fiction at its best. The two protagonists, Tiffy Moore and Leon Twomey, are immensely likeable and the comic situation they find themselves in is entirely believable. Tiffy works in publishing and needs a cheap flat while palliative nurse Leon works nights and needs extra cash. The pair agree to share a one-bed flat, with Tiffy sleeping there at nights and weekends and Leon using it by day. It sounds simple, but with Tiffy’s horrible ex-boyfriend, demanding clients at work, Leon’s wrongly imprisoned brother and the fact that they still haven’t met, the situation gets more complicated by the day.'
		bot.send_photo(message.chat.id, Book11Photo)
		bot.send_message(message.chat.id, Book11t)

	if message.text.lower() == 'queenie':
		Book12Photo = open('book/12.jpg', 'rb')
		Book12t = 'Candice Carty-Williams wrote her debut novel after bestselling author Jojo Moyes offered her the use of her rural cottage to finish the book, choosing her from more than 600 applicants. Queenie Jenkins is a young black woman who’s just broken up with her long-term boyfriend, Tom. Her boss at the newspaper where she works doesn’t appreciate her and her family never listens (they’re not interested unless the conversation is about Jesus or water rates). A fresh, funny and at times painful read.'
		bot.send_photo(message.chat.id, Book12Photo)
		bot.send_message(message.chat.id, Book12t)

	if message.text.lower() == 'the doll factory':
		Book13Photo = open('book/13.jpg', 'rb')
		Book13t = "It’s astonishing to discover that this accomplished book is Elizabeth Macneal’s debut novel. Macneal is a writer and potter and worked in the City for several years before completing a creative writing MA at the University of East Anglia. Set amid the squalor and chaos of Victorian London, The Doll Factory is the tale of aspiring artist Iris, who becomes a model for Pre-Raphaelite artist Louis Frost on the condition that he teaches her to paint. But she’s also been noticed by Silas Reed, a sinister collector who is obsessed by strange and beautiful things. An atmospheric book that will stay with you long after you’ve finished reading."
		bot.send_photo(message.chat.id, Book13Photo)
		bot.send_message(message.chat.id, Book13t)

	if message.text.lower() == 'city of girls':
		Book14Photo = open('book/14.jpg', 'rb')
		Book14t = 'Elizabeth Gilbert is best-known for Eat Pray Love, the 2006 memoir that chronicled her journey across Italy, India and Indonesia. In City of Girls, her third novel, she turns her attention to 1940s New York and a rundown, midtown theatre called The Lily. Nineteen-year-old Vivian Morris has dropped out of her sophomore year at Vassar and her despairing parents send her to stay with her unconventional Aunt Peg, who owns The Lily. Once there, Vivian makes firm friends with the showgirls, throws herself into their hedonistic lifestyle and learns some tough lessons. Glamorous and vivid, with fascinating historical detail.'
		bot.send_photo(message.chat.id, Book14Photo)
		bot.send_message(message.chat.id, Book14t)

	if message.text.lower() == 'circe':
		Book15Photo = open('book/15.jpg', 'rb')
		Book15t = 'Madeline Miller won the Orange prize in 2012 for her first novel, A Song for Achilles and earlier this year Circe, her long-awaited second novel, was one of the six shortlisted contenders for the Women’s Prize for Fiction (previously the Orange prize). Miller takes the legendary story of Circe, who appeared in ancient Greek texts like Homer’s The Odyssey, and brings it alive for a 21st century audience. A captivating book that races along with verve and panache.'
		bot.send_photo(message.chat.id, Book15Photo)
		bot.send_message(message.chat.id, Book15t)


bot.polling()