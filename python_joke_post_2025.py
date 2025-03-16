open_mics_that_are_gone_now_i_miss_them = ["comedy_blvd", "PDA_Altadena", "ice_house", "dat_phan_and_friends"]
open_mics_i_still_love = ["fourth_wall", "THC", "Flappers", "Flashback", "the_crow", "no_bad_mics"]
new_mics_i_love = ["tao_comedy_studio", "hot_lunch_mic", "courtyard_comedy", "Chatterbox", "Clubhouse"]
open_mics_where_parking_situation_got_worse = ["badger_and_jam", "hollywood_improv", "comedy_store"]

money_left_in_bank = 20
new_fans = 100
old_fans = 1000
haters_getting_triggered = 100

def kill_on_stage(authenticity, word_economy, pathos, relatability, presence, truth, new_fans, haters):
	good_set = authenticity + word_economy + pathos + relatability + presence + truth
	if good_set: 
		new_fans += 5
		haters += 1
	elif bad_set:
		print("Ain't No Thang")
		break 
	return good_set

while new_fans + old_fans > haters_getting_triggered and money_left_in_bank > 0:
	kill_on_stage(1,1,1,1,1, new_fans, haters)
	money_left_in_bank = money_left_in_bank - 1

well_paid_comedy_gigs_in_LA = [] #empty list

bookers_dictionary = {
	"flappers": "josh",
	"improv": "reeta",
	"fourth_wall": "joe"
}

for club, booker in bookers_dictionary:
	print("Hi {club}, may I please speak to {booker} for a spot?")
	print("You gon learn today. Say it with your chest. 34.50. What's the deal with bananas?")