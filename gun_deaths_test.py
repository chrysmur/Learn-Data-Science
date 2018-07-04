#!/usr/bin/env python3
if __name__ == __main__:
  #Run the code
  print(headers)
  yeardeaths = count_yearly_deaths(gun_data)
  monthdeaths = count_monthly_deaths(gun_data)
  sexdeaths = count_gender(gun_data)
  racedeaths = count_race(gun_data)
  racedeathrate = count_race_per_hundrendk(racedeaths)

  print("\nYearly")
  print(yeardeaths)
  print("\nMonthly")
  print(monthdeaths)
  print("\nGender")
  print(sexdeaths)
  print("\nRacial")
  print(racedeaths)
  print("\nRace Per 100000")
  print(racedeathrate)
  print("\n\nHomicide")
  print(count_by_intent(gun_data))
  print("\nRate for Homicide")
  homicide_per_race = count_by_intent(gun_data)
  homicide_rate_per_race = count_race_per_hundrendk(homicide_per_race)
  print(homicide_rate_per_race)
  print("\nPolice Involvement")
  police_racial_involvement= count_by_police(gun_data)

  print(police_racial_involvement)
  police_race_count_rate = count_race_per_hundrendk(police_racial_involvement)
  print("\nPolice Involvement per 100000")
  print(police_race_count_rate)

  cause = "Suicide"
  print("\n",cause,"per Month")
  cause_month = intent_rel_month(gun_data,cause)
  print(sorted(cause_month.items()))
  print("\n",cause,"per Gender- Link between gender and causes of death")
  cause_sex = intent_rel_gender(gun_data,cause)
  print(cause_sex)

  cause = "Homicide"
  print("\n",cause,"per Month")
  cause_month = intent_rel_month(gun_data,cause)
  print(sorted(cause_month.items()))
  print("\n",cause,"per Gender- Link between gender and causes of death")
  cause_sex = intent_rel_gender(gun_data,cause)
  print(cause_sex)
